from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Faculty, Department
from app.forms import FacultyForm

faculty_blueprint = Blueprint('faculty', __name__)

# Create

@faculty_blueprint.route('/faculty/new', methods=['GET', 'POST'])
def create_faculty():
    form = FacultyForm()
    form.faculty_dept_id.choices = [(d.department_id, d.department_name) for d in Department.query.all()]
    if request.method == 'POST' and form.validate_on_submit():
        faculty = Faculty(
            faculty_fname=form.faculty_fname.data,
            faculty_lname=form.faculty_lname.data,
            faculty_dept_id=form.faculty_dept_id.data
        )
        db.session.add(faculty)
        db.session.commit()
        if 'submit_and_add_another' in request.form:
            return redirect(url_for('faculty.create_faculty'))  # redirect to the create faculty page
        else:
            return redirect(url_for('faculty.list_faculty'))  # redirect to the faculty list page
    return render_template('create_faculty.html', form=form)  # pass the form to the template


# Read
@faculty_blueprint.route('/faculty/<int:faculty_id>')
def get_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    return render_template('faculty.html', faculty=faculty)

# Update
@faculty_blueprint.route('/faculty/<int:faculty_id>/edit', methods=['GET', 'POST'])
def update_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    if request.method == 'POST':
        faculty.faculty_fname = request.form['faculty_fname']
        faculty.faculty_lname = request.form['faculty_lname']
        faculty.faculty_dept_id = request.form['faculty_dept_id']
        db.session.commit()
        return redirect(url_for('faculty.get_faculty', faculty_id=faculty.faculty_id))
    return render_template('edit_faculty.html', faculty=faculty)

# Delete
@faculty_blueprint.route('/faculty/<int:faculty_id>/delete', methods=['POST'])
def delete_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    db.session.delete(faculty)
    db.session.commit()
    return redirect(url_for('faculty.list_faculty'))

# List
@faculty_blueprint.route('/faculty')
def list_faculty():
    faculties = Faculty.query.all()
    return render_template('faculty.html', faculties=faculties)