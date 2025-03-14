from flask import Blueprint, request, jsonify
from .service import add_course_service,get_all_courses_service

courses = Blueprint("courses", __name__,url_prefix="/api/courses")

@courses.route("/course-management/course", methods=["POST"])

def add_course():
    return add_course_service()

@courses.route("/course-management/get-all-courses", methods=["GET"])
def get_all_courses():
    return jsonify(get_all_courses_service())