# Simple Vue Blog

A modern, responsive blog application built with Vue 3, featuring a clean design and reusable UI components.

## 🚀 Features

- **Modern Vue 3** with Composition API
- **Responsive Design** with mobile-first approach
- **Reusable UI Components** (Button, Input, Text)
- **Form Validation** with proper autocomplete attributes
- **Code Formatting** with Prettier
- **Vue Router** for navigation
- **Floating Label Inputs** with smooth animations

## 🛠️ Tech Stack

- **Vue 3** - Progressive JavaScript framework
- **Vite** - Fast build tool and dev server
- **Vue Router** - Official router for Vue.js
- **Prettier** - Code formatter
- **CSS3** - Modern styling with animations

## 📁 Project Structure

```
src/
├── components/
│   ├── ui/           # Reusable UI components
│   │   ├── Button.vue
│   │   ├── Input.vue
│   │   └── Text.vue
│   └── layout/       # Layout components
│       ├── Header.vue
│       └── Footer.vue
├── views/            # Page components
│   ├── HomeView.vue
│   ├── LoginView.vue
│   ├── RegisterView.vue
│   └── ForgotPasswordView.vue
├── router/           # Vue Router configuration
└── assets/           # Static assets
```

## 🎨 UI Components

### Button Component
- Multiple variants: `primary`, `secondary`, `outline`, `success`, `danger`
- Loading state with spinner
- Disabled state support
- Custom class support

### Input Component
- Floating label animation
- Form validation support
- Autocomplete attributes
- Error state styling
- Multiple input types

### Text Component
- Semantic HTML elements (h1-h6, p, span, div, label)
- Color variants: `primary`, `title`, `subtitle`, `text`, `link`, `error`, `success`, `white`
- Text alignment: `left`, `center`, `right`, `justify`
- Text transform: `uppercase`, `lowercase`, `capitalize`
- Font weight: `bold`, `normal`, `light`

## 🚀 Getting Started

### Prerequisites

- Node.js (v20.19.0 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/otabek0302/simple-vue-blog.git
cd simple-vue-blog
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:5173`

## 📜 Available Scripts

- `npm run dev` - Start development server with hot reload
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run format` - Format code with Prettier
- `npm run format:check` - Check code formatting

## 🎯 Development Setup

### Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (disable Vetur if installed).

### Browser DevTools

- **Chrome/Edge**: [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
- **Firefox**: [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)

## 🔧 Configuration

- **Vite**: See [Vite Configuration Reference](https://vite.dev/config/)
- **Prettier**: Configured in `.prettierrc`
- **Vue Router**: Configured in `src/router/index.js`

## 📱 Responsive Design

The application is fully responsive and optimized for:
- Mobile devices (320px+)
- Tablets (768px+)
- Desktop (1024px+)

## 🎨 Design System

### Colors
- Primary: `#0057ff`
- Text: `#010101`, `#323232`, `#555555`
- Success: `#28a745`
- Error: `#dc3545`
- White: `#ffffff`

### Typography
- Font weights: 300 (light), 400 (normal), 600 (bold)
- Text transforms: uppercase, lowercase, capitalize
- Line height: 1.25

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Otabek**
- GitHub: [@otabek0302](https://github.com/otabek0302)

---

⭐ Star this repository if you found it helpful!
