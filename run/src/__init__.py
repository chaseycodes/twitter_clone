#!/usr/bin/env python3

import os

from flask import Flask,render_template,request

from .controllers.private import link as private_link
from .controllers.public  import link as public_link

chain = Flask(__name__)
chain.secret_key = 'hi'

chain.register_blueprint(private_link)
chain.register_blueprint(public_link)







