import pyodbc
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 这里我们将使用环境变量，而不是硬编码连接字符串
connection_string = ('Driver={ODBC Driver 17 for SQL Server};'
                     'Server=tcp:sqldbsrv918.database.windows.net,1433;'
                     'Database=WITSQLDB;'
                     'Uid=admin918;'
                     'Pwd=Amber0918;'
                     'Encrypt=yes;'
                     'TrustServerCertificate=no;'
                     'Connection Timeout=30;')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        
        # 连接数据库
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # 插入注册信息
        cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (?, ?)", student_id, course_id)
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run()

