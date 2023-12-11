from flask import Flask, jsonify, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# In-memory data structures
todo_lists = {}
todos = {}


class TodoList:
    def __init__(self, name):
        self.id = str(len(todo_lists) + 1)
        self.name = name
        self.todos = []

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Todo:
    def __init__(self, description, todolist_id):
        self.id = str(len(todos) + 1)
        self.description = description
        self.completed = False
        self.todolist_id = todolist_id

    def to_dict(self):
        return {'id': self.id, 'description': self.description, 'completed': self.completed}


@app.route('/todos/<todolist_id>', methods=['POST'])
def create_todo(todolist_id):
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todolist = todo_lists.get(todolist_id)
        if todolist:
            todo = Todo(description=description, todolist_id=todolist_id)
            todolist.todos.append(todo)
            todos[todo.id] = todo
            body = todo.to_dict()
        else:
            error = True
    except:
        error = True

    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos', methods=['POST'])
def create_list():
    error = False
    body = {}
    try:
        name = request.get_json()['name']
        todolist = TodoList(name=name)
        todo_lists[todolist.id] = todolist
        body = todolist.to_dict()
    except:
        error = True

    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<list_id>/<todo_id>', methods=['PATCH'])
def update_todo(list_id, todo_id):
    error = False
    body = {}
    try:
        completed = request.get_json()['completed']
        todo = todos.get(todo_id)
        if todo and todo.todolist_id == list_id:
            todo.completed = completed
            body = {'completed': todo.completed}
        else:
            error = True
    except:
        error = True

    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<list_id>', methods=['PUT'])
def update_all(list_id):
    error = False
    body = {}
    try:
        todolist = todo_lists.get(list_id)
        if todolist:
            for todo in todolist.todos:
                todo.completed = True
            body = {'successful': not error}
        else:
            error = True
    except:
        error = True

    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<list_id>/<todo_id>', methods=["DELETE"])
def delete_todo(list_id, todo_id):
    error = False
    body = {}
    try:
        todo = todos.get(todo_id)
        if todo and todo.todolist_id == list_id:
            del todos[todo.id]
            todo_lists[list_id].todos.remove(todo)
            body = {'successful': not error}
        else:
            error = True
    except:
        error = True

    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<list_id>', methods=["DELETE"])
def delete_list(list_id):
    error = False
    body = {}
    try:
        todolist = todo_lists.get(list_id)
        if todolist:
            del todo_lists[list_id]
            body = {'successful': not error}
        else:
            error = True
    except:
        error = True

    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<list_id>')
def get_todo_list(list_id):
    if list_id in todo_lists:
        todolist = todo_lists[list_id]
        return render_template('index.html', data=todolist.todos, list_id=list_id, list=todo_lists.values(), name=todolist.name)
    else:
        return render_template('index.html', data=[], list_id='welcome', list=[], name='Starter Task')


@app.route('/')
def index():
    first_todolist = next(iter(todo_lists.values()), None)
    return redirect(url_for('get_todo_list', list_id=first_todolist.id if first_todolist else 'welcome'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
