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
    documentation_url
):

    job_manager = JobManager()

    job = job_manager.create_job(
        "Repository Build"
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

        return inventory

    except Exception as ex:

        job_manager.fail_job(
            job["job_id"],
            str(ex)
        )

        raise