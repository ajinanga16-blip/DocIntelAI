from job_engine.job_manager import JobManager
from job_engine.job_results.result_manager import save_job_result


class BaseIntelligenceJob:
    """
    Base class for all Documentation Intelligence jobs.
    """

    def __init__(
        self,
        job_type,
        repository_name,
        notification_email=""
    ):

        self.job_manager = JobManager()

        self.job = self.job_manager.create_job(
            job_type=job_type,
            repository_name=repository_name,
            notification_email=notification_email
        )

    @property
    def job_id(self):
        return self.job["job_id"]

    def start(self):
        """
        Standard job lifecycle entry point.
        Reserved for future initialization.
        """
        return self.job_id

    def update_progress(
        self,
        progress,
        message="Running",
        current_step=None,
        total_steps=None,
        current_phase=None,
        current_item=None
    ):

        self.job_manager.update_progress(
            job_id=self.job_id,
            progress=progress,
            message=message,
            current_step=current_step,
            total_steps=total_steps,
            current_phase=current_phase,
            current_item=current_item
        )

    def save_result(
        self,
        result_type,
        repository,
        data
    ):

        save_job_result(
            job_id=self.job_id,
            result_type=result_type,
            repository=repository,
            data=data
        )

    def complete(
        self,
        message="Job completed",
        result_type=None
    ):

        self.job_manager.complete_job(
            job_id=self.job_id,
            message=message,
            result_type=result_type,
            result_id=self.job_id
        )

        self.cleanup()

    def fail(self, error):

        self.job_manager.fail_job(
            job_id=self.job_id,
            message=str(error)
        )

        self.cleanup()

    def log(self, message):
        """
        Reserved for centralized logging.
        """
        print(f"[{self.job_id}] {message}")

    def cleanup(self):
        """
        Reserved for future resource cleanup.
        """
        pass