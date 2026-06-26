import uuid


def create_job():

    return {

        "job_id": str(uuid.uuid4()),

        "status": "Running"

    }