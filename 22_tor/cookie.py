#!/usr/bin/python

import socks
import socket
import time
from stem.control import Controller
from stem import Signal
import urllib2
import sys
import httplib


with Controller.from_port(port = 9051) as controller:
  controller.authenticate()
  controller.signal(Signal.NEWNYM)
  print "Controller authenticated"