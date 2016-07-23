## script to run Register_Virtual_Stack as CLI based on http://imagej.net/Register_Virtual_Stack_Slices#Scripting_.2F_PlugIn

import sys       # to get command line args
# import argparse  # fiji's jython does not have argparse: https://ilovesymposia.com/2014/02/26/fiji-jython/

from register_virtual_stack import Register_Virtual_Stack_MT

argv = sys.argv

# shrinkage option (false)
use_shrinking_constraint = 0

## http://javadoc.imagej.net/Fiji/register_virtual_stack/Register_Virtual_Stack_MT.html
p = Register_Virtual_Stack_MT.Param()
# p.sift.maxOctaveSize = 1024 # The "maximum image size"
# p.minInlierRatio = 0.05 # The "inlier ratio"
p.featuresModelIndex = Register_Virtual_Stack_MT.RIGID # 0=TRANSLATION, 1=RIGID, 2=SIMILARITY, 3=AFFINE
p.registrationModelIndex = Register_Virtual_Stack_MT.RIGID # 0=TRANSLATION, 1=RIGID, 2=SIMILARITY, 3=AFFINE, 4=ELASTIC, 5=MOVING_LEAST_SQUARES


Register_Virtual_Stack_MT.save_transforms= True
Register_Virtual_Stack_MT.exec(argv[1], argv[2], argv[3], argv[4], p, use_shrinking_constraint)
