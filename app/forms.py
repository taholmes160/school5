# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from models import Gender, GradeLevel, Department

class StudentForm(FlaskForm):
    student_fname = StringField('First Name', validators=[DataRequired()])
    student_lname = StringField('Last Name', validators=[DataRequired()])
    student_age = IntegerField('Age', validators=[DataRequired()])
    
    # Update choices dynamically from the database
    student_gender_id = SelectField('Gender', coerce=int, validators=[DataRequired()])
    student_level_id = SelectField('Grade', coerce=int, validators=[DataRequired()])

    submit = SubmitField('Submit')


class CourseForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    department_id = SelectField('Department', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Course')

# forms.py

class DepartmentForm(FlaskForm):
    department_name = StringField('Department Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class FacultyForm(FlaskForm):
    faculty_fname = StringField('First Name', validators=[DataRequired()])
    faculty_lname = StringField('Last Name', validators=[DataRequired()])
    faculty_dept_id = SelectField('Department', coerce=int)  # remove choices from here
    submit = SubmitField('Submit')
    
    