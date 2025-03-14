from flask import Flask, request, Blueprint
from .students.controller import students
from .courses.controller import courses
from .fact_student_course_score.controller import fact_student_course_scores
from .extension import db, ma
from .model import Students, Courses,Term,fact_student_course_score
import os 

def create_db(app):
    if not os.path.exists("library/library.db"):
        with app.app_context():
            db.create_all()
        print("Create DB")
def create_app(config_file ="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(fact_student_course_scores)
    return app