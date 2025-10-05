[README.md](https://github.com/user-attachments/files/22705071/README.md)

# 🔐 Secure Web Form System

A student-friendly project that demonstrates **secure form handling** with Flask.  
This project shows **web security best practices** like CSRF protection, input validation, SQL injection prevention, password hashing, and rate limiting.

---

## ✨ Features
- Secure HTML form (Name, Email, Password, Comments)
- Flask backend with CSRF protection & validators
- Passwords stored with **bcrypt hashing**
- SQLite database with SQLAlchemy ORM
- Rate limiting (e.g., 5 submissions/min per IP)
- Logs suspicious inputs & failed attempts
- Admin dashboard with basic analytics

---

## 🛠️ Tech Stack
Flask | Flask-WTF | SQLAlchemy | Flask-Limiter | bcrypt

---

## 🚀 Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=app.app
flask run
```
Visit → http://localhost:5000/form

---

## 📂 Project Structure
```
secure-web-form/
  app/
    app.py            # Flask application
    models.py         # SQLAlchemy models
    forms.py          # WTForms for validation
  templates/
    form.html         # user form
    dashboard.html    # admin dashboard
  static/
    style.css         # styling
  requirements.txt
  README.md
```

---

## 📊 Why it’s valuable
This project is ideal for students to learn how to build a real-world secure web application. It highlights SWE + security practices and can be expanded (e.g., logging anomalies, Dockerizing, or adding a React frontend).

