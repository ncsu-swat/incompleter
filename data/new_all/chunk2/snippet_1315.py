# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46630857/filenotfounderror-on-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
img = _n_(455906, "printscreen_pil", lambda: printscreen_pil)
_l_(455907)
img = _c_(455913, _a_(455909, _n_(455908, "img", lambda: img), "filter"), _c_(455912, _a_(455911, _n_(455910, "ImageFilter", lambda: ImageFilter), "MedianFilter")))
_l_(455914)
enhancer = _c_(455918, _a_(455916, _n_(455915, "ImageEnhance", lambda: ImageEnhance), "Contrast"), _n_(455917, "img", lambda: img))
_l_(455919)
img = _c_(455922, _a_(455921, _n_(455920, "enhancer", lambda: enhancer), "enhance"), 2)
_l_(455923)
img = _c_(455926, _a_(455925, _n_(455924, "img", lambda: img), "convert"), '1')
_l_(455927)
_c_(455930, _a_(455929, _n_(455928, "img", lambda: img), "save"), 'temp.jpg')
_l_(455931)
text = _c_(455937, _a_(455933, _n_(455932, "pytesseract", lambda: pytesseract), "image_to_string"), _c_(455936, _a_(455935, _n_(455934, "Image", lambda: Image), "open"), 'temp.jpg'))
_l_(455938)