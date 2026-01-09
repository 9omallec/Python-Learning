# Flask - Building Backend APIs

**Status**: Coming Soon (After you complete Python fundamentals)
**Estimated Time**: 2-3 weeks
**Prerequisites**: Lessons 1-13 complete

---

## 🎯 What You'll Learn

Flask is a lightweight Python web framework that lets you build REST APIs (backends) for your applications. This is what powers the backend of the Dex app.

**By the end, you'll be able to:**
- Create routes that respond to HTTP requests
- Build JSON APIs for your frontends
- Connect to databases to store data
- Handle user authentication
- Deploy your APIs online

---

## 📚 Learning Path

### Week 1: Flask Basics
- [ ] Setting up Flask projects
- [ ] Routes and decorators (`@app.route()`)
- [ ] Handling GET and POST requests
- [ ] Returning JSON responses
- [ ] Request parameters and data

### Week 2: Working with Data
- [ ] SQLite database basics
- [ ] Creating database models
- [ ] CRUD operations (Create, Read, Update, Delete)
- [ ] Error handling and validation
- [ ] Environment variables and config

### Week 3: Building Your First API
- [ ] Plan a simple API (todo list, notes, etc.)
- [ ] Implement all CRUD endpoints
- [ ] Test with Postman or curl
- [ ] Add basic security
- [ ] Deploy to Render or similar

---

## 🔍 Study the Dex App

Before starting these lessons, spend time studying the Dex app backend:

**Location**: `03_Study_This/Dex_Full_Stack_Example/app.py`

**What to look for:**
1. How routes are structured (`@app.route()`)
2. How JSON is returned (`jsonify()`)
3. How data is processed and formatted
4. Helper functions for modularity
5. Type effectiveness calculation logic

**Study exercise**: Read through `app.py` and try to understand:
- What does the `/api/pokemon/<name>` route do?
- How does `calculate_type_effectiveness()` work?
- How are moves filtered and sorted?

---

## 🎓 Your First Flask Project Ideas

After learning Flask, build one of these:

### 1. Todo API
- Create todos with title/description
- Mark todos as complete
- Delete todos
- Get all todos

### 2. Notes API
- Create/edit/delete notes
- Organize by tags or categories
- Search notes

### 3. Weather API Wrapper
- Wrap the OpenWeatherMap API
- Add caching to reduce API calls
- Format responses your way

### 4. Pokedex API
- Rebuild your Pokedex as a REST API
- Store favorite Pokemon in database
- Track stats and teams

---

## 📖 Resources

**Official Docs**: https://flask.palletsprojects.com/
**Deployment**: https://render.com (free tier available)

---

## ⏭️ After Flask

Once you complete Flask basics, you'll move to:
1. HTML/CSS - Building the interface
2. JavaScript - Making it interactive
3. Connecting your Flask API to your frontend

---

**Don't start this yet** - finish Python fundamentals first!
Once you're ready, lessons will be added here.
