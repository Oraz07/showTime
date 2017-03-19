#!/usr/bin/python
import gi
import os.path
from time import gmtime, strftime

f = "/sys/class/power_supply/BAT0/capacity"
if os.path.exists(f):
	in_file = open(f,"r")
	level = in_file.read()
	in_file.close()
	level = str(level) + "%"
else:
	level = "only AC"
hour=strftime("%H:%M:%S")
date=strftime("%d-%m-%Y")
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Hello world")
Hello=Notify.Notification.new(date, hour + "      |      bat: " + level,
"dialog-information")
Hello.show()
