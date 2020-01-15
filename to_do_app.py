from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an api'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit'},
}

def abort_todo_if_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
    def get(self, todo_id):
        abort_todo_if_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_todo_if_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task':args['task']}
        TODOS[todo_id] = task
        return task, 201

class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 200

class Time(Resource):
    def get(self):
        return jsonify({"message":datetime.now()}), 200

class IP(Resource):
    def get(self):
        return request.environ.get('HTTP_X_REAL_IP',request.remote_addr), 200


api.add_resource(TodoList,'/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Time,'/time')
api.add_resource(IP,'/ip')

if __name__ == "__main__":
    app.run(debug=True)






