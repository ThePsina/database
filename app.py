from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'technopark'
app.config['MYSQL_DATABASE_PASSWORD'] = 'db'
app.config['MYSQL_DATABASE_DB'] = 'school'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    try:
        a = request.form['send']
    except:
        a = None
    if a == 'send':
        year_form = request.form['grind_year']
        month_form = request.form['grind_month']
        print('year: ', year_form)
        print('month: ', month_form)

        cursor = mysql.connect().cursor()

        _SQL = """select student_name, student_surname from Student where year(birth) = %s and month(birth) = %s;"""

        data = (year_form, month_form)
        cursor.execute(_SQL, data)

        result = cursor.fetchall()
        res = []
        schema = ['student_name', 'student_surname']

        for stud in result:
            res.append(dict(zip(schema, stud)))

        print(res)

        return render_template('inc/request.html', grind_year=year_form, grind_month=month_form, students=res)
    else:
        return render_template('inc/index.html')


if __name__ == '__main__':
    app.run()
