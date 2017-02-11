from flask import Flask,render_template,redirect,url_for,request
import mongoengine
from mongoengine import *



connect(
    "pre_hackathon",
    host ="ds159328.mlab.com",
    port= 59328,
    username = "vuhoang98",
    password = "141298",
)

class UserSignUp(Document):
    name     = StringField()
    username = StringField()
    password = StringField()


class UserSignIn(Document):
    username     = StringField()
    password = StringField()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("homepage.html")


@app.route('/sign')
def sign():
    return render_template("sign-up.html")

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method =="GET" :
        return render_template("sign-up.html")
    elif request.method == "POST":
        usernamex = request.form["userSignUp"]
        namex     = request.form["userName"]
        passwordx = request.form["SignUpPassw"]
        user = UserSignUp(name=namex,username= usernamex, password=passwordx)
        user.save()
        return ("Thank You")


@app.route('/signin',methods=["GET","POST"])
def signin():
    if request.method =="GET" :
        return render_template("sign-up.html")
    elif request.method == "POST":
        usernamex = request.form["userSignIn"]
        passwordx = request.form["SignInPassw"]
        user = UserSignUp.objects(username=usernamex).first()
        if (user is not None) and (passwordx == user.password):
            print("ahihi")
        else: print("tài khoản hoặc mật khẩu không chính xác")
        print(user)
        return("OK")
        # if

if __name__ == '__main__':
    app.run()
