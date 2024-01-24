# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42090620/typeerror-int-object-is-not-iterable-on-gresycale-image
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import*
    _l_(624748)

except ImportError:
    pass
try:
    import tkinter as Tkinter
    _l_(624750)

except ImportError:
    pass
try:
    from tkinter import filedialog, DISABLED, messagebox as tkMessageBox
    _l_(624752)

except ImportError:
    pass
try:
    import os
    _l_(624754)

except ImportError:
    pass
try:
    import ntpath
    _l_(624756)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk, ImageFilter
    _l_(624758)

except ImportError:
    pass
try:
    import PIL
    _l_(624760)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(624762)

except ImportError:
    pass
try:
    from random import randint
    _l_(624764)

except ImportError:
    pass
try:
    import random
    _l_(624766)

except ImportError:
    pass
try:
    import PIL.ImageOps
    _l_(624768)

except ImportError:
    pass


def EchelleDeGris():
    _l_(624840)

    Ima2=_c_(624773, _a_(624770, _n_(624769, "Image", lambda: Image), "new"), "RGB",(_n_(624771, "z", lambda: z)[0],_n_(624772, "z", lambda: z)[1]))
    _l_(624774)
    px=_c_(624777, _a_(624776, _n_(624775, "Ima1", lambda: Ima1), "load"))
    _l_(624778)
    px1=_c_(624781, _a_(624780, _n_(624779, "Ima2", lambda: Ima2), "load"))
    _l_(624782)
    for x in _c_(624785, _n_(624783, "range", lambda: range), _n_(624784, "z", lambda: z)[0]):
        _l_(624816)

        for y in _c_(624788, _n_(624786, "range", lambda: range), _n_(624787, "z", lambda: z)[1]):
            _l_(624815)

            p=_n_(624789, "px", lambda: px)[_n_(624790, "x", lambda: x),_n_(624791, "y", lambda: y)]
            _l_(624792)
            if _c_(624795, _n_(624793, "type", lambda: type), _n_(624794, "p", lambda: p))==_n_(624796, "int", lambda: int):
                _l_(624801)

                p=(_n_(624797, "p", lambda: p),_n_(624798, "p", lambda: p),_n_(624799, "p", lambda: p))
                _l_(624800)
            o=_c_(624806, _n_(624802, "int", lambda: int), (_n_(624803, "p", lambda: p)[0]+_n_(624804, "p", lambda: p)[1]+_n_(624805, "p", lambda: p)[2])/3)
            _l_(624807)
            _n_(624808, "px1", lambda: px1)[_n_(624809, "x", lambda: x),_n_(624810, "y", lambda: y)]=(_n_(624811, "o", lambda: o),_n_(624812, "o", lambda: o),_n_(624813, "o", lambda: o))
            _l_(624814)
    _c_(624820, _a_(624818, _n_(624817, "Ima2", lambda: Ima2), "save"), ""+_n_(624819, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(624821)
    im2 = _c_(624825, _a_(624823, _n_(624822, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(624824, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(624826)
    _n_(624827, "main", lambda: main).image = _n_(624828, "im2", lambda: im2)
    _l_(624829)
    I2 = _c_(624834, _a_(624831, _n_(624830, "Tkinter", lambda: Tkinter), "Label"), _n_(624832, "main", lambda: main), image=_n_(624833, "im2", lambda: im2))
    _l_(624835)
    _c_(624838, _a_(624837, _n_(624836, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(624839)

def SupprimerImage():
    _l_(624851)

    I2 = _c_(624845, _a_(624842, _n_(624841, "Tkinter", lambda: Tkinter), "Label"), _n_(624843, "main", lambda: main), image=_n_(624844, "imt", lambda: imt))
    _l_(624846)
    _c_(624849, _a_(624848, _n_(624847, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(624850)

def Luminosite():
    _l_(624926)

    Ima2=_c_(624856, _a_(624853, _n_(624852, "Image", lambda: Image), "new"), "RGB",(_n_(624854, "z", lambda: z)[0],_n_(624855, "z", lambda: z)[1]))
    _l_(624857)
    px=_c_(624860, _a_(624859, _n_(624858, "Ima1", lambda: Ima1), "load"))
    _l_(624861)
    px1=_c_(624864, _a_(624863, _n_(624862, "Ima2", lambda: Ima2), "load"))
    _l_(624865)
    for x in _c_(624868, _n_(624866, "range", lambda: range), _n_(624867, "z", lambda: z)[0]):
        _l_(624902)

        for y in _c_(624871, _n_(624869, "range", lambda: range), _n_(624870, "z", lambda: z)[1]):
            _l_(624901)

            p=_n_(624872, "px", lambda: px)[_n_(624873, "x", lambda: x),_n_(624874, "y", lambda: y)]
            _l_(624875)
            if _c_(624878, _n_(624876, "type", lambda: type), _n_(624877, "p", lambda: p))==_n_(624879, "int", lambda: int):
                _l_(624884)

                p=(_n_(624880, "p", lambda: p),_n_(624881, "p", lambda: p),_n_(624882, "p", lambda: p))
                _l_(624883)
            _n_(624885, "px1", lambda: px1)[_n_(624886, "x", lambda: x),_n_(624887, "y", lambda: y)]=(_n_(624888, "p", lambda: p)[0]+_c_(624891, _a_(624890, _n_(624889, "S1", lambda: S1), "get")),_n_(624892, "p", lambda: p)[1]+_c_(624895, _a_(624894, _n_(624893, "S1", lambda: S1), "get")),_n_(624896, "p", lambda: p)[2]+_c_(624899, _a_(624898, _n_(624897, "S1", lambda: S1), "get")))
            _l_(624900)
    _c_(624906, _a_(624904, _n_(624903, "Ima2", lambda: Ima2), "save"), ""+_n_(624905, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(624907)
    im2 = _c_(624911, _a_(624909, _n_(624908, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(624910, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(624912)
    _n_(624913, "main", lambda: main).image = _n_(624914, "im2", lambda: im2)
    _l_(624915)
    I2 = _c_(624920, _a_(624917, _n_(624916, "Tkinter", lambda: Tkinter), "Label"), _n_(624918, "main", lambda: main), image=_n_(624919, "im2", lambda: im2))
    _l_(624921)
    _c_(624924, _a_(624923, _n_(624922, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(624925)

def AnnulerModifications():
    _l_(624937)

    I2 = _c_(624931, _a_(624928, _n_(624927, "Tkinter", lambda: Tkinter), "Label"), _n_(624929, "main", lambda: main), image=_n_(624930, "im1", lambda: im1))
    _l_(624932)
    _c_(624935, _a_(624934, _n_(624933, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(624936)

def get_pixel(pixels, x, y):
    _l_(624946)

    try:
        _l_(624945)

        aux = _n_(624938, "pixels", lambda: pixels)[_n_(624939, "x", lambda: x), _n_(624940, "y", lambda: y)]
        _l_(624941)
        return aux
    except _n_(624942, "IndexError", lambda: IndexError):
        _l_(624944)

        aux = None
        _l_(624943)
        return aux


def get_neighbors(pixels, x, y):
    _l_(625024)

    neighbors = _c_(624948, _n_(624947, "list", lambda: list))
    _l_(624949)
    _c_(624957, _a_(624951, _n_(624950, "neighbors", lambda: neighbors), "append"), _c_(624956, _n_(624952, "get_pixel", lambda: get_pixel), _n_(624953, "pixels", lambda: pixels), _n_(624954, "x", lambda: x), _n_(624955, "y", lambda: y) - 1))
    _l_(624958)
    _c_(624966, _a_(624960, _n_(624959, "neighbors", lambda: neighbors), "append"), _c_(624965, _n_(624961, "get_pixel", lambda: get_pixel), _n_(624962, "pixels", lambda: pixels), _n_(624963, "x", lambda: x), _n_(624964, "y", lambda: y) + 1))
    _l_(624967)
    _c_(624975, _a_(624969, _n_(624968, "neighbors", lambda: neighbors), "append"), _c_(624974, _n_(624970, "get_pixel", lambda: get_pixel), _n_(624971, "pixels", lambda: pixels), _n_(624972, "x", lambda: x) - 1, _n_(624973, "y", lambda: y)))
    _l_(624976)
    _c_(624984, _a_(624978, _n_(624977, "neighbors", lambda: neighbors), "append"), _c_(624983, _n_(624979, "get_pixel", lambda: get_pixel), _n_(624980, "pixels", lambda: pixels), _n_(624981, "x", lambda: x) + 1, _n_(624982, "y", lambda: y)))
    _l_(624985)
    _c_(624993, _a_(624987, _n_(624986, "neighbors", lambda: neighbors), "append"), _c_(624992, _n_(624988, "get_pixel", lambda: get_pixel), _n_(624989, "pixels", lambda: pixels), _n_(624990, "x", lambda: x) - 1, _n_(624991, "y", lambda: y) - 1))
    _l_(624994)
    _c_(625002, _a_(624996, _n_(624995, "neighbors", lambda: neighbors), "append"), _c_(625001, _n_(624997, "get_pixel", lambda: get_pixel), _n_(624998, "pixels", lambda: pixels), _n_(624999, "x", lambda: x) - 1, _n_(625000, "y", lambda: y) + 1))
    _l_(625003)
    _c_(625011, _a_(625005, _n_(625004, "neighbors", lambda: neighbors), "append"), _c_(625010, _n_(625006, "get_pixel", lambda: get_pixel), _n_(625007, "pixels", lambda: pixels), _n_(625008, "x", lambda: x) + 1, _n_(625009, "y", lambda: y) - 1))
    _l_(625012)
    _c_(625020, _a_(625014, _n_(625013, "neighbors", lambda: neighbors), "append"), _c_(625019, _n_(625015, "get_pixel", lambda: get_pixel), _n_(625016, "pixels", lambda: pixels), _n_(625017, "x", lambda: x) + 1, _n_(625018, "y", lambda: y) + 1))
    _l_(625021)
    aux = _n_(625022, "neighbors", lambda: neighbors)
    _l_(625023)
    return aux


def filter_art(pixels, size):
    _l_(625070)

    indexes = _c_(625026, _n_(625025, "dict", lambda: dict))
    _l_(625027)
    for x in _c_(625030, _n_(625028, "range", lambda: range), _n_(625029, "size", lambda: size)[0]):
        _l_(625060)

        for y in _c_(625033, _n_(625031, "range", lambda: range), _n_(625032, "size", lambda: size)[1]):
            _l_(625059)

            color = _c_(625038, _n_(625034, "get_pixel", lambda: get_pixel), _n_(625035, "pixels", lambda: pixels), _n_(625036, "x", lambda: x), _n_(625037, "y", lambda: y))
            _l_(625039)
            neighbors = _c_(625044, _n_(625040, "get_neighbors", lambda: get_neighbors), _n_(625041, "pixels", lambda: pixels), _n_(625042, "x", lambda: x), _n_(625043, "y", lambda: y))
            _l_(625045)
            new_color = _c_(625050, _a_(625049, _c_(625048, _n_(625046, "Counter", lambda: Counter), _n_(625047, "neighbors", lambda: neighbors)), "most_common"))[0][0]
            _l_(625051)
            if _n_(625052, "new_color", lambda: new_color) is not None:
                _l_(625058)

                _n_(625053, "indexes", lambda: indexes)[_n_(625054, "x", lambda: x), _n_(625055, "y", lambda: y)] = _n_(625056, "new_color", lambda: new_color)
                _l_(625057)
    for x, y in _n_(625061, "indexes", lambda: indexes):
        _l_(625069)

        _n_(625062, "pixels", lambda: pixels)[_n_(625063, "x", lambda: x), _n_(625064, "y", lambda: y)] = _n_(625065, "indexes", lambda: indexes)[_n_(625066, "x", lambda: x), _n_(625067, "y", lambda: y)]
        _l_(625068)


def pop_art(path_orig, path_mod, coef):
    _l_(625430)


    s=[]
    _l_(625071)
    for i in _c_(625073, _n_(625072, "range", lambda: range), 9):
        _l_(625194)


        r=(_c_(625075, _n_(625074, "randint", lambda: randint), 0,255), _c_(625077, _n_(625076, "randint", lambda: randint), 0,255), _c_(625079, _n_(625078, "randint", lambda: randint), 0,255))
        _l_(625080)
        g=(_c_(625082, _n_(625081, "randint", lambda: randint), 0,255), _c_(625084, _n_(625083, "randint", lambda: randint), 0,255), _c_(625086, _n_(625085, "randint", lambda: randint), 0,255))
        _l_(625087)
        b=(_c_(625089, _n_(625088, "randint", lambda: randint), 0,255), _c_(625091, _n_(625090, "randint", lambda: randint), 0,255), _c_(625093, _n_(625092, "randint", lambda: randint), 0,255))
        _l_(625094)

        image_orig = _c_(625098, _a_(625096, _n_(625095, "Image", lambda: Image), "open"), _n_(625097, "path_orig", lambda: path_orig))
        _l_(625099)
        size = _a_(625101, _n_(625100, "image_orig", lambda: image_orig), "size")
        _l_(625102)
        image_mod = _c_(625107, _a_(625104, _n_(625103, "Image", lambda: Image), "new"), "RGB",(_n_(625105, "size", lambda: size)[0],_n_(625106, "size", lambda: size)[1]))
        _l_(625108)
        pixels_orig = _c_(625111, _a_(625110, _n_(625109, "image_orig", lambda: image_orig), "load"))
        _l_(625112)
        pixels_mod = _c_(625115, _a_(625114, _n_(625113, "image_mod", lambda: image_mod), "load"))
        _l_(625116)
        for x in _c_(625119, _n_(625117, "range", lambda: range), _n_(625118, "size", lambda: size)[0]):
            _l_(625175)

            for y in _c_(625122, _n_(625120, "range", lambda: range), _n_(625121, "size", lambda: size)[1]):
                _l_(625174)

                p = _n_(625123, "pixels_orig", lambda: pixels_orig)[_n_(625124, "x", lambda: x), _n_(625125, "y", lambda: y)]
                _l_(625126)
                if _c_(625130, _n_(625127, "isinstance", lambda: isinstance), _n_(625128, "p", lambda: p), _n_(625129, "int", lambda: int)):
                    _l_(625148)

                    rgb = (_n_(625131, "p", lambda: p),_n_(625132, "p", lambda: p),_n_(625133, "p", lambda: p))
                    _l_(625134)
                elif _c_(625138, _n_(625135, "isinstance", lambda: isinstance), _n_(625136, "p", lambda: p), _n_(625137, "tuple", lambda: tuple)) and _c_(625141, _n_(625139, "len", lambda: len), _n_(625140, "p", lambda: p)) in (3, 4):
                    _l_(625147)

                    rgb = _n_(625142, "p", lambda: p)[:3]
                    _l_(625143)
                else:
                    raise _c_(625145, _n_(625144, "TypeError", lambda: TypeError), 'Unknown pallete')
                    _l_(625146)
                average_color = _c_(625151, _n_(625149, "sum", lambda: sum), _n_(625150, "rgb", lambda: rgb)) / 3
                _l_(625152)
                if _n_(625153, "average_color", lambda: average_color) <= 85:
                    _l_(625173)

                    _n_(625154, "pixels_mod", lambda: pixels_mod)[_n_(625155, "x", lambda: x), _n_(625156, "y", lambda: y)] = _n_(625157, "r", lambda: r)
                    _l_(625158)
                elif 85 < _n_(625159, "average_color", lambda: average_color) <= 170:
                    _l_(625172)

                    _n_(625160, "pixels_mod", lambda: pixels_mod)[_n_(625161, "x", lambda: x), _n_(625162, "y", lambda: y)] = _n_(625163, "g", lambda: g)
                    _l_(625164)
                elif _n_(625165, "average_color", lambda: average_color) > 170:
                    _l_(625171)

                    _n_(625166, "pixels_mod", lambda: pixels_mod)[_n_(625167, "x", lambda: x), _n_(625168, "y", lambda: y)] = _n_(625169, "b", lambda: b)
                    _l_(625170)
        for _ in _c_(625178, _n_(625176, "range", lambda: range), _n_(625177, "coef", lambda: coef)):
            _l_(625184)

            _c_(625182, _n_(625179, "filter_art", lambda: filter_art), _n_(625180, "pixels_mod", lambda: pixels_mod), _n_(625181, "size", lambda: size))
            _l_(625183)
        _c_(625191, _a_(625186, _n_(625185, "image_mod", lambda: image_mod), "save"), ''+_n_(625187, "dir_path", lambda: dir_path)+'\\PopArt\\Modified Images\\result'+_c_(625190, _n_(625188, "str", lambda: str), _n_(625189, "i", lambda: i))+'.png')
        _l_(625192)
        Img=[None]*9
        _l_(625193)
    for i in _c_(625196, _n_(625195, "range", lambda: range), 9):
        _l_(625252)

        _n_(625197, "Img", lambda: Img)[_n_(625198, "i", lambda: i)]=_c_(625205, _a_(625200, _n_(625199, "Image", lambda: Image), "open"), ""+_n_(625201, "dir_path", lambda: dir_path)+"\\PopArt\\Modified Images\\result"+_c_(625204, _n_(625202, "str", lambda: str), _n_(625203, "i", lambda: i))+".png")
        _l_(625206)
        basewidth = _c_(625211, _n_(625207, "int", lambda: int), _a_(625210, _n_(625208, "Img", lambda: Img)[_n_(625209, "i", lambda: i)], "size")[1]/3)
        _l_(625212)
        wpercent = (_n_(625213, "basewidth", lambda: basewidth) / _c_(625218, _n_(625214, "float", lambda: float), _a_(625217, _n_(625215, "Img", lambda: Img)[_n_(625216, "i", lambda: i)], "size")[0]))
        _l_(625219)
        hsize = _c_(625229, _n_(625220, "int", lambda: int), (_c_(625225, _n_(625221, "float", lambda: float), _a_(625224, _n_(625222, "Img", lambda: Img)[_n_(625223, "i", lambda: i)], "size")[1]) * _c_(625228, _n_(625226, "float", lambda: float), _n_(625227, "wpercent", lambda: wpercent) )))
        _l_(625230)
        _n_(625231, "Img", lambda: Img)[_n_(625232, "i", lambda: i)] = _c_(625241, _a_(625235, _n_(625233, "Img", lambda: Img)[_n_(625234, "i", lambda: i)], "resize"), (_n_(625236, "basewidth", lambda: basewidth) , _n_(625237, "hsize", lambda: hsize) ), _a_(625240, _a_(625239, _n_(625238, "PIL", lambda: PIL), "Image"), "ANTIALIAS"))
        _l_(625242)
        _c_(625250, _a_(625245, _n_(625243, "Img", lambda: Img)[_n_(625244, "i", lambda: i)], "save"), ''+_n_(625246, "dir_path", lambda: dir_path)+'\\PopArt\\Resized Images\\resized_image'+_c_(625249, _n_(625247, "str", lambda: str), _n_(625248, "i", lambda: i))+'.png')
        _l_(625251)


    Img1=[None]*9
    _l_(625253)
    pixels1=[None]*9
    _l_(625254)
    Imaz=_c_(625259, _a_(625256, _n_(625255, "Image", lambda: Image), "new"), "RGB",(_n_(625257, "basewidth", lambda: basewidth)*3,_n_(625258, "hsize", lambda: hsize)*3))
    _l_(625260)
    pixels=_c_(625263, _a_(625262, _n_(625261, "Imaz", lambda: Imaz), "load"))
    _l_(625264)
    for i in _c_(625266, _n_(625265, "range", lambda: range), 9):
        _l_(625284)

        _n_(625267, "Img1", lambda: Img1)[_n_(625268, "i", lambda: i)]=_c_(625275, _a_(625270, _n_(625269, "Image", lambda: Image), "open"), ''+_n_(625271, "dir_path", lambda: dir_path)+'\\PopArt\\Resized Images\\resized_image'+_c_(625274, _n_(625272, "str", lambda: str), _n_(625273, "i", lambda: i))+'.png')
        _l_(625276)
        _n_(625277, "pixels1", lambda: pixels1)[_n_(625278, "i", lambda: i)]=_c_(625282, _a_(625281, _n_(625279, "Img1", lambda: Img1)[_n_(625280, "i", lambda: i)], "load"))
        _l_(625283)


    for x in _c_(625287, _n_(625285, "range", lambda: range), 0,_n_(625286, "basewidth", lambda: basewidth)):
        _l_(625325)

        for y in _c_(625290, _n_(625288, "range", lambda: range), 0,_n_(625289, "hsize", lambda: hsize)):
            _l_(625298)

            _n_(625291, "pixels", lambda: pixels)[_n_(625292, "x", lambda: x),_n_(625293, "y", lambda: y)]=_n_(625294, "pixels1", lambda: pixels1)[0][_n_(625295, "x", lambda: x),_n_(625296, "y", lambda: y)]
            _l_(625297)
        for y in _c_(625302, _n_(625299, "range", lambda: range), _n_(625300, "hsize", lambda: hsize),_n_(625301, "hsize", lambda: hsize)*2):
            _l_(625311)

            _n_(625303, "pixels", lambda: pixels)[_n_(625304, "x", lambda: x),_n_(625305, "y", lambda: y)]=_n_(625306, "pixels1", lambda: pixels1)[1][_n_(625307, "x", lambda: x),_n_(625308, "y", lambda: y)-_n_(625309, "hsize", lambda: hsize)]
            _l_(625310)
        for y in _c_(625315, _n_(625312, "range", lambda: range), _n_(625313, "hsize", lambda: hsize)*2,_n_(625314, "hsize", lambda: hsize)*3):
            _l_(625324)

            _n_(625316, "pixels", lambda: pixels)[_n_(625317, "x", lambda: x),_n_(625318, "y", lambda: y)]=_n_(625319, "pixels1", lambda: pixels1)[2][_n_(625320, "x", lambda: x),_n_(625321, "y", lambda: y)-_n_(625322, "hsize", lambda: hsize)*2]
            _l_(625323)

    for x in _c_(625329, _n_(625326, "range", lambda: range), _n_(625327, "basewidth", lambda: basewidth),_n_(625328, "basewidth", lambda: basewidth)*2):
        _l_(625370)

        for y in _c_(625332, _n_(625330, "range", lambda: range), 0,_n_(625331, "hsize", lambda: hsize)):
            _l_(625341)

            _n_(625333, "pixels", lambda: pixels)[_n_(625334, "x", lambda: x),_n_(625335, "y", lambda: y)]=_n_(625336, "pixels1", lambda: pixels1)[3][_n_(625337, "x", lambda: x)-_n_(625338, "basewidth", lambda: basewidth),_n_(625339, "y", lambda: y)]
            _l_(625340)
        for y in _c_(625345, _n_(625342, "range", lambda: range), _n_(625343, "hsize", lambda: hsize),_n_(625344, "hsize", lambda: hsize)*2):
            _l_(625355)

            _n_(625346, "pixels", lambda: pixels)[_n_(625347, "x", lambda: x),_n_(625348, "y", lambda: y)]=_n_(625349, "pixels1", lambda: pixels1)[4][_n_(625350, "x", lambda: x)-_n_(625351, "basewidth", lambda: basewidth),_n_(625352, "y", lambda: y)-_n_(625353, "hsize", lambda: hsize)]
            _l_(625354)
        for y in _c_(625359, _n_(625356, "range", lambda: range), _n_(625357, "hsize", lambda: hsize)*2,_n_(625358, "hsize", lambda: hsize)*3):
            _l_(625369)

            _n_(625360, "pixels", lambda: pixels)[_n_(625361, "x", lambda: x),_n_(625362, "y", lambda: y)]=_n_(625363, "pixels1", lambda: pixels1)[5][_n_(625364, "x", lambda: x)-_n_(625365, "basewidth", lambda: basewidth),_n_(625366, "y", lambda: y)-_n_(625367, "hsize", lambda: hsize)*2]
            _l_(625368)

    for x in _c_(625374, _n_(625371, "range", lambda: range), _n_(625372, "basewidth", lambda: basewidth)*2,_n_(625373, "basewidth", lambda: basewidth)*3):
        _l_(625415)

        for y in _c_(625377, _n_(625375, "range", lambda: range), 0,_n_(625376, "hsize", lambda: hsize)):
            _l_(625386)

            _n_(625378, "pixels", lambda: pixels)[_n_(625379, "x", lambda: x),_n_(625380, "y", lambda: y)]=_n_(625381, "pixels1", lambda: pixels1)[6][_n_(625382, "x", lambda: x)-_n_(625383, "basewidth", lambda: basewidth)*2,_n_(625384, "y", lambda: y)]
            _l_(625385)
        for y in _c_(625390, _n_(625387, "range", lambda: range), _n_(625388, "hsize", lambda: hsize),_n_(625389, "hsize", lambda: hsize)*2):
            _l_(625400)

            _n_(625391, "pixels", lambda: pixels)[_n_(625392, "x", lambda: x),_n_(625393, "y", lambda: y)]=_n_(625394, "pixels1", lambda: pixels1)[7][_n_(625395, "x", lambda: x)-_n_(625396, "basewidth", lambda: basewidth)*2,_n_(625397, "y", lambda: y)-_n_(625398, "hsize", lambda: hsize)]
            _l_(625399)
        for y in _c_(625404, _n_(625401, "range", lambda: range), _n_(625402, "hsize", lambda: hsize)*2,_n_(625403, "hsize", lambda: hsize)*3):
            _l_(625414)

            _n_(625405, "pixels", lambda: pixels)[_n_(625406, "x", lambda: x),_n_(625407, "y", lambda: y)]=_n_(625408, "pixels1", lambda: pixels1)[8][_n_(625409, "x", lambda: x)-_n_(625410, "basewidth", lambda: basewidth)*2,_n_(625411, "y", lambda: y)-_n_(625412, "hsize", lambda: hsize)*2]
            _l_(625413)
    Imaz = _c_(625423, _a_(625417, _n_(625416, "Imaz", lambda: Imaz), "resize"), (_n_(625418, "size", lambda: size)[0] , _n_(625419, "size", lambda: size)[1] ), _a_(625422, _a_(625421, _n_(625420, "PIL", lambda: PIL), "Image"), "ANTIALIAS"))
    _l_(625424)
    _c_(625428, _a_(625426, _n_(625425, "Imaz", lambda: Imaz), "save"), ""+_n_(625427, "dir_path", lambda: dir_path)+"\\PopArt\\Result Image\\result.png")
    _l_(625429)


def usepop():
    _l_(625475)

    im2 = _c_(625434, _a_(625432, _n_(625431, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(625433, "dir_path", lambda: dir_path)+"\\Requirements\\traitement.png")
    _l_(625435)
    _n_(625436, "main", lambda: main).image = _n_(625437, "im2", lambda: im2)
    _l_(625438)
    I2 = _c_(625443, _a_(625440, _n_(625439, "Tkinter", lambda: Tkinter), "Label"), _n_(625441, "main", lambda: main), image=_n_(625442, "im2", lambda: im2))
    _l_(625444)
    _c_(625447, _a_(625446, _n_(625445, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(625448)
    _c_(625451, _a_(625450, _n_(625449, "I2", lambda: I2), "update_idletasks"))
    _l_(625452)
    _c_(625455, _n_(625453, "pop_art", lambda: pop_art), _n_(625454, "a", lambda: a), None, coef=4)
    _l_(625456)
    im2 = _c_(625460, _a_(625458, _n_(625457, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(625459, "dir_path", lambda: dir_path)+"\\PopArt\\Result Image\\result.png")
    _l_(625461)
    _n_(625462, "main", lambda: main).image = _n_(625463, "im2", lambda: im2)
    _l_(625464)
    I2 = _c_(625469, _a_(625466, _n_(625465, "Tkinter", lambda: Tkinter), "Label"), _n_(625467, "main", lambda: main), image=_n_(625468, "im2", lambda: im2))
    _l_(625470)
    _c_(625473, _a_(625472, _n_(625471, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(625474)

def change_contrast(level):
    _l_(625521)


    img = _c_(625479, _a_(625477, _n_(625476, "Image", lambda: Image), "open"), _n_(625478, "a", lambda: a))
    _l_(625480)
    _c_(625483, _a_(625482, _n_(625481, "img", lambda: img), "load"))
    _l_(625484)

    factor = (259 * (_n_(625485, "level", lambda: level)+255)) / (255 * (259-_n_(625486, "level", lambda: level)))
    _l_(625487)
    for x in _c_(625491, _n_(625488, "range", lambda: range), _a_(625490, _n_(625489, "img", lambda: img), "size")[0]):
        _l_(625518)

        for y in _c_(625495, _n_(625492, "range", lambda: range), _a_(625494, _n_(625493, "img", lambda: img), "size")[1]):
            _l_(625517)

            color = _c_(625500, _a_(625497, _n_(625496, "img", lambda: img), "getpixel"), (_n_(625498, "x", lambda: x), _n_(625499, "y", lambda: y)))
            _l_(625501)
            new_color = _c_(625508, _n_(625502, "tuple", lambda: tuple), (_c_(625506, _n_(625503, "int", lambda: int), _n_(625504, "factor", lambda: factor) * (_n_(625505, "c", lambda: c)-128) + 128) for c in _n_(625507, "color", lambda: color)))
            _l_(625509)
            _c_(625515, _a_(625511, _n_(625510, "img", lambda: img), "putpixel"), (_n_(625512, "x", lambda: x), _n_(625513, "y", lambda: y)), _n_(625514, "new_color", lambda: new_color))
            _l_(625516)
    aux = _n_(625519, "img", lambda: img)
    _l_(625520)

    return aux

def use_contrast():
    _l_(625551)

    result = _c_(625526, _n_(625522, "change_contrast", lambda: change_contrast), _c_(625525, _a_(625524, _n_(625523, "S2", lambda: S2), "get")))
    _l_(625527)
    _c_(625531, _a_(625529, _n_(625528, "result", lambda: result), "save"), ""+_n_(625530, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(625532)
    im2 = _c_(625536, _a_(625534, _n_(625533, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(625535, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(625537)
    _n_(625538, "main", lambda: main).image = _n_(625539, "im2", lambda: im2)
    _l_(625540)
    I2 = _c_(625545, _a_(625542, _n_(625541, "Tkinter", lambda: Tkinter), "Label"), _n_(625543, "main", lambda: main), image=_n_(625544, "im2", lambda: im2))
    _l_(625546)
    _c_(625549, _a_(625548, _n_(625547, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(625550)

def recherche_contours():
    _l_(625672)

    Ima2=_c_(625556, _a_(625553, _n_(625552, "Image", lambda: Image), "new"), "RGB",(_n_(625554, "z", lambda: z)[0],_n_(625555, "z", lambda: z)[1]))
    _l_(625557)
    px=_c_(625560, _a_(625559, _n_(625558, "Ima1", lambda: Ima1), "load"))
    _l_(625561)
    px1=_c_(625564, _a_(625563, _n_(625562, "Ima2", lambda: Ima2), "load"))
    _l_(625565)
    for x in _c_(625568, _n_(625566, "range", lambda: range), _n_(625567, "z", lambda: z)[0]):
        _l_(625599)

        for y in _c_(625571, _n_(625569, "range", lambda: range), _n_(625570, "z", lambda: z)[1]):
            _l_(625598)

            p=_n_(625572, "px", lambda: px)[_n_(625573, "x", lambda: x),_n_(625574, "y", lambda: y)]
            _l_(625575)
            if _c_(625578, _n_(625576, "type", lambda: type), _n_(625577, "p", lambda: p))==_n_(625579, "int", lambda: int):
                _l_(625584)

                p=(_n_(625580, "p", lambda: p),_n_(625581, "p", lambda: p),_n_(625582, "p", lambda: p))
                _l_(625583)
            o=_c_(625589, _n_(625585, "int", lambda: int), (_n_(625586, "p", lambda: p)[0]+_n_(625587, "p", lambda: p)[1]+_n_(625588, "p", lambda: p)[2])/3)
            _l_(625590)
            _n_(625591, "px1", lambda: px1)[_n_(625592, "x", lambda: x),_n_(625593, "y", lambda: y)]=(_n_(625594, "o", lambda: o),_n_(625595, "o", lambda: o),_n_(625596, "o", lambda: o))
            _l_(625597)
    Ima2 = _c_(625604, _a_(625601, _n_(625600, "Ima2", lambda: Ima2), "filter"), _a_(625603, _n_(625602, "ImageFilter", lambda: ImageFilter), "FIND_EDGES"))
    _l_(625605)
    image = _n_(625606, "Ima2", lambda: Ima2)
    _l_(625607)
    if _a_(625609, _n_(625608, "image", lambda: image), "mode") == 'RGBA':
        _l_(625653)

        r,g,b,a = _c_(625612, _a_(625611, _n_(625610, "image", lambda: image), "split"))
        _l_(625613)
        rgb_image = _c_(625619, _a_(625615, _n_(625614, "Image", lambda: Image), "merge"), 'RGB', (_n_(625616, "r", lambda: r),_n_(625617, "g", lambda: g),_n_(625618, "b", lambda: b)))
        _l_(625620)

        inverted_image = _c_(625624, _a_(625622, _a_(625621, PIL, "ImageOps"), "invert"), _n_(625623, "rgb_image", lambda: rgb_image))
        _l_(625625)

        r2,g2,b2 = _c_(625628, _a_(625627, _n_(625626, "inverted_image", lambda: inverted_image), "split"))
        _l_(625629)

        final_transparent_image = _c_(625636, _a_(625631, _n_(625630, "Image", lambda: Image), "merge"), 'RGBA', (_n_(625632, "r2", lambda: r2),_n_(625633, "g2", lambda: g2),_n_(625634, "b2", lambda: b2),_n_(625635, "a", lambda: a)))
        _l_(625637)

        _c_(625641, _a_(625639, _n_(625638, "final_transparent_image", lambda: final_transparent_image), "save"), ""+_n_(625640, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
        _l_(625642)

    else:
        inverted_image = _c_(625646, _a_(625644, _a_(625643, PIL, "ImageOps"), "invert"), _n_(625645, "image", lambda: image))
        _l_(625647)
        _c_(625651, _a_(625649, _n_(625648, "inverted_image", lambda: inverted_image), "save"), ""+_n_(625650, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
        _l_(625652)
    im2 = _c_(625657, _a_(625655, _n_(625654, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(625656, "dir_path", lambda: dir_path)+"\\Requirements\\ImageMod.png")
    _l_(625658)
    _n_(625659, "main", lambda: main).image = _n_(625660, "im2", lambda: im2)
    _l_(625661)
    I2 = _c_(625666, _a_(625663, _n_(625662, "Tkinter", lambda: Tkinter), "Label"), _n_(625664, "main", lambda: main), image=_n_(625665, "im2", lambda: im2))
    _l_(625667)
    _c_(625670, _a_(625669, _n_(625668, "I2", lambda: I2), "grid"), row=0, column=4, columnspan =4)
    _l_(625671)

main=_c_(625674, _n_(625673, "Tk", lambda: Tk))
_l_(625675)

_c_(625678, _a_(625677, _n_(625676, "main", lambda: main), "withdraw"))
_l_(625679)
a = _c_(625682, _a_(625681, _n_(625680, "filedialog", lambda: filedialog), "askopenfilename"))
_l_(625683)
_c_(625686, _a_(625685, _n_(625684, "main", lambda: main), "deiconify"))
_l_(625687)

dir_path = _c_(625695, _a_(625690, _a_(625689, _n_(625688, "os", lambda: os), "path"), "dirname"), _c_(625694, _a_(625693, _a_(625692, _n_(625691, "os", lambda: os), "path"), "realpath"), "Test2.py"))
_l_(625696)

_c_(625699, _a_(625698, _n_(625697, "main", lambda: main), "configure"), background="#a1dbcd")
_l_(625700)
_c_(625703, _a_(625702, _n_(625701, "main", lambda: main), "title"), "Photoshop Version.Megzari")
_l_(625704)

Ima1=_c_(625708, _a_(625706, _n_(625705, "Image", lambda: Image), "open"), _n_(625707, "a", lambda: a))
_l_(625709)
z=_a_(625711, _n_(625710, "Ima1", lambda: Ima1), "size")
_l_(625712)
nux=_c_(625717, _a_(625714, _n_(625713, "Image", lambda: Image), "new"), "RGB",(_n_(625715, "z", lambda: z)[0],_n_(625716, "z", lambda: z)[1]))
_l_(625718)
nuxy=_c_(625721, _a_(625720, _n_(625719, "nux", lambda: nux), "load"))
_l_(625722)
for x in _c_(625725, _n_(625723, "range", lambda: range), _n_(625724, "z", lambda: z)[0]):
    _l_(625734)

    for y in _c_(625728, _n_(625726, "range", lambda: range), _n_(625727, "z", lambda: z)[1]):
        _l_(625733)

        _n_(625729, "nuxy", lambda: nuxy)[_n_(625730, "x", lambda: x),_n_(625731, "y", lambda: y)]=(255,255,255)
        _l_(625732)
_c_(625738, _a_(625736, _n_(625735, "nux", lambda: nux), "save"), ""+_n_(625737, "dir_path", lambda: dir_path)+"\\Requirements\\Blank.png")
_l_(625739)


if _n_(625740, "z", lambda: z)>(400,400):
    _l_(625882)

    _c_(625743, _a_(625742, _n_(625741, "main", lambda: main), "withdraw"))
    _l_(625744)
    _c_(625747, _a_(625746, _n_(625745, "tkMessageBox", lambda: tkMessageBox), "showinfo"), "Resolution Error", "The image is too big, please select a smaller one.")
    _l_(625748)
    _c_(625751, _a_(625750, _n_(625749, "sys", lambda: sys), "exit"))
    _l_(625752)


elif _n_(625753, "z", lambda: z)<(400,400):
    _l_(625881)

    im1 = _c_(625757, _a_(625755, _n_(625754, "ImageTk", lambda: ImageTk), "PhotoImage"), file=_n_(625756, "a", lambda: a))
    _l_(625758)
    I1 = _c_(625763, _a_(625760, _n_(625759, "Tkinter", lambda: Tkinter), "Label"), _n_(625761, "main", lambda: main), image=_n_(625762, "im1", lambda: im1))
    _l_(625764)
    _c_(625767, _a_(625766, _n_(625765, "I1", lambda: I1), "grid"), row=0, column=1, columnspan =3)
    _l_(625768)
    imt = _c_(625772, _a_(625770, _n_(625769, "ImageTk", lambda: ImageTk), "PhotoImage"), file=""+_n_(625771, "dir_path", lambda: dir_path)+"\\Requirements\\Blank.png")
    _l_(625773)
    T1 = _c_(625778, _a_(625775, _n_(625774, "Tkinter", lambda: Tkinter), "Label"), _n_(625776, "main", lambda: main), image=_n_(625777, "imt", lambda: imt))
    _l_(625779)
    _c_(625782, _a_(625781, _n_(625780, "T1", lambda: T1), "grid"), row=0, column=4, columnspan =4)
    _l_(625783)
    B1 = _c_(625789, _a_(625785, _n_(625784, "Tkinter", lambda: Tkinter), "Button"), _n_(625786, "main", lambda: main), text ="Echelle de gris", command = _n_(625787, "EchelleDeGris", lambda: EchelleDeGris), fg="#a1dbcd", bg="#383a39", state=_n_(625788, "NORMAL", lambda: NORMAL))
    _l_(625790)
    _c_(625793, _a_(625792, _n_(625791, "B1", lambda: B1), "grid"), padx=20, pady=20, row=1, column=0)
    _l_(625794)
    B3 = _c_(625799, _a_(625796, _n_(625795, "Tkinter", lambda: Tkinter), "Button"), _n_(625797, "main", lambda: main), text ="Appliquer Luminosité", command = _n_(625798, "Luminosite", lambda: Luminosite), fg="#a1dbcd", bg="#383a39")
    _l_(625800)
    _c_(625803, _a_(625802, _n_(625801, "B3", lambda: B3), "grid"), padx=20, pady=20, row=1, column=1)
    _l_(625804)
    S1 = _c_(625808, _n_(625805, "Scale", lambda: Scale), _n_(625806, "main", lambda: main), from_=0, to=254, orient=_n_(625807, "HORIZONTAL", lambda: HORIZONTAL), fg="#a1dbcd", bg="#383a39", length = 200)
    _l_(625809)
    _c_(625812, _a_(625811, _n_(625810, "S1", lambda: S1), "grid"), row=2, column=1)
    _l_(625813)
    B2 = _c_(625818, _a_(625815, _n_(625814, "Tkinter", lambda: Tkinter), "Button"), _n_(625816, "main", lambda: main), text ="Supprimer Image", command = _n_(625817, "SupprimerImage", lambda: SupprimerImage), fg="#a1dbcd", bg="#383a39")
    _l_(625819)
    _c_(625822, _a_(625821, _n_(625820, "B2", lambda: B2), "grid"), padx=20, pady=20, row=1, column=7)
    _l_(625823)
    B3 = _c_(625828, _a_(625825, _n_(625824, "Tkinter", lambda: Tkinter), "Button"), _n_(625826, "main", lambda: main), text ="Annuler Modifications", command = _n_(625827, "AnnulerModifications", lambda: AnnulerModifications), fg="#a1dbcd", bg="#383a39")
    _l_(625829)
    _c_(625832, _a_(625831, _n_(625830, "B3", lambda: B3), "grid"), padx=20, pady=20, row=1, column=6)
    _l_(625833)
    B4 = _c_(625838, _a_(625835, _n_(625834, "Tkinter", lambda: Tkinter), "Button"), _n_(625836, "main", lambda: main), text ="Pop Art", command = _n_(625837, "usepop", lambda: usepop), fg="#a1dbcd", bg="#383a39")
    _l_(625839)
    _c_(625842, _a_(625841, _n_(625840, "B4", lambda: B4), "grid"), padx=20, pady=20, row=1, column=3)
    _l_(625843)
    S2 = _c_(625847, _n_(625844, "Scale", lambda: Scale), _n_(625845, "main", lambda: main), from_=-258, to=258, orient=_n_(625846, "HORIZONTAL", lambda: HORIZONTAL), fg="#a1dbcd", bg="#383a39", length = 200)
    _l_(625848)
    _c_(625851, _a_(625850, _n_(625849, "S2", lambda: S2), "grid"), row=2, column=4)
    _l_(625852)
    B4 = _c_(625857, _a_(625854, _n_(625853, "Tkinter", lambda: Tkinter), "Button"), _n_(625855, "main", lambda: main), text ="Appliquer Contraste", command = _n_(625856, "use_contrast", lambda: use_contrast), fg="#a1dbcd", bg="#383a39")
    _l_(625858)
    _c_(625861, _a_(625860, _n_(625859, "B4", lambda: B4), "grid"), padx=20, pady=20, row=1, column=4)
    _l_(625862)
    B5 = _c_(625867, _a_(625864, _n_(625863, "Tkinter", lambda: Tkinter), "Button"), _n_(625865, "main", lambda: main), text ="Trouver Contours", command = _n_(625866, "recherche_contours", lambda: recherche_contours), fg="#a1dbcd", bg="#383a39")
    _l_(625868)
    _c_(625871, _a_(625870, _n_(625869, "B5", lambda: B5), "grid"), padx=20, pady=20, row=1, column=5)
    _l_(625872)

    s=_c_(625875, _a_(625874, _n_(625873, "S1", lambda: S1), "get"))
    _l_(625876)
    s2=_c_(625879, _a_(625878, _n_(625877, "S2", lambda: S2), "get"))
    _l_(625880)





_c_(625885, _a_(625884, _n_(625883, "main", lambda: main), "mainloop"))
_l_(625886)