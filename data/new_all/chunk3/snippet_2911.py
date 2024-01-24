# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58649555/typeerror-cannot-unpack-non-iterrable-nonetype-object-zbar-raspberry-pi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyzbar import pyzbar
    _l_(563071)

except ImportError:
    pass
try:
    import argparse
    _l_(563073)

except ImportError:
    pass
try:
    import cv2
    _l_(563075)

except ImportError:
    pass

#code
ap = _c_(563078, _a_(563077, _n_(563076, "argparse", lambda: argparse), "ArgumentParser"))
_l_(563079)
_c_(563082, _a_(563081, _n_(563080, "ap", lambda: ap), "add_argument"), "-i", "--image", required=True,
    help="chemin de l'image")
_l_(563083)
args = _c_(563088, _n_(563084, "vars", lambda: vars), _c_(563087, _a_(563086, _n_(563085, "ap", lambda: ap), "parse_args")))
_l_(563089)

#load l'image
image=_c_(563093, _a_(563091, _n_(563090, "cv2", lambda: cv2), "imread"), _n_(563092, "args", lambda: args)["image"])
_l_(563094)

#trouver lesQR/barcode dans l'image puisles decoder
barcodes=_c_(563098, _a_(563096, _n_(563095, "pyzbar", lambda: pyzbar), "decode"), _n_(563097, "image", lambda: image))
_l_(563099)

#loop barcode
for barcode in _n_(563100, "barcodes", lambda: barcodes):
    _l_(563145)

    #extraire les box des coins et faire un carre rouge autour du
    #barcode reconnu
    (x,y,w,h)=_a_(563102, _n_(563101, "barcode", lambda: barcode), "rect")
    _l_(563103)
    _c_(563113, _a_(563105, _n_(563104, "cv2", lambda: cv2), "rectangle"), _n_(563106, "image", lambda: image), (_n_(563107, "x", lambda: x),_n_(563108, "y", lambda: y)),(_n_(563109, "x", lambda: x)+_n_(563110, "w", lambda: w),_n_(563111, "y", lambda: y)+_n_(563112, "h", lambda: h)),(0,0,255), 2)
    _l_(563114)

    #barcode est un byte donc besoin convertir en string en premier
    barcodeData=_c_(563118, _a_(563117, _a_(563116, _n_(563115, "barcode", lambda: barcode), "data"), "decode"), "utf=8")
    _l_(563119)
    barcodeType=_a_(563121, _n_(563120, "barcode", lambda: barcode), "type")
    _l_(563122)

    #dessiner data barcode et ecrire sur image
    text=_c_(563126, _a_(563123, "{}({})", "format"), _n_(563124, "barcodeData", lambda: barcodeData),_n_(563125, "barcodeType", lambda: barcodeType))
    _l_(563127)
    _c_(563136, _a_(563129, _n_(563128, "cv2", lambda: cv2), "putText"), _n_(563130, "image", lambda: image),_n_(563131, "text", lambda: text),(_n_(563132, "x", lambda: x),_n_(563133, "y", lambda: y)-10),_a_(563135, _n_(563134, "cv2", lambda: cv2), "FONT_HERSHEY_SIMPLEX"),
        0.5, (0,0,255),2)
    _l_(563137)

    _c_(563143, _n_(563138, "print", lambda: print), _c_(563142, _a_(563139, "[INFO] {} code, contenu: {}", "format"), _n_(563140, "barcodeType", lambda: barcodeType),_n_(563141, "barcodeData", lambda: barcodeData)))
    _l_(563144)

#montrer output
_c_(563149, _a_(563147, _n_(563146, "cv2", lambda: cv2), "imshow"), "Image",_n_(563148, "image", lambda: image))
_l_(563150)
_c_(563153, _a_(563152, _n_(563151, "cv2", lambda: cv2), "waitKey"), 0)
_l_(563154)