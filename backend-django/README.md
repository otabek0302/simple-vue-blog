# Django Backend - Simple Vue Blog

REST API backend for the Simple Vue Blog application built with Django and Django REST Framework.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Running the Server](#running-the-server)
- [Database](#database)

## ✨ Features

- User registration and authentication
- JWT token-based authentication
- Password reset via email
- CORS enabled for frontend integration
- RESTful API endpoints
- Custom middleware for request handling
- Secure password hashing

## 🚀 Installation

### 1. Navigate to backend directory

```bash
cd backend-django
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the backend-django directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Configuration (for password reset)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Frontend URL
FRONTEND_URL=http://localhost:5173
```

### CORS Configuration

CORS is configured in `settings.py` to allow requests from the frontend:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

## 📡 API Documentation

### Base URL

```
http://localhost:8000/api/
```

### Authentication Endpoints

#### 1. Register User

```http
POST /api/register/
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

#### 2. Login User

```http
POST /api/login/
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

#### 3. Forgot Password

```http
POST /api/forgot-password/
Content-Type: application/json

{
  "email": "john@example.com"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Password reset link sent to your email"
}
```

#### 4. Reset Password

```http
POST /api/reset-password/
Content-Type: application/json

{
  "token": "unique-reset-token",
  "password": "newsecurepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Password reset successfully"
}
```

## 📁 Project Structure

```
backend-django/
├── backend/
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── blog/
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── middleware.py        # Custom middleware
│   ├── models.py            # Database models (Users, Posts)
│   ├── permissions.py       # Custom permissions
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App URL configuration
│   ├── views.py             # API views
│   └── tests.py             # Unit tests
├── venv/                    # Virtual environment
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## 🗄️ Database

### Models

#### Users Model
```python
- id (Primary Key)
- username (CharField)
- email (EmailField, unique)
- password (CharField, hashed)
- password_reset_token (CharField, nullable)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

#### Posts Model (Coming Soon)
```python
- id (Primary Key)
- title (CharField)
- content (TextField)
- author (ForeignKey to Users)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### Migrations

Run migrations when models change:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🔧 Development

### Running Tests

```bash
python manage.py test
```

### Django Admin

Access the admin panel at `http://localhost:8000/admin/`

### Shell

Access Django shell:

```bash
python manage.py shell
```

## 📦 Dependencies

```txt
Django==5.2.7
djangorestframework==3.16.1
djangorestframework-simplejwt==5.5.1
django-cors-headers==4.9.0
Pillow==11.3.0
PyJWT==2.10.1
```

## 🛡️ Security

- Passwords are hashed using Django's default PBKDF2 algorithm
- JWT tokens for secure authentication
- CSRF protection enabled
- CORS configured for specific origins
- SQL injection protection via ORM

## 🐛 Troubleshooting

### Port already in use

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Database locked error

```bash
# Delete db.sqlite3 and migrations, then re-run migrations
rm db.sqlite3
python manage.py migrate
```

## 📝 API Testing

### Using cURL

```bash
# Register
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"test123"}'

# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

### Using Postman

Import the API endpoints and test them with Postman or any API client.

## 🤝 Contributing

1. Create a new branch for your feature
2. Make your changes
3. Write tests for your changes
4. Run tests and ensure they pass
5. Submit a pull request

## 👨‍💻 Developer

Developed by [@amonovotabek](https://github.com/otabek0302)

---

© 2025 Simple Vue Blog Backend. All rights reserved.

