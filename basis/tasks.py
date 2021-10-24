from smatova_project.celery import app
from .scheduler import run_scheduled_jobs
from .timer import run_task, TASK_DELAY_INTERVAL_1_MINUTE


@app.task
def run_background():
    run_task(TASK_DELAY_INTERVAL_1_MINUTE, run_scheduled_jobs)
