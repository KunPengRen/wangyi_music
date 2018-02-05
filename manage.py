#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : darmon (ren675523481@gmail.com)
# @Link    : github.com/KunPengRen
# @Version : $Id$

from flask_script import Manager,Server
from app import app
from app.models import Quest,UserLog

manager = Manager(app)
manager.add_command("runserver",
	Server(host='0.0.0.0',port=5000,use_debugger=True))



if __name__=='__main__':

	manager.run()
	
