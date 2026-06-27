<img width="1907" height="912" alt="image" src="https://github.com/user-attachments/assets/67a6a2aa-469b-4200-84f8-48c5bb4c02e4" />
<img width="1906" height="912" alt="image" src="https://github.com/user-attachments/assets/8823de50-d3f0-4abb-9f57-8eceaa85933f" />


# 🚀 Customer Churn Prediction MLOps

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql)

![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2?logo=mlflow)
![DagsHub](https://img.shields.io/badge/DagsHub-Versioning-4A4A4A)

![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Orchestration-2496ED?logo=docker)

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws)

![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-success)

---

## 📖 Overview

Customer Churn Prediction MLOps is a production-ready end-to-end Machine Learning Operations project that predicts customer churn using the **IBM Telco Customer Churn** dataset.

The project demonstrates the complete lifecycle of a machine learning application—from data ingestion and preprocessing to model training, experiment tracking, API development, containerization, CI/CD automation, and cloud deployment on AWS.

It follows software engineering and MLOps best practices, making it suitable for real-world deployment.

---

## 🎯 Business Problem

Customer churn directly affects business revenue and long-term customer retention.

By identifying customers who are likely to leave, organizations can take proactive actions such as personalized offers, targeted marketing campaigns, and improved customer support to reduce churn and increase customer lifetime value.

This project builds a machine learning solution capable of predicting customer churn based on customer demographics, account information, and service usage patterns.

---

# 🏗️ Project Architecture

```text
                      Customer Dataset
                              │
                              ▼
                    Data Ingestion Pipeline
                              │
                              ▼
                     Data Validation Pipeline
                              │
                              ▼
                  Data Transformation Pipeline
                              │
                              ▼
                      Model Training Pipeline
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
                  Docker & Docker Compose
                              │
                              ▼
                 GitHub Actions CI/CD Pipeline
                              │
                              ▼
                     AWS EC2 Cloud Deployment
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Machine Learning | Scikit-Learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Database | MySQL |
| Experiment Tracking | MLflow, DagsHub |
| API Development | FastAPI |
| Frontend | Streamlit |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions, Self-Hosted Runner |
| Cloud | AWS EC2 |

---

# 📂 Project Structure

```text
customer-churn-mlops
│
├── artifacts/
├── config/
├── docker/
├── logs/
├── notebooks/
├── src/
│   └── churn/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       ├── serving/
│       ├── frontend/
│       ├── utils/
│       ├── logger.py
│       └── exception.py
│
├── .github/
│   └── workflows/
├── docker-compose.yml
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

---

# ⚙️ Machine Learning Pipeline

### 📥 Data Ingestion

- Reads the IBM Telco Customer Churn dataset
- Stores the raw dataset inside the artifacts directory

---

### ✅ Data Validation

- Schema validation
- Missing value verification
- Data quality checks
- Dataset consistency verification

---

### 🔄 Data Transformation

- Data preprocessing
- Feature engineering
- Numerical feature scaling
- Categorical feature encoding

---

### 🤖 Model Training

The following machine learning algorithms were trained and evaluated:

- Logistic Regression
- Random Forest
- XGBoost

---

### 📊 Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

# 🏆 Model Performance

| Model | Test Accuracy | F1 Score |
|--------|--------------:|----------:|
| Logistic Regression | **79.99%** | **0.618** |
| Random Forest | 80.48% | 0.610 |
| XGBoost | 78.14% | 0.573 |

### ✅ Selected Model

**Logistic Regression**

---

# 📈 Experiment Tracking

The project uses **MLflow** integrated with **DagsHub** for experiment management.

Tracked artifacts include:

- Parameters
- Metrics
- Trained Models
- Training Runs
- Experiment History

---

# 🌐 REST API

## Health Check

```http
GET /
```

Response

```json
{
    "message": "Customer Churn API Running"
}
```

---

## Prediction Endpoint

```http
POST /predict
```

Users can upload customer datasets and receive churn predictions through the REST API.

---

# 💻 Streamlit Application

The project includes a user-friendly Streamlit interface that allows users to:

- Upload customer datasets
- Generate churn predictions
- View prediction results interactively

---

# 🐳 Docker

The application is fully containerized using Docker.

Services include:

- FastAPI Backend
- Streamlit Frontend

Run locally using:

```bash
docker compose up --build -d
```

---

# 🔄 CI/CD Pipeline

The deployment pipeline is fully automated using GitHub Actions.

```text
Developer Push
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ▼
Self-Hosted GitHub Runner
      │
      ▼
Docker Image Build
      │
      ▼
Docker Compose Deployment
      │
      ▼
AWS EC2 Server
```

---

# ☁️ AWS Deployment

Deployment Infrastructure:

- AWS EC2
- Docker Compose
- Self-Hosted GitHub Runner

Hosted Services:

- FastAPI Backend
- Streamlit Web Application

---

# ✨ Key Features

- Modular MLOps Architecture
- End-to-End Machine Learning Pipeline
- Custom Logging & Exception Handling
- MySQL Integration
- MLflow Experiment Tracking
- DagsHub Integration
- FastAPI REST API
- Interactive Streamlit Dashboard
- Dockerized Deployment
- Automated CI/CD Pipeline
- AWS EC2 Hosting

---

# 👨‍💻 Author

**Sudip Modak**

**MIS Analyst | Data Analyst | Aspiring Machine Learning Engineer**

📧 **LinkedIn:** *https://www.linkedin.com/in/sudip-modak-6173a9283*

💻 **GitHub:** https://github.com/SudipModak

---

⭐ **If you found this project useful, consider giving it a Star!**
````
