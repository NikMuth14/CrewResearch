
# 🚀 CREWAI Basic Project Setup

This project demonstrates a basic setup using [CREWAI](https://github.com/joaomdmoura/crewAI), packaged in a Docker container.

---

## 📁 Project Structure

```
crew_basic/
├── .dockerignore        # Files/folders to exclude from Docker context
├── .env                 # Environment variables (e.g. API keys)
├── Dockerfile           # Docker configuration for building the app
├── main.py              # Your Python entry point
└── requirements.txt     # Python dependencies
```

---

## 🧱 Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- Python 3.12 (only if running locally without Docker)

---

## ⚙️ Configuration

Edit the `.env` file to include your environment variables. For example:

```env
CREWAI_API_KEY=your-crewai-key-here
OPENAI_API_KEY=your-openai-key-here
DEBUG=True
```

> **Note**: Never commit sensitive `.env` values to public repositories.

---

## 🐳 Running with Docker

### 1. Build the Docker image:

```bash
docker build -t crewai-app .
```

### 2. Run the container:

```bash
docker run --rm -it --env-file .env crewai-app
```

---

## 🧪 Running Locally (without Docker)

If you prefer to run it directly on your machine:

### 1. Create a virtual environment:

```bash
python -m venv venv
.env\Scriptsctivate  # Windows
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the app:

```bash
python main.py
```

---

## 🛠️ Customizing

Edit `main.py` to add agents, tasks, or any other CREWAI logic.
