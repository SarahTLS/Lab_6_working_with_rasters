# Sarah Lerman-Sinkoff, lab 6 part 5

# convert elevation values from meters to feeet

elevraster = arcpy.Raster("elevation")
outraster3 = elevraster * 3.281 # convert from meters to feet
outraster3.save("elev_ft")

# run the slope spatial analysis tool

slope = Slope(elevraster)

# run the slope spatial analysis tool, in places where slope < 20 degeres, and where elevation is < 200 m

goodslope = slope < 20 # find areas less than 20 degrees slope
goodelev = elevraster < 2000 # find areas where eelvation <200 m
goodfinal = goodslope & goodelev # combine these criteria
goodfinal.save("final") # save the raster

# get pngs for these layers

import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT") # define which mxd
df = arcpy.mapping.ListDataFrames(mxd)[0] # get the file path
layers = ['goodslope','goodelev','goodfinal'] # define the layer names


for lyr in arcpy.mapping.ListLayers(mxd):  # for each layer in the mxd
    if lyr.name in layers: 
        lyr.visible = True  # make them visible         
        ext = lyr.getExtent()# grab their extents
        df.extent = ext
        arcpy.RefreshTOC() # update table of contents
        arcpy.RefreshActiveView() # refresh active view
        arcpy.mapping.ExportToPNG(mxd,lyr.name + ".png") #export the layer to PNG
        lyr.visible = False # turn off the layer
