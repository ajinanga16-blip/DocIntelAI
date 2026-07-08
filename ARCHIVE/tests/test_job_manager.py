from job_engine.job_manager import JobManager

manager = JobManager()

job = manager.create_job("Repository Build")

print("Created Job:")
print(job)

manager.update_progress(job["job_id"], 50)

print("\nUpdated Job:")
print(manager.get_job(job["job_id"]))

manager.complete_job(job["job_id"])

print("\nCompleted Job:")
print(manager.get_job(job["job_id"]))