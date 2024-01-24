# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70104866/python-nonetype-attribute-error-using-to-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(582925, _a_(582924, _n_(582923, "r", lambda: r), "open"), "final_image.tif") as src:
    _l_(582978)

    watershed_params = {
        'markers': 10000, # F1: 2500, F2, F3: 5000, F4: 10000
        'compactness': 0.0000001 # F1, F2, F3: 0.0001, F4: 0.0000001
    }
    _l_(582926)
    image = _c_(582929, _a_(582928, _n_(582927, "src", lambda: src), "read"))
    _l_(582930)
  
    rout = _c_(582935, _n_(582931, "segmentation", lambda: segmentation), model = _n_(582932, "watershed", lambda: watershed), params = _n_(582933, "watershed_params", lambda: watershed_params), image = _n_(582934, "image", lambda: image))
    _l_(582936)
      
    vout = _c_(582945, _n_(582937, "vectorize", lambda: vectorize), image=_n_(582938, "rout", lambda: rout), transform = _a_(582940, _n_(582939, "src", lambda: src), "transform"),
                      crs=_c_(582944, _a_(582943, _a_(582942, _n_(582941, "src", lambda: src), "crs"), "to_proj4")))
    _l_(582946)
  
    vout = _c_(582952, _n_(582947, "add_zonal_properties", lambda: add_zonal_properties), image=_n_(582948, "image", lambda: image), transform= _a_(582950, _n_(582949, "src", lambda: src), "transform"), 
      
                                  bands=[1, 2, 3], band_names=['red', 'green', 'blue'],
                                  stats=['mean','min','max','std'],
                                  gdf=_n_(582951, "vout", lambda: vout))
    _l_(582953)

    vout = _c_(582957, _n_(582954, "add_shape_properties", lambda: add_shape_properties), _n_(582955, "rout", lambda: rout), _n_(582956, "vout", lambda: vout), ['area', 'perimeter',
                                              'eccentricity', 
                                              'equivalent_diameter',
                                              'major_axis_length',
                                              'minor_axis_length',
                                              'orientation'])
    _l_(582958)

    edges = _c_(582961, _n_(582959, "sobel_edge_detect", lambda: sobel_edge_detect), _n_(582960, "src", lambda: src), band=1)
    _l_(582962)

      
    vout = _c_(582968, _n_(582963, "add_zonal_properties", lambda: add_zonal_properties), image= _n_(582964, "image", lambda: image), band_names=['sobel'],
                                  stats=['mean','min','max','std'],
                                  transform = _a_(582966, _n_(582965, "src", lambda: src), "transform"), gdf=_n_(582967, "vout", lambda: vout))
    _l_(582969)
    
    _c_(582973, _a_(582971, _n_(582970, "vout", lambda: vout), "to_file"), "segmentation.gpkg", layer=f"seg-{_n_(582972, 'idx', lambda: idx)}", driver="GPKG")
    _l_(582974)
    
    _c_(582976, _n_(582975, "print", lambda: print), "All done!!")
    _l_(582977)