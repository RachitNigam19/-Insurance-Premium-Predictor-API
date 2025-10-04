💸 Insurance-Premium-Predictor-API
This repository contains a machine learning-powered API for predicting insurance premiums based on user input data. Built with FastAPI, validated with Pydantic, and containerized using Docker, this project demonstrates expertise in developing scalable, production-ready APIs and machine learning applications.
📖 Overview
The Insurance Premium Predictor API is a full-stack project that leverages a trained machine learning model to estimate insurance premiums. It uses FastAPI for high-performance API development, Pydantic for robust data validation, and Docker for seamless deployment. The project showcases practical skills in building, validating, and deploying ML-driven APIs for real-world applications.
🎯 Features

Accurate insurance premium predictions using a trained ML model.
RESTful API built with FastAPI for fast and scalable request handling.
Data validation and serialization using Pydantic schemas.
Containerized deployment with Docker for portability and consistency.
Modular project structure for easy maintenance and scalability.

🛠️ Tech Stack

Python: Core programming language.
FastAPI: High-performance framework for building APIs.
Pydantic: Data validation and schema definition.
Scikit-learn (assumed): For training and serving the ML model.
Docker: Containerization for deployment.
Uvicorn: ASGI server for running FastAPI applications.
Git: Version control with .gitignore for clean repository management.

🚀 Getting Started
Prerequisites

Python 3.8+
Docker
Git

Installation

Clone the repository:git clone https://github.com/RachitNigam19/Insurance-Premium-Predictor-API.git
cd Insurance-Premium-Predictor-API


Install Python dependencies:pip install -r requirements.txt


Build and run the Docker container:docker build -t insurance-predictor-api .
docker run -p 8000:8000 insurance-predictor-api



Usage

Run the FastAPI application locally:uvicorn app:app --reload


Access the API at http://localhost:8000.
Explore interactive API documentation at http://localhost:8000/docs.


Send a POST request to the prediction endpoint (e.g., /predict) with input data (refer to Pydantic_Schema for input format).
Use the trained model in the Model directory for predictions.

📂 Project Structure
Insurance-Premium-Predictor-API/
├── Model/                       # Trained ML model and related files
├── Pydantic_Schema/             # Pydantic models for data validation
├── config/                      # Configuration files for API and model
├── app.py                       # Main FastAPI application
├── Dockerfile                   # Docker configuration for containerization
├── requirements.txt             # Project dependencies
├── myenvv/                      # Virtual environment (excluded from Git)
├── __pycache__/                 # Python bytecode cache (auto-generated)

🔍 How It Works

Machine Learning Model: The Model directory contains a trained model (e.g., regression model) for predicting insurance premiums based on features like age, health, etc.
API Development: app.py defines FastAPI endpoints for receiving user input and returning predictions.
Data Validation: The Pydantic_Schema directory includes Pydantic models to validate incoming data and ensure reliable API responses.
Configuration: The config directory stores settings for the API and model (e.g., environment variables or hyperparameters).
Dockerization: The Dockerfile enables containerized deployment for consistent execution across environments.

🌟 Why This Project?

Demonstrates expertise in machine learning and API development with FastAPI.
Highlights proficiency in data validation using Pydantic.
Showcases DevOps skills with Docker for containerized deployments.
Reflects clean coding practices with a modular, well-organized codebase.
Provides a practical example of a real-world ML-driven application.

📫 Contact

GitHub: RachitNigam19
LinkedIn: Rachit Nigam
Email: rachitn46@gmail.com

Feel free to explore, contribute, or reach out for collaboration!
