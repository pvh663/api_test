from .extension import db

class Students(db.Model):
    student_sk = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.String(50), unique=True, nullable=False)
    student_name = db.Column(db.String(255))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(1))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(10), unique=True)
    city = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    
    def __init__(self, student_no, student_name, date_of_birth, gender, address,phone_number, city, email):
        self.student_no = student_no
        self.student_name = student_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.city = city
        self.email = email

class Courses(db.Model):
    course_sk = db.Column(db.Integer, primary_key=True)
    course_no = db.Column(db.String(50), unique=True, nullable=False)
    course_name = db.Column(db.String(255))
    
    def __init__(self, course_no, course_name):
        self.course_no=course_no
        self.course_name =course_name

class Term(db.Model):
    term_sk = db.Column(db.Integer, primary_key=True)
    term_no = db.Column(db.String(20), unique=True, nullable=False)
    term_name = db.Column(db.String(255))


    def __init__(self, term_no, term_name):
        self.term_no = term_no
        self.term_name = term_name

class fact_student_course_score(db.Model):

    fact_student_course_score_sk = db.Column(db.Integer, primary_key=True)
    student_sk = db.Column(db.Integer, db.ForeignKey('students.student_sk'))
    course_sk = db.Column(db.Integer, db.ForeignKey('courses.course_sk'))
    term_sk = db.Column(db.Integer, db.ForeignKey('term.term_sk'))
    midterm_score = db.Column(db.Integer)
    final_score = db.Column(db.Integer)
    total_score = db.Column(db.Integer)

    def __init__(self, student_sk, course_sk, term_sk, midterm_score, final_score, total_score):
        self.student_sk = student_sk
        self.course_sk = course_sk
        self.term_sk = term_sk
        self.midterm_score = midterm_score
        self.final_score = final_score
        self.total_score = total_score

