from flask import Flask
from flask import render_template, redirect, url_for
from flask import request, session
from flask import json, jsonify

app=Flask(__name__)
app.secret_key="eiddccidtcdbjlgennuivccuehhdeubkb"

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="12345678",
    database="website"
)
mycursor = mydb.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form['name']
    username=request.form["username"]
    password=request.form["password"]

    sql = "SELECT username from member WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    usernamecheck = mycursor.fetchone()

    if len(name) == 0 or len(username) == 0 or len(password) == 0:
        return redirect(url_for("error", message="請輸入姓名、帳號、密碼"))
    elif usernamecheck:
        return redirect(url_for("error", message="帳號已經被註冊"))
    else:
        sql_insert = "INSERT INTO member(name, username, password) VALUES (%s, %s, %s)"
        val_insert = (name, username, password)
        mycursor.execute(sql_insert, val_insert)
        mydb.commit()
        return redirect('/')

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]

    sql = "SELECT name, username, password FROM member WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    signincheck = mycursor.fetchone()
    name = signincheck[0]

    if len(username) == 0 or len(password) == 0:
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    elif signincheck:
        session['username'] = name
        return redirect("/member")
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/member")
def member():
    if 'username' in session:
        return render_template("member", name=session['username'])
    else:
        return render_template("index.html")

@app.route("/error")
def error():
    errMessage = request.args.get("message")
    return render_template("error", message=errMessage)

@app.route("/signout")
def signout():
    session.pop('username', None)
    return render_template("index.html")


@app.route("/api/members", methods=["GET"])
def searchmember():
    username = request.args.get("username")
    sql = "SELECT id, name, username FROM member WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    usernamesearch = mycursor.fetchone()
    if usernamesearch:
        response = {
            "id": usernamesearch[0],
            "name": usernamesearch[1],
            "username": usernamesearch[2]
        }
        return jsonify({"data": response})
    else:
        return jsonify({"data": None})


app.run(port=3000)

mycursor.close()
mydb.close()
