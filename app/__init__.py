#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

from flask import Flask

from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object("config")
bootstrap = Bootstrap(app)
from flask_mongoengine import MongoEngine
db = MongoEngine(app)

from app import models,api,tpamain
