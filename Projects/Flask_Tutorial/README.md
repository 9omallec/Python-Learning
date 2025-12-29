# Flask Web Development Tutorial

## What is Flask?
Flask is a lightweight Python web framework that lets you build websites and web applications. It's:
- Easy to learn (perfect for beginners)
- Widely used in the industry
- Great for both small and large projects

## What You'll Build
A simple **Task Manager** web app where you can:
- View a list of tasks
- Add new tasks
- Mark tasks as complete
- Delete tasks

This teaches you the fundamentals of web development!

## Setup Instructions

### 1. Create Virtual Environment
```bash
cd "c:\Users\CRO\Desktop\Python Learning\Projects\Flask_Tutorial"
python -m venv venv
```

### 2. Activate Virtual Environment
```bash
venv\Scripts\activate
```

### 3. Install Flask
```bash
pip install flask
```

### 4. Run the App
```bash
python app.py
```

Then open your browser to: `http://127.0.0.1:5000`

## Project Structure
```
Flask_Tutorial/
├── app.py              # Main Flask application
├── templates/          # HTML files
│   ├── base.html       # Base template
│   └── index.html      # Home page
├── static/            # CSS, JavaScript, images
│   └── style.css      # Styling
└── README.md          # This file
```

## Learning Path

### Phase 1: Basic Flask (Start Here!)
- [x] Install Flask
- [ ] Create a simple "Hello World" route
- [ ] Understand routes and views
- [ ] Render HTML templates
- [ ] Add CSS styling

### Phase 2: Dynamic Content
- [ ] Display a list of tasks
- [ ] Use Jinja2 templating (loops, conditionals)
- [ ] Pass data from Python to HTML

### Phase 3: Forms & User Input
- [ ] Create a form to add tasks
- [ ] Handle POST requests
- [ ] Add task to the list

### Phase 4: Data Persistence
- [ ] Store tasks in a list (temporary)
- [ ] Add "Mark Complete" functionality
- [ ] Add "Delete Task" functionality

### Phase 5: Database (Advanced)
- [ ] Install SQLite
- [ ] Create database models
- [ ] Save tasks to database permanently

## Key Concepts You'll Learn

1. **Routes** - URLs that trigger different functions
2. **Templates** - HTML files with dynamic content
3. **HTTP Methods** - GET (retrieve) vs POST (submit data)
4. **Forms** - Getting user input
5. **Sessions** - Remembering user data

## Common Commands

```bash
# Activate virtual environment
venv\Scripts\activate

# Install a package
pip install package-name

# See installed packages
pip list

# Run Flask app
python app.py

# Deactivate virtual environment
deactivate
```

## Next Steps After This Tutorial

1. **Add Features:**
   - Task priorities (high, medium, low)
   - Due dates
   - Categories/tags
   - Search functionality

2. **Deploy Online:**
   - Heroku (free tier)
   - PythonAnywhere
   - Render

3. **Build Another Project:**
   - Blog
   - Weather app (using APIs like your Pokedex!)
   - Personal portfolio
   - Note-taking app

## Resources

- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/)

## Troubleshooting

**Problem:** `flask` is not recognized
**Solution:** Make sure virtual environment is activated

**Problem:** Port already in use
**Solution:** Change port in app.py: `app.run(debug=True, port=5001)`

**Problem:** Changes not showing
**Solution:** Make sure `debug=True` is set, or hard refresh browser (Ctrl+F5)
