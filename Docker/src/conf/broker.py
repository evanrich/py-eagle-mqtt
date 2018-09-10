import os
#===========================================================================
#
# MQTT message broker location.  Default broker location is port 1883
# for regular and 8883 for SSL.
#
#===========================================================================
host = os.getenv('MQTT_BROKER_IP', '192.168.1.20')
port = os.getenv('MQTT_BROKER_PORT', 1883)

# Keep alive time in seconds.  Client sends a ping if no other message
# is sent in this interval.
keepAlive = os.getenv('KEEPALIVE', 60)

#===========================================================================
#
# User name and password (strings) for broker log in.
#
#===========================================================================
user = os.getenv('MQTT_USER', None)
password = os.getenv('MQTT_PASS', None)

#===========================================================================
#
# Secure connection options.  See the paho-mqtt docs for details.
#
#===========================================================================
# List of certificate files.
ca_certs = [
   ]

certFile = None
keyFile = None


