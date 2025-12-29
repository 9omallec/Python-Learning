"""
Flask Task Manager - Tutorial Application

This is your first Flask web application!
Follow along step-by-step to learn web development.
"""

from flask import Flask, render_template, request, redirect, url_for

# Create Flask application
app = Flask(__name__)

# Temporary storage for tasks (will reset when you restart the server)
# Later we'll replace this with a database
tasks = [
    {'id': 1, 'title': 'Learn Flask basics', 'completed': False},
    {'id': 2, 'title': 'Build a web app', 'completed': False},
    {'id': 3, 'title': 'Deploy to the internet', 'completed': False}
]

# Counter for task IDs
next_id = 4


# ============================================
# ROUTES (URLs)
# ============================================

@app.route('/')
def index():
    """
    Home page - displays all tasks

    How this works:
    1. User visits http://127.0.0.1:5000/
    2. Flask runs this function
    3. We render the index.html template with our tasks
    4. User sees the rendered HTML page
    """
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    """
    Add a new task

    How this works:
    1. User submits the form on the homepage
    2. Form data is sent as a POST request to /add
    3. We get the task title from the form
    4. We create a new task and add it to our list
    5. We redirect back to the homepage
    """
    global next_id

    # Get task title from the form
    title = request.form.get('title')

    # Only add if title is not empty
    if title:
        new_task = {
            'id': next_id,
            'title': title,
            'completed': False
        }
        tasks.append(new_task)
        next_id += 1

    # Redirect back to homepage
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """
    Mark a task as complete/incomplete

    How this works:
    1. User clicks "Complete" button
    2. Browser visits /complete/1 (where 1 is the task ID)
    3. We find the task with that ID
    4. We toggle its completed status
    5. We redirect back to homepage
    """
    # Find the task with this ID
    for task in tasks:
        if task['id'] == task_id:
            # Toggle completed status
            task['completed'] = not task['completed']
            break

    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """
    Delete a task

    How this works:
    1. User clicks "Delete" button
    2. Browser visits /delete/1 (where 1 is the task ID)
    3. We remove that task from the list
    4. We redirect back to homepage
    """
    global tasks

    # Remove task with this ID
    tasks = [task for task in tasks if task['id'] != task_id]

    return redirect(url_for('index'))


# ============================================
# RUN THE APPLICATION
# ============================================

if __name__ == '__main__':
    """
    This runs the Flask development server

    debug=True means:
    - Server restarts automatically when you change code
    - Detailed error messages in browser
    - DON'T use debug=True in production!
    """
    app.run(debug=True)


"""
============================================
EXERCISES TO TRY:
============================================

1. Add a "Clear All Completed Tasks" button

2. Add task priorities (high, medium, low)
   - Update the task dictionary to include priority
   - Show different colors for different priorities

3. Add a counter showing "X tasks remaining"

4. Add the ability to edit a task's title

5. Sort tasks by completed status (incomplete first)

6. Add a due date field to tasks

7. Style it to look amazing with CSS!

8. Add categories/tags to tasks

9. Add a search/filter feature

10. Save tasks to a file so they persist after restart
"""
