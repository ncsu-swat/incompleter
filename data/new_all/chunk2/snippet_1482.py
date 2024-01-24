# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53217439/car-tracking-cascade-typeerror-integer-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(470565)

except ImportError:
    pass
try:
    import numpy as np
    _l_(470567)

except ImportError:
    pass

def diffUpDown(img):
    _l_(470603)

    # compare top and bottom size of the image
    # 1. cut image in two
    # 2. flip the top side
    # 3. resize to same size
    # 4. compare difference  
    height, width, depth = _a_(470569, _n_(470568, "img", lambda: img), "shape")
    _l_(470570)
    half = _n_(470571, "height", lambda: height)/2
    _l_(470572)
    top = _n_(470573, "img", lambda: img)[0:_n_(470574, "half", lambda: half), 0:_n_(470575, "width", lambda: width)]
    _l_(470576)
    bottom = _n_(470577, "img", lambda: img)[_n_(470578, "half", lambda: half):_n_(470579, "half", lambda: half)+_n_(470580, "half", lambda: half), 0:_n_(470581, "width", lambda: width)]
    _l_(470582)
    top = _c_(470586, _a_(470584, _n_(470583, "cv2", lambda: cv2), "flip"), _n_(470585, "top", lambda: top),1)
    _l_(470587)
    bottom = _c_(470591, _a_(470589, _n_(470588, "cv2", lambda: cv2), "resize"), _n_(470590, "bottom", lambda: bottom), (32, 64)) 
    _l_(470592) 
    top = _c_(470596, _a_(470594, _n_(470593, "cv2", lambda: cv2), "resize"), _n_(470595, "top", lambda: top), (32, 64))  
    _l_(470597)  
    aux = _c_(470601, _n_(470598, "mse", lambda: mse), _n_(470599, "top", lambda: top),_n_(470600, "bottom", lambda: bottom))
    _l_(470602)
    return aux


def diffLeftRight(img):
    _l_(470639)

    # compare left and right size of the image
    # 1. cut image in two
    # 2. flip the right side
    # 3. resize to same size
    # 4. compare difference  
    height, width, depth = _a_(470605, _n_(470604, "img", lambda: img), "shape")
    _l_(470606)
    half = _n_(470607, "width", lambda: width)/2
    _l_(470608)
    left = _n_(470609, "img", lambda: img)[0:_n_(470610, "height", lambda: height), 0:_n_(470611, "half", lambda: half)]
    _l_(470612)
    right = _n_(470613, "img", lambda: img)[0:_n_(470614, "height", lambda: height), _n_(470615, "half", lambda: half):_n_(470616, "half", lambda: half) + _n_(470617, "half", lambda: half)-1]
    _l_(470618)
    right = _c_(470622, _a_(470620, _n_(470619, "cv2", lambda: cv2), "flip"), _n_(470621, "right", lambda: right),1)
    _l_(470623)
    left = _c_(470627, _a_(470625, _n_(470624, "cv2", lambda: cv2), "resize"), _n_(470626, "left", lambda: left), (32, 64)) 
    _l_(470628) 
    right = _c_(470632, _a_(470630, _n_(470629, "cv2", lambda: cv2), "resize"), _n_(470631, "right", lambda: right), (32, 64))  
    _l_(470633)  
    aux = _c_(470637, _n_(470634, "mse", lambda: mse), _n_(470635, "left", lambda: left),_n_(470636, "right", lambda: right))
    _l_(470638)
    return aux


def mse(imageA, imageB):
    _l_(470659)

    err = _c_(470648, _a_(470641, _n_(470640, "np", lambda: np), "sum"), (_c_(470644, _a_(470643, _n_(470642, "imageA", lambda: imageA), "astype"), "float") - _c_(470647, _a_(470646, _n_(470645, "imageB", lambda: imageB), "astype"), "float")) ** 2)
    _l_(470649)
    err /= _c_(470655, _n_(470650, "float", lambda: float), _a_(470652, _n_(470651, "imageA", lambda: imageA), "shape")[0] * _a_(470654, _n_(470653, "imageA", lambda: imageA), "shape")[1])
    _l_(470656)
    aux = _n_(470657, "err", lambda: err)
    _l_(470658)
    return aux

