#===========================================================================
#
# Parse XML messages into an object.
#
#===========================================================================
import defusedxml.ElementTree as ET
from . import messages

#==========================================================================

# <rainForest ...>
#    <[Message]>...</[Message]>
# </rainForest>
def parse( xmlText ):
   root = ET.fromstring( xmlText )
   assert( root.tag == "rainforest" )

   child = root[0]

   msgClass = messages.tagMap.get( child.tag, None )
   if not msgClass:
      return None

   return msgClass( child )
   
#==========================================================================
