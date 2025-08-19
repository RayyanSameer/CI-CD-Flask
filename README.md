CI/CD Flask App with Docker and Render Deployment
Overview

This project demonstrates a complete CI/CD pipeline for a Flask application using GitHub Actions, Docker, and Render. Changes pushed to GitHub automatically trigger builds, tests, Docker image creation, and deployment to Render.

Features

Flask Web App: Simple Python web app with multi-line response support and test routes.
CI/CD Pipeline: Automated pipeline with GitHub Actions:
Installs dependencies
Runs tests using pytest
Builds Docker image
Pushes to DockerHub
Triggers deployment to Render
Dockerized: Lightweight Python 3.11-slim image with only required files copied for efficiency.
Environment Variables: Configurable FLASK_ENV and PORT for production readiness.
Logs & Monitoring: Render web service logs accessible for debugging and monitoring.

Tech Stack

Python 3.11
Flask
Docker
GitHub Actions (CI/CD)
Render (Web Service Deployment)
pytest (Automated Testing)

Usage

Clone the repo:
git clone https://github.com/RayyanSameer/CI-CD-Flask.git
cd CI-CD-Flask
Build Docker image locally:
docker build -t my-flask-app ./ci_cd-flask-ap

Run the app:

docker run -p 5000:1000 my-flask-app


Access the app at: http://localhost:5000

CI/CD Pipeline (GitHub Actions)

Triggered on pushes or pull requests to the main branch.

Steps:

Checkout repository
Set up Python 3.11
Install dependencies
Run tests
Build Docker image
Log in to DockerHub
Push Docker image
Trigger Render deployment

Resume Highlights

Built full CI/CD pipeline integrating GitHub Actions, Docker, and Render.

Implemented Dockerfile optimization by copying only necessary files.

Automated test execution and deployment, ensuring continuous integration and delivery.

Configured environment variables for production-ready deployment.
