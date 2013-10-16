#!/usr/bin/python

import zmq
import time
import re
from collections import deque

rr = deque(maxlen=5)

context = zmq.Context()
port = "55555"
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
counter = 0
rr.append("starting up")

while True: 
    
    msg = socket.recv()
    match = re.search('^NOTIFY (.*)',msg)
    if match:
	rr.append(match.group(1))
	socket.send("notification received")
    match = re.search('^GET',msg)
    if match:
	socket.send(rr[counter])
    time.sleep(1)
    counter = counter + 1
    if counter == len(rr):
	counter = 0
