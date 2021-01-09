#!/bin/pytho3

import sys
import socket
from datetime import datetime

#check first the arguments
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Missing IP address")
    print("Syntax: Scanner.py <ip>")

#display some information
print("Scanner start at " + str(datetime.now()))
print("*" * 40)
print("Start scanning at " + target)
print("*" * 40)

#start scanner
try:
    for port in range(50,85):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        #print("port:"  + format(port))
        #check if its open
        result = con.connect_ex((target,port))
        #print(result)
        if result == 0:
            print("The port " + str(port) + " is open")
        con.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Cant resolve host")
    sys.exit()

except socket.error:
    print("Cant connect to server")
    sys.exit()
