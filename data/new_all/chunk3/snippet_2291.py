# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(528183, _a_(528181, _n_(528180, "tf", lambda: tf), "name_scope"), _n_(528182, "name_scope", lambda: name_scope)):
    _l_(528302)

    resh_inp = _c_(528187, _a_(528185, _n_(528184, "tf", lambda: tf), "reshape"), _n_(528186, "input", lambda: input), [-1, 10, 10])
    _l_(528188)
    input_shape = _c_(528192, _a_(528190, _n_(528189, "tf", lambda: tf), "shape"), _n_(528191, "resh_inp", lambda: resh_inp))
    _l_(528193)
    rows, cols = _n_(528194, "input_shape", lambda: input_shape)[1], _n_(528195, "input_shape", lambda: input_shape)[2]
    _l_(528196)
    d_rows, d_cols = 2, 2
    _l_(528197)
    subm_rows, subm_cols = _n_(528198, "rows", lambda: rows) - _n_(528199, "d_rows", lambda: d_rows) + 1, _n_(528200, "cols", lambda: cols) - _n_(528201, "d_cols", lambda: d_cols) + 1
    _l_(528202)
    ii, jj = _c_(528213, _a_(528204, _n_(528203, "tf", lambda: tf), "meshgrid"), _c_(528208, _a_(528206, _n_(528205, "tf", lambda: tf), "range"), _n_(528207, "subm_rows", lambda: subm_rows)), _c_(528212, _a_(528210, _n_(528209, "tf", lambda: tf), "range"), _n_(528211, "subm_cols", lambda: subm_cols)), indexing='ij')
    _l_(528214)
    d_ii, d_jj = _c_(528225, _a_(528216, _n_(528215, "tf", lambda: tf), "meshgrid"), _c_(528220, _a_(528218, _n_(528217, "tf", lambda: tf), "range"), _n_(528219, "d_rows", lambda: d_rows)), _c_(528224, _a_(528222, _n_(528221, "tf", lambda: tf), "range"), _n_(528223, "d_cols", lambda: d_cols)), indexing='ij')
    _l_(528226)

    subm_ii = _n_(528227, "ii", lambda: ii)[:, :, _a_(528229, _n_(528228, "tf", lambda: tf), "newaxis"), _a_(528231, _n_(528230, "tf", lambda: tf), "newaxis")] + _n_(528232, "d_ii", lambda: d_ii)
    _l_(528233)
    subm_jj = _n_(528234, "jj", lambda: jj)[:, :, _a_(528236, _n_(528235, "tf", lambda: tf), "newaxis"), _a_(528238, _n_(528237, "tf", lambda: tf), "newaxis")] + _n_(528239, "d_jj", lambda: d_jj)
    _l_(528240)
    subm = _c_(528250, _a_(528242, _n_(528241, "tf", lambda: tf), "gather_nd"), _n_(528243, "resh_inp", lambda: resh_inp)[0, :, :], _c_(528248, _a_(528245, _n_(528244, "tf", lambda: tf), "stack"), [_n_(528246, "subm_ii", lambda: subm_ii), _n_(528247, "subm_jj", lambda: subm_jj)], axis=-1), name=_n_(528249, "layer_name", lambda: layer_name) + "_gather")
    _l_(528251)
    subm_sum = _c_(528256, _a_(528253, _n_(528252, "tf", lambda: tf), "reduce_sum"), _n_(528254, "subm", lambda: subm), axis=(2, 3), name=_n_(528255, "layer_name", lambda: layer_name) + "_subm_sum")
    _l_(528257)
    _, top_idx = _c_(528274, _a_(528260, _a_(528259, _n_(528258, "tf", lambda: tf), "nn"), "top_k"), _c_(528264, _a_(528262, _n_(528261, "tf", lambda: tf), "reshape"), _n_(528263, "subm_sum", lambda: subm_sum), [-1]), _c_(528272, _a_(528266, _n_(528265, "tf", lambda: tf), "minimum"), _n_(528267, "k", lambda: k), _c_(528271, _a_(528269, _n_(528268, "tf", lambda: tf), "size"), _n_(528270, "subm_sum", lambda: subm_sum))), name=_n_(528273, "layer_name", lambda: layer_name) + "_top_idx")
    _l_(528275)
    top_row = _n_(528276, "top_idx", lambda: top_idx) // _n_(528277, "subm_cols", lambda: subm_cols)
    _l_(528278)
    top_col = _n_(528279, "top_idx", lambda: top_idx) % _n_(528280, "subm_cols", lambda: subm_cols)
    _l_(528281)
    result = _c_(528287, _a_(528283, _n_(528282, "tf", lambda: tf), "stack"), [_n_(528284, "top_row", lambda: top_row), _n_(528285, "top_col", lambda: top_col)], axis=-1, name=_n_(528286, "layer_name", lambda: layer_name) + "_result")
    _l_(528288)
    result_shape = _c_(528292, _a_(528290, _n_(528289, "tf", lambda: tf), "shape"), _n_(528291, "result", lambda: result))
    _l_(528293)
    result = _c_(528300, _a_(528295, _n_(528294, "tf", lambda: tf), "reshape"), _n_(528296, "result", lambda: result), [-1, _n_(528297, "result_shape", lambda: result_shape)[0], _n_(528298, "result_shape", lambda: result_shape)[1]], name=_n_(528299, "layer_name", lambda: layer_name) + "_shaped_result")
    _l_(528301)