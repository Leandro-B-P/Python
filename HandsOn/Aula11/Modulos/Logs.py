#!/usr/bin/python

from datetime import datetime

class Logs:
	def __init__(self):
		self.log_file = "provision.log"
		pass

	def writeLogs(self,msg):
		with  open(self.log_file,"a") as f:
			data = datetime.now().strftime("%d/%m/%Y - %H:%M")
			f.write("%s - %s\n"%(data,msg))
