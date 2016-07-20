## script to run Register_Virtual_Stack as CLI based on http://imagej.net/Register_Virtual_Stack_Slices#Scripting_.2F_PlugIn

from register_virtual_stack import Register_Virtual_Stack_MT
 
# source directory
source_dir = "/path/to/source/"
# output directory
target_dir = "/path/to/target/"
# transforms directory
transf_dir = "/path/to/transforms/"
# reference image
reference_name = "reference_image"
# shrinkage option (false)
use_shrinking_constraint = 0
 
p = Register_Virtual_Stack_MT.Param()
# The "maximum image size":
p.sift.maxOctaveSize = 1024
# The "inlier ratio":
p.minInlierRatio = 0.05
 
Register_Virtual_Stack_MT.exec(source_dir, target_dir, transf_dir, 
reference_name, p, use_shrinking_constraint)
