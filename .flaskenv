FLASK_ENV=development
FLASK_APP=baoapi.app:create_app
SECRET_KEY=changeme
DATABASE_URI=postgresql://baotran:baotranpassword@139.99.91.150:5433/baotran
CELERY_BROKER_URL='redis://95.216.114.137:6380/0'
CELERY_RESULT_BACKEND_URL='redis://95.216.114.137:6380/0'
