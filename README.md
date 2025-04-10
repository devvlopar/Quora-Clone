Quora Clone - Django Assignment

This is a simple Quora-like web application built using Django.

---

## ✨ Features

- User Registration and Login
- Post Questions
- View Questions from Others
- Answer Questions
- Like/Unlike Answers
- Logout Functionality

---

## 🛠 Tech Stack

- Python 3
- Django (4+)
- SQLite (default database)
- Django Forms & Auth
- HTML (basic templates)

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/devvlopar/Quora-Clone.git
cd Quora-Clone

### 2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Requirements
pip install -r requirements.txt

### 4. Apply Migrations
python manage.py migrate

### 5. Open in Browser
Visit: http://127.0.0.1:8000

📂 Project Structure

Quora-Clone/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── question_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
