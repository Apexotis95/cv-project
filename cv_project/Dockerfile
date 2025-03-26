# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose the port Railway assigns
EXPOSE $PORT

# Start Gunicorn server
CMD gunicorn cv_project.wsgi:application --bind 0.0.0.0:$PORT
