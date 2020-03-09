# Sarah Lerman-Sinkoff. Lab 6 Pt. 4

import arcpy
from arcpy import env
env.workspace = "C:\Users\Sarah\Desktop\Commons\Lab_6_Working_with_Rasters"
rasterband = "tm.img/Layer_1"
desc = arcpy.Describe(rasterband)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.angularUnitName #changed for angular units!
print "The raster resolution of band one is " + str(x) + " by " + str(y) + " " + units + "."

# The output gives the raster resolution of band 1

## The raster resolution of band one is 0.000277778 by 0.000277778 Degree.

