# Phase 12: Deployment & MLOps (Days 151-180)

> Goal: Learn how to deploy AI/ML/GenAI applications into production using FastAPI, Docker, CI/CD, Cloud Platforms, Monitoring, Logging, and MLOps best practices.

---

# Overview

By the end of this phase, you will be able to:

✅ Build Production APIs using FastAPI

✅ Containerize applications using Docker

✅ Deploy AI Applications to Cloud

✅ Implement CI/CD using GitHub Actions

✅ Manage Environment Variables Securely

✅ Monitor Production Systems

✅ Version ML Models

✅ Build End-to-End AI Deployment Pipelines

✅ Become Job Ready for AI Engineer / GenAI Engineer Roles

---

# Skills You Will Learn

## Backend

- FastAPI
- REST APIs
- API Documentation
- Request Validation
- Authentication

## Deployment

- Docker
- Docker Compose
- Render
- Railway
- AWS Basics

## MLOps

- MLflow
- Model Versioning
- Experiment Tracking
- Data Versioning

## DevOps

- GitHub Actions
- CI/CD
- Linux Basics

## Monitoring

- Logging
- Error Tracking
- Performance Monitoring

---

# Week 1: FastAPI Fundamentals

---

# Day 151

## Topics

- What is FastAPI?
- Why FastAPI for AI?
- Installation
- Project Structure

## Install

```bash
pip install fastapi uvicorn
```

## Create First API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello World"}
```

## Assignment

Build:

- Hello API

---

# Day 152

## Topics

- GET Requests
- Query Parameters

```python
@app.get("/user")
def user(name:str):
    return {"name":name}
```

## Assignment

Build:

- User Information API

---

# Day 153

## Topics

- POST Requests
- Request Body

```python
from pydantic import BaseModel
```

## Assignment

Build:

- Student Registration API

---

# Day 154

## Topics

- PUT Requests
- DELETE Requests

## Assignment

Build:

- Student CRUD API

---

# Day 155

## Topics

- Path Parameters
- Validation

## Assignment

Extend CRUD API

---

# Day 156

## Topics

- API Documentation

FastAPI Auto Generates:

```text
/docs
/redoc
```

## Assignment

Explore Swagger Documentation

---

# Day 157

## Project

Build:

# Task Manager API

Features

- Add Task
- Update Task
- Delete Task
- Get Tasks

---

# Week 2: FastAPI + Database

---

# Day 158

## Topics

- SQLAlchemy Basics

Install

```bash
pip install sqlalchemy
```

## Assignment

Create Database Connection

---

# Day 159

## Topics

- Models
- Tables

## Assignment

Create User Table

---

# Day 160

## Topics

- Relationships

Learn

- One To One
- One To Many

---

# Day 161

## Topics

- CRUD with Database

## Assignment

Store Tasks in Database

---

# Day 162

## Topics

- Dependency Injection

FastAPI Dependency System

---

# Day 163

## Topics

- Pagination

## Assignment

Add Pagination

---

# Day 164

## Mini Project

Task Manager API + MySQL

---

# Week 3: Docker

---

# Day 165

## Topics

- What is Docker?
- Containers vs Virtual Machines

## Learn

```bash
docker --version
```

---

# Day 166

## Topics

- Docker Images
- Docker Containers

Commands

```bash
docker build
docker run
```

---

# Day 167

## Topics

- Dockerfile

Example

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app"]
```

---

# Day 168

## Assignment

Containerize FastAPI Project

---

# Day 169

## Topics

- Docker Volumes

---

# Day 170

## Topics

- Docker Compose

Example

```yaml
version: "3"
```

---

# Day 171

## Mini Project

FastAPI + MySQL + Docker

---

# Week 4: Cloud Deployment

---

# Day 172

## Topics

- Deployment Basics
- Environment Variables

Learn

```env
API_KEY=
DB_URL=
```

---

# Day 173

## Deploy on Render

Learn

- Create Service
- Environment Variables

Assignment

Deploy API

---

# Day 174

## Deploy on Railway

Assignment

Deploy Database Project

---

# Day 175

## Deploy GenAI Project

Deploy:

- Chatbot API

---

# Day 176

## AWS Basics

Learn

- EC2
- S3
- IAM

Interview Questions

- What is EC2?
- What is S3?

---

# Day 177

## Assignment

Deploy Dockerized App

---

# Week 5: CI/CD + GitHub Actions

---

# Day 178

## Topics

- What is CI/CD?

Learn

- Continuous Integration
- Continuous Deployment

---

# Day 179

## GitHub Actions

Create

```yaml
.github/workflows/deploy.yml
```

Example

```yaml
name: Deploy
```

---

# Day 180

# Final Capstone

## Production AI Deployment System

Features

### Backend

- FastAPI

### AI

- OpenAI API

### Database

- PostgreSQL

### Deployment

- Docker

### CI/CD

- GitHub Actions

### Hosting

- Render

### Monitoring

- Logging

---

# MLOps Section

---

# Learn MLflow

## Why

Track Experiments

Install

```bash
pip install mlflow
```

Topics

- Experiment Tracking
- Metrics
- Parameters
- Model Registry

---

# Learn Model Versioning

Tools

- MLflow
- DVC

---

# Learn Data Versioning

Tool

- DVC

Install

```bash
pip install dvc
```

---

# Logging

Learn

```python
import logging
```

Topics

- INFO
- WARNING
- ERROR

---

# Monitoring

Learn

- Application Monitoring
- API Monitoring
- Uptime Monitoring

Tools

- Prometheus
- Grafana

---

# Production Architecture

```text
User
 |
FastAPI
 |
Authentication
 |
Business Logic
 |
OpenAI/Gemini
 |
Vector Database
 |
PostgreSQL
 |
Monitoring
 |
Docker
 |
Cloud
```

---

# Deployment Projects

## Beginner

1. FastAPI CRUD API

2. Notes API

3. Student Management API

---

## Intermediate

4. Authentication API

5. Task Manager API

6. Blog API

---

## Advanced

7. AI Chatbot API

8. RAG API

9. Multi-Agent API

10. AI Interview Assistant

---

# Interview Questions

## FastAPI

1. Why FastAPI?
2. Difference between Flask and FastAPI?
3. What is Dependency Injection?
4. What is Pydantic?
5. How does FastAPI handle validation?

---

## Docker

1. What is Docker?
2. What is a Container?
3. What is Dockerfile?
4. Difference between Image and Container?
5. What is Docker Compose?

---

## CI/CD

1. What is CI/CD?
2. Why GitHub Actions?
3. What is Pipeline?

---

## AWS

1. What is EC2?
2. What is S3?
3. What is IAM?

---

## MLOps

1. What is MLOps?
2. What is MLflow?
3. What is Model Versioning?
4. What is Data Versioning?
5. What is Experiment Tracking?

---

# GitHub Repository Structure

```text
Phase-12-Deployment-MLOps/
│
├── Day151-HelloAPI
├── Day152-QueryParameters
├── Day153-PostRequests
├── Day154-CRUDAPI
├── Day157-TaskManagerAPI
│
├── Day164-FastAPI-MySQL
│
├── Day168-Dockerized-App
├── Day171-Docker-Compose
│
├── Day173-Render-Deployment
├── Day174-Railway-Deployment
│
├── Day179-GitHub-Actions
│
└── Day180-Capstone-Deployment
```

---

# Phase 12 Completion Checklist

- [ ] FastAPI Mastery
- [ ] REST API Development
- [ ] Database Integration
- [ ] Docker Fundamentals
- [ ] Docker Compose
- [ ] Render Deployment
- [ ] Railway Deployment
- [ ] AWS Basics
- [ ] GitHub Actions
- [ ] CI/CD Pipeline
- [ ] MLflow
- [ ] Logging
- [ ] Monitoring
- [ ] Production AI Deployment

---

# Milestone Achieved

After completing Phase 12, you will be able to:

- Build Production APIs
- Deploy AI Applications
- Containerize Projects
- Create CI/CD Pipelines
- Manage MLOps Workflows
- Deploy RAG Systems
- Deploy Agentic AI Applications
- Work as a Junior AI Engineer / GenAI Engineer / AI Application Engineer