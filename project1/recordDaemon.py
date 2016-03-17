#Here is the daeomon which is recording the flight (will use python-daemon)
import sys, time
from daemon import runner

class RecordDaemon:
	def run(self):
		while True:
			print("Howdy!  Gig'em!  Whoop!")
			time.sleep(10)