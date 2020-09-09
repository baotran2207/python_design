from baoapi.extensions import celery


@celery.task
def dummy_task():
    return "OK"

@celery.task
def send_email():
    pass
