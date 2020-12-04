# This is a simple Dockerfile to use while developing
# It's not suitable for production
#
# It allows you to run both flask and celery if you enabled it
# for flask: docker run --env-file=.flaskenv image flask run
# for celery: docker run --env-file=.flaskenv image celery worker -A myapi.celery_app:app
#
# note that celery will require a running broker and result backend
# FROM python:3.70-slim

# RUN mkdir /code
# WORKDIR /code

# COPY requirements.txt setup.py tox.ini ./
# RUN pip install -r requirements.txt
# RUN pip install -e .

# COPY baoapi baoapi/
# COPY migrations migrations/

# EXPOSE 5000

FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install -e .

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 30 baoapi.wsgi:app
