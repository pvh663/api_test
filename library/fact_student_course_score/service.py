from library.extension import db
from library.library_ma import FactStudentCourseScoreSchema
from library.model import fact_student_course_score
from flask import request,jsonify
import json
import os 

def get_student_course_score():
    # Lấy tham số filename từ URL
    filename = os.path.basename(request.path).strip('/')
    # Đường dẫn tới thư mục chứa file JSON
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', '..', filename + '.json')
    try:
        # Kiểm tra nếu file tồn tại
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        # Đọc dữ liệu từ file JSON
        with open(file_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


