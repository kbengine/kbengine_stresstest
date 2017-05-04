# -*- coding: utf-8 -*-

import os
import time
import signal
import sys

count = 0

def CtrlCHandler(signum, frame):
	print("CtrlCHandler()")
	sys.exit(0)
	
def printStatus():
	global count
	os.system(("echo \"------------------------------>%d\" >> stressstatus.log" % (count)))
	os.system("echo %f >> stressstatus.log" % (time.time()))
	os.system("python $KBE_ROOT/kbe/tools/server/pycluster/cluster_controller.py >> stressstatus.log")
	# iftop >= iftop-1.0pre3
	# http://www.ex-parrot.com/~pdw/iftop/
	os.system("/usr/local/sbin/iftop -t -s 1 >> stressstatus.log")
	print("printStatus(%d)" % count)
	count += 1


if __name__ == "__main__":
	signal.signal(signal.SIGINT, CtrlCHandler)
	os.system("echo begin: > stressstatus.log")
	lastTime = time.time()

	while True:
		nowtime = time.time()
		if nowtime - lastTime >= 60:
	
			printStatus()
			lastTime = nowtime
		else:
			time.sleep(nowtime - lastTime)


