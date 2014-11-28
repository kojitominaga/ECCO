require(rgdal)
require(raster)
require(rgeos)

demfp <- '../../../../GIS_DATA/Koji_GIS/dem_NE_VFP/dem_NE_VFP.vrt'
lakesdir <- '../../../../GIS_DATA/FENOSCAN lakes'
lakeslayername <- 'FENOSCAND_lakes'

lakesutm33n <- readOGR(lakesdir, lakeslayername)
centroidslayername <- paste0(lakeslayername, '_centroids')
## centroidsutm33n <- gCentroid(lakesutm33n, byid=TRUE)
## centroidsutm33nspdf <- SpatialPointsDataFrame(centroidsutm33n,
##                                               data = lakesutm33n@data)
## writeOGR(centroidsutm33nspdf, lakesdir, centroidslayername,
##          'ESRI Shapefile')
centroidsutm33nspdf <- readOGR(lakesdir, centroidslayername)

dem <- raster(demfp)
centroids <- spTransform(centroidsutm33nspdf, CRS(proj4string(dem)))
lakes <- spTransform(lakesutm33n, CRS(proj4string(dem)))


writeOGR(lakes, lakesdir, paste0(lakeslayername, '_geographical'),
         'ESRI Shapefile')
writeOGR(lakes[1:10, ], lakesdir, paste0(lakeslayername, '_geographical_10'),
         'ESRI Shapefile')
writeOGR(centroids, lakesdir,
         paste0(lakeslayername, '_centroids_geographical'),
         'ESRI Shapefile')
writeOGR(centroids[1:10, ], lakesdir,
         paste0(lakeslayername, '_centroids_geographical_10'),
         'ESRI Shapefile')

areas <- gArea(lakesutm33n, byid=TRUE)



rm(lakesutm33n)
rm(centroidsutm33nspdf)

for (li in 100000:100399) {
  e <- median(extract(dem, spsample(lakes[li, ], 3, type='random'),
                      buffer=1, fun=median))
  print(e)
}
 
