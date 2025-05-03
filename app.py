from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if not title or title.strip() == "":
        flash("Task title cannot be empty.")
        print("⚠️ Warning: Empty task submission attempted!")
        return redirect(url_for("home"))
    if len(title.strip()) > 50:
        flash("⚠️ Task title cannot exceed 50 characters.")
        print(f"⚠️  Warning: Task title too long ({len(title.strip())} characters). Submission rejected.")
        return redirect(url_for("home"))
    new_todo = Todo(title=title.strip(), complete=False)
    db.session.add(new_todo)
    db.session.commit()
    print(f"✅ Task added: {title.strip()}")
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.complete = not todo.complete
        db.session.commit()
        status = "Completed" if todo.complete else "Reopened"
        print(f"🔄 Task Updated: '{todo.title}' (ID: {todo_id}) is now {status}")
    else:
        print(f"⚠️  Warning: Tried to update non-existent task ID {todo_id}")
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
        print(f"🗑️  Task Deleted: '{todo.title}' (ID: {todo_id})")  # ✅ Log to terminal
    else:
        print(f"⚠️  Warning: Tried to delete non-existent task ID {todo_id}")  # ✅ Log warning if ID invalid
    return redirect(url_for("home"))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


