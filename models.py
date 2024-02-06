# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Gender(db.Model):
    __tablename__ = 'tbl_gender'
    gender_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender_name = db.Column(db.String(20), nullable=False)

class GradeLevel(db.Model):
    __tablename__ = 'tbl_grade_levels'  # Renamed from 'tbl_levels'
    grade_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade_name = db.Column(db.String(20), nullable=False)
    sections = relationship('Section', backref='grade_level', lazy=True)

class Course(db.Model):
    __tablename__ = 'tbl_courses'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('tbl_departments.department_id'), nullable=False)
    department = db.relationship('Department', backref='courses')
    sections = db.relationship('Section', backref='course', lazy=True)

class Section(db.Model):
    __tablename__ = 'tbl_sections'
    section_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    section_name = db.Column(db.String(20), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('tbl_courses.course_id'), nullable=False)
    grade_id = db.Column(db.Integer, db.ForeignKey('tbl_grade_levels.grade_id'), nullable=False)
    enrollments = relationship('Enrollment', backref='section', lazy=True)

class Student(db.Model):
    __tablename__ = 'tbl_student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_fname = db.Column(db.String(45), nullable=True)
    student_lname = db.Column(db.String(45), nullable=True)
    student_gender_id = db.Column(db.Integer, db.ForeignKey('tbl_gender.gender_id'), nullable=True)
    grade_level_id = db.Column(db.Integer, db.ForeignKey('tbl_grade_levels.grade_id'), nullable=True)   
    student_age = db.Column(db.Integer, nullable=True)
    enrollments = relationship('Enrollment', backref='student', lazy=True)

    # Define relationships
    gender = relationship(Gender, foreign_keys=[student_gender_id])
    grade_level = relationship(GradeLevel, foreign_keys=[grade_level_id])

class Enrollment(db.Model):
    __tablename__ = 'tbl_enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('tbl_student.student_id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('tbl_sections.section_id'), nullable=False)
    
class Department(db.Model):
    __tablename__ = 'tbl_departments'
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(50), nullable=False)

class Faculty(db.Model):
    __tablename__ = 'tbl_faculty'
    faculty_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    faculty_fname = db.Column(db.String(45), nullable=False)
    faculty_lname = db.Column(db.String(45), nullable=False)
    faculty_dept_id = db.Column(db.Integer, db.ForeignKey('tbl_departments.department_id'), nullable=False)

    # Define relationships
    department = db.relationship('Department', foreign_keys=[faculty_dept_id])
