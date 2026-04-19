# Apple TV+ Clone — Flask App

A simple Python/Flask web app inspired by Apple TV+, built for learning **GitHub Actions CI/CD**, **Docker**, and **Docker Compose**.

---

## Project Structure

```
appletv-project/
├── app.py                  # Flask application (main entry point)
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Home page with show grid
│   └── detail.html         # Show detail page
├── static/
│   ├── css/style.css       # Dark Apple TV+ styling
│   └── js/main.js          # Navbar scroll effect
├── Dockerfile              # YOU write this (see guide below)
├── docker-compose.yml      # YOU write this (see guide below)
└── .github/
    └── workflows/
        └── ci-cd.yml       # YOU write this (see guide below)
```

---

## Run Locally (Without Docker)

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

App will run at: http://localhost:5000

---

## Step 1 — Write Your Dockerfile

Create a file named `Dockerfile` in the project root:

```dockerfile
# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the app using gunicorn (production-grade server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

**Build and run manually:**

```bash
docker build -t appletv-app .
docker run -p 5000:5000 appletv-app
```

---

## Step 2 — Write Your docker-compose.yml

Create a file named `docker-compose.yml` in the project root:

```yaml
version: '3.9'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
```

**Run with Docker Compose:**

```bash
docker compose up --build
```

---

## Step 3 — Write Your GitHub Actions CI/CD Workflow

Create the file `.github/workflows/ci-cd.yml`:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:

  # ---- JOB 1: Test ----
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run basic health check
        run: |
          python -c "from app import app; print('App imported successfully')"

  # ---- JOB 2: Build Docker Image ----
  build:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: test           # Only runs if 'test' job passes

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t appletv-app:${{ github.sha }} .

      - name: Smoke test container
        run: |
          docker run -d -p 5000:5000 --name test-app appletv-app:${{ github.sha }}
          sleep 3
          curl --fail http://localhost:5000 || exit 1
          docker stop test-app

  # ---- JOB 3: Push to Docker Hub (on main branch only) ----
  push:
    name: Push to Docker Hub
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKER_USERNAME }}/appletv-app:latest
```

---

## Step 4 — Add GitHub Secrets (for Docker Hub Push)

1. Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add:
   - `DOCKER_USERNAME` → your Docker Hub username
   - `DOCKER_PASSWORD` → your Docker Hub password or access token

---

## Step 5 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Apple TV+ Flask app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Once pushed, go to your repo → **Actions** tab to watch the CI/CD pipeline run automatically!

---

## CI/CD Flow Summary

```
Push to GitHub
      |
      v
  [test job]          ← Installs deps, checks app imports
      |
      v
  [build job]         ← Builds Docker image, smoke tests it
      |
      v
  [push job]          ← Pushes image to Docker Hub (main branch only)
```

---

## Key Concepts You'll Learn

| Concept | What You Practice |
|---|---|
| **Dockerfile** | Containerizing a Python app |
| **Docker Compose** | Running multi-service apps locally |
| **GitHub Actions** | Automating build, test, and deploy |
| **Secrets** | Storing credentials safely |
| **Gunicorn** | Production-grade Python server |
| **CI/CD Pipeline** | Automated software delivery |

---

Happy Learning! 🚀
