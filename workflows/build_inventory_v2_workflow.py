from urllib.parse import urlparse

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

        #
        # Create Repository
        #

        job_manager.update_progress(
            job["job_id"],
            10,
            "Creating repository..."
        )

        repository_folder = create_repository(
            repository_name,
            documentation_url
        )

        #
        # Discovery
        #

        job_manager.update_progress(
            job["job_id"],
            40,
            "Discovering documentation..."
        )

        def progress_callback(
            current,
            total,
            title
        ):

            progress = 40 + int(
                (current / total) * 35
            )

            job_manager.update_progress(

                job["job_id"],

                progress=progress,

                message=f"[{current}/{total}]",

                current_step=current,

                total_steps=total,

                current_phase="Building Knowledge Index",

                current_item=title

            )

        inventory = build_inventory_v2(

            documentation_url,

            progress_callback=progress_callback

        )

        #
        # Final Repository Metadata
        #

        total_articles = len(inventory)

        for index, article in enumerate(inventory):

            progress = 75 + int(
                ((index + 1) / total_articles) * 15
            )

            job_manager.update_progress(

                job["job_id"],

                progress=progress,

                message=f"[{index+1}/{total_articles}] Finalizing",

                current_step=index + 1,

                total_steps=total_articles,

                current_phase="Finalizing Repository",

                current_item=article.get(
                    "title",
                    ""
                )

            )

            article["repository"] = repository_name

            article["domain"] = urlparse(
                article["url"]
            ).netloc

            #
            # Lightweight statistics
            #

            description = article.get(
                "description",
                ""
            )

            article["word_count"] = len(
                description.split()
            )

            article["reading_time_minutes"] = max(
                1,
                round(
                    len(description.split()) / 200
                )
            )

        #
        # Save Inventory
        #

        job_manager.update_progress(
            job["job_id"],
            95,
            "Saving inventory..."
        )

        save_inventory(
            repository_folder,
            inventory
        )

        #
        # Update Repository
        #

        update_repository_status(
            repository_name,
            "Ready",
            len(inventory)
        )

        #
        # Complete
        #

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