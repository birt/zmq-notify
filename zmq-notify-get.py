#!/usr/bin/python

import zmq
import time
import sys

context = zmq.Context()
port = "55555"
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

socket.send("GET") # + " ".join(sys.argv[1:]))
msg = socket.recv()

print msg