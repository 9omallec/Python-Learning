# HTML/CSS - Building User Interfaces

**Status**: Coming Soon (After Flask basics)
**Estimated Time**: 3-4 weeks
**Prerequisites**: Flask fundamentals complete

---

## 🎯 What You'll Learn

HTML/CSS is how you build the visual interface that users see and interact with. No more tkinter - you'll build modern, responsive web UIs.

**By the end, you'll be able to:**
- Structure web pages with semantic HTML
- Style interfaces with modern CSS
- Create responsive layouts (flexbox, grid)
- Build glassmorphism effects like in the Dex app
- Make interfaces that work on any screen size

---

## 📚 Learning Path

### Week 1: HTML Fundamentals
- [ ] HTML structure (DOCTYPE, head, body)
- [ ] Semantic tags (header, nav, main, footer, section, article)
- [ ] Forms and inputs
- [ ] Links and buttons
- [ ] Lists and tables
- [ ] Images and media

### Week 2: CSS Basics
- [ ] CSS syntax (selectors, properties, values)
- [ ] Colors and typography
- [ ] Box model (margin, border, padding, content)
- [ ] Display and positioning
- [ ] CSS units (px, rem, %, vh/vw)

### Week 3: Modern CSS Layouts
- [ ] Flexbox (1D layouts)
- [ ] Grid (2D layouts)
- [ ] Responsive design (media queries)
- [ ] CSS variables (custom properties)
- [ ] Transitions and animations

### Week 4: Advanced Effects
- [ ] Glassmorphism (backdrop-filter, blur)
- [ ] Gradients and shadows
- [ ] Pseudo-elements and pseudo-classes
- [ ] Dark mode implementation
- [ ] Accessibility basics

---

## 🔍 Study the Dex App

Before starting these lessons, study the Dex app frontend:

**Location**: `03_Study_This/Dex_Full_Stack_Example/`
- **HTML**: `templates/index.html`
- **CSS**: `static/css/style.css`

**What to look for:**

### In index.html:
1. Semantic HTML structure (header, main, aside, section)
2. How forms and inputs are structured
3. Data attributes for JavaScript hooks
4. How the layout is organized

### In style.css:
1. CSS variables for theming (`--bg-gradient-1`, etc.)
2. Glassmorphism effect (`.glass-effect` class)
3. Flexbox layouts (team builder sidebar)
4. Dark mode implementation
5. Pokemon type color gradients
6. Animations (slideIn, fadeIn, pulse)

**Study exercise**:
- Find the `.glass-effect` class - what properties make it work?
- How is dark mode implemented? (hint: look at `:root` and `body.dark-mode`)
- Pick a Pokemon type gradient - how is it created?

---

## 🎓 Your First HTML/CSS Projects

### 1. Personal Landing Page
- About section
- Skills showcase
- Links to projects
- Contact information

### 2. Pokedex UI (Static)
- Design the interface in HTML/CSS
- No functionality yet - just the look
- Practice glassmorphism and animations

### 3. Todo App UI
- Input for new todos
- List display
- Filter buttons (all/active/completed)
- No functionality yet - pure HTML/CSS

---

## 🎨 Design Inspiration

**Glassmorphism Examples**:
- https://hype4.academy/tools/glassmorphism-generator
- https://ui.glass/generator/

**Color Palettes**:
- https://coolors.co
- https://colorhunt.co

**Layout Inspiration**:
- https://dribbble.com
- https://codepen.io (search for CSS layouts)

---

## 📖 Key Concepts to Master

### HTML:
- **Semantic tags** - Use the right tag for the job
- **Forms** - Inputs, labels, validation
- **Accessibility** - Alt text, ARIA labels, keyboard navigation

### CSS:
- **Specificity** - Which styles take precedence
- **Box model** - How sizing works
- **Flexbox vs Grid** - When to use each
- **Responsive design** - Mobile-first approach
- **CSS variables** - Reusable values for theming

---

## 🛠️ Tools You'll Use

- **Browser DevTools** - Inspect and debug (F12 or Ctrl+Shift+I)
- **VS Code extensions** - Live Server, HTML/CSS preview
- **Online tools** - Gradient generator, shadow generator

---

## ⏭️ After HTML/CSS

Once you complete HTML/CSS basics, you'll move to:
1. JavaScript - Add interactivity and connect to your Flask APIs
2. Full-stack project - Bring everything together

---

**Don't start this yet** - finish Flask first!
Once you're ready, lessons will be added here.
