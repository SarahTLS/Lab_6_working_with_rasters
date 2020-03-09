# Sarah Lerman-Sinkoff, Lab 6 part 7

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:\Users\Sarah\Desktop\Commons\Lab_6_Working_with_Rasters"
if arcpy.CheckExtension("spatial")== "Available":
    arcpy.CheckOutExtension("spatial")
    outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")
    outraster.save("slope_per")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available." 

# export this layer to png - there's probably an easier way to do this
# the arcpy.mapping.ExportToPNG function exports whole dataframes instead of individual layers
# This loop tells it to just turn this one on and work with it
# it's adapted from code given to us, I just replaced which layer it loops through
# There's just 1 iteration - through the "slope_per" layer


mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
layers = ['slope_per']

for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name in layers:
        lyr.visible = True
        ext = lyr.getExtent()
        df.extent = ext
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()
        arcpy.mapping.ExportToPNG(mxd,lyr.name + ".png")
        lyr.visible = False
