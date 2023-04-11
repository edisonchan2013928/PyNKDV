library(sp)
library(maptools)
library(rgeos)
library(spNetwork)
library(sf)

road_gpkg = st_read("road.gpkg", layer="road")
events = st_read("points_layer.gpkg", layer="points_layer")

start = Sys.time()
samples <- lines_points_along(road_gpkg, 20)

# calculating densities
densities <- nkde(lines = road_gpkg,
                  events = events,
                  w = rep(1,nrow(events)),
                  samples = samples,
                  kernel_name = "epanechnikov",
                  bw = 500, div= "bw",
                  method = "simple",
                  digits = 2, tol =  0,
                  grid_shape = c(1,1),
                  agg = NULL, sparse = TRUE,
                  verbose = FALSE)
                  
print(Sys.time() - start)
densities <- densities*1000
samples$density <- densities
