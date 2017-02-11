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

class Flashcard(Document):
    image = StringField()
    word  = StringField()
    meaning = StringField()


class UserSignUp(Document):
    name     = StringField()
    username = StringField()
    password = StringField()


app = Flask(__name__)
images_folder = os.path.join(APP_ROOT, 'static/images/')


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/sign')
def sign():
    return render_template("sign.html")

@app.route("/create",methods=["GET","POST"])
def create():
    if not os.path.isdir(images_folder) : #neu folder chua duoc khoi tao
        os.mkdir(images_folder) #mkdir = make directory
    if request.method == "GET" :
        return render_template('create.html')
    if request.method == "POST":
        for image in request.files.getlist('file'):
            image_name = image.filename
            imagex = "/".join([images_folder, image_name])
            print(imagex)
            image.save(imagex)
        wordx = request.form["word"]
        meaningx = request.form["meaning"]
        user = Flashcard(image=image_name, word = wordx , meaning=meaningx)
        user.save()
    return ("Thank you")


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



@app.route('/learn',methods=["GET"])
def learn():
    user= Flashcard.objects
    for i in user:
        print(i.word)
    return render_template('learn.html')

if __name__ == '__main__':
    app.run()
