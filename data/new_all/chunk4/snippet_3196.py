# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77439178/typeerror-when-using-cv2-rectangle-in-python-opencv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
colors = [(245,117,16), (117,245,16), (16,117,245)]
_l_(599635)
def prob_viz(res, actions, input_frame, colors):
    _l_(599670)

    output_frame = _c_(599638, _a_(599637, _n_(599636, "input_frame", lambda: input_frame), "copy"))
    _l_(599639)
    for num, prob in _c_(599642, _n_(599640, "enumerate", lambda: enumerate), _n_(599641, "res", lambda: res)):
        _l_(599667)

        _c_(599653, _a_(599644, _n_(599643, "cv2", lambda: cv2), "rectangle"), _n_(599645, "output_frame", lambda: output_frame), (0,60+_n_(599646, "num", lambda: num)*40), (_c_(599649, _n_(599647, "int", lambda: int), _n_(599648, "prob", lambda: prob)*100), 90+_n_(599650, "num", lambda: num)*40), _n_(599651, "colors", lambda: colors)[_n_(599652, "num", lambda: num)], -1)
        _l_(599654)
        _c_(599665, _a_(599656, _n_(599655, "cv2", lambda: cv2), "putText"), _n_(599657, "output_frame", lambda: output_frame), _n_(599658, "actions", lambda: actions)[_n_(599659, "num", lambda: num)], (0, 85+_n_(599660, "num", lambda: num)*40), _a_(599662, _n_(599661, "cv2", lambda: cv2), "FONT_HERSHEY_SIMPLEX"), 1, (255,255,255), 2, _a_(599664, _n_(599663, "cv2", lambda: cv2), "LINE_AA"))
        _l_(599666)
    aux = _n_(599668, "output_frame", lambda: output_frame)
    _l_(599669)
    return aux
_c_(599673, _a_(599672, _n_(599671, "plt", lambda: plt), "figure"), figsize=(18,18))
_l_(599674)
_c_(599683, _a_(599676, _n_(599675, "plt", lambda: plt), "imshow"), _c_(599682, _n_(599677, "prob_viz", lambda: prob_viz), _n_(599678, "res", lambda: res), _n_(599679, "actions", lambda: actions), _n_(599680, "image", lambda: image), _n_(599681, "colors", lambda: colors))) 
_l_(599684) 