# 🎓 Smart FAQ AI Chatbot

[![Built with Flask](https://img.shields.io/badge/Built%20with-Flask-blue)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

An intelligent, lightweight Flask-based AI chatbot that answers student and alumni queries using smart fuzzy matching, Wikipedia, DuckDuckGo, and Google Search fallback mechanisms.


---

## 📚 Features
- 🎯 **Quick FAQs** via smart buttons (CGPA, Registration, Backlogs, Contact Info)
- 🎯 **Free text queries** with intelligent response matching
- 🎯 **Self-Learning Mode**: Unknown queries are **automatically logged** for admin review
- 🎯 **Admin Dashboard**: Admin can view unknown queries and **add new FAQs directly** from a secure panel
- 🎯 **Wikipedia fallback** for general queries
- 🎯 **DuckDuckGo Search** fallback for crisp answers
- 🎯 **Google Search** fallback if nothing found
- 🎯 **Fully responsive and aesthetic frontend**
- 🎯 **No external API keys required (safe public deployment)**

---

## ⚙️ Tech Stack
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Flask (Python)
- **AI/Logic:** 
  - FuzzyWuzzy (for smart matching)
  - Wikipedia API
  - DuckDuckGo Search
  - Google Search fallback
- **Database:** JSON files (for FAQs and logging unknown queries)

---

## 🛠️ How to Run Locally
1. Clone this repository:

```bash
git clone https://github.com/Taha-Gituser/Smart-FAQ-AI-Chatbot.git
cd Smart-FAQ-AI-Chatbot
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

To access Admin Panel:

```
http://127.0.0.1:5000/admin/dashboard
```

(Use predefined admin credentials if implemented.)

---

## 📁 Project Structure
```
Smart-FAQ-AI-Chatbot/
├── app.py
├── templates/
│   ├── index.html
│   ├── admin_login.html
│   └── admin_dashboard.html
├── static/
│   └── style.css
├── data/
│   ├── faq.json
│   └── unknown_queries.log
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🙌 Credits
Developed independently with ❤️ by [Taha](https://github.com/Taha-Gituser)

---
