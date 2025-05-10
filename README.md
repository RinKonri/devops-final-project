# DevOps Final Project – Flask + Redis + CI/CD

## 📌 Description

This is a simple DevOps project built as part of a final course assignment.  
The application consists of two connected containers:

- 🐍 **Flask application** — displays a visit counter
- 🐳 **Redis** — stores the number of visits

## ⚙️ Technologies Used

- Docker & Docker Compose
- Python (Flask)
- Redis
- GitHub Actions (CI/CD)
- Docker Volumes (persistent Redis data)

---

## 🚀 How to Run

1. Make sure you have Docker and Docker Compose installed
2. Clone the repository:

git clone https://github.com/RinKonri/devops-final-project.git
cd devops-final-project

    Build and start the services:

docker-compose up --build

    Open the application in your browser:

http://localhost:5000

🔄 CI/CD

This project uses GitHub Actions to automatically:

    Build the Docker image

    Start the container

    Test application availability

Workflow runs on each push to the main branch.
CI/CD file: .github/workflows/docker-build.yml

Live CI status: GitHub Actions
📦 Docker Volume

Redis uses a named volume (redis-data) to persist data between container restarts.

volumes:
  redis-data:

This ensures the counter value is saved even if the container stops or restarts.

👤 Author

    Name: Danial

    Course: Fundamentals of DevOps – Final Project
