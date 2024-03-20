# ImageSync Installition Guidelines on the docker

Running application locally using Docker

Tip: You can utilize the docker file for deployment purpose too by modifying it based on environment/platform needs.
Prerequisites#
Before you begin, ensure you have the following prerequisites:

Docker installed on your server or local development machine.
Basic knowledge of Docker and Docker Compose.
Start with Docker#
To check if docker is already installed on your system, open your terminal/command prompt and run:

User
docker --version
Step 1 - Download the template
Download package from where you have purchased it and extract the zip file.
Navigate to full-version or starter-kit
User
cd app
Step 2 - Start the APP in Docker
Important: Check if debug mode is set to False; if so, run the following command to generate static files before launching the project in Docker:
python manage.py collectstatic.
The full-version/starter-kit folder houses essential files for running your Django application with Docker, including:

Dockerfile: This file defines how your application image is built.
docker-compose.yml: Use this file for orchestrating multi-container Docker applications.
.dockerignore: This file specifies which files and directories should be excluded when building Docker images for a more efficient and secure deployment.
Execute the following command to build and run the application using Docker:

User
docker-compose up --build
This will generate a Docker image named full-version-web-project-django and set up a container named web_project_django.

Visit http://localhost:5050/ in your browser. The app should be up & running.

Docker python django tutorial:

Dockerize a Python django App in 3 minutes.
