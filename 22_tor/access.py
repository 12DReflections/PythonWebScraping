#!/usr/bin/python

import socks
import socket
import time
from stem.control import Controller
from stem import Signal
import urllib2
import sys

from stem import Signal

def info():
	print "This program enables you to hit a website from multiple varying IP addresses"
	print "The domain must be in the format of www.example.com"

if len(sys.argv) == 2:
	info()
	counter = 0
	url = str(sys.argv[1])
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
		socket.socket = socks.socksocket
		#visit url in infinite loop
		while True:
			urllib2.urlopen("http://"+url)
			counter = counter+1
			print "Page " + url + " visited = " + str(counter)
			#wait until next identity IP becomes available
			controller.signal(Signal.NEWNYM)
			time.sleep(controller.get_newnym_wait())

else:
	info()