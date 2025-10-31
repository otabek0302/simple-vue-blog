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
- Simple JWT 5.5.1 (Token authentication)
- Django CORS Headers 4.9.0
- Pillow 11.3.0 (Image processing)
- SQLite (development)
- Email backend (password reset)

### Frontend
- Vue.js 3 (Composition API)
- Vue Router 4
- Vuex 4 (Modular state management)
- Axios (HTTP client with interceptors)
- Vite (Build tool)
- Vue Sonner (Toast notifications)
- Font Awesome (Icons)

## ✨ Features

### Authentication & User Management
- ✅ User registration and login
- ✅ Password reset via email
- ✅ JWT token-based authentication with auto-refresh
- ✅ Persistent login state
- ✅ User profile management
- ✅ Avatar upload and removal
- ✅ Change password functionality
- ✅ Edit profile (username, email)

### Posts Management
- ✅ Create, read, update, and delete posts
- ✅ Post images with drag-and-drop upload
- ✅ View all posts on home page
- ✅ View user's own posts on profile page
- ✅ View liked posts on profile page
- ✅ Single post detail page
- ✅ Like/unlike posts
- ✅ Post search functionality
- ✅ Pagination for posts
- ✅ Loading skeletons for better UX

### Comments System
- ✅ Add comments to posts
- ✅ Edit own comments
- ✅ Delete own comments
- ✅ View all comments on post detail page

### UI/UX
- ✅ Responsive design (mobile-first)
- ✅ Toast notifications for all actions
- ✅ Modern card-based design
- ✅ Loading states and skeletons
- ✅ Search functionality with debouncing
- ✅ Image preview with uploader component
- ✅ Modal dialogs for forms
- ✅ Custom component library

## 🔐 API Endpoints

### Authentication
- `POST /api/v1/register/` - User registration
- `POST /api/v1/login/` - User login
- `POST /api/v1/forgot-password/` - Request password reset
- `POST /api/v1/reset-password/` - Reset password with token
- `PUT /api/v1/update-profile/` - Update user profile (username, email)
- `POST /api/v1/change-password/` - Change user password
- `POST /api/v1/update-avatar/` - Upload or remove avatar

### Posts
- `GET /api/v1/posts/` - List all posts (with pagination and search)
- `POST /api/v1/posts/` - Create a new post
- `GET /api/v1/posts/me/` - Get current user's posts
- `GET /api/v1/posts/others/` - Get posts from other users
- `GET /api/v1/posts/liked/` - Get liked posts by current user
- `GET /api/v1/posts/<id>/` - Get single post details
- `PUT /api/v1/posts/<id>/` - Update a post (owner only)
- `DELETE /api/v1/posts/<id>/` - Delete a post (owner only)
- `POST /api/v1/posts/<id>/like/` - Like a post
- `POST /api/v1/posts/<id>/unlike/` - Unlike a post
- `GET /api/v1/users/<user_id>/posts/` - Get posts by specific user

### Comments
- `GET /api/v1/posts/<post_id>/comments/` - Get comments for a post
- `POST /api/v1/posts/<post_id>/comments/` - Add a comment
- `GET /api/v1/comments/<id>/` - Get single comment
- `PUT /api/v1/comments/<id>/` - Update a comment (owner only)
- `DELETE /api/v1/comments/<id>/` - Delete a comment (owner only)

## 🗺️ Frontend Routes

- `/` - Home page (all posts)
- `/login` - User login
- `/register` - User registration
- `/forgot-password` - Request password reset
- `/reset-password` - Reset password with token
- `/profile` - User profile (posts, liked posts, settings)
- `/posts/:id` - Single post detail page with comments

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
