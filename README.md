# Simple Vue Blog

A full-stack blog application built with Vue.js 3 and Django REST Framework.

## 📋 Project Structure

```
simple-vue-blog/
├── backend-django/          # Django REST API backend
├── client-vue/              # Vue.js 3 frontend
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or pnpm

### Backend Setup

```bash
cd backend-django
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will run on: `http://localhost:8000`

### Frontend Setup

```bash
cd client-vue
npm install  # or pnpm install
npm run dev  # or pnpm dev
```

Frontend will run on: `http://localhost:5173`

## 📚 Documentation

- [Backend Documentation](./backend-django/README.md)
- [Frontend Documentation](./client-vue/README.md)

## 🛠️ Tech Stack

### Backend
- Django 5.2.7
- Django REST Framework 3.16.1
- Simple JWT 5.5.1
- Django CORS Headers 4.9.0
- SQLite (development)

### Frontend
- Vue.js 3
- Vue Router 4
- Vuex 4
- Axios
- Vite
- Vue Sonner (Toast notifications)

## ✨ Features

- ✅ User authentication (Register, Login, Logout)
- ✅ Password reset functionality
- ✅ JWT token-based authentication
- ✅ Persistent login state
- ✅ Responsive design
- ✅ Toast notifications
- ✅ Modern UI with custom components

## 🔐 API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `POST /api/forgot-password/` - Request password reset
- `POST /api/reset-password/` - Reset password with token

## 📝 Development

### Backend Development
See [backend-django/README.md](./backend-django/README.md) for detailed backend development instructions.

### Frontend Development
See [client-vue/README.md](./client-vue/README.md) for detailed frontend development instructions.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Developer

Developed by [@amonovotabek](https://github.com/otabek0302)

---

© 2025 Simple Vue Blog. All rights reserved.
