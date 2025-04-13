# 🎥🧠 Real-Time Meeting Analysis & Summarization Tool

Welcome to the **Real-Time Meeting Analysis & Summarization Tool** – a full-stack AI-powered platform that transforms lengthy meetings into **smart, actionable summaries** in seconds. Built with **Django**, **MySQL**, **HTML/CSS/JS**, and **AI**, this tool enables real-time video uploads, intelligent processing, and crisp summarization.

---

## 🚀 Features

- 📹 **Video Upload** – Upload meetings and sessions directly via an intuitive UI.
- 🧠 **AI Summarization** – Automatically summarize long discussions using NLP.
- 🔍 **Keyword Extraction** – Get key takeaways and highlight important topics.
- 🛠 **Backend API** – Robust Django RESTful API integrated with MySQL database.
- 🌐 **Responsive UI** – Built with HTML, CSS, and JavaScript for a smooth experience.
- 🧾 **Downloadable Summary** – Export summaries for reports or sharing.

---

## 🛠️ Tech Stack

| Frontend       | Backend        | AI & Data        | DevOps |
|----------------|----------------|------------------|--------|
| HTML / CSS     | Django         | Python AI Models | Git    |
| JavaScript     | Django REST API| MySQL            | GitHub |

---

## 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/konar01official/Real-Time-Meeting-Analysis-Summarization-Tool.git
cd Real-Time-Meeting-Analysis-Summarization-Tool

# Create virtual environment & activate
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver
