import socket
import socks
import httplib

def connectTor():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
	socket.socket = socks.socksocket # routes traffic through tor
def main():
	print 'kitty'
	connectTor()
	print "Connected"

	conn = httplib.HTTPConnection("my-ip.herokuapp.com")
	conn.request("GET", "/")
	response = conn.getresponse() #var to save response
	print response.read()
	print 'end'







if __name__ == "__main__":
	main()
