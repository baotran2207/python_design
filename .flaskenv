FLASK_ENV=development
FLASK_APP=baoapi.app:create_app
SECRET_KEY=changeme
# DATABASE_URI=postgresql://baotran:baotranpassword@139.99.91.150:5433/baotran
DATABASE_URI=postgresql://dise:passw0rD!@95.216.114.137:5432/baotran

CELERY_BROKER_URL='redis://95.216.114.137:6379/0'
CELERY_RESULT_BACKEND_URL='redis://95.216.114.137:6379/0'

