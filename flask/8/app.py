from flask import Flask, jsonify
from db import Session, Group, Student

app = Flask(__name__)


@app.route('/groups', methods=['GET'])
def get_groups():
    with Session() as session:
        groups = session.query(Group).all()
        result = [{'id': group.id, 'name': group.name} for group in groups]
        return jsonify(result)


@app.route('/students', methods=['GET'])
def get_students():
    with Session() as session:
        students = session.query(Student).all()
        result = [{'id': student.id, 'name': student.name,
                   'email': student.email} for student in students]
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
