from flask import Flask,render_template,redirect,url_for,request
import mongoengine
from mongoengine import *
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

images_folder = os.path.join(APP_ROOT, 'static/images/')

unit = []

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


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/sign')
def sign():
    return render_template("sign.html")

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method =="GET" :
        return render_template("signup.html")
    elif request.method == "POST":
        namex     = request.form["Name"]
        usernamex = request.form["userSignUp"]
        passwordx = request.form["SignUpPassw"]
        user = UserSignUp.objects(username=usernamex).first()
        if user is None:
            user = UserSignUp(name=namex,username= usernamex, password=passwordx)
            user.save()
        else: print('tài khoản đã tồn tại')
        return ("Thank You")

images_folder = os.path.join(APP_ROOT, 'static/images/')




@app.route('/signin',methods=["GET","POST"])
def signin():
    if request.method =="GET" :
        return render_template("signin.html")
    elif request.method == "POST":
        usernamex = request.form["userSignIn"]
        passwordx = request.form["SignInPassw"]
        user = UserSignUp.objects(username=usernamex).first()
        if (user is not None) and (passwordx == user.password):
            print("ahihi")
        else:
            return render_template("signin.html")
        print(user)
        # if


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/index1')
def HelloHuy():
    return render_template('create.html')

if __name__ == '__main__':
    app.run()
