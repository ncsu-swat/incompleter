# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61568031/how-can-i-avoid-typeerror-not-supported-between-instances-of-tuple-and-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(662893)

except ImportError:
    pass

Malcolm_Brogdon_tendencies = { "Under_Basket_Rate" : 396, 
"Close_Left_Rate" : 32, "Close_Mid_Rate" : 50, "Close_Right_Rate" : 38, "Mid_Left_Rate" : 6, "Mid_Mleft_Rate" : 36, "Mid_Mleft" : 375, "Mid_Mid_Rate" : 47, 
"Mid_Mright_Rate" : 83, "Mid_Right_Rate" : 15, "Three_Left_Rate" : 8, "Three_Mleft_Rate" : 91, "Three_Mid_Rate" : 70, "Three_Mright_Rate" : 109, "Three_right_Rate" : 18}
_l_(662894)

Malcolm_Brogdon_Percentages = {"Under_Basket" : 487, "Close_Left" : 571, "Close_Mid" : 515, "Close_Right" : 480, "Mid_Left" : 500, "Mid_Mleft" : 375,
 "Mid_Mid" : 452, "Mid_Mright" : 564, "Mid_Right" : 400, "Three_Left" : 0, "Three_Mleft" : 350, "Three_Mid" : 261, "Three_Mright" : 319, "Three_Right" : 417}
_l_(662895)

Malcolm_Brogdon_Person = {"Shot_Attempts" : _c_(662898, _a_(662897, _n_(662896, "random", lambda: random), "randint"), 10,16)}
_l_(662899)

do_not_include = [0]
_l_(662900)
total_shots = 0
_l_(662901)


while _n_(662902, "total_shots", lambda: total_shots)< _n_(662903, "Malcolm_Brogdon_Person", lambda: Malcolm_Brogdon_Person)["Shot_Attempts"]:
    _l_(662930)

    for tendencies, numbers in _c_(662906, _a_(662905, _n_(662904, "Malcolm_Brogdon_tendencies", lambda: Malcolm_Brogdon_tendencies), "items")):
        _l_(662929)

        for numbers in _c_(662909, _a_(662908, _n_(662907, "Malcolm_Brogdon_tendencies", lambda: Malcolm_Brogdon_tendencies), "items")):
            _l_(662928)

            while _n_(662910, "numbers", lambda: numbers) > 0:
                _l_(662927)

                shot_distribution = _c_(662913, _a_(662912, _n_(662911, "random", lambda: random), "randint"), 1,1001) 
                _l_(662914) 
                if _n_(662915, "shot_distribution", lambda: shot_distribution) not in _n_(662916, "do_not_include", lambda: do_not_include):
                    _l_(662926)

                    _c_(662920, _a_(662918, _n_(662917, "do_not_include", lambda: do_not_include), "append"), _n_(662919, "shot_distribution", lambda: shot_distribution)) 
                    _l_(662921) 
                    total_shots = _n_(662922, "total_shots", lambda: total_shots) + 1 
                    _l_(662923) 
                    numbers = _n_(662924, "numbers", lambda: numbers) - 1 
                    _l_(662925) 
_c_(662933, _n_(662931, "print", lambda: print), _n_(662932, "do_not_include", lambda: do_not_include))
_l_(662934)