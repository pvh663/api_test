
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os

app = Flask(__name__)

# MySQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1111@localhost:3307/btth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Database
db = SQLAlchemy(app)

# Define the StudentScores model
class StudentScore(db.Model):
    __tablename__ = 'student_scores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    studentID = db.Column(db.String(20), nullable=False)
    courseID = db.Column(db.String(20), nullable=False)
    mid_term = db.Column(db.Float, nullable=False)
    final_term = db.Column(db.Float, nullable=False)
    score = db.Column(db.Float, nullable=False)

# Create the table if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read CSV file
        df = pd.read_csv(file)

        # Insert data into MySQL
        for _, row in df.iterrows():
            new_score = StudentScore(
                studentID=row['studentID'],
                courseID=row['courseID'],
                mid_term=row['mid_term'],
                final_term=row['final_term'],
                score=row['score']
            )
            db.session.add(new_score)

        db.session.commit()

        return jsonify({"message": "File uploaded and data stored successfully!"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route('/check-db', methods=['GET'])
def check_db_connection():
    try:
        # Use text() for raw SQL queries (SQLAlchemy 2.x requirement)
        db.session.execute(text('SELECT 1'))
        return jsonify({"status": "success", "message": "Connected to MySQL on port 3307 successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
