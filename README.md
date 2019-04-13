# py-eagle-mqtt
Python3 based Docker for Eagle to MQTT reader

I have only ported this into a dockerfile, All Original code (with one minor modification for XML root tag) is credit to [Ted Drain - TD22057](https://github.com/TD22057/T-Home).

## UPDATES:
2019-04-12: Rebase to python 3.7.3-alpine3.9

2019-03-08: Rebase to python 3.7.2-alpine3.9, update bottle and astral versions to latest

2019-01-03: Rebase to python 3.7.2-alpine3.8, changed logging level to Info (should output to /var/log/tHome/eagle.log)

2018-09-10: Ported to Python3, Added pricing info.  Merged into master branch


## Usage

```
docker create \ 
  --name=py-eagle-mqtt \
  -e MQTT_BROKER_IP=<broker ip address> \
  -e MQTT_BROKER_PORT=<broker port number> \
  -e KEEPALIVE=<keepalive time in seconds> \
  -e MQTT_USER=<username>
  -e MQTT_PASSWORD=<password>
  -p 22042:22042 \
  evanrich/py-eagle-mqtt
```
&nbsp;

## Parameters

| Parameter | Function |
| :---: | --- |
| `-e MQTT_BROKER_IP` | The IP address of your MQTT Broker |
| `-e MQTT_BROKER_PORT` | The PORT your MQTT Broker listens on. Defaults to 1883 if not specified |

## Optional Parameters 
| Parameter | Function |
| :---: | --- |
| `-e KEEPALIVE` | Keepalive time in seconds. Defaults to 60 seconds if not specified |
| `-e MQTT_USER` | The User Name for your MQTT Broker if you use one. Defaults to None if not specified |
| `-e MQTT_PASSWORD` | The Password for your MQTT Broker if you use one. Defaults to None if not specified |

&nbsp;


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

