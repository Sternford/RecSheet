import Globals


def load_students():

    rows = Globals.get_students(1)
    '''conn = Globals.get_connection()
    cursor = conn.cursor()'''
    for row in rows:
        '''cursor.execute(
            'INSERT INTO practical_mark_sheet (CourseId, StudentId, LevelOfStudy, DeptId, T1, T2, A1, A2, Lab1, Lab2, PCW, TCW, OCW, Exam, FinalMark) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (row[0], row[1], row[2], row[3], '', '', '', '', '', '', '', '', '', '', ''))
        conn.commit()'''
        print(row[0], row[1], row[2], row[3])
    '''conn.close()'''


load_students()


arr = ["dfghjkl", "dfghjkl"]
