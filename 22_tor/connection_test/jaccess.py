import sys
import socket
import socks
import httplib
from stem import Signal
import time
import os

from stem.connection import connect

controller = connect()

conn = httplib.HTTPConnection("my-ip.herokuapp.com")
conn.request("GET", "/")
response = conn.getresponse() #var to save response
print response.read()

print 'Tor is running version %s' % controller.get_version()
controller.close()

time.sleep(controller.get_newnym_wait())
os.system("killall -HUP tor")

print 'Tor is running version %s' % controller.get_version()
controller.close()


