# app.py
from flask import Flask
from app.app_creator import create_app
from app.index_blueprint import index_bp
from app.student_blueprint import student_bp
from app.courses_blueprint import courses_blueprint
from app.department_blueprint import departments_blueprint  
from app.faculty_blueprint import faculty_blueprint

app, db = create_app()

# Register blueprints
app.register_blueprint(index_bp, url_prefix='/')
app.register_blueprint(student_bp, url_prefix='/students')
app.register_blueprint(courses_blueprint, url_prefix='/courses')
app.register_blueprint(departments_blueprint, url_prefix='/departments')
app.register_blueprint(faculty_blueprint, url_prefix='/faculty')


# Other app initialization code...
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)