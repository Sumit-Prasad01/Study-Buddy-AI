# 📚 Study Buddy AI

Study Buddy AI is an AI-powered learning assistant that helps users practice and evaluate their knowledge through **MCQ quizzes** and **Fill in the Blanks** questions.  
It generates questions using **LLMs (Groq - Llama 3.1)** via **LangChain**, evaluates user answers, provides performance insights, and exports a **report card in CSV format**.

This project also demonstrates a complete **DevOps + MLOps pipeline** using **Docker, Kubernetes (Minikube), Jenkins CI/CD, ArgoCD GitOps, Webhooks**, and deployment on **Google Cloud Platform (GCP VM)**.

---

## 🚀 Features

✅ Generate AI-based quizzes  
- **MCQ Questions (4 options each)**
- **Fill in the Blanks Questions**

✅ AI Evaluation of Answers  
- Checks correctness of answers
- Gives total correct and wrong answers

✅ Performance Report  
- Displays results in UI
- Exports results as a downloadable **CSV Report Card**

✅ Clean and smooth Streamlit UI

✅ Complete DevOps Pipeline  
- Dockerized application
- Kubernetes deployment (Minikube)
- Jenkins CI/CD pipeline
- GitHub Webhooks automation
- ArgoCD GitOps deployment
- Hosted on GCP VM

---

## 🧠 Tech Stack

### 🏗️ Core Development
- **Python**
- **Streamlit** (Frontend UI)
- **LangChain**
- **Groq API (Llama-3.1)**
- **Pydantic**
- **Pandas** (CSV report generation)

### ☁️ DevOps / Deployment
- **Docker**
- **Kubernetes (Minikube + kubectl)**
- **Jenkins**
- **ArgoCD**
- **GitHub Webhooks**
- **Google Cloud Platform (GCP VM)**

---

## 📂 Project Structure

```bash
Study-Buddy-AI/
│── src/
│   ├── common/
│   ├── config/
│   ├── generator/
│   ├── llm/
│   ├── models/
│   ├── prompts/
│   ├── utils/
│   └── __init__.py
│
│── manifests/              # Kubernetes manifests
│── results/                # Stores quiz results and CSV report cards
│── logs/                   # App logs
│── .env                    # Environment variables (DO NOT COMMIT)
│── .gitignore
│── application.py          # Streamlit entry point
│── Dockerfile
│── Jenkinsfile
│── requirements.txt
│── setup.py
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sumit-Prasad01/Study-Buddy-AI.git
cd Study-Buddy-AI
```

---

### 2️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.1-70b-versatile
```

⚠️ Never commit your `.env` file to GitHub.

---

## ▶️ Run the Application Locally

```bash
streamlit run application.py
```

Then open:

```
http://localhost:8501
```

---

## 🧪 How It Works

### 📌 Question Generation
Users enter a topic and difficulty level.  
The AI generates:

- **MCQs (4 options)**
- **Fill in the blanks questions**

### 📌 Answer Evaluation
User submits answers, and the AI evaluates them:

- Correct Answers Count
- Wrong Answers Count

### 📌 Report Card (CSV Export)
After evaluation, a report card is generated and saved in:

```bash
results/report_card.csv
```

The CSV contains:

- Question Type
- Question
- User Answer
- Correct Answer
- Result (Correct/Wrong)

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t study-buddy-ai .
```

### Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env study-buddy-ai
```

Now open:

```
http://localhost:8501
```

---

## ☸️ Kubernetes Deployment (Minikube)

### 1️⃣ Start Minikube

```bash
minikube start
```

### 2️⃣ Apply Kubernetes Manifests

```bash
kubectl apply -f manifests/
```

### 3️⃣ Check Pods

```bash
kubectl get pods
```

### 4️⃣ Access the Application

```bash
minikube service study-buddy-ai-service
```

---

## 🔁 Jenkins CI/CD Pipeline

This project includes a **Jenkinsfile** for automation.

### Pipeline Flow
1. Pull latest code from GitHub
2. Run tests (if configured)
3. Build Docker image
4. Push image to DockerHub
5. Update Kubernetes manifests (optional)
6. Trigger ArgoCD sync

---

## 🔗 GitHub Webhooks

GitHub Webhooks are configured so that whenever code is pushed:

- Jenkins pipeline is triggered automatically
- ArgoCD updates deployment based on GitOps

---

## 🚀 ArgoCD GitOps Deployment

ArgoCD continuously monitors Kubernetes manifests stored in GitHub and syncs deployments automatically.

### ArgoCD Installation (Example)

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Access ArgoCD UI

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open:

```
https://localhost:8080
```

---

## ☁️ Deployment on GCP VM

This project can be deployed on a **Google Cloud VM Instance**.

### Steps
1. Create VM on GCP
2. Install Docker, Minikube, kubectl
3. Setup Jenkins
4. Setup ArgoCD
5. Deploy application via Kubernetes manifests

---

## 📊 Example Output (Result Summary)

After quiz submission, the UI shows:

- ✅ Correct Answers: 7  
- ❌ Wrong Answers: 3  
- 📌 Total Questions: 10  

CSV report is generated and downloadable.

---

## 🛡️ Security Best Practices

- Never push API keys to GitHub
- Add `.env` to `.gitignore`
- Use GitHub Secrets / Jenkins Credentials Manager for storing keys
- Rotate keys immediately if leaked

---

## 📌 Future Improvements

- User authentication (login system)
- Leaderboard system
- Topic-wise analytics dashboard
- PDF report export
- Support for multiple LLM providers (OpenAI, Gemini, etc.)

---


