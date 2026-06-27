import json
import uuid
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent

JOBS_FOLDER = PROJECT_ROOT / "data" / "jobs"
JOBS_FOLDER.mkdir(parents=True, exist_ok=True)


class JobManager:

    def create_job(self, job_type):

        job_id = str(uuid.uuid4())

        job = {
            "job_id": job_id,
            "job_type": job_type,
            "status": "Queued",
            "message": "Job created",
            "progress": 0,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        self._save_job(job)

        return job

    def get_job(self, job_id):

        job_file = JOBS_FOLDER / f"{job_id}.json"

        if not job_file.exists():
            return None

        with open(job_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def update_progress(self, job_id, progress, message="Running"):

        job = self.get_job(job_id)

        if not job:
            return None

        job["status"] = "Running"
        job["progress"] = progress
        job["message"] = message
        job["updated_at"] = datetime.now().isoformat()

        self._save_job(job)

        return job

    def complete_job(self, job_id, message="Job completed"):

        job = self.get_job(job_id)

        if not job:
            return None

        job["status"] = "Completed"
        job["progress"] = 100
        job["message"] = message
        job["updated_at"] = datetime.now().isoformat()

        self._save_job(job)

        return job

    def fail_job(self, job_id, message="Job failed"):

        job = self.get_job(job_id)

        if not job:
            return None

        job["status"] = "Failed"
        job["message"] = message
        job["updated_at"] = datetime.now().isoformat()

        self._save_job(job)

        return job

    def _save_job(self, job):

        job_file = JOBS_FOLDER / f"{job['job_id']}.json"

        with open(job_file, "w", encoding="utf-8") as file:
            json.dump(job, file, indent=4)