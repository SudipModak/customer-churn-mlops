# Customer Churn Prediction MLOps Project

## Overview

This project is an end-to-end Machine Learning Operations (MLOps) solution for predicting customer churn using the IBM Telco Customer Churn dataset.

The project covers the complete ML lifecycle including data ingestion, validation, transformation, model training, experiment tracking, containerization, CI/CD automation, and cloud deployment on AWS EC2.

---

## Business Problem

Customer churn directly impacts business revenue and customer retention strategies.

The objective of this project is to predict whether a customer is likely to leave a telecom service provider based on customer demographics, account information, and service usage patterns.

---

## Project Architecture

```text
Customer Data
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
MLflow + DagsHub Tracking
      │
      ▼
FastAPI Backend
      │
      ▼
Streamlit Frontend
      │
      ▼
Docker Containers
      │
      ▼
GitHub Actions CI/CD
      │
      ▼
AWS EC2 Deployment
```

---

## Tech Stack

### Programming

* Python

### Machine Learning

* Scikit-Learn
* XGBoost

### Data Processing

* Pandas
* NumPy

### Database

* MySQL

### Experiment Tracking

* MLflow
* DagsHub

### API Development

* FastAPI

### Frontend

* Streamlit

### Containerization

* Docker
* Docker Compose

### CI/CD

* GitHub Actions
* Self-Hosted GitHub Runner

### Cloud

* AWS EC2

---

## Project Structure

```text
customer-churn-mlops
│
├── artifacts
├── config
├── logs
├── notebooks
├── src
│   └── churn
│       ├── components
│       ├── config
│       ├── constants
│       ├── entity
│       ├── pipeline
│       ├── serving
│       ├── frontend
│       ├── utils
│       ├── logger.py
│       └── exception.py
│
├── docker
├── .github
│   └── workflows
├── requirements.txt
├── setup.py
├── pyproject.toml
└── docker-compose.yml
```

---

## Machine Learning Pipeline

### Data Ingestion

* Reads customer churn data
* Stores raw dataset in artifacts

### Data Validation

* Schema validation
* Missing value checks
* Data quality verification

### Data Transformation

* Feature preprocessing
* Numerical scaling
* Categorical encoding

### Model Training

Models trained:

* Logistic Regression
* Random Forest
* XGBoost

### Model Evaluation

Performance metrics:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Best Performing Model

| Model               | Test Accuracy | F1 Score |
| ------------------- | ------------- | -------- |
| Logistic Regression | 79.99%        | 0.618    |
| Random Forest       | 80.48%        | 0.610    |
| XGBoost             | 78.14%        | 0.573    |

Selected Model: **Logistic Regression**

---

## Experiment Tracking

All experiments are tracked using:

* MLflow
* DagsHub

Tracked artifacts:

* Parameters
* Metrics
* Models
* Training Runs

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Customer Churn API Running"
}
```

### Prediction Endpoint

```http
POST /predict
```

Upload customer data file and receive churn predictions.

---

## Frontend Application

The project includes a Streamlit-based user interface that allows users to:

* Upload customer datasets
* Generate predictions
* View churn results

---

## Dockerization

The application is fully containerized.

Containers:

* FastAPI Service
* Streamlit Service

Run locally:

```bash
docker compose up --build -d
```

---

## CI/CD Pipeline

Deployment is automated using GitHub Actions.

Workflow:

```text
Developer Push
      │
      ▼
GitHub Actions
      │
      ▼
Self-Hosted Runner
      │
      ▼
Docker Build
      │
      ▼
Container Deployment
      │
      ▼
AWS EC2
```

---

## AWS Deployment

Deployment Infrastructure:

* AWS EC2
* Docker Compose
* Self-Hosted GitHub Runner

Public Services:

* FastAPI API
* Streamlit Web Application

---

## Key Features

* Modular ML pipeline
* Custom logging and exception handling
* MySQL integration
* MLflow experiment tracking
* DagsHub integration
* FastAPI serving layer
* Streamlit frontend
* Dockerized deployment
* GitHub Actions CI/CD
* AWS EC2 hosting

---

## Future Improvements

* Model Monitoring
* Data Drift Detection
* Automated Retraining
* Kubernetes Deployment
* AWS ECR/ECS Integration
* Prometheus & Grafana Monitoring

---

## Author

**Sudip Modak**

MIS Analyst | Data Analyst | Aspiring Machine Learning Engineer

GitHub: https://github.com/SudipModak
