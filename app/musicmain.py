#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

from app import app 
from flask import request,render_template,url_for,redirect
from flask import jsonify


import os 



@app.route("/searchuser",methods=['POST'])
def crawluser():
    error = None
    if request.method == 'POST':
        userid = request.form['userid']
        user_email = request.form['email']
        