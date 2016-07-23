## script to run Register_Virtual_Stack as CLI based on http://imagej.net/Register_Virtual_Stack_Slices#Scripting_.2F_PlugIn

import sys       # to get command line args
# import argparse  # fiji's jython does not have argparse: https://ilovesymposia.com/2014/02/26/fiji-jython/

from register_virtual_stack import Transform_Virtual_Stack_MT

argv = sys.argv

## http://javadoc.imagej.net/Fiji/register_virtual_stack/Transform_Virtual_Stack_MT.html
interpolate= True
Transform_Virtual_Stack_MT.exec(argv[1], argv[2], argv[3], interpolate)
