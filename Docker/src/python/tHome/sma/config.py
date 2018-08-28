#===========================================================================
#
# Config file
#
#===========================================================================

__doc__ = """Config file parsing.
"""

from .. import util
from ..util import config as C

#===========================================================================

# Config file section name and defaults.
configEntries = [
   # ( name, converter function, default value )
   C.Entry( "host", str ),
   C.Entry( "port", int, 9522 ),
   C.Entry( "group", str, "USER" ),
   C.Entry( "password", str, "0000" ),
   C.Entry( "logFile", util.path.expand ),
   C.Entry( "logLevel", int, 20 ), # INFO
   C.Entry( "pollPower", int, 10 ),
   C.Entry( "pollEnergy", int, 600 ), # 10 minutes
   C.Entry( "pollFull", int, 0 ), # disabled
   C.Entry( "mqttEnergy", str, "elec/solar/meter" ),
   C.Entry( "mqttPower", str, "elec/solar/instant" ),
   C.Entry( "mqttFull", str, "elec/solar/detail" ),
   C.Entry( "lat", float ), 
   C.Entry( "lon", float ),
   C.Entry( "timePad", float, 600 ), # 10 minutes
   ]

#===========================================================================
def parse( configDir, configFile='sma.py' ):
   return C.readAndCheck( configDir, configFile, configEntries )

#===========================================================================
def log( config, logFile=None ):
   if not logFile:
      logFile = config.logFile
   
   return util.log.get( "sma", config.logLevel, logFile )

#===========================================================================



