#!/usr/bin/env python3

import sqlite3

from random import randint
from time import sleep,time,clock

from ..mappers.opencursor import OpenCursor


class User:
    def __init__(self, row={}, username='', password=''):
        if username:
            self.check_cred(username,password)
        else:
            self.row_set(row)

    def __enter__(self):
        return self

    def __exit__(self,exception_type,exception_value,exception_traceback):
        sleep(randint(10,10000)/10000)

    def row_set(self,row={}):
        row               = dict(row)
        self.pk           = row.get('pk')
        self.username     = row.get('username')
        self.password     = row.get('password')

    def check_cred(self,username,password):
        with OpenCursor() as cur:
            SQL = """ SELECT * FROM users WHERE
                  username=? and password=?; """
            val = (username,password)
            cur.execute(SQL,val)
            row = cur.fetchone()
        if row:
            self.row_set(row)
        else:
            self.row_set({})

    def check_un(self,username):
        with OpenCursor() as cur:
            SQL = """ SELECT username FROM users WHERE
                  username=?; """
            val = (username,)
            cur.execute(SQL,val)
            row = cur.fetchone()
        if row:
            return True
        else:
            return False

    def login(self,password):
        with OpenCursor() as cur:
            cur.execute('SELECT password FROM users WHERE username=?;',(self.username,))
            if password == cur.fetchone()['password']:
                return True
            else:
                return False
    
    def create_user(self,username,password):
        self.username = username
        self.password = password
        with OpenCursor() as cur:
            SQL = """ INSERT INTO users(
                username,password) VALUES (
                ?,?); """
            val = (self.username,self.password)
            cur.execute(SQL,val)
    
    def get_tweets(self):
        with OpenCursor() as cur:
            SQL = """ SELECT * FROM tweets WHERE users_pk=?; """
            val = (self.pk,)
            cur.execute(SQL,val)
            data = cur.fetchall()
        if data:
            print(data, len(data))
            return [Tweets(rows) for rows in data]
         

class Tweets:

    def __init__(self, row={}):
        # print(row)
        # dict(row)
        if row:
            self.pk       = row[0]
            self.post     = row[1]
            self.time     = row[2]
            self.users_pk = row[3]
        else:
            self.pk = None
            self.post = None
            self.time = None
            self.user_pk = None

    def __bool__(self):
        return bool(self.pk)
    
    def save(self):
        with OpenCursor() as cur:
            SQL = """ INSERT INTO tweets(
                post,time,users_pk
                ) VALUES (?,?,?); """
            val = (self.post,self.time,self.users_pk)
            cur.execute(SQL,val)

    def __repr__(self):
        output = '{}@{}: {}'
        return output.format(self.users_pk,self.time,self.post)