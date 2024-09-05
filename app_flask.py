from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/login",methods=["POST","GET"])

def login_():
    if request.method=="POST":
        name=request.form["username"]
        password=request.form["password"]

        return render_template ("view.html",name=name,password=password)
        
    return render_template('login_page.html')

if __name__== "__main__":
    app.run(debug=True)

