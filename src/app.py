from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import random
import os

app = Flask(__name__)
if os.environ.get('DOCKERIZED'):
    mydb = mysql.connector.connect(
        host='mysql',
        user='root',
        passwd='root',
        database='project',
        port=3306
    )
else:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Itay5858',
        database='project',
        port=3306
    )

@app.route("/")
def index():
    a = random.randint(1, 2)
    i = random.randint(1, 25)
    sql = "SELECT * FROM facts WHERE fact_id = {}".format(i)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    l = list(myresult[0])
    if a == 1:
        a1 = l[1]
        a2 = l[2]
    else:
        a1 = l[2]
        a2 = l[1]
    answer = l[3]
    question = l[4]
    return render_template("homepage.html", question=question, answer=answer, a1=a1, a2=a2, a=a)


@app.route("/add")
def add():
    return render_template("addfacts.html")


@app.route("/submit_fact", methods=["POST"])
def submit_fact():
    fact = request.form["fact"]
    question = request.form["question"]
    true_option = request.form["true_option"]
    false_option = request.form["false_option"]

    if not fact or not question or not true_option or not false_option:
        return "All fields are required.", 400

    mycursor = mydb.cursor()
    sql = "INSERT INTO fansfacts (fact, true_option, false_option, question) VALUES (%s, %s, %s, %s)"
    val = (fact, true_option, false_option, question)
    mycursor.execute(sql, val)
    mydb.commit()

    return redirect(url_for("add"))


@app.route("/delete", methods=["POST"])
def delete():
    mycursor = mydb.cursor()
    sql = "delete from project.fansfacts where fact = 'good'"
    mycursor.execute(sql)
    mydb.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
