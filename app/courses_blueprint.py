# app/courses_blueprint.py
from flask import Blueprint, render_template, request, jsonify, flash, url_for, redirect
from models import db, Course, Department
from app.forms import CourseForm  # Import the CourseForm

courses_blueprint = Blueprint('courses', __name__)

# Update the get_all_courses route
@courses_blueprint.route('/courses', methods=['GET'])
def get_all_courses():
    courses = Course.query.options(db.joinedload(Course.department)).all()
    return render_template('get_all_courses.html', courses=courses)

# Render the create course page
@courses_blueprint.route('/courses/create', methods=['GET', 'POST'])
def create_course_page():
    # Fetch any necessary data for the template (e.g., a list of existing courses and departments)
    courses = Course.query.all()
    departments = Department.query.all()

    # Create an instance of the CourseForm
    form = CourseForm()

    # Populate department choices
    form.department_id.choices = [(dept.department_id, dept.department_name) for dept in departments]

    if form.validate_on_submit():
        # If the form is submitted and valid, create a new course
        course_name = form.course_name.data
        department_id = form.department_id.data

        if not course_name:
            flash('Course name is required', 'error')
            return redirect(url_for('courses.create_course_page'))

        new_course = Course(course_name=course_name, department_id=department_id)
        db.session.add(new_course)
        db.session.commit()

        flash('Course created successfully', 'success')
        return redirect(url_for('courses.create_course_page'))

    return render_template('create_course.html', courses=courses, departments=departments, form=form)


# Render the update course page
@courses_blueprint.route('/courses/update/<int:course_id>', methods=['GET', 'POST'])
def update_course_page(course_id):
    course = Course.query.get(course_id)
    if not course:
        return render_template('course_not_found.html', course_id=course_id)

    form = CourseForm(obj=course)

    # Fetch department choices
    departments = Department.query.all()
    form.department_id.choices = [(dept.department_id, dept.department_name) for dept in departments]

    if request.method == 'POST':
        # Form submission
        if form.validate_on_submit():
            course.course_name = form.course_name.data
            course.department_id = form.department_id.data
            db.session.commit()

            flash('Course updated successfully', 'success')
            return redirect(url_for('courses.get_all_courses'))

    # GET request or form validation failed, render the update form
    return render_template('update_course.html', course=course, form=form)
