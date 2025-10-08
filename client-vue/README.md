# Vue.js Frontend - Simple Vue Blog

Modern, responsive frontend application built with Vue.js 3, Vite, and Vuex for the Simple Vue Blog.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Design System](#design-system)
- [Components](#components)
- [State Management](#state-management)
- [Routing](#routing)
- [Development](#development)

## ✨ Features

- Modern UI with custom component library
- JWT authentication with persistent login
- Responsive design
- Toast notifications
- Form validation
- Password reset flow
- BEM methodology for CSS
- Vuex state management
- Vue Router navigation

## 🚀 Installation

### 1. Navigate to frontend directory

```bash
cd client-vue
```

### 2. Install dependencies

Using npm:
```bash
npm install
```

Using pnpm:
```bash
pnpm install
```

### 3. Run development server

```bash
npm run dev
# or
pnpm dev
```

The application will be available at `http://localhost:5173`

### 4. Build for production

```bash
npm run build
# or
pnpm build
```

## 📁 Project Structure

```
client-vue/
├── public/
│   └── favicon.ico
├── src/
│   ├── assets/
│   │   ├── images/
│   │   │   └── logo.png
│   │   └── styles/
│   ├── components/
│   │   ├── blocks/           # Block components
│   │   ├── layout/
│   │   │   ├── Header.vue    # App header
│   │   │   └── Footer.vue    # App footer
│   │   ├── ui/
│   │   │   ├── Button.vue    # Reusable button
│   │   │   ├── Input.vue     # Form input with floating label
│   │   │   └── Text.vue      # Typography component
│   │   └── index.js          # Component registration
│   ├── modules/
│   │   ├── authentication.js # Auth Vuex module
│   │   └── types.js          # Vuex getter types
│   ├── router/
│   │   └── index.js          # Vue Router configuration
│   ├── service/
│   │   ├── axios.js          # Axios configuration
│   │   └── authentication.js # Auth API service
│   ├── store/
│   │   └── index.js          # Vuex store configuration
│   ├── views/
│   │   ├── HomeView.vue
│   │   ├── LoginView.vue
│   │   ├── RegisterView.vue
│   │   ├── ForgotPasswordView.vue
│   │   ├── ResetPasswordView.vue
│   │   └── index.js
│   ├── App.vue               # Root component
│   └── main.js               # Application entry point
├── index.html
├── vite.config.js
├── package.json
├── jsconfig.json
└── README.md
```

## 🎨 Design System

### Color Palette

```css
/* Primary Colors */
--primary-blue: #0057ff;
--primary-blue-hover: #0041cc;

/* Text Colors */
--text-title: #010101;
--text-subtitle: #323232;
--text-body: #555555;
--text-muted: #666666;

/* Border */
--border-color: #e0e0e0;

/* Semantic Colors */
--success: #28a745;
--error: #dc3545;
--warning: #ffc107;
--white: #ffffff;
```

### Typography

```css
/* Font Sizes */
--font-size-sm: 12px;
--font-size-base: 16px;

/* Font Weights */
--font-light: 300;
--font-normal: 400;
--font-medium: 500;
--font-bold: 600;

/* Line Height */
--line-height: 1.25;
```

### Spacing

```css
/* Padding/Margin */
--space-xs: 8px;
--space-sm: 12px;
--space-md: 16px;
--space-lg: 32px;

/* Border Radius */
--radius-sm: 10px;
--radius-md: 12px;
--radius-lg: 16px;
```

### Layout

```css
/* Container */
--container-max-width: 1280px;
--form-max-width: 480px;

/* Padding */
--container-padding: 0 16px;
```

## 🧩 Components

### UI Components

#### Button Component

```vue
<Button 
  variant="outline" 
  type="submit" 
  :disabled="false"
  :loading="false"
>
  Click Me
</Button>
```

**Props:**
- `variant`: `primary` | `secondary` | `outline` | `success` | `danger`
- `type`: `button` | `submit` | `reset`
- `disabled`: Boolean
- `loading`: Boolean

#### Input Component

```vue
<Input 
  v-model="email"
  type="email"
  label="Email"
  placeholder="Enter your email"
  :error="errors.email"
  autocomplete="email"
/>
```

**Props:**
- `label`: String (required)
- `modelValue`: String | Number
- `type`: `text` | `email` | `password` | `number` | `tel` | `url`
- `placeholder`: String
- `error`: String
- `disabled`: Boolean
- `required`: Boolean
- `autocomplete`: String

#### Text Component

```vue
<Text 
  type="h3"
  variant="primary"
  weight="bold"
  align="center"
  transform="uppercase"
>
  Welcome
</Text>
```

**Props:**
- `type`: `p` | `h1` | `h2` | `h3` | `h4` | `h5` | `h6` | `span` | `div` | `label`
- `variant`: `primary` | `title` | `subtitle` | `text` | `link` | `error` | `warning` | `success` | `white`
- `align`: `left` | `center` | `right` | `justify`
- `transform`: `uppercase` | `lowercase` | `capitalize`
- `weight`: `bold` | `normal` | `light`
- `textStyle`: `italic` | `underline` | `no-decoration`

### Layout Components

#### Header Component
- Logo with navigation
- User authentication status
- Conditional navigation based on auth state

#### Footer Component
- Logo
- Developer credits
- Copyright information

## 🗄️ State Management

### Vuex Store Structure

```javascript
// Authentication Module
state: {
  user: null,           // Current user object
  tokens: null,         // JWT tokens (access & refresh)
  success: null,        // Success message
  error: null,          // Error message
  loading: false        // Loading state
}

getters: {
  IS_AUTHENTICATED,     // Check if user is logged in
  USER                  // Get current user
}

mutations: {
  SET_USER,             // Set user data
  SET_TOKENS,           // Set JWT tokens
  SET_SUCCESS,          // Set success message
  SET_ERROR,            // Set error message
  SET_LOADING,          // Set loading state
  LOGOUT                // Clear auth state
}

actions: {
  register,             // User registration
  login,                // User login
  forgotPassword,       // Request password reset
  resetPassword,        // Reset password
  logout,               // User logout
  initializeAuth        // Restore auth from localStorage
}
```

### Usage in Components

```javascript
// Dispatch action
await this.$store.dispatch('authentication/login', {
  email: 'user@example.com',
  password: 'password123'
});

// Access state
const user = this.$store.state.authentication.user;

// Use getter
const isAuthenticated = this.$store.getters['authentication/IS_AUTHENTICATED'];
```

## 🧭 Routing

### Routes

```javascript
[
  { path: '/', name: 'home', component: HomeView },
  { path: '/login', name: 'login', component: LoginView },
  { path: '/register', name: 'register', component: RegisterView },
  { path: '/forgot-password', name: 'forgot-password', component: ForgotPasswordView },
  { path: '/reset-password', name: 'reset-password', component: ResetPasswordView }
]
```

### Navigation

```vue
<!-- Using RouterLink -->
<RouterLink :to="{ name: 'login' }">Login</RouterLink>

<!-- Programmatic navigation -->
this.$router.push({ name: 'home' });
```

## 🔧 Development

### Environment Configuration

Create a `.env` file:

```env
VITE_API_BASE_URL=http://localhost:8000
```

### API Configuration

Located in `src/service/axios.js`:

```javascript
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth token
axiosInstance.interceptors.request.use(config => {
  const tokens = localStorage.getItem('tokens');
  if (tokens) {
    const { access } = JSON.parse(tokens);
    config.headers.Authorization = `Bearer ${access}`;
  }
  return config;
});
```

### Development Commands

```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

## 🎯 Best Practices

### BEM Methodology

```css
/* Block */
.login-view { }

/* Element */
.login-view__container { }
.login-view__form { }
.login-view__form-header { }

/* Modifier */
.login-view__button--disabled { }
```

### Component Naming

- PascalCase for component names
- Descriptive names (e.g., `LoginView`, `Button`, `Input`)
- Suffix views with `View`

### State Management

- Use Vuex for global state
- Use local state for component-specific data
- Actions for async operations
- Mutations for state changes

## 📦 Dependencies

```json
{
  "vue": "^3.x",
  "vue-router": "^4.x",
  "vuex": "^4.x",
  "axios": "^1.x",
  "vue-sonner": "^1.x",
  "vite": "^5.x"
}
```

## 🐛 Troubleshooting

### Port already in use

```bash
# Change port in vite.config.js
export default {
  server: {
    port: 3000
  }
}
```

### API connection issues

- Ensure backend is running on `http://localhost:8000`
- Check CORS settings in backend
- Verify API base URL in axios configuration

## 🔐 Authentication Flow

1. User registers/logs in
2. Backend returns JWT tokens + user data
3. Tokens and user stored in localStorage + Vuex
4. On page reload, `initializeAuth` restores state
5. Axios interceptor adds token to all requests
6. On logout, clear localStorage + Vuex state

## 🎨 Styling Guidelines

- Use scoped styles in components
- Follow BEM naming convention
- Use CSS variables for consistency
- Mobile-first responsive design
- Smooth transitions (0.3s ease)

## 🤝 Contributing

1. Follow the existing code style
2. Use BEM for CSS class names
3. Write descriptive commit messages
4. Test your changes thoroughly
5. Update documentation as needed

## 👨‍💻 Developer

Developed by [@amonovotabek](https://github.com/otabek0302)

---

© 2025 Simple Vue Blog Frontend. All rights reserved.
