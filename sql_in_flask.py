from flask import Flask,render_template,request,redirect
import sqlite3

con = sqlite3.connect('user.db',check_same_thread=False)
cur=con.cursor()

con.execute('create table if not exists login_data (id integer primary key autoincrement,name varchar(32),email varchar(32),password varchar(32),confirm_password varchar(32))')

app=Flask(__name__)

@app.route("/registration",methods=["GET","POST"])
def reg():

    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm']
        print(name,email,password,confirm)

        if password == confirm:
            cur.execute("insert into login_data(name,email,password,confirm_password) values(?,?,?,?)",(name,email,password,confirm))
            con.commit()
        else:
            return render_template("register.html")

        return "reg Success!!!!!!!!"



    return render_template("register.html")



@app.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":
        name=request.form["username"]
        password=request.form["password"]

        cur.execute("select * from login_data where name=? AND password=?",(name,password))
        data=cur.fetchall()

        if data is not None :
            return "Login Successfull!!!!!"
        else:
            return "User not found"
    
    return render_template("login_page.html")
@app.route("/view")
def view():
    pass


if __name__=="__main__":
    app.run(debug=True)
