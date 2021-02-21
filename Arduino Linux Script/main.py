from bridgeclient import BridgeClient as bridgeclient
import sys
from socket import *

sys.path.insert(0, '/usr/lib/python2.7/bridge/')

client = bridgeclient()
client.begin()

s = socket(AF_INET, SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen(100)
while True:
    conn, addr = s.accept()
    val = client.get('TH_DATA')
    print str(addr) + "connected and got data" + str(val)
    conn.send(val)
