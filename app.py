from flask import Flask, render_template, request, redirect, url_for
from stack import Stack

app = Flask(__name__)
task_stack = Stack()

@app.route('/')
def index():
    next_task = task_stack.peek()
    return render_template('stack.html', tasks=task_stack.items, next_task=next_task)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        task_stack.push(task)
    return redirect(url_for('index'))

@app.route('/review', methods=['POST'])
def review_task():
    task_stack.pop()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
