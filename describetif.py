# Sarah Lerman-Sinkoff. Lab 6 Pt. 3

import arcpy
from arcpy import env
env.workspace = "C:\Users\Sarah\Desktop\Commons\Lab_6_Working_with_Rasters"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "The raster resolution is " + str(x) + " by " + str(y)  + " units " + "."

# Output is a printed statement about raster resolution

## The raster resolution is 30.0 by 30.0 units 
