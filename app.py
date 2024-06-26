from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# 使用您的数据库连接字符串
connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:sqldbsrv918.database.windows.net,1433;Initial Catalog=WITSQLDB_2024-04-23T06-38Z;Persist Security Info=False;User ID=admin918;Password=Amber0918;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 从表单获取数据
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        
        # 连接数据库
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # 执行注册逻辑
        cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        
        # 关闭数据库连接
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
