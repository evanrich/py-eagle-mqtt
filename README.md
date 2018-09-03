# py-eagle-mqtt
Python based Docker for Eagle to MQTT reader

I have only ported this into a dockerfile, All Original code (with one minor modification for XML root tag) is credit to 


Original Readme as follows from creator, Ted Drain.  You can view the original repo this is based on here: https://github.com/TD22057/T-Home

snippet from my MQTT Broker showing container connecting and dissconnecting when I start/stop it:
```
{"pid":1,"hostname":"mqtt-867c776494-6rc57","name":"mosca","level":30,"time":1535955884767,"msg":"client connected","client":"","v":1}
{"pid":1,"hostname":"mqtt-867c776494-6rc57","name":"mosca","level":30,"time":1535955905640,"msg":"closed","client":"","v":1}
```

T-Home Automation Software
==========================

A collection of scripts and utilities for various home automation projects.

- bin/  Command line tools
- conf/ Sample config files
- init.d/   Init.d style Linux start up scripts
- python/  Main scripting library
- systemd/  Systemd (latest Raspian) start up scripts
- upstart/  Upstart (Ubuntu 14.04) style start up scripts

Currently most of the scripts read data from various sources and
translate the data into JSON'ed dictionaries which get published to a
MQTT message broker.  


Rainforest Eagle Energy Monitor
-------------------------------

http://rainforestautomation.com/rfa-z109-eagle/

python/tHome/eagle contains code for reading data directly from an
Eagle energy monitor.  Use bin/tHome-eagle.py to start a small web
server and set the address as the "cloud provider" in the Eagle.  The
Eagle will publish energy data to the server which will converts it
into a message and publishes that as a MQTT messages.

