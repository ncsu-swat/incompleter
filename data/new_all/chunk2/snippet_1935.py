# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/19034714/pygame-typeerror-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame,time,sys
    _l_(471612)

except ImportError:
    pass
try:
    from pygame import *
    _l_(471614)

except ImportError:
    pass



class pauseMenu():
    _l_(472057)


    goToMenu = False
    _l_(471615)
    imageDict = {}
    _l_(471616)
    textDict = {}
    _l_(471617)
    rectDict = {}
    _l_(471618)
    Clicked_Button = ''
    _l_(471619)
    DarkGrey =      (134, 134, 134)
    _l_(471620)
    volume = 10
    _l_(471621)
    FPSCLOCK = _c_(471625, _a_(471624, _a_(471623, _n_(471622, "pygame", lambda: pygame), "time"), "Clock"))
    _l_(471626)


    def pauseMenuFunct(self,screen,WINDIM):
        _l_(472052)

        _c_(471628, _n_(471627, "print", lambda: print), "made it here")
        _l_(471629)
        def check_collisions(self,pos,list):
            _l_(471644)

        # iterate dict, check for collisions in systems
        #     print('Made it to teh da function')
            for k,v in _c_(471632, _a_(471631, _n_(471630, "list", lambda: list), "items")):
                _l_(471643)

                # print('Made into to the for loop')
                if _c_(471636, _a_(471634, _n_(471633, "v", lambda: v), "collidepoint"), _n_(471635, "pos", lambda: pos)):
                    _l_(471642)

                    # print(v)
                    # print("clicked button:", k)
                    _n_(471637, "self", lambda: self).Clicked_Button = _n_(471638, "k", lambda: k)
                    _l_(471639)
                    aux = True,_n_(471640, "k", lambda: k)
                    _l_(471641)
                    # print(self.Clicked_Button)
                    return aux

        WINWIDTH,WINHEIGHT = _n_(471645, "WINDIM", lambda: WINDIM)
        _l_(471646)
        # print('Made it to the function')
        # screen.fill(background)
        imageDict = {'buttons': _c_(471650, _a_(471649, _a_(471648, _n_(471647, "pygame", lambda: pygame), "image"), "load"), 'Resources/Pics/PauseOptions.png')
        }
        _l_(471651)

        _n_(471652, "imageDict", lambda: imageDict)['buttons']=_c_(471663, _a_(471655, _a_(471654, _n_(471653, "pygame", lambda: pygame), "transform"), "smoothscale"), _n_(471656, "imageDict", lambda: imageDict)['buttons'],(_c_(471659, _n_(471657, "int", lambda: int), _n_(471658, "WINWIDTH", lambda: WINWIDTH)*.2),_c_(471662, _n_(471660, "int", lambda: int), _n_(471661, "WINHEIGHT", lambda: WINHEIGHT)*.1)))
        _l_(471664)

        buttonX,buttonY= _c_(471667, _a_(471666, _n_(471665, "imageDict", lambda: imageDict)['buttons'], "get_size"))
        _l_(471668)
        # print(buttonX , buttonY)
        textSize = _c_(471671, _n_(471669, "int", lambda: int), _n_(471670, "buttonY", lambda: buttonY)/2)
        _l_(471672)
        # print(textSize)
        _n_(471673, "self", lambda: self).font = _c_(471678, _a_(471676, _a_(471675, _n_(471674, "pygame", lambda: pygame), "font"), "Font"), 'Resources/chunkfont.ttf', _n_(471677, "textSize", lambda: textSize))
        _l_(471679)
        textOptions  = _c_(471685, _a_(471682, _a_(471681, _n_(471680, "self", lambda: self), "font"), "render"), "Options", 1, _a_(471684, _n_(471683, "self", lambda: self), "DarkGrey"))
        _l_(471686)
        textSave     = _c_(471692, _a_(471689, _a_(471688, _n_(471687, "self", lambda: self), "font"), "render"), "Save", 1, _a_(471691, _n_(471690, "self", lambda: self), "DarkGrey"))
        _l_(471693)
        textQuit     = _c_(471699, _a_(471696, _a_(471695, _n_(471694, "self", lambda: self), "font"), "render"), "Quit", 1, _a_(471698, _n_(471697, "self", lambda: self), "DarkGrey"))
        _l_(471700)
        textVolume   = _c_(471706, _a_(471703, _a_(471702, _n_(471701, "self", lambda: self), "font"), "render"), "Volume", 1, _a_(471705, _n_(471704, "self", lambda: self), "DarkGrey"))
        _l_(471707)
        textBackToGame = _c_(471713, _a_(471710, _a_(471709, _n_(471708, "self", lambda: self), "font"), "render"), 'Return', 1, _a_(471712, _n_(471711, "self", lambda: self), "DarkGrey"))
        _l_(471714)
        VolumePopUp  = _c_(471724, _a_(471717, _a_(471716, _n_(471715, "self", lambda: self), "font"), "render"), _c_(471721, _n_(471718, "str", lambda: str), _a_(471720, _n_(471719, "self", lambda: self), "volume")), 1, _a_(471723, _n_(471722, "self", lambda: self), "DarkGrey"))
        _l_(471725)
        textBackToMenu = _c_(471731, _a_(471728, _a_(471727, _n_(471726, "self", lambda: self), "font"), "render"), 'Menu', 1 , _a_(471730, _n_(471729, "self", lambda: self), "DarkGrey"))
        _l_(471732)


        _a_(471734, _n_(471733, "self", lambda: self), "rectDict")['Options'] =           _c_(471740, _a_(471736, _n_(471735, "screen", lambda: screen), "blit"), _n_(471737, "imageDict", lambda: imageDict)['buttons'], (_n_(471738, "WINWIDTH", lambda: WINWIDTH)/4,(_n_(471739, "WINHEIGHT", lambda: WINHEIGHT)/3)))
        _l_(471741)
        _a_(471743, _n_(471742, "self", lambda: self), "rectDict")['Save'] =              _c_(471749, _a_(471745, _n_(471744, "screen", lambda: screen), "blit"), _n_(471746, "imageDict", lambda: imageDict)['buttons'], (_n_(471747, "WINWIDTH", lambda: WINWIDTH)/2+60.5,_n_(471748, "WINHEIGHT", lambda: WINHEIGHT)/3))
        _l_(471750)
        _a_(471752, _n_(471751, "self", lambda: self), "rectDict")['Quit'] =              _c_(471758, _a_(471754, _n_(471753, "screen", lambda: screen), "blit"), _n_(471755, "imageDict", lambda: imageDict)['buttons'], (_n_(471756, "WINWIDTH", lambda: WINWIDTH)/4,(_n_(471757, "WINHEIGHT", lambda: WINHEIGHT)/2)))
        _l_(471759)
        _a_(471761, _n_(471760, "self", lambda: self), "rectDict")['Volume'] =            _c_(471767, _a_(471763, _n_(471762, "screen", lambda: screen), "blit"), _n_(471764, "imageDict", lambda: imageDict)['buttons'], ((_n_(471765, "WINWIDTH", lambda: WINWIDTH)/2+60.5),(_n_(471766, "WINHEIGHT", lambda: WINHEIGHT)/2)))
        _l_(471768)
        _a_(471770, _n_(471769, "self", lambda: self), "rectDict")['Return'] =            _c_(471776, _a_(471772, _n_(471771, "screen", lambda: screen), "blit"), _n_(471773, "imageDict", lambda: imageDict)['buttons'], (_n_(471774, "WINWIDTH", lambda: WINWIDTH)/4,(_n_(471775, "WINHEIGHT", lambda: WINHEIGHT)/1.5)))
        _l_(471777)
        _a_(471779, _n_(471778, "self", lambda: self), "rectDict")['Menu'] =              _c_(471785, _a_(471781, _n_(471780, "screen", lambda: screen), "blit"), _n_(471782, "imageDict", lambda: imageDict)['buttons'], (_n_(471783, "WINWIDTH", lambda: WINWIDTH)/2+60.5,_n_(471784, "WINHEIGHT", lambda: WINHEIGHT)/1.5))
        _l_(471786)
        _a_(471788, _n_(471787, "self", lambda: self), "textDict")['textOptions'] =       _c_(471796, _a_(471790, _n_(471789, "screen", lambda: screen), "blit"), _n_(471791, "textOptions", lambda: textOptions),(_n_(471792, "WINWIDTH", lambda: WINWIDTH)/4 + (_n_(471793, "buttonX", lambda: buttonX)/4),(_n_(471794, "WINHEIGHT", lambda: WINHEIGHT)/3+_n_(471795, "textSize", lambda: textSize)/2)))
        _l_(471797)
        _a_(471799, _n_(471798, "self", lambda: self), "textDict")['textQuit'] =          _c_(471807, _a_(471801, _n_(471800, "screen", lambda: screen), "blit"), _n_(471802, "textQuit", lambda: textQuit),(_n_(471803, "WINWIDTH", lambda: WINWIDTH)/4 + (_n_(471804, "buttonX", lambda: buttonX)/4),(_n_(471805, "WINHEIGHT", lambda: WINHEIGHT)/2+_n_(471806, "textSize", lambda: textSize)/2)))
        _l_(471808)
        _a_(471810, _n_(471809, "self", lambda: self), "textDict")['textSave'] =          _c_(471818, _a_(471812, _n_(471811, "screen", lambda: screen), "blit"), _n_(471813, "textSave", lambda: textSave),(_n_(471814, "WINWIDTH", lambda: WINWIDTH)/2+60.5 + (_n_(471815, "buttonX", lambda: buttonX)/3),(_n_(471816, "WINHEIGHT", lambda: WINHEIGHT)/3+_n_(471817, "textSize", lambda: textSize)/2)))
        _l_(471819)
        _a_(471821, _n_(471820, "self", lambda: self), "textDict")['textVolume'] =        _c_(471829, _a_(471823, _n_(471822, "screen", lambda: screen), "blit"), _n_(471824, "textVolume", lambda: textVolume),(_n_(471825, "WINWIDTH", lambda: WINWIDTH)/2+50.5 + (_n_(471826, "buttonX", lambda: buttonX)/4.5),(_n_(471827, "WINHEIGHT", lambda: WINHEIGHT)/2+_n_(471828, "textSize", lambda: textSize)/2)))
        _l_(471830)
        _a_(471832, _n_(471831, "self", lambda: self), "textDict")['textBacktoGame']=     _c_(471840, _a_(471834, _n_(471833, "screen", lambda: screen), "blit"), _n_(471835, "textBackToGame", lambda: textBackToGame),(_n_(471836, "WINWIDTH", lambda: WINWIDTH)/4+ (_n_(471837, "buttonX", lambda: buttonX)/4),(_n_(471838, "WINHEIGHT", lambda: WINHEIGHT)/1.5+_n_(471839, "textSize", lambda: textSize)/2)))
        _l_(471841)
        _a_(471843, _n_(471842, "self", lambda: self), "textDict")['textMenu']=           _c_(471851, _a_(471845, _n_(471844, "screen", lambda: screen), "blit"), _n_(471846, "textBackToMenu", lambda: textBackToMenu),(_n_(471847, "WINWIDTH", lambda: WINWIDTH)/2+60.5+ (_n_(471848, "buttonX", lambda: buttonX)/4),(_n_(471849, "WINHEIGHT", lambda: WINHEIGHT)/1.5+_n_(471850, "textSize", lambda: textSize)/2)))
        _l_(471852)
        _a_(471854, _n_(471853, "self", lambda: self), "textDict")['volumeNum']=          _c_(471862, _a_(471856, _n_(471855, "screen", lambda: screen), "blit"), _n_(471857, "VolumePopUp", lambda: VolumePopUp),(_n_(471858, "WINWIDTH", lambda: WINWIDTH)/2+55.5 + _n_(471859, "buttonX", lambda: buttonX)/1.25,(_n_(471860, "WINHEIGHT", lambda: WINHEIGHT)/2+_n_(471861, "textSize", lambda: textSize)/2)))
        _l_(471863)
        _c_(471867, _a_(471866, _a_(471865, _n_(471864, "pygame", lambda: pygame), "display"), "update"))
        _l_(471868)
        _c_(471870, _n_(471869, "print", lambda: print), 'made it to the update')
        _l_(471871)


        while True:
            _l_(472051)

            _c_(471875, _a_(471874, _a_(471873, _n_(471872, "self", lambda: self), "FPSCLOCK"), "tick"), 60)
            _l_(471876)
            for event in _c_(471880, _a_(471879, _a_(471878, _n_(471877, "pygame", lambda: pygame), "event"), "get")):
                _l_(472050)

                if _a_(471882, _n_(471881, "event", lambda: event), "type") == _n_(471883, "QUIT", lambda: QUIT):
                    _l_(472049)

                    _c_(471886, _a_(471885, _n_(471884, "sys", lambda: sys), "exit"))
                    _l_(471887)
                elif _a_(471889, _n_(471888, "event", lambda: event), "type") == _n_(471890, "KEYDOWN", lambda: KEYDOWN):
                    _l_(472048)

                    if _a_(471892, _n_(471891, "event", lambda: event), "key") == _n_(471893, "K_ESCAPE", lambda: K_ESCAPE):
                        _l_(471898)

                        _c_(471896, _a_(471895, _n_(471894, "sys", lambda: sys), "exit"))
                        _l_(471897)

                elif _a_(471900, _n_(471899, "event", lambda: event), "type") == _n_(471901, "MOUSEBUTTONDOWN", lambda: MOUSEBUTTONDOWN):
                    _l_(472047)

                    if _a_(471903, _n_(471902, "event", lambda: event), "button") == 1:
                        _l_(472046)

                        if _c_(471910, _n_(471904, "check_collisions", lambda: check_collisions), _n_(471905, "self", lambda: self),_a_(471907, _n_(471906, "event", lambda: event), "pos"),_a_(471909, _n_(471908, "self", lambda: self), "rectDict")):
                            _l_(471988)


                            # print('Button Clicked from Event Loop is: '+self.Clicked_Button)

                            if _a_(471912, _n_(471911, "self", lambda: self), "Clicked_Button") == 'Quit':
                                _l_(471987)

                                _c_(471915, _a_(471914, _n_(471913, "sys", lambda: sys), "exit"))
                                _l_(471916)
                            elif _a_(471918, _n_(471917, "self", lambda: self), "Clicked_Button") == 'Save':
                                _l_(471986)

                                _c_(471920, _n_(471919, "print", lambda: print), 'It will be saved later')
                                _l_(471921)
                            elif _a_(471923, _n_(471922, "self", lambda: self), "Clicked_Button") == 'Volume' and _a_(471925, _n_(471924, "self", lambda: self), "volume")>0:
                                _l_(471985)

                                _n_(471926, "self", lambda: self).volume -= 1
                                _l_(471927)
                                _c_(471931, _n_(471928, "print", lambda: print), _a_(471930, _n_(471929, "self", lambda: self), "volume"))
                                _l_(471932)

                                VolumePopUp  = _c_(471942, _a_(471935, _a_(471934, _n_(471933, "self", lambda: self), "font"), "render"), _c_(471939, _n_(471936, "str", lambda: str), _a_(471938, _n_(471937, "self", lambda: self), "volume")), 1, _a_(471941, _n_(471940, "self", lambda: self), "DarkGrey"))
                                _l_(471943)
                                _c_(471949, _a_(471945, _n_(471944, "screen", lambda: screen), "blit"), _n_(471946, "imageDict", lambda: imageDict)['buttons'], ((_n_(471947, "WINWIDTH", lambda: WINWIDTH)/2+60.5),(_n_(471948, "WINHEIGHT", lambda: WINHEIGHT)/2)))
                                _l_(471950)
                                _c_(471958, _a_(471952, _n_(471951, "screen", lambda: screen), "blit"), _n_(471953, "VolumePopUp", lambda: VolumePopUp),(_n_(471954, "WINWIDTH", lambda: WINWIDTH)/2+55.5 + _n_(471955, "buttonX", lambda: buttonX)/1.25,(_n_(471956, "WINHEIGHT", lambda: WINHEIGHT)/2+_n_(471957, "textSize", lambda: textSize)/2)))
                                _l_(471959)

                                _c_(471965, _a_(471962, _a_(471961, _n_(471960, "pygame", lambda: pygame), "display"), "update"), _a_(471964, _n_(471963, "self", lambda: self), "textDict")['volumeNum'])
                                _l_(471966)


                            elif _a_(471968, _n_(471967, "self", lambda: self), "Clicked_Button") == 'Return':
                                _l_(471984)

                                _c_(471970, _n_(471969, "print", lambda: print), 'This will close the menu and you return you to the game.')
                                _l_(471971)
                            elif _a_(471973, _n_(471972, "self", lambda: self), "Clicked_Button") == 'Options':
                                _l_(471983)

                                _c_(471975, _n_(471974, "print", lambda: print), 'This will take you to an options screen')
                                _l_(471976)
                            elif _a_(471978, _n_(471977, "self", lambda: self), "Clicked_Button") == 'Menu':
                                _l_(471982)

                                _c_(471980, _n_(471979, "print", lambda: print), 'Will take you to main menu sooner or later')
                                _l_(471981)
                    elif _a_(471990, _n_(471989, "event", lambda: event), "button") == 3:
                        _l_(472045)

                        if _c_(471997, _n_(471991, "check_collisions", lambda: check_collisions), _n_(471992, "self", lambda: self),_a_(471994, _n_(471993, "event", lambda: event), "pos"),_a_(471996, _n_(471995, "self", lambda: self), "rectDict")):
                            _l_(472044)

                            if _a_(471999, _n_(471998, "self", lambda: self), "Clicked_Button") == 'Volume' and _a_(472001, _n_(472000, "self", lambda: self), "volume")<10:
                                _l_(472043)

                                _n_(472002, "self", lambda: self).volume += 1
                                _l_(472003)
                                _c_(472007, _n_(472004, "print", lambda: print), _a_(472006, _n_(472005, "self", lambda: self), "volume"))
                                _l_(472008)

                                VolumePopUp  = _c_(472018, _a_(472011, _a_(472010, _n_(472009, "self", lambda: self), "font"), "render"), _c_(472015, _n_(472012, "str", lambda: str), _a_(472014, _n_(472013, "self", lambda: self), "volume")), 1, _a_(472017, _n_(472016, "self", lambda: self), "DarkGrey"))
                                _l_(472019)
                                _c_(472025, _a_(472021, _n_(472020, "screen", lambda: screen), "blit"), _n_(472022, "imageDict", lambda: imageDict)['buttons'], ((_n_(472023, "WINWIDTH", lambda: WINWIDTH)/2+60.5),(_n_(472024, "WINHEIGHT", lambda: WINHEIGHT)/2)))
                                _l_(472026)
                                _c_(472034, _a_(472028, _n_(472027, "screen", lambda: screen), "blit"), _n_(472029, "VolumePopUp", lambda: VolumePopUp),(_n_(472030, "WINWIDTH", lambda: WINWIDTH)/2+55.5 + _n_(472031, "buttonX", lambda: buttonX)/1.25,(_n_(472032, "WINHEIGHT", lambda: WINHEIGHT)/2+_n_(472033, "textSize", lambda: textSize)/2)))
                                _l_(472035)

                                _c_(472041, _a_(472038, _a_(472037, _n_(472036, "pygame", lambda: pygame), "display"), "update"), _a_(472040, _n_(472039, "self", lambda: self), "textDict")['volumeNum'])
                                _l_(472042)


    def __init__(self):
        _l_(472056)

        _c_(472054, _n_(472053, "print", lambda: print), 'PauseMenu _init_ ran')
        _l_(472055)