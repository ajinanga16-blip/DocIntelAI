import json
import os


RESULT_FOLDER = os.path.join(

    "job_engine",

    "job_results"

)

os.makedirs(

    RESULT_FOLDER,

    exist_ok=True

)


def save_job_result(

    job_id,

    result_type,

    repository,

    data

):

    filename = f"{job_id}.json"

    path = os.path.join(

        RESULT_FOLDER,

        filename

    )

    payload = {

        "job_id": job_id,

        "result_type": result_type,

        "repository": repository,

        "data": data

    }

    with open(

        path,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            payload,

            file,

            indent=4,

            ensure_ascii=False

        )

    return path


def load_job_result(

    job_id

):

    path = os.path.join(

        RESULT_FOLDER,

        f"{job_id}.json"

    )

    if not os.path.exists(path):

        return None

    with open(

        path,

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(file)