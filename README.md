# py-eagle-mqtt
Python based Docker for Eagle to MQTT reader

I have only ported this into a dockerfile, All Original code (with one minor modification for XML root tag) is credit to 


You can run this with the following:

```
docker run --name py-eagle-mqtt -d -e "MQTT_BROKER_IP=" -e "MQTT_BROKER_PORT=" evanrich/py-eagle/mqtt
```
**MQTT_BROKER_IP** = your broker's IP address.  Defaults to 192.168.1.20 (my local k8s node)

**MQTT_BROKER_PORT** = your broker's port #.  Defaults to 1883 (used in my k8s)

Optionally, you can add the following:

**"KEEPALVE="**  Sets the keepalive for MQTT, defaults to 60 seconds if not specificed

**"MQTT_USER="** Sets the MQTT user, if using authentication.  Defaults to "None".  Don't specify if not using authentication.

**"MQTT_PASS="** Sets the MQTT pasword if using authentication.  Defaults to "None".  Don't specify if not using authentication.


snippet from my MQTT Broker showing container connecting and dissconnecting when I start/stop it:
```
{"pid":1,"hostname":"mqtt-867c776494-6rc57","name":"mosca","level":30,"time":1535955884767,"msg":"client connected","client":"","v":1}
{"pid":1,"hostname":"mqtt-867c776494-6rc57","name":"mosca","level":30,"time":1535955905640,"msg":"closed","client":"","v":1}
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

Original Readme as follows from creator, Ted Drain.  You can view the original repo this is based on here: https://github.com/TD22057/T-Home
---

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

