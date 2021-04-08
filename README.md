# py-eagle-mqtt

Python3 based Docker for Eagle to MQTT reader

I have only ported this into a dockerfile, as well as made some changes to code for security or other purposes. All Original code is credit to [Ted Drain - TD22057](https://github.com/TD22057/T-Home).

This project utilizes the following tools:

[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/evanrich/py-eagle-mqtt)

![Gitlab pipeline status (self-hosted)](https://img.shields.io/gitlab/pipeline/erichardson/py-eagle-mqtt/master?gitlab_url=https%3A%2F%2Fgitlab.evanrichardsonphotography.com)

## UPDATES:

2020-04-06: Moved Updates to a CHANGELOG.md file to clean this up.

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

