zmq-notify
==========

A ZeroMQ-based command-line notification system in Python

Introduction
------------

Got notification envy? You're using a CLI most of the time but you see those people running X desktops 
receiving sweet notifications all the time? 

Say no more!

This little program consists of a zmq server (zmq-notifier.py) an two clients, one to
send new notifications to the server (zmq-notify-send.py) and one to retrieve a notification 
from the server. (zmq-notify-get.py)

The server keeps the last 5 notifications in memory and returns a notification when you
issue a GET request (through zmq-notify-get.py). Next time you issue a GET the next notification in 
the list is returned, and so on.


How can I use this?
-------------------

Start the server in the background:

$ zmq-notifier.py & 


Send some notifications to it:

$ zmq-notify-send This is a notification

$ zmq-notify-send "This should work too"


## But where do you display the notifications?


Requirements
------------

