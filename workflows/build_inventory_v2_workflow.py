from metadata_enrichment.metadata_enrichment_service import (
    enrich_article
)
from notifications.email_service import (
    send_email
)
from notifications.notification_service import (
    create_notification
)
from documentation_discovery.inventory_builder_v2 import (
    build_inventory_v2
)

from repositories.repository_manager import (
    create_repository
)

from repositories.repository_registry import (
    update_repository_status
)

from agents.article_inventory_agent import (
    save_inventory
)

from job_engine.job_manager import (
    JobManager
)


def build_inventory_workflow_v2(
    repository_name,
    documentation_url,
    notification_email
):

    job_manager = JobManager()

    job = job_manager.create_job(
        job_type="Repository Build",
        repository_name=repository_name,
        notification_email=notification_email
    )

    try:

        job_manager.update_progress(
            job["job_id"],
            10,
            "Creating repository..."
        )

        repository_folder = create_repository(
            repository_name,
            documentation_url
        )

        job_manager.update_progress(
            job["job_id"],
            40,
            "Discovering documentation..."
        )

        inventory = build_inventory_v2(
            documentation_url
        )

        enriched_inventory = []

        for article in inventory:

            enriched_inventory.append(
                enrich_article(
                    article,
                    repository_name
                )
            )

        inventory = enriched_inventory

        job_manager.update_progress(
            job["job_id"],
            75,
            "Saving inventory..."
        )

        save_inventory(
            repository_folder,
            inventory
        )

        job_manager.update_progress(
            job["job_id"],
            90,
            "Updating repository status..."
        )

        update_repository_status(
            repository_name,
            "Ready",
            len(inventory)
        )

        job_manager.complete_job(
            job["job_id"],
            "Repository build completed successfully."
        )

        create_notification(
            title="Repository Build Completed",
            message=f"{repository_name} has finished building successfully."
        )

        send_email(
            job["notification_email"],
            "Repository Build Completed",
            f"""
            <h2>Repository Build Completed</h2>

            <p><b>Repository:</b> {repository_name}</p>

            <p>Your repository has been built successfully.</p>

            <p>You can now use it across all DocIntel AI modules.</p>
            """
        )

        return inventory

    except Exception as ex:

        job_manager.fail_job(
            job["job_id"],
            str(ex)
        )

        create_notification(
            title="Repository Build Failed",
            message=f"{repository_name} failed to build.\n\n{str(ex)}"
        )

        send_email(
            job["notification_email"],
            "Repository Build Failed",
            f"""
            <h2>Repository Build Failed</h2>

            <p><b>Repository:</b> {repository_name}</p>

            <p><b>Error:</b></p>

            <p>{str(ex)}</p>
            """
        )

        raise