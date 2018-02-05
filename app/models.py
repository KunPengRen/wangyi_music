#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$abc

from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Comment(db.Document):
    #Columns
    userid = db.StringField(required=True)
    musicid = db.StringField(required=True)
    time = db.StringField(required=True)
    