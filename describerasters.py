# Sarah Lerman-Sinkoff. Lab 6 Pt. 2

import arcpy
from arcpy import env
env.workspace = "C:\Users\Sarah\Desktop\Commons\Lab_6_Working_with_Rasters"
raster = "tm.img"
desc = arcpy.Describe(raster)
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension

# output is the name of the raster, its datatype, and what kind of extension the file has

##Raster base name is: tm
##Raster data type is: RasterDataset
##Raster file extension is: img


print "Raster spatial reference is: " + desc.spatialReference.name # determine the spatial reference
print "Raster format is: " + desc.format
print "Raster compression type is: " + desc.compressionType 
print "There are " + str(desc.bandCount) + " bands in the raster"

# output from four lines of code above, which gives the spatial reference for the raster, its raster format, what compression type it is, and the number of bands it has

##Raster spatial reference is: GCS_North_American_1983
##Raster format is: IMAGINE Image
##Raster compression type is: RLE
##There are 3 bands in the raster
