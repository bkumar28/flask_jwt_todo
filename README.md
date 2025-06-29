# 🛡️ Flask JWT ToDo API

A simple, secure, and RESTful ToDo API built with **Flask**, featuring **JWT-based authentication**.  
This app allows users to sign up, log in, reset their passwords, and perform full CRUD operations on user data after authentication.

---

## ✨ Features

- ✅ User Signup & Login (JWT Authentication)
- 🔐 Password Reset and Logout
- 📋 ToDo CRUD Operations (Create, Read, Update, Delete)
- 🧰 Built with Flask-RESTful, Flask-JWT-Extended, SQLAlchemy, and PostgreSQL
- 🧪 Easy setup with virtual environment and Alembic for migrations

---

## 🛠️ Tech Stack

- Python 3.x
- Flask & Flask-RESTful
- Flask-JWT-Extended
- PostgreSQL
- SQLAlchemy
- Alembic (for DB migrations)

---

## 📦 Project Structure

```bash
flask-jwt-todo/
├── app/
│   ├── models/
│   ├── resources/
│   ├── __init__.py
│   └── app.py
├── migrations/
├── manage.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-jwt-todo.git
cd flask-jwt-todo
```

### 2. Create and Activate a Virtual Environment

```bash
virtualenv -p python3 venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate a Secret Key

```bash
python
>>> import os
>>> os.urandom(24)
# Copy the output and set it in your config.py or environment
```

---

## 🗃️ Database Setup

### PostgreSQL Setup

1. Create a PostgreSQL database manually or using a tool like `psql` or PgAdmin.

```sql
CREATE DATABASE flask_jwt_todo;
```

2. Update your `config.py` with the DB URI, e.g.:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/flask_jwt_todo'
```

---

## 🔄 Migrations

### Using Alembic

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Or Manually Create Tables

```python
python
>>> from app.app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> db.session.commit()
```

---

## 🔐 API Endpoints (Overview)

| Method | Endpoint           | Description                    |
|--------|--------------------|--------------------------------|
| POST   | `/signup`          | Create a new user              |
| POST   | `/login`           | Authenticate user and return JWT |
| POST   | `/reset-password`  | Send password reset (mock)     |
| POST   | `/logout`          | Invalidate token (blacklist)   |
| GET    | `/users`           | Get list of users (auth)       |
| POST   | `/users`           | Create new user (auth)         |
| PUT    | `/users/<id>`      | Update user (auth)             |
| DELETE | `/users/<id>`      | Delete user (auth)             |

---

## ✅ Example Usage (with curl)

```bash
# Sign Up
curl -X POST http://localhost:5000/signup -H "Content-Type: application/json" \
-d '{"username": "john", "password": "doe123"}'

# Login and receive JWT token
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" \
-d '{"username": "john", "password": "doe123"}'
```

---

## 🧪 Run the Application

```bash
python manage.py run
# or, if using app.py directly
python app/app.py
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Contributions

Feel free to open issues, submit PRs, or fork and customize the project for your own use.

---

## 👨‍💻 Maintainer

**Bharat Kumar**  
_Senior Software Engineer | Cloud & Backend Systems_  
📧 kumar.bhart28@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/bharat-kumar28)
