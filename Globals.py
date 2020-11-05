import sqlite3


def get_connection():
    con = sqlite3.connect("recSheet.db")
    return con


def get_students(course_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        'SELECT cos.Id , std.Id, cos.LevelOfStudy,  std.DeptId FROM student std JOIN course cos ON std.LevelOfStudy = cos.LevelOfStudy AND std.DeptId = cos.DeptId WHERE cos.Id = ?', (course_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def course_type():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM component_type")
    options_list = cursor.fetchall()
    conn.close()
    return options_list


def get_practical_marks():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT std.RegNumber, std.FullName, mark.T1, mark.T2, mark.A1, mark.A2, mark.Lab1, mark.Lab2 "
        "FROM student std "
        "JOIN practical_mark_sheet mark "
        "ON std.Id = mark.StudentId "
        "AND std.LevelOfStudy = mark.LevelOfStudy "
        "AND std.DeptId = mark.DeptId "
        "WHERE mark.CourseId = 1 ")
    rows = cursor.fetchall()
    conn.close()
    return rows


def component():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT comp.Id, comp.Name, comp.Abreviation, comp.Marks, c_type.Name FROM component comp JOIN component_type c_type ON comp.ComponetType = c_type.Id")
    rows = cursor.fetchall()
    conn.close()
    return rows
