from .extension import ma


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('student_sk','student_no', 'student_name', 'date_of_birth','gender', 'address','phone_number','city', 'email')

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('course_sk','course_no', 'course_name')

class TermSchema(ma.Schema):
    class Meta:
        fields = ('term_sk','term_no', 'term_name')

class FactStudentCourseScoreSchema(ma.Schema):
    class Meta:
        fields = ('fact_student_course_score_sk','student_sk', 'course_sk', 'term_sk', 'midterm_score', 'final_score', 'total_score')