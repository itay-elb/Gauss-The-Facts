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


def get_db_connection():
    try:
        # Attempt to connect to the database using the first set of parameters
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWD,
            database=DB_DATABASE,
            port=3306
        )
        print("Connected to MySQL database on port 3306!")
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        print("host: " + DB_HOST + " user: " + DB_USER + " password: " + DB_PASSWD + " database: " + DB_DATABASE)
        # If the first connection attempt fails, catch the exception and try the second set of parameters
        print("First connection attempt failed. Trying the second connection parameters.")
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWD,
            database=DB_DATABASE,
            port=3307
        )
        print("Connected to MySQL database on port 3307!")
    return connection


@app.route("/")  #homepage take a random question and put it on the Variables
def index():
    connection = get_db_connection()
    cursor = connection.cursor()

    a = random.randint(1, 2)
    i = random.randint(1, 25)

    # Use parameterized query to prevent SQL injection
    sql = "SELECT * FROM facts WHERE fact_id = %s"
    cursor.execute(sql, (i,))
    myresult = cursor.fetchone()

    if not myresult:
        return "No fact found", 404

    l = list(myresult)
    if a == 1:
        a1 = l[1]
        a2 = l[2]
    else:
        a1 = l[2]
        a2 = l[1]

    answer = l[3]
    question = l[4]

    cursor.close()
    connection.close()

    return render_template("homepage.html", question=question, answer=answer, a1=a1, a2=a2, a=a)


@app.route("/add")
def add():
    return render_template("addfacts.html")


@app.route("/submit_fact", methods=["POST"])  # take Variables and send it to the database
def submit_fact():
    fact = request.form["fact"]
    question = request.form["question"]
    true_option = request.form["true_option"]
    false_option = request.form["false_option"]

    if not fact or not question or not true_option or not false_option:
        return "All fields are required.", 400

    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO fansfacts (fact, true_option, false_option, question) VALUES (%s, %s, %s, %s)"
    val = (fact, true_option, false_option, question)
    cursor.execute(sql, val)
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("add"))


@app.route("/delete", methods=["POST"])  # this function for the test to delete the test we do
def delete():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        sql = "DELETE FROM project.fansfacts WHERE fact = %s"
        cursor.execute(sql, ('good',))
        connection.commit()

        cursor.close()
        connection.close()

        return "Deleted test entry", 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred", 500


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
