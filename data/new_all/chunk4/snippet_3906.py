# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65473488/type-error-in-functions-to-run-point-in-polygon-query-on-rapids
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def create_iterations(start, end, batches):
    _l_(581325)

    iterations = _c_(581316, _n_(581309, "list", lambda: list), _c_(581315, _a_(581311, _n_(581310, "np", lambda: np), "arange"), _n_(581312, "start", lambda: start), _n_(581313, "end", lambda: end), _n_(581314, "batches", lambda: batches)))
    _l_(581317)
    _c_(581321, _a_(581319, _n_(581318, "iterations", lambda: iterations), "append"), _n_(581320, "end", lambda: end))
    _l_(581322)
    aux = _n_(581323, "iterations", lambda: iterations)
    _l_(581324)
    return aux


pip_iterations = _c_(581327, _n_(581326, "create_iterations", lambda: create_iterations), 0, 264, 24)
_l_(581328)


#loop to do point in polygon query in a table
def perform_pip(cuda_df, cuspatial_data, polygon_name, iter_batch):
    _l_(581367)

    _n_(581329, "cuda_df", lambda: cuda_df)['borough'] = " "
    _l_(581330)
    for i in _c_(581335, _n_(581331, "range", lambda: range), _c_(581334, _n_(581332, "len", lambda: len), _n_(581333, "iter_batch", lambda: iter_batch))-1):
        _l_(581364)

        start = _n_(581336, "pip_iterations", lambda: pip_iterations)[_n_(581337, "i", lambda: i)]
        _l_(581338)
        end = _n_(581339, "pip_iterations", lambda: pip_iterations)[_n_(581340, "i", lambda: i)+1]
        _l_(581341)
        pip = _c_(581352, _a_(581343, _n_(581342, "cuspatial", lambda: cuspatial), "point_in_polygon"), _n_(581344, "cuda_df", lambda: cuda_df)['pickup_longitude'], _n_(581345, "cuda_df", lambda: cuda_df)['pickup_latitude'],
                                         _n_(581346, "cuspatial_data", lambda: cuspatial_data)[0][_n_(581347, "start", lambda: start):_n_(581348, "end", lambda: end)],  #poly_offsets
                                         _n_(581349, "cuspatial_data", lambda: cuspatial_data)[1],  #poly_ring_offsets
                                         _n_(581350, "cuspatial_data", lambda: cuspatial_data)[2]['x'],  #poly_points_x
                                         _n_(581351, "cuspatial_data", lambda: cuspatial_data)[2]['y']  #poly_points_y
                                        )
        _l_(581353)

        for i in _a_(581355, _n_(581354, "pip", lambda: pip), "columns"):
            _l_(581363)

            _a_(581357, _n_(581356, "cuda_df", lambda: cuda_df)['borough'], "loc")[_n_(581358, "pip", lambda: pip)[_n_(581359, "i", lambda: i)]] = _n_(581360, "polygon_name", lambda: polygon_name)[_n_(581361, "i", lambda: i)]
            _l_(581362)
    aux = _n_(581365, "cuda_df", lambda: cuda_df)
    _l_(581366)
    return aux