from library.extension import db
from library.library_ma import CourseSchema
from library.model import Courses
from flask import request,jsonify
import json

course_schema = CourseSchema
courses_schema = CourseSchema(many=True)

def add_course_service():
    course_sk = request.json['course_sk']
    course_name = request.json['course_name']
    try:
        new_course= Courses(course_sk,course_name)
        db.session.add(new_course)
        db.session.commit()
        return "Add success"
    except IndentationError:
        db.session.rollback()
        return "can not add course"
    
def get_all_courses_service():
    all_courses = Courses.query.all()
    course_schema = CourseSchema(many=True)
    return course_schema.dump(all_courses)
