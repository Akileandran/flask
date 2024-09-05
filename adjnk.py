from flask import Flask,render_template,request,redirect

import random 

import sqlite3

con=sqlite3.connect('user.db',check_same_thread=False)
cur=con.cursor()

con.execute('create table if not exists login_data (id integer primary key autoincrement,name varchar(32),phone int,password varchar(32),confirm_password varchar(32))')


con.execute("create table if not exists emp_data(id integer primary key autoincrement,name varchar(32),role varchar(32),email varchar(32),salary int)")

app=Flask(_name_)

@app.route("/register",methods=["GET","POST"])

def reg():

    if request.method=="POST":
        name=request.form['name']
        phone=request.form['phone']
        password=request.form['password']
        confirm=request.form['confirm']
        print(name,phone,password,confirm)

        if password==confirm:

            cur.execute("insert into login_data(name,phone,password,confirm_password) values(?,?,?,?)",(name,phone,password,confirm))
            con.commit()
        else:
            return render_template("register.html")

        return "Success!!!"




    return render_template('register.html')

@app.route('/login',methods=["GET","POST"])
def login():

    if request.method=="POST":
        name=request.form["username"]
        password=request.form["password"]

        cur.execute("select * from login_data where name=? AND password=?",(name,password))
        user=cur.fetchone()

        if user is not None :
            return "login Successful!!!!!"
        else:
            return "user not valid"
    return render_template('login.html')





@app.route('/home')
def home():

    return render_template("home.html")


@app.route("/add",methods=["POST","GET"])
def add():

    if request.method=="POST":
        name=request.form["name"]
        role=request.form["role"]
        email=request.form["email"]
        salary=request.form["salary"]

        cur.execute("insert into emp_data(name,role,email,salary)values(?,?,?,?)",(name,role,email,salary))
        con.commit()
        return "added"
    return render_template("add.html")



@app.route("/view")
def view():

    cur.execute("select * from emp_data")
    data=cur.fetchall()
    return render_template("view.html",data=data)





if _name=="main_":
    app.run(debug=True)