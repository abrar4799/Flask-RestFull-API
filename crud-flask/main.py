from flask import Flask ,request
from flask_restful import Resource, Api , abort , reqparse
app = Flask(__name__)
api =Api(app)

Todos = {
    'todo1': {'task' : 'build an api' },
    'todo2':{'task': 'start session two'}
}
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in Todos:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

#provide simple and uniform access to any variable
#parser
parser = reqparse.RequestParser()
parser.add_argument('task')

#show single data item
class Todo(Resource):
    def get(self , todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return Todos[todo_id]
    def delete(self , todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del Todos[todo_id]
        return '',204
    def put(self , todo_id):
        args= parser.parse_args()
        task ={'task': args['task']}
        Todos[todo_id] = task
        return task , 201
class TodoList(Resource):
    def get(self):
        return Todos
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(Todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id   #concate
        Todos[todo_id] = {'task': args['task']}
        return Todos[todo_id], 201

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
if __name__ == '__main__':
    app.run(host='127.0.01' , port=5005, debug=True)




# @app.route('/')
# def hello_world():
#     return 'Hello World!'
