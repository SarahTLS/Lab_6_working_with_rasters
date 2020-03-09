# Sarah Lerman-Sinkoff. Lab 6 Pt. 1

import arcpy
from arcpy import env
env.workspace = "C:\Users\Sarah\Desktop\Commons\Lab_6_Working_with_Rasters"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster

# Output. The output is the list of all the rasters in the directory

##Elevation
##landcover.tif
##tm.img
