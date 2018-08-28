#===========================================================================
#
# MQTT message broker location.  Default broker location is port 1883
# for regular and 8883 for SSL.
#
#===========================================================================
host = '192.168.1.20'
port = 31333

# Keep alive time in seconds.  Client sends a ping if no other message
# is sent in this interval.
keepAlive = 60

#===========================================================================
#
# User name and password (strings) for broker log in.
#
#===========================================================================
user = None
password = None

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


