from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
from datetime import datetime
import os
from werkzeug import secure_filename

with open('config.json','r') as c:
    params=json.load(c)["params"]

local_server=True

app = Flask(__name__)
app.secret_key='jawad-super-key'
app.config['UPLOAD_FOLDER']=params['location']
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-pass']



)

mail=Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI']=params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db=SQLAlchemy(app)


class Contact(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    mes = db.Column(db.String(120), nullable=False)

class Post(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(13), nullable=True)
    slug = db.Column(db.String(20), nullable=False)

@app.route("/")
def index():
    post=Post.query.filter_by().all()[0:params['no_of_post']]
    return render_template('index.html', param=params, post=post)

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if('user' in session and session['user']==params['admin_username']):
        post = Post.query.all()
        return render_template('dashboard.html',param=params, post=post)

    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if(username==params['admin_username'] and userpass==params['password']):
            session['user']=username
            post=Post.query.all()
            return render_template('dashboard.html', param=params,post=post)

    return render_template('login.html', param=params)


@app.route("/delete/<string:sno>" ,methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session['user']==params['admin_username']):
        post=Post.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route("/edit/<string:sno>" ,methods=['GET','POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_username']):
        if request.method=='POST':
            titleb=request.form.get('title')
            contentb=request.form.get('content')
            slugb=request.form.get('slug')
            dateb=datetime.now()

            if sno=='0':
                post=Post(title=titleb,content=contentb,date=dateb,slug=slugb)
                db.session.add(post)
                db.session.commit()
            else:
                post=Post.query.filter_by(sno).first()
                post.title=titleb
                post.content=contentb
                post.slug=slugb
                post.date=dateb
                db.session.commit()
                return redirect('/edit/'+sno)
        post=Post.query.filter_by(sno=sno).first()
        return render_template('edit.html', param=params,post=post)



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/uploader",methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user']==params['admin_username']):
        if request.method=='POST':
            f=request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return "Uploaded Successfully"


@app.route("/about")
def about():
    return render_template('about.html', param=params)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post=Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html', param=params, post=post)

@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        mes=request.form.get('mes')
        entry=Contact(name=name,email=email,phone=phone,mes=mes)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('message from blog', sender=email, recipients=[params['gmail-user']],body=mes +'\n'+phone)
    return render_template('contact.html')

app.run(debug=True)
