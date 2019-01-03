#!/usr/bin/env python3

import time

from flask import Blueprint,render_template,request,redirect,url_for,session

from ..models.altiore import User,Tweets

link = Blueprint('private',__name__,url_prefix='/private')

# @link.before_request
# def before_request():
#     g.username = None
#     if session['username']:
#         g.username = session['username']

@link.route('/account',methods=['GET','POST'])
def account():
    un = User(username=session['username'],password=session['password'])
    user_posts = un.get_tweets()
    # print(session['username'])
    # print(user_posts)
    if request.method == 'GET':
        return render_template('private/account.html')
    elif request.method == 'POST':
        tw          = Tweets()
        tw.post     = request.form['tweet']
        tw.time     = int(time.time())
        tw.users_pk = un.pk
        tw.save()
        return render_template('private/account.html',posts=user_posts)
    else:
        pass

