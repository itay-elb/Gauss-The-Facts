from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import random

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="la159951159",
    database="project"
)

@app.route("/")
def index():
    a=random.randint(1,2)
    i=random.randint(1,20)
    sql = "select * from facts where fact_id = {}".format(i)
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
    return render_template("homepage.html", question=question, answer=answer, a1=a1, a2=a2)

@app.route("/add")
def add():
    return render_template("addfacts.html")
  
@app.route("/submit_fact", methods=["POST"])
def submit_fact():
        fact = request.form["fact"]
        answer = request.form["answer"]
        true_option = request.form["true_option"]
        false_option = request.form["false_option"]
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO fansfacts (fact, true_option, false_option, answer) VALUES (%s, %s, %s, %s)"
        val = (fact, true_option, false_option, answer)
        mycursor.execute(sql, val)
        mydb.commit()

        return redirect(url_for("add"))

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")
