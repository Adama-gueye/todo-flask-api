from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/todo_db"
db = SQLAlchemy(app)

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=True)
    done = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Enum('low', 'medium', 'high'), default='low')
    created_at = db.Column(db.DateTime, server_default=db.func.now())


@app.route('/tasks', methods=['GET'])
def get_tasks():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = Tasks.query.paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items
    tasks = Tasks.query.all()
    return jsonify({"tasks": [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done,
            'priority': task.priority,
            'created_at': task.created_at
        } for task in tasks],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page
    })

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_id(id):
    task = Tasks.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'done': task.done,
        'created_at': task.created_at
    })

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Tasks(
        title=data['title'],
        description=data.get('description', ''),
        done=data.get('done', False),
        created_at=db.func.now()

    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        'id': new_task.id,
        'title': new_task.title,
        'description': new_task.description,
        'done': new_task.done,
        'created_at': new_task.created_at
    }), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Tasks.query.get(id)
    data = request.get_json()
    if not task:
        return jsonify({"error": "Task not found"}), 404
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'done': task.done,
        'created_at': task.created_at
    },{
 
 "error": "Tâche non trouvée"}), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Tasks.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 204

@app.route('/tasksdone', methods=['GET'])
def get_tasksDone():
    tasks = Tasks.query.filter_by(done=True).all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'done': task.done,
        'created_at': task.created_at
    } for task in tasks])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
