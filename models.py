from datetime import datetime
from config import db, ma

class Student(db.Model):
    __tablename__ = "student_data"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    bio = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Student {self.firstname}>'

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Student
        load_instance=True
        sqla_session=db.session
student_schema=StudentSchema()
students_schema=StudentSchema(many=True)
