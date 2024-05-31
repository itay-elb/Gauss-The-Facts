from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import random
import os

app = Flask(__name__)

# Retrieve database hostname from environment variable
DB_HOST = os.getenv('MYSQL_HOST', 'localhost')  # Use 'localhost' as fallback
DB_USER = os.getenv('MYSQL_USER', 'root')
DB_PASSWD = os.getenv('MYSQL_PASSWD', 'root')
DB_DATABASE = os.getenv('MYSQL_DATABASE', 'project')
try:
    # Attempt to connect to the database using the first set of parameters
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWD,
        database=DB_DATABASE,
        port=3306
    )
    print("Connected to MySQL database!")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    print("host: " + DB_HOST + " user: " + DB_USER + " password: " + DB_PASSWD + " database: " + DB_DATABASE)
    # If the first connection attempt fails, catch the exception and try the second set of parameters
    print("First connection attempt failed. Trying the second connection parameters.")
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWD,
        database=DB_DATABASE,
        port=3307
    )

@app.route("/")
def index():              # homepage take a random question and put it on the Variables
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


@app.route("/submit_fact", methods=["POST"])       # take Variables and send it to the database
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


@app.route("/delete", methods=["POST"])         # this function for the test to delete the test we do
def delete():
    mycursor = mydb.cursor()
    sql = "delete from project.fansfacts where fact = 'good'"
    mycursor.execute(sql)
    mydb.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
