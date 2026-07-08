from job_engine.base_intelligence_job import BaseIntelligenceJob

job = BaseIntelligenceJob(
    job_type="Test Job",
    repository_name="Test Repository"
)

job.update_progress(
    progress=50,
    message="Testing"
)

job.save_result(
    result_type="Test",
    repository="Test Repository",
    data=[{"status": "ok"}]
)

job.complete(
    message="Test completed",
    result_type="Test"
)

print("Job ID:", job.job_id)