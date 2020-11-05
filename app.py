from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import Globals


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/record_marks', methods=['GET', 'POST'])
def record_marks():
    rows = Globals.get_practical_marks()
    return render_template("practical_mark_sheet.html", rows=rows)


@app.route('/student', methods=['GET', 'POST'])
def student():
    return render_template('student.html')


@app.route('/config_course', methods=['GET', 'POST'])
def config_course():
    if request.method == "GET":
        options = Globals.course_type()
        rows = Globals.component()
        return render_template('config_course.html', options=options, rows=rows)
    else:
        nm = request.form['name']
        abv = request.form['abv']
        c_type = request.form.get('c_type')
        cos_id = 1
        marks = request.form['marks']
        con = sqlite3.connect("recSheet.db")
        cur = con.cursor()
        cur.execute(
            'INSERT INTO component (Name, Abreviation, ComponetType, CourseId, Marks) VALUES(?,?,?,?,?)',
            (nm, abv, c_type, cos_id, marks))
        con.commit()
        con.close()
    return render_template("config_course.html")


@app.route('/load_students', methods=['GET', 'POST'])
def load_students():
    if request.method == "GET":
        return render_template("config_course.html")
    else:
        course_id = request.form['course_id']
        rows = Globals.get_students(course_id)
        conn = Globals.get_connection()
        cursor = conn.cursor()
        for row in rows:
            cursor.execute(
                'INSERT INTO practical_mark_sheet (CourseId, StudentId, LevelOfStudy, DeptId, T1, T2, A1, A2, Lab1, Lab2, PCW, TCW, OCW, Exam, FinalMark) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (row[0], row[1], row[2], row[3], '', '', '', '', '', '', '', '', '', '', ''))
            conn.commit()
        conn.close()
        return render_template("config_course.html")


if __name__ == '__main__':
    app.run()
