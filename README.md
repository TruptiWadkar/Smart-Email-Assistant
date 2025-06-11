# 📧 Smart Email Assistant

This project automates the handling of internal company emails using **Machine Learning (ML)** and **Generative AI (Google Gemini)**. Built as part of an AI assessment project, it classifies incoming emails, escalates low-confidence ones, and generates context-aware replies.

---

## 🎯 Objectives

- Classify internal emails as `HR`, `IT`, or `Other`.
- Automatically generate context-aware replies using a Generative AI model (Google Gemini).
- Escalate low-confidence or unclear emails for manual review.

---

## ⚙️ How It Works

### 🔹 Step 1: Email Classification Agent
- A **Logistic Regression** model is trained on synthetic HR/IT/Other emails.
- It predicts the category of a new incoming email.
- If `confidence >= 0.6` and the category is not `Other`, it proceeds to the response generator.

### 🔹 Step 2: Response Generator Agent
- Uses **Google Gemini 1.5 Flash API** to generate a polite, professional reply.
- Context is passed to the model through a structured prompt.

### 🔹 Step 3: Escalation Agent
- If the confidence is low (`< 0.6`) or the category is `Other`, the email is logged in `escalation_log.txt` for manual handling.

---
'''
## 🧱 Project Architecture

smart-email-assistant/
│
├── Agents/
│ ├── email_classifier.py
│ ├── response_generator.py
│ └── escalation_agent.py
│
├── models/
│ ├── email_classifier.pkl
│ └── vectorizer.pkl
│
├── smart_ui.py # Streamlit-based UI
├── orchestrator.py # Main controller script
├── emails.csv # Sample dataset
├── escalation_log.txt # Logged low-confidence/Other emails
├── requirements.txt
├── README.md
└── .gitignore
'''
---
## 💡 Features

- Simple **Streamlit UI** to test emails.
- Input box, category and confidence prediction.
- Editable AI-generated reply.
- Fallback logging for unhandled emails.

---

## 📦 Dependencies

Install all requirements using:

```bash
pip install -r requirements.txt