def isNewRoi(rx,ry,rw,rh,rectangles):
    _l_(470673)

    for r in _n_(470660, "rectangles", lambda: rectangles):
        _l_(470671)

        if _c_(470664, _n_(470661, "abs", lambda: abs), _n_(470662, "r", lambda: r)[0] - _n_(470663, "rx", lambda: rx)) < 40 and _c_(470668, _n_(470665, "abs", lambda: abs), _n_(470666, "r", lambda: r)[1] - _n_(470667, "ry", lambda: ry)) < 40:
            _l_(470670)

            aux = False  
            _l_(470669)  
            return aux  
    aux = True
    _l_(470672)
    return aux

def detectRegionsOfInterest(frame, cascade):
    _l_(470751)

    scaleDown = 2
    _l_(470674)
    frameHeight, frameWidth, fdepth = _a_(470676, _n_(470675, "frame", lambda: frame), "shape") 
    _l_(470677) 

    # Resize
    frame = _c_(470685, _a_(470679, _n_(470678, "cv2", lambda: cv2), "resize"), _n_(470680, "frame", lambda: frame), (_n_(470681, "frameWidth", lambda: frameWidth)/_n_(470682, "scaleDown", lambda: scaleDown), _n_(470683, "frameHeight", lambda: frameHeight)/_n_(470684, "scaleDown", lambda: scaleDown))) 
    _l_(470686) 
    frameHeight, frameWidth, fdepth = _a_(470688, _n_(470687, "frame", lambda: frame), "shape") 
    _l_(470689) 

    # haar detection.
    cars = _c_(470693, _a_(470691, _n_(470690, "cascade", lambda: cascade), "detectMultiScale"), _n_(470692, "frame", lambda: frame), 1.2, 1)
    _l_(470694)

    newRegions = []
    _l_(470695)
    minY = _c_(470698, _n_(470696, "int", lambda: int), _n_(470697, "frameHeight", lambda: frameHeight)*0.3)
    _l_(470699)

    # iterate regions of interest
    for (x,y,w,h) in _n_(470700, "cars", lambda: cars):
        _l_(470748)

        roi = [_n_(470701, "x", lambda: x),_n_(470702, "y", lambda: y),_n_(470703, "w", lambda: w),_n_(470704, "h", lambda: h)]
        _l_(470705)
        roiImage = _n_(470706, "frame", lambda: frame)[_n_(470707, "y", lambda: y):_n_(470708, "y", lambda: y)+_n_(470709, "h", lambda: h), _n_(470710, "x", lambda: x):_n_(470711, "x", lambda: x)+_n_(470712, "w", lambda: w)]   
        _l_(470713)   

        carWidth = _a_(470715, _n_(470714, "roiImage", lambda: roiImage), "shape")[0]
        _l_(470716)
        if _n_(470717, "y", lambda: y) > _n_(470718, "minY", lambda: minY):
            _l_(470747)

            diffX = _c_(470721, _n_(470719, "diffLeftRight", lambda: diffLeftRight), _n_(470720, "roiImage", lambda: roiImage))
            _l_(470722)
            diffY = _c_(470727, _n_(470723, "round", lambda: round), _c_(470726, _n_(470724, "diffUpDown", lambda: diffUpDown), _n_(470725, "roiImage", lambda: roiImage)))
            _l_(470728)

            if _n_(470729, "diffX", lambda: diffX) > 1600 and _n_(470730, "diffX", lambda: diffX) < 3000 and _n_(470731, "diffY", lambda: diffY) > 12000:
                _l_(470746)

                rx,ry,rw,rh = _n_(470732, "roi", lambda: roi)
                _l_(470733)
                _c_(470744, _a_(470735, _n_(470734, "newRegions", lambda: newRegions), "append"), [_n_(470736, "rx", lambda: rx)*_n_(470737, "scaleDown", lambda: scaleDown),_n_(470738, "ry", lambda: ry)*_n_(470739, "scaleDown", lambda: scaleDown),_n_(470740, "rw", lambda: rw)*_n_(470741, "scaleDown", lambda: scaleDown),_n_(470742, "rh", lambda: rh)*_n_(470743, "scaleDown", lambda: scaleDown)] )
                _l_(470745)
    aux = _n_(470749, "newRegions", lambda: newRegions)
    _l_(470750)

    return aux


