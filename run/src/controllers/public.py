#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for

from ..models.altiore import User
from ..mappers.opencursor import OpenCursor

link = Blueprint('public',__name__,url_prefix='/public')

@link.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('public/index.html')
    elif request.method == 'POST':
        with User(username=request.form['username'],password=request.form['password']) as un:
            try:
                if un.login(request.form['password']):
                    session['username'] = un.username
                    session['password'] = un.password
                    session['pk']       = un.pk
                    return redirect(url_for('private.account'))
                else:
                    return render_template('public/index.html',message='Bad Credentials')
            except TypeError:
                return render_template('public/index.html',message='Bad Credentials')
    else:
        pass

@link.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('public/register.html')
    elif request.method == 'POST':
        with User(username=request.form['username'],password=request.form['password']) as un:
            if un.check_un(request.form['username']):
                return render_template('public/register.html', message='Username Exists')  
            else:
                un.create_user(request.form['username'],request.form['password'])
                return render_template('public/register.html',message='Created Account')
    else:
        return render_template('public/login.html', message='Bad Credentials')  
