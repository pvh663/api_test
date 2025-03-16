from flask import Blueprint, request, jsonify
from .service import get_student_course_score

fact_student_course_scores = Blueprint("fact_student_course_score", __name__, url_prefix="/api/scores")

# Thêm tham số <filename> trong route
# @fact_student_course_scores.route('/<filename>', methods=['GET'])
# def get_student_scores_route(filename):
#     return get_student_course_score(filename)
    # return "Hello"

@fact_student_course_scores.route('/', methods=['GET'])
def check_db_connection():
    try:
        # Try executing a simple query
        db.session.execute('SELECT 1')
        return jsonify({"status": "success", "message": "Connected to MySQL successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@fact_student_course_scores.route('/', methods=['GET'])
def get_student_scores_route():
    # return get_student_course_score()
    return "Hello"