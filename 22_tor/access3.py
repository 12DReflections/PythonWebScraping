from TorCtl import TorCtl

import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

import urllib2

__originalSocket = socket.socket

def newId():
    ''' Clean circuit switcher

    Restores socket to original system value.
    Calls TOR control socket and closes it
    Replaces system socket with socksified socket
    '''
    socket.socket = __originalSocket
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="123")
    TorCtl.Connection.send_signal(conn, "NEWNYM")
    conn.close()
    socket.socket = socks.socksocket

newId()

print(urllib2.urlopen("http://www.ifconfig.me/ip").read())