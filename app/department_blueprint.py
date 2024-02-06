# departments_blueprint.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import Department, db
from app.forms import DepartmentForm

departments_blueprint = Blueprint('departments', __name__)

@departments_blueprint.route('/departments', methods=['GET'])
def departments():
    departments = Department.query.all()
    return render_template('departments.html', departments=departments)

@departments_blueprint.route('/departments/new', methods=['GET', 'POST'])
def create_department_page():
    print("handling request")
    form = DepartmentForm()
    if form.validate_on_submit():
        print("Form validated")
        department = Department(department_name=form.department_name.data)
        try:
            db.session.add(department)
            db.session.commit()
            print("Department added to database")
            return redirect(url_for('departments.departments'))
        except Exception as e:
            print("Failed to add department: ", e)
            db.session.rollback()
    else:
        print("Form errors: ", form.errors)
    return render_template('create_department_page.html', form=form)

@departments_blueprint.route('/departments/<int:id>', methods=['GET', 'POST'])
def update_department(id):
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.department_name = form.department_name.data
        db.session.commit()
        return redirect(url_for('departments.departments'))
    return render_template('update_department.html', form=form)

@departments_blueprint.route('/departments/<int:id>/delete', methods=['POST'])
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for('departments.departments'))