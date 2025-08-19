import mysql.connector
from flask import Flask
import os

app = Flask(__name__)

debug_mode = os.getenv("DEBUG", False)

@app.route('/')
def hello():
    return "<h1>Hola Mundo desde Python usando Flask</h1>"

@app.route('/healthcheck')
def healthcheck():
    return "<h1>Todo OK</h1>"

@app.route('/users')
def get_users():
    mydb = mysql.connector.connect(
            host="db",
            user="user",
            password="password",
            database="db"
            )
    mycursor = mydb.cursor()

    mycursor.execute("select * from users")
    result = mycursor.fetchall()
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=debug_mode)
