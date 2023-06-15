from flask import Flask, request, jsonify, abort, make_response, render_template
from models import Student, student_schema, students_schema
import config

app = config.connex_app

@app.route("/api/student/", methods=['GET'])
def read_all():
    students=Student.query.all()
    return students_schema.dump(students)
@app.route("/api/student/<fname>/", methods=['GET'])
def read_one(fname):
    student=Student.query.filter(Student.firstname==fname).one_or_none()
    if student is not None:
        return student_schema.dump(student) 
    else:
        abort(404,f"Student with first name {fname} not found")
@app.route("/api/student/", methods=['POST'])
def create_new():
    student=request.get_json()
    student_name=student.get('firstname')
    student_check=Student.query.filter(Student.firstname==student_name).one_or_none()
    if student_check is None:
        new_student=student_schema.load(student, session=config.db.session)
        config.db.session.add(new_student)
        config.db.session.commit()
        return student_schema.dump(new_student), 201
    else:
        abort(406, f"Person with firstname {student_name} already exist")

@app.route("/api/student/<fname>/", methods=['DELETE'])
def delete_student(fname):
    student=Student.query.filter(Student.firstname==fname).one_or_none()
    if student is not None:
        config.db.session.delete(student)
        config.db.session.commit()
        return make_response(f"{fname} successfully deleted", 200)
    else:
        abort(404,f"Student with first name {fname} not found")
@app.route("/api/student/<fname>/", methods=['PUT'])
def update_student(fname):
    student=request.get_json()
    student_check=Student.query.filter(Student.firstname==fname).one_or_none()
    if student_check:
        update_student=student_schema.load(student, session=config.db.session)
        student_check.lastname=update_student.lastname
        config.db.session.merge(update_student)
        config.db.session.commit()
        return student_schema.dump(update_student), 201


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