def detectCars(filename):
    _l_(470834)

    rectangles = []
    _l_(470752)
    cascade = _c_(470755, _a_(470754, _n_(470753, "cv2", lambda: cv2), "CascadeClassifier"), 'cars.xml')
    _l_(470756)
    vc = _c_(470760, _a_(470758, _n_(470757, "cv2", lambda: cv2), "VideoCapture"), _n_(470759, "filename", lambda: filename))
    _l_(470761)

    if _c_(470764, _a_(470763, _n_(470762, "vc", lambda: vc), "isOpened")):
        _l_(470770)

        rval , frame = _c_(470767, _a_(470766, _n_(470765, "vc", lambda: vc), "read"))
        _l_(470768)
    else:
        rval = False
        _l_(470769)

    roi = [0,0,0,0]
    _l_(470771)
    frameCount = 0
    _l_(470772)

    while _n_(470773, "rval", lambda: rval):
        _l_(470814)

        rval, frame = _c_(470776, _a_(470775, _n_(470774, "vc", lambda: vc), "read"))
        _l_(470777)
        frameHeight, frameWidth, fdepth = _a_(470779, _n_(470778, "frame", lambda: frame), "shape") 
        _l_(470780) 

        newRegions = _c_(470784, _n_(470781, "detectRegionsOfInterest", lambda: detectRegionsOfInterest), _n_(470782, "frame", lambda: frame), _n_(470783, "cascade", lambda: cascade))
        _l_(470785)
        for region in _n_(470786, "newRegions", lambda: newRegions):
            _l_(470800)

            if _c_(470793, _n_(470787, "isNewRoi", lambda: isNewRoi), _n_(470788, "region", lambda: region)[0],_n_(470789, "region", lambda: region)[1],_n_(470790, "region", lambda: region)[2],_n_(470791, "region", lambda: region)[3],_n_(470792, "rectangles", lambda: rectangles)):
                _l_(470799)

                _c_(470797, _a_(470795, _n_(470794, "rectangles", lambda: rectangles), "append"), _n_(470796, "region", lambda: region))
                _l_(470798)

        for r in _n_(470801, "rectangles", lambda: rectangles):
            _l_(470813)

            _c_(470811, _a_(470803, _n_(470802, "cv2", lambda: cv2), "rectangle"), _n_(470804, "frame", lambda: frame),(_n_(470805, "r", lambda: r)[0],_n_(470806, "r", lambda: r)[1]),(_n_(470807, "r", lambda: r)[0]+_n_(470808, "r", lambda: r)[2],_n_(470809, "r", lambda: r)[1]+_n_(470810, "r", lambda: r)[3]), 
(0,0,255),3) 
            _l_(470812) 

    frameCount = _n_(470815, "frameCount", lambda: frameCount) + 1
    _l_(470816)
    if _n_(470817, "frameCount", lambda: frameCount) > 30:
        _l_(470829)

        frameCount = 0
        _l_(470818)
        rectangles = []
        _l_(470819)

    # show result
        _c_(470823, _a_(470821, _n_(470820, "cv2", lambda: cv2), "imshow"), "Result",_n_(470822, "frame", lambda: frame))
        _l_(470824)
        _c_(470827, _a_(470826, _n_(470825, "cv2", lambda: cv2), "waitKey"), 1);
        _l_(470828)
    _c_(470832, _a_(470831, _n_(470830, "vc", lambda: vc), "release"))
    _l_(470833)

_c_(470836, _n_(470835, "detectCars", lambda: detectCars), '../DeteccionVehiculos/road.mp4')
_l_(470837)