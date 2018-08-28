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
   C.Entry( "httpPort", int, 22042 ),
   C.Entry( "mqttEnergy", str ),
   C.Entry( "mqttPower", str ),
   C.Entry( "logFile", util.path.expand ),
   C.Entry( "logLevel", int, 20 ), # INFO
   ]

#===========================================================================
def parse( configDir, configFile='eagle.py' ):
   return C.readAndCheck( configDir, configFile, configEntries )

#===========================================================================
def log( config, logFile=None ):
   if not logFile:
      logFile = config.logFile
   
   return util.log.get( "eagle", config.logLevel, logFile )

#===========================================================================
