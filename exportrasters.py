# Sarah Lerman-Sinkoff, Lab 6 part 6

# A script to export the goodslope, goodelev, and goodfinal layers as PNGs

import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
layers = ['goodslope','goodelev','goodfinal']

for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name in layers:
        lyr.visible = True
        ext = lyr.getExtent()
        df.extent = ext
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()
        arcpy.mapping.ExportToPNG(mxd,lyr.name + ".png")
        lyr.visible = False
