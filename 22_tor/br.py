
import urllib2, socks, socket
from stem import Signal
from stem.control import Controller
'''
old_socket = socket.socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
'''
with Controller.from_port(port = 9051) as controller:
  controller.authenticate()
  controller.signal(Signal.NEWNYM)

'''
def newI():
    socket.socket = old_socket  # don't use proxy
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    # set up the proxy again
    socket.socket = socks.socksocket

newI()

headers = {'User-Agent': 'Mozilla/3.0 (x86 [en] Windows NT 5.1; Sun)'} 
req = urllib2.Request('https://google.com', None, headers)
response = urllib2.urlopen(req)
html = response.read()
print html
newI()
'''