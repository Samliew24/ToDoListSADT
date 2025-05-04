
from flask import Flask, render_template_string, request, redirect, abort

app = Flask(__name__)

# In-memory storage for tasks
tasks = []
task_id_counter = 1

# Basic HTML template
template = """
<!doctype html>
<title>To-Do List</title>
<h1>To-Do List</h1>
<form action="/add" method="post">
  <input type="text" name="title">
  <input type="submit" value="Add Task">
</form>
<ul>
  {% for task in tasks %}
    <li>
      {% if task.completed %}<strike>{{ task.title }}</strike>{% else %}{{ task.title }}{% endif %}
      <a href="/complete/{{ task.id }}">[Complete]</a>
      <a href="/delete/{{ task.id }}">[Delete]</a>
    </li>
  {% endfor %}
</ul>
"""

class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.completed = False

@app.route('/')
def index():
    return render_template_string(template, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form.get('title', '').strip()
    if not title:
        # Do nothing if title is empty
        return redirect('/')
    new_task = Task(task_id_counter, title)
    tasks.append(new_task)
    task_id_counter += 1
    return redirect('/')

@app.route('/complete/<int:id>')
def complete_task(id):
    for task in tasks:
        if task.id == id:
            task.completed = True
            break
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task.id != id]
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1>", 404

@app.errorhandler(405)
def method_not_allowed(e):
    return "<h1>405 - Method Not Allowed</h1>", 405

if __name__ == '__main__':
    app.run(debug=True)
