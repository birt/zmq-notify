#!/usr/bin/python

import zmq
import time
import sys

context = zmq.Context()
port = "55555"
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

socket.send("NOTIFY " + " ".join(sys.argv[1:]))
msg = socket.recv()

#print "Reply: " + msg