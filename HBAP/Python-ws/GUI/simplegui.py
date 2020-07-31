#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    simplegui.py
# @Author:      manunellutla
# @Time:        7/8/20 12:32 PM

from guietta import _, Gui, Quit
gui = Gui(
	[ "Enter numbers:",  "__a__", "__op__", "__b__", ["Calculate"] ],
	[    "Result: -->", "result",   _,       _,             _ ],
	[                _,        _,   _,       _,          Quit ],
	[ "Status       ",           "msg"    ,_,_,_,]
)

with gui.Calculate:
	ops = ['+','-','*','/','']

	if gui.op == '+':
		gui.result = float(gui.a) + float(gui.b)
		gui.msg = 'Ok.'
	elif gui.op == '-':
		gui.result = float(gui.a) - float(gui.b)
		gui.msg = 'Ok.'
	elif gui.op == '*':
		gui.result = float(gui.a) * float(gui.b)
		gui.msg = 'Ok.'
	elif gui.op == '/':
		gui.result = float(gui.a) / float(gui.b)
		gui.msg = 'Ok.'
	elif gui.op not in ops and gui.a is not None and gui.b is not None:
		gui.result = " N/A"
		gui.msg = 'Operator not supported!'
	elif gui.op == '' or gui.op is None:
		gui.result = " result"
		gui.msg = 'Enter Values.'

gui.run()
