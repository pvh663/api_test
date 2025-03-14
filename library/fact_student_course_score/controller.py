from flask import Blueprint, request, jsonify
from .service import get_student_course_score

fact_student_course_scores = Blueprint("fact_student_course_score", __name__, url_prefix="/api/scores")

# Thêm tham số <filename> trong route
@fact_student_course_scores.route('/<filename>', methods=['GET'])
def get_student_scores_route():
    #return get_student_course_score()
    return "Hello"
