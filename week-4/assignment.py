from email import message
from telnetlib import LOGOUT
from unicodedata import name
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
app=Flask(__name__)

app.secret_key="eiddccidtcdbjlgennuivccuehhdeubkb"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    if username  == "test" and password == "test":
        session['username'] = username
        return redirect("/member")
    elif len(username) == 0 or len(password) == 0:
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/member")
def member():
    if 'username' in session:
        return render_template("member")
    else:
        return render_template("index.html")

@app.route("/error")
def error():
    errMessage = request.args.get("message")
    return render_template("error", message=errMessage)

@app.route("/signout")
def singout():
    session.pop('username', None)
    return render_template("index.html")

app.run(port=3000)

