# 🤖 AI Code Reviewer

An AI-powered code review system that analyzes code for syntax issues, logical errors, performance bottlenecks, and security vulnerabilities. It also integrates **OWASP ZAP** for automated security scanning and supports multiple programming languages including **Python**, **Java**, and **C++**.

---

## 🚀 Features

- ✅ **AI Code Analysis** using GPT-4 or Gemini
- 🧠 Detects **syntax & logical issues**
- ⚡ Recommends **performance optimizations**
- 🔐 **Security scanning** with OWASP ZAP
- 📘 **Explains code** in simple terms
- 🌐 RESTful API with **FastAPI**
- 📊 Streamlit-based **web UI**
- 🐳 Fully containerized using **Docker**
- 🛠 Supports **Python, Java, C++**

---

## 🧱 Tech Stack

| Layer       | Technology       |
|-------------|------------------|
| Backend     | FastAPI          |
| Frontend    | Streamlit        |
| AI Models   | GPT-4 / Gemini   |
| Security    | OWASP ZAP        |
| Deployment  | Docker, Docker Compose |
| Supported Langs | Python, Java, C++ |

---

## 📂 Project Structure

ai-code-reviewer/ │ ├── backend/ │ ├── main.py # FastAPI backend │ ├── code_analysis.py # AI-based code review logic │ └── zap_scanner.py # OWASP ZAP integration │ ├── frontend/ │ ├── app.py # Streamlit UI │ └── assets/ # Optional UI assets │ ├── docker-compose.yml # Multi-service orchestration ├── Dockerfile.backend # Backend Dockerfile ├── Dockerfile.frontend # Frontend Dockerfile