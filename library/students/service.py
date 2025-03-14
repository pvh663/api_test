from library.extension import db
from library.library_ma import StudentSchema
from library.model import Students
from flask import request
import json

student_schema = StudentSchema
students_schema = StudentSchema(many=True)

def add_student_service():
    name = request.json