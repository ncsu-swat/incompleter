# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68196436/attributeerror-event-object-has-no-attribute-x-win-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(553995)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(553997)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(553999)

except ImportError:
    pass
try:
    from tkinter import font
    _l_(554001)

except ImportError:
    pass

win = _c_(554004, _a_(554003, _n_(554002, "tk", lambda: tk), "Tk"))
_l_(554005)
_c_(554008, _a_(554007, _n_(554006, "win", lambda: win), "overrideredirect"), 1)
_l_(554009)





# def realcenter( o, w, h ) ->'o(w,h) centered on screen':
#     x = o.winfo_screenwidth( ) - w
#     y = o.winfo_screenheight( ) - h
#     o.geometry( f'{w}x{h}+{int( x/2 )}+{int( y/2 )}' )

# def restore( ev ):
#     win.overrideredirect( 0 )

# def unrestore( ev ):
#     win.overrideredirect( 1 )

# win.geometry( '500x525' )
# realcenter( win, 500, 525)

# win.update_idletasks()

# win.overrideredirect( 1 )

# win.bind( '<F1>', restore )
# win.bind( '<F2>', unrestore )

font1 = _c_(554012, _a_(554011, _n_(554010, "font", lambda: font), "Font"), family = 'Helvetica', size = 15)
_l_(554013)
font3 = _c_(554016, _a_(554015, _n_(554014, "font", lambda: font), "Font"), family = 'Helvetica', size = 8, weight = 'bold')
_l_(554017)
font2 = _c_(554020, _a_(554019, _n_(554018, "font", lambda: font), "Font"), family = 'Helvetica', size = 20, weight = 'bold')
_l_(554021)

def aaa(colora, colorb, colorc, colord, colore, colorf):
    _l_(554029)

    Dark = _c_(554023, _n_(554022, "Theme", lambda: Theme), '#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F")
    _l_(554024)
    _c_(554027, _n_(554025, "Ecrire", lambda: Ecrire), '',_n_(554026, "Light", lambda: Light))
    _l_(554028)

def aaaa(colora, colorb, colorc, colord, colore, colorf):
    _l_(554037)

    Light = _c_(554031, _n_(554030, "Theme", lambda: Theme), '#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#C47ED6")
    _l_(554032)
    _c_(554035, _n_(554033, "Ecrire", lambda: Ecrire), '',_n_(554034, "Dark", lambda: Dark))
    _l_(554036)

def strl(list):
    _l_(554044)

    
    list =_c_(554040, _a_(554038, "", "join"), _n_(554039, "list", lambda: list))
    _l_(554041)
    aux = _n_(554042, "list", lambda: list)
    _l_(554043)
    return aux



# menubar = Menu(win)
# win.config(menu=menubar)
# menufichier = Menu(menubar,tearoff=0)
# menubar.add_cascade(label="Theme", menu=menufichier) 
# menufichier.add_command(label=" Dark mode",font = font3,command =lambda: aaa('#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F"))
# menufichier.add_command(label=" Light mode",font = font3,command =lambda: aaaa('#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#C47ED6"))
 
pixel = _c_(554047, _a_(554046, _n_(554045, "tk", lambda: tk), "PhotoImage"), width=1, height=1)
_l_(554048)

a =95
_l_(554049)
b =95
_l_(554050)

theme = 0
_l_(554051)
t = 0
_l_(554052)

ecrit = []
_l_(554053)
nombre_de_multdiv = 0
_l_(554054)
nombre_de_sous_add = 0
_l_(554055)

def Del(self):
    _l_(554071)

    global ecrit
    _l_(554056)
    del ecrit[-1]
    _l_(554057)
    affichage = _c_(554060, _n_(554058, "strl", lambda: strl), _n_(554059, "ecrit", lambda: ecrit))
    _l_(554061)
    _a_(554063, _n_(554062, "self", lambda: self), "label1")['text'] = _n_(554064, "affichage", lambda: affichage)
    _l_(554065)
    _c_(554069, _a_(554068, _a_(554067, _n_(554066, "self", lambda: self), "label1"), "place"), anchor = 'e', x = 450, y = 75)
    _l_(554070)

def Del_all(self):
    _l_(554087)

    global ecrit
    _l_(554072)
    del ecrit[:]
    _l_(554073)
    affichage = _c_(554076, _n_(554074, "strl", lambda: strl), _n_(554075, "ecrit", lambda: ecrit))
    _l_(554077)
    _a_(554079, _n_(554078, "self", lambda: self), "label1")['text'] = _n_(554080, "affichage", lambda: affichage)
    _l_(554081)
    _c_(554085, _a_(554084, _a_(554083, _n_(554082, "self", lambda: self), "label1"), "place"), anchor = 'e', x = 450, y = 75)
    _l_(554086)

def Ecrire(symbole,self):
    _l_(554106)


    _c_(554091, _a_(554089, _n_(554088, "ecrit", lambda: ecrit), "append"), _n_(554090, "symbole", lambda: symbole))
    _l_(554092)
    affichage = _c_(554095, _n_(554093, "strl", lambda: strl), _n_(554094, "ecrit", lambda: ecrit))
    _l_(554096)
    _a_(554098, _n_(554097, "self", lambda: self), "label1")['text'] = _n_(554099, "affichage", lambda: affichage)
    _l_(554100)
    _c_(554104, _a_(554103, _a_(554102, _n_(554101, "self", lambda: self), "label1"), "place"), anchor = 'e', x = 450, y = 75)
    _l_(554105)


def Ecrire_Resulat(valeur,self):
    _l_(554115)

    valeur = _c_(554109, _n_(554107, "strl", lambda: strl), _n_(554108, "valeur", lambda: valeur))
    _l_(554110)
    _a_(554112, _n_(554111, "self", lambda: self), "label1")['text'] = _n_(554113, "valeur", lambda: valeur)
    _l_(554114)

def Calcul(self):
    _l_(554477)

    global nombre_de_multdiv
    _l_(554116)
    global nombre_de_sous_add
    _l_(554117)

    for i in _c_(554122, _n_(554118, "range", lambda: range), _c_(554121, _n_(554119, "len", lambda: len), _n_(554120, "ecrit", lambda: ecrit))):
        _l_(554129)

        if _n_(554123, "ecrit", lambda: ecrit)[_n_(554124, "i", lambda: i)]  == '/' or _n_(554125, "ecrit", lambda: ecrit)[_n_(554126, "i", lambda: i)] == '*':
            _l_(554128)

            nombre_de_multdiv +=1
            _l_(554127)
    for i in _c_(554134, _n_(554130, "range", lambda: range), _c_(554133, _n_(554131, "len", lambda: len), _n_(554132, "ecrit", lambda: ecrit))):
        _l_(554141)

        if _n_(554135, "ecrit", lambda: ecrit)[_n_(554136, "i", lambda: i)]  == '+' or _n_(554137, "ecrit", lambda: ecrit)[_n_(554138, "i", lambda: i)] == '-':
            _l_(554140)

            nombre_de_sous_add +=1
            _l_(554139)

    for i in _c_(554144, _n_(554142, "range", lambda: range), _n_(554143, "nombre_de_multdiv", lambda: nombre_de_multdiv)):
        _l_(554306)


        for i in _c_(554149, _n_(554145, "range", lambda: range), _c_(554148, _n_(554146, "len", lambda: len), _n_(554147, "ecrit", lambda: ecrit))):
            _l_(554305)

            if _n_(554150, "ecrit", lambda: ecrit)[_n_(554151, "i", lambda: i)] == '*' or _n_(554152, "ecrit", lambda: ecrit)[_n_(554153, "i", lambda: i)] == '/':
                _l_(554304)


                numero = _n_(554154, "i", lambda: i)
                _l_(554155)
                nb = _n_(554156, "i", lambda: i)
                _l_(554157)
                nbb = _n_(554158, "i", lambda: i)
                _l_(554159)

                for i in _c_(554165, _n_(554160, "range", lambda: range), _c_(554163, _n_(554161, "len", lambda: len), _n_(554162, "ecrit", lambda: ecrit))-_n_(554164, "numero", lambda: numero)-1):
                    _l_(554194)


                    if _n_(554166, "ecrit", lambda: ecrit)[_n_(554167, "i", lambda: i)+1 + _n_(554168, "numero", lambda: numero)] != '/' and _n_(554169, "ecrit", lambda: ecrit)[_n_(554170, "i", lambda: i)+1 + _n_(554171, "numero", lambda: numero)] != '*' and _n_(554172, "ecrit", lambda: ecrit)[_n_(554173, "i", lambda: i)+1 + _n_(554174, "numero", lambda: numero)] != '+' and _n_(554175, "ecrit", lambda: ecrit)[_n_(554176, "i", lambda: i)+1 + _n_(554177, "numero", lambda: numero)] != '-':
                        _l_(554193)


                        nb +=1
                        _l_(554178)

                    elif _n_(554179, "ecrit", lambda: ecrit)[_n_(554180, "i", lambda: i)+1+_n_(554181, "numero", lambda: numero)] == '/' or _n_(554182, "ecrit", lambda: ecrit)[_n_(554183, "i", lambda: i)+1+_n_(554184, "numero", lambda: numero)] == '*' or _n_(554185, "ecrit", lambda: ecrit)[_n_(554186, "i", lambda: i)+1+_n_(554187, "numero", lambda: numero)] == '+' or _n_(554188, "ecrit", lambda: ecrit)[_n_(554189, "i", lambda: i)+1+_n_(554190, "numero", lambda: numero)] == '-':
                        _l_(554192)


                        break 
                        _l_(554191) 

                for i in _c_(554197, _n_(554195, "range", lambda: range), _n_(554196, "numero", lambda: numero)):
                    _l_(554228)


                    i = -_n_(554198, "i", lambda: i)
                    _l_(554199)

                    if _n_(554200, "ecrit", lambda: ecrit)[_n_(554201, "i", lambda: i)-1+_n_(554202, "numero", lambda: numero)] != '/' and _n_(554203, "ecrit", lambda: ecrit)[_n_(554204, "i", lambda: i)-1+_n_(554205, "numero", lambda: numero)] != '*' and _n_(554206, "ecrit", lambda: ecrit)[_n_(554207, "i", lambda: i)-1+_n_(554208, "numero", lambda: numero)] != '+' and _n_(554209, "ecrit", lambda: ecrit)[_n_(554210, "i", lambda: i)-1+_n_(554211, "numero", lambda: numero)] != '-':
                        _l_(554227)


                        nbb -=1
                        _l_(554212)

                    elif _n_(554213, "ecrit", lambda: ecrit)[_n_(554214, "i", lambda: i)-1+_n_(554215, "numero", lambda: numero)] == '/' or _n_(554216, "ecrit", lambda: ecrit)[_n_(554217, "i", lambda: i)-1+_n_(554218, "numero", lambda: numero)] == '*' or _n_(554219, "ecrit", lambda: ecrit)[_n_(554220, "i", lambda: i)-1+_n_(554221, "numero", lambda: numero)] == '+' or _n_(554222, "ecrit", lambda: ecrit)[_n_(554223, "i", lambda: i)-1+_n_(554224, "numero", lambda: numero)] == '-':
                        _l_(554226)


                        break 
                        _l_(554225) 

                nombre1 = _c_(554233, _a_(554229, "", "join"), _n_(554230, "ecrit", lambda: ecrit)[_n_(554231, "numero", lambda: numero)+1:_n_(554232, "nb", lambda: nb)+1])
                _l_(554234)
                nombre1 = _c_(554237, _n_(554235, "float", lambda: float), _n_(554236, "nombre1", lambda: nombre1))
                _l_(554238)
                nombre2 = _c_(554243, _a_(554239, "", "join"), _n_(554240, "ecrit", lambda: ecrit)[_n_(554241, "nbb", lambda: nbb):_n_(554242, "numero", lambda: numero)])
                _l_(554244)
                nombre2 = _c_(554247, _n_(554245, "float", lambda: float), _n_(554246, "nombre2", lambda: nombre2))
                _l_(554248)

                if _n_(554249, "ecrit", lambda: ecrit)[_n_(554250, "numero", lambda: numero)] =='*':
                    _l_(554287)

                    resultat = _n_(554251, "nombre1", lambda: nombre1) * _n_(554252, "nombre2", lambda: nombre2)
                    _l_(554253)

                    if _n_(554254, "resultat", lambda: resultat) == _c_(554257, _n_(554255, "int", lambda: int), _n_(554256, "resultat", lambda: resultat)):
                        _l_(554262)

                        resultat = _c_(554260, _n_(554258, "int", lambda: int), _n_(554259, "resultat", lambda: resultat))
                        _l_(554261)

                    resultat = _c_(554267, _n_(554263, "list", lambda: list), _c_(554266, _n_(554264, "str", lambda: str), _n_(554265, "resultat", lambda: resultat)))
                    _l_(554268)


                else:
                    resultat = _n_(554269, "nombre2", lambda: nombre2) / _n_(554270, "nombre1", lambda: nombre1)
                    _l_(554271)

                    if _n_(554272, "resultat", lambda: resultat) == _c_(554275, _n_(554273, "int", lambda: int), _n_(554274, "resultat", lambda: resultat)):
                        _l_(554280)

                        resultat = _c_(554278, _n_(554276, "int", lambda: int), _n_(554277, "resultat", lambda: resultat))
                        _l_(554279)

                    resultat = _c_(554285, _n_(554281, "list", lambda: list), _c_(554284, _n_(554282, "str", lambda: str), _n_(554283, "resultat", lambda: resultat)))
                    _l_(554286)

                del ecrit[nbb:nb+1]
                _l_(554288)
                for i in _c_(554293, _n_(554289, "range", lambda: range), _c_(554292, _n_(554290, "len", lambda: len), _n_(554291, "resultat", lambda: resultat))):
                    _l_(554302)


                    _c_(554300, _a_(554295, _n_(554294, "ecrit", lambda: ecrit), "insert"), _n_(554296, "nbb", lambda: nbb)+_n_(554297, "i", lambda: i),_n_(554298, "resultat", lambda: resultat)[_n_(554299, "i", lambda: i)])
                    _l_(554301)
                break
                _l_(554303)

    for i in _c_(554309, _n_(554307, "range", lambda: range), _n_(554308, "nombre_de_sous_add", lambda: nombre_de_sous_add)):
        _l_(554471)


        for i in _c_(554314, _n_(554310, "range", lambda: range), _c_(554313, _n_(554311, "len", lambda: len), _n_(554312, "ecrit", lambda: ecrit))):
            _l_(554470)

            if _n_(554315, "ecrit", lambda: ecrit)[_n_(554316, "i", lambda: i)] == '+' or _n_(554317, "ecrit", lambda: ecrit)[_n_(554318, "i", lambda: i)] == '-':
                _l_(554469)


                numero = _n_(554319, "i", lambda: i)
                _l_(554320)
                nb = _n_(554321, "i", lambda: i)
                _l_(554322)
                nbb = _n_(554323, "i", lambda: i)
                _l_(554324)

                for i in _c_(554330, _n_(554325, "range", lambda: range), _c_(554328, _n_(554326, "len", lambda: len), _n_(554327, "ecrit", lambda: ecrit))-_n_(554329, "numero", lambda: numero)-1):
                    _l_(554359)



                    if _n_(554331, "ecrit", lambda: ecrit)[_n_(554332, "i", lambda: i)+1 + _n_(554333, "numero", lambda: numero)] != '/' and _n_(554334, "ecrit", lambda: ecrit)[_n_(554335, "i", lambda: i)+1 + _n_(554336, "numero", lambda: numero)] != '*' and _n_(554337, "ecrit", lambda: ecrit)[_n_(554338, "i", lambda: i)+1 + _n_(554339, "numero", lambda: numero)] != '+' and _n_(554340, "ecrit", lambda: ecrit)[_n_(554341, "i", lambda: i)+1 + _n_(554342, "numero", lambda: numero)] != '-':
                        _l_(554358)


                        nb +=1
                        _l_(554343)

                    elif _n_(554344, "ecrit", lambda: ecrit)[_n_(554345, "i", lambda: i)+1+_n_(554346, "numero", lambda: numero)] == '/' or _n_(554347, "ecrit", lambda: ecrit)[_n_(554348, "i", lambda: i)+1+_n_(554349, "numero", lambda: numero)] == '*' or _n_(554350, "ecrit", lambda: ecrit)[_n_(554351, "i", lambda: i)+1+_n_(554352, "numero", lambda: numero)] == '+' or _n_(554353, "ecrit", lambda: ecrit)[_n_(554354, "i", lambda: i)+1+_n_(554355, "numero", lambda: numero)] == '-':
                        _l_(554357)


                        break 
                        _l_(554356) 

                for i in _c_(554362, _n_(554360, "range", lambda: range), _n_(554361, "numero", lambda: numero)):
                    _l_(554393)


                    i = -_n_(554363, "i", lambda: i)
                    _l_(554364)

                    if _n_(554365, "ecrit", lambda: ecrit)[_n_(554366, "i", lambda: i)-1+_n_(554367, "numero", lambda: numero)] != '/' and _n_(554368, "ecrit", lambda: ecrit)[_n_(554369, "i", lambda: i)-1+_n_(554370, "numero", lambda: numero)] != '*' and _n_(554371, "ecrit", lambda: ecrit)[_n_(554372, "i", lambda: i)-1+_n_(554373, "numero", lambda: numero)] != '+' and _n_(554374, "ecrit", lambda: ecrit)[_n_(554375, "i", lambda: i)-1+_n_(554376, "numero", lambda: numero)] != '-':
                        _l_(554392)


                        nbb -=1
                        _l_(554377)

                    elif _n_(554378, "ecrit", lambda: ecrit)[_n_(554379, "i", lambda: i)-1+_n_(554380, "numero", lambda: numero)] == '/' or _n_(554381, "ecrit", lambda: ecrit)[_n_(554382, "i", lambda: i)-1+_n_(554383, "numero", lambda: numero)] == '*' or _n_(554384, "ecrit", lambda: ecrit)[_n_(554385, "i", lambda: i)-1+_n_(554386, "numero", lambda: numero)] == '+' or _n_(554387, "ecrit", lambda: ecrit)[_n_(554388, "i", lambda: i)-1+_n_(554389, "numero", lambda: numero)] == '-':
                        _l_(554391)


                        break 
                        _l_(554390) 

                nombre1 = _c_(554398, _a_(554394, "", "join"), _n_(554395, "ecrit", lambda: ecrit)[_n_(554396, "numero", lambda: numero)+1:_n_(554397, "nb", lambda: nb)+1])
                _l_(554399)
                nombre1 = _c_(554402, _n_(554400, "float", lambda: float), _n_(554401, "nombre1", lambda: nombre1))
                _l_(554403)
                nombre2 = _c_(554408, _a_(554404, "", "join"), _n_(554405, "ecrit", lambda: ecrit)[_n_(554406, "nbb", lambda: nbb):_n_(554407, "numero", lambda: numero)])
                _l_(554409)
                nombre2 = _c_(554412, _n_(554410, "float", lambda: float), _n_(554411, "nombre2", lambda: nombre2))
                _l_(554413)

                if _n_(554414, "ecrit", lambda: ecrit)[_n_(554415, "numero", lambda: numero)] =='+':
                    _l_(554452)

                    resultat = _n_(554416, "nombre1", lambda: nombre1) + _n_(554417, "nombre2", lambda: nombre2)
                    _l_(554418)

                    if _n_(554419, "resultat", lambda: resultat) == _c_(554422, _n_(554420, "int", lambda: int), _n_(554421, "resultat", lambda: resultat)):
                        _l_(554427)

                        resultat = _c_(554425, _n_(554423, "int", lambda: int), _n_(554424, "resultat", lambda: resultat))
                        _l_(554426)

                    resultat = _c_(554432, _n_(554428, "list", lambda: list), _c_(554431, _n_(554429, "str", lambda: str), _n_(554430, "resultat", lambda: resultat)))
                    _l_(554433)


                else:
                    resultat = _n_(554434, "nombre2", lambda: nombre2) - _n_(554435, "nombre1", lambda: nombre1)
                    _l_(554436)

                    if _n_(554437, "resultat", lambda: resultat) == _c_(554440, _n_(554438, "int", lambda: int), _n_(554439, "resultat", lambda: resultat)):
                        _l_(554445)

                        resultat = _c_(554443, _n_(554441, "int", lambda: int), _n_(554442, "resultat", lambda: resultat))
                        _l_(554444)

                    resultat = _c_(554450, _n_(554446, "list", lambda: list), _c_(554449, _n_(554447, "str", lambda: str), _n_(554448, "resultat", lambda: resultat)))
                    _l_(554451)

                del ecrit[nbb:nb+1]
                _l_(554453)

                for i in _c_(554458, _n_(554454, "range", lambda: range), _c_(554457, _n_(554455, "len", lambda: len), _n_(554456, "resultat", lambda: resultat))):
                    _l_(554467)


                    _c_(554465, _a_(554460, _n_(554459, "ecrit", lambda: ecrit), "insert"), _n_(554461, "nbb", lambda: nbb)+_n_(554462, "i", lambda: i),_n_(554463, "resultat", lambda: resultat)[_n_(554464, "i", lambda: i)])
                    _l_(554466)

                break
                _l_(554468)
    _c_(554475, _n_(554472, "Ecrire_Resulat", lambda: Ecrire_Resulat), _n_(554473, "ecrit", lambda: ecrit),_n_(554474, "self", lambda: self))
    _l_(554476)


class Theme():
    _l_(555178)


    def move_window(self,event):
        _l_(554499)

        # global x, y
        _c_(554483, _n_(554478, "print", lambda: print), _a_(554480, _n_(554479, "self", lambda: self), "x"), _a_(554482, _n_(554481, "self", lambda: self), "y"))
        _l_(554484)
        _c_(554497, _a_(554486, _n_(554485, "win", lambda: win), "geometry"), _c_(554496, _a_(554487, '+{0}+{1}', "format"), _a_(554489, _n_(554488, "event", lambda: event), "x_win") - _a_(554491, _n_(554490, "self", lambda: self), "x"), _a_(554493, _n_(554492, "event", lambda: event), "y_win") - _a_(554495, _n_(554494, "self", lambda: self), "y")))
        _l_(554498)

    def set_xy(self,event):
        _l_(554519)


        _n_(554500, "self", lambda: self).x=_a_(554502, _n_(554501, "event", lambda: event), "x_win") - _c_(554505, _a_(554504, _n_(554503, "win", lambda: win), "winfo_x"))
        _l_(554506)
        _n_(554507, "self", lambda: self).y=_a_(554509, _n_(554508, "event", lambda: event), "y_win") - _c_(554512, _a_(554511, _n_(554510, "win", lambda: win), "winfo_y"))
        _l_(554513)
        aux = _a_(554515, _n_(554514, "self", lambda: self), "x"),_a_(554517, _n_(554516, "self", lambda: self), "y")
        _l_(554518)
        # print(x,y)
        return aux

    def boutontheme(self,colora, colorb, colorc, colord, colore, colorf):
        _l_(554543)

        _c_(554528, _a_(554521, _n_(554520, "self", lambda: self), "openmenu"), _n_(554522, "colora", lambda: colora), _n_(554523, "colorb", lambda: colorb), _n_(554524, "colorc", lambda: colorc), _n_(554525, "colord", lambda: colord), _n_(554526, "colore", lambda: colore), _n_(554527, "colorf", lambda: colorf))
        _l_(554529)
        if _a_(554531, _n_(554530, "self", lambda: self), "t") == 0:
            _l_(554542)

            Light = _c_(554533, _n_(554532, "Theme", lambda: Theme), '#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#915ec4")
            _l_(554534)
            _n_(554535, "self", lambda: self).t = 1
            _l_(554536)
        else:
            Dark = _c_(554538, _n_(554537, "Theme", lambda: Theme), '#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F")
            _l_(554539)
            _n_(554540, "self", lambda: self).t = 0
            _l_(554541)



    def openmenu(self,colora, colorb, colorc, colord, colore, colorf):
        _l_(554675)

        if _a_(554545, _n_(554544, "self", lambda: self), "ouvert") == False:
            _l_(554652)

            _c_(554550, _a_(554548, _a_(554547, _n_(554546, "self", lambda: self), "b_theme"), "config"), bg = _n_(554549, "colore", lambda: colore))
            _l_(554551)
            if _a_(554553, _n_(554552, "self", lambda: self), "t") == 0:
                _l_(554638)

                _n_(554554, "self", lambda: self).b_theme_dark = _c_(554573, _a_(554556, _n_(554555, "tk", lambda: tk), "Button"), _n_(554557, "win", lambda: win),state=_n_(554558, "DISABLED", lambda: DISABLED), text = 'Dark theme',font = _n_(554559, "font3", lambda: font3),borderwidth=0, highlightthickness=0,compound="c",image = _n_(554560, "pixel", lambda: pixel),height = 20,width = 70,activebackground =_n_(554561, "colore", lambda: colore),bg =_n_(554562, "colora", lambda: colora),fg = _n_(554563, "colord", lambda: colord),command = lambda: _c_(554572, _a_(554565, _n_(554564, "self", lambda: self), "boutontheme"), _n_(554566, "colora", lambda: colora), _n_(554567, "colorb", lambda: colorb), _n_(554568, "colorc", lambda: colorc), _n_(554569, "colord", lambda: colord), _n_(554570, "colore", lambda: colore), _n_(554571, "colorf", lambda: colorf)))
                _l_(554574)
                _n_(554575, "self", lambda: self).b_theme_light = _c_(554594, _a_(554577, _n_(554576, "tk", lambda: tk), "Button"), _n_(554578, "win", lambda: win),state=_n_(554579, "NORMAL", lambda: NORMAL), text = 'Light theme',font = _n_(554580, "font3", lambda: font3),borderwidth=0, highlightthickness=0,compound="c",image = _n_(554581, "pixel", lambda: pixel),height = 20,width = 70,activebackground =_n_(554582, "colore", lambda: colore),bg =_n_(554583, "colora", lambda: colora),fg = _n_(554584, "colord", lambda: colord),command = lambda: _c_(554593, _a_(554586, _n_(554585, "self", lambda: self), "boutontheme"), _n_(554587, "colora", lambda: colora), _n_(554588, "colorb", lambda: colorb), _n_(554589, "colorc", lambda: colorc), _n_(554590, "colord", lambda: colord), _n_(554591, "colore", lambda: colore), _n_(554592, "colorf", lambda: colorf)))
                _l_(554595)
            else:
                _n_(554596, "self", lambda: self).b_theme_dark = _c_(554615, _a_(554598, _n_(554597, "tk", lambda: tk), "Button"), _n_(554599, "win", lambda: win),state=_n_(554600, "NORMAL", lambda: NORMAL), text = 'Dark theme',font = _n_(554601, "font3", lambda: font3),borderwidth=0, highlightthickness=0,compound="c",image = _n_(554602, "pixel", lambda: pixel),height = 20,width = 70,activebackground =_n_(554603, "colore", lambda: colore),bg =_n_(554604, "colora", lambda: colora),fg = _n_(554605, "colord", lambda: colord),command = lambda: _c_(554614, _a_(554607, _n_(554606, "self", lambda: self), "boutontheme"), _n_(554608, "colora", lambda: colora), _n_(554609, "colorb", lambda: colorb), _n_(554610, "colorc", lambda: colorc), _n_(554611, "colord", lambda: colord), _n_(554612, "colore", lambda: colore), _n_(554613, "colorf", lambda: colorf)))
                _l_(554616)
                _n_(554617, "self", lambda: self).b_theme_light = _c_(554636, _a_(554619, _n_(554618, "tk", lambda: tk), "Button"), _n_(554620, "win", lambda: win),state=_n_(554621, "DISABLED", lambda: DISABLED), text = 'Light theme',font = _n_(554622, "font3", lambda: font3),borderwidth=0, highlightthickness=0,compound="c",image = _n_(554623, "pixel", lambda: pixel),height = 20,width = 70,activebackground =_n_(554624, "colore", lambda: colore),bg =_n_(554625, "colora", lambda: colora),fg = _n_(554626, "colord", lambda: colord),command = lambda: _c_(554635, _a_(554628, _n_(554627, "self", lambda: self), "boutontheme"), _n_(554629, "colora", lambda: colora), _n_(554630, "colorb", lambda: colorb), _n_(554631, "colorc", lambda: colorc), _n_(554632, "colord", lambda: colord), _n_(554633, "colore", lambda: colore), _n_(554634, "colorf", lambda: colorf)))
                _l_(554637)
            
            _c_(554642, _a_(554641, _a_(554640, _n_(554639, "self", lambda: self), "b_theme_dark"), "place"), anchor = 'nw', x = 5, y = 25)
            _l_(554643)
            _c_(554647, _a_(554646, _a_(554645, _n_(554644, "self", lambda: self), "b_theme_light"), "place"), anchor = 'nw', x = 5, y = 45) 
            _l_(554648) 
            _n_(554649, "self", lambda: self).ouvert = True
            _l_(554650)
            aux = ""
            _l_(554651)
            return aux

        if _a_(554654, _n_(554653, "self", lambda: self), "ouvert") == True:
            _l_(554674)

            _c_(554659, _a_(554657, _a_(554656, _n_(554655, "self", lambda: self), "b_theme"), "config"), bg = _n_(554658, "colorb", lambda: colorb))
            _l_(554660)
            _c_(554664, _a_(554663, _a_(554662, _n_(554661, "self", lambda: self), "b_theme_dark"), "destroy"))
            _l_(554665)
            _c_(554669, _a_(554668, _a_(554667, _n_(554666, "self", lambda: self), "b_theme_light"), "destroy"))
            _l_(554670)
            _n_(554671, "self", lambda: self).ouvert = False 
            _l_(554672) 
            aux = ""
            _l_(554673)
            return aux


    # def closemenu(self):
    #   self.b_theme_dark.forget()
    #   self.b_theme_light.forget()

    #   ouvert = False 


    def __init__(self,colora, colorb, colorc, colord, colore, colorf):
        _l_(555177)


        
        if _n_(554676, "colora", lambda: colora) == '#18181F':
            _l_(554681)

            _n_(554677, "self", lambda: self).t = 0
            _l_(554678)
        else:
            _n_(554679, "self", lambda: self).t = 1
            _l_(554680)

        _n_(554682, "self", lambda: self).ouvert = False
        _l_(554683)
        _n_(554684, "self", lambda: self).x = 0
        _l_(554685)
        _n_(554686, "self", lambda: self).y=0
        _l_(554687)

        #creation menu

        _n_(554688, "self", lambda: self).canvas_menu = _c_(554692, _n_(554689, "Canvas", lambda: Canvas), _n_(554690, "win", lambda: win), width =500, height =25, bg = _n_(554691, "colora", lambda: colora), borderwidth=0, highlightthickness=0)
        _l_(554693)
        _n_(554694, "self", lambda: self).exit = _c_(554697, _n_(554695, "Canvas", lambda: Canvas), bg = _n_(554696, "colora", lambda: colora),borderwidth=0, highlightthickness=0)
        _l_(554698)
        _c_(554703, _a_(554701, _a_(554700, _n_(554699, "self", lambda: self), "exit"), "create_oval"), 0,0,20,20, fill= _n_(554702, "colore", lambda: colore),width = 0)
        _l_(554704)
        _c_(554710, _a_(554707, _a_(554706, _n_(554705, "self", lambda: self), "exit"), "create_text"), 10, 10, text="x", fill = _n_(554708, "colord", lambda: colord), font= _n_(554709, "font3", lambda: font3))
        _l_(554711)
        _c_(554718, _a_(554714, _a_(554713, _n_(554712, "self", lambda: self), "exit"), "bind"), "<Button-1>", lambda e: _c_(554717, _a_(554716, _n_(554715, "win", lambda: win), "destroy")))
        _l_(554719)

        #affichage menu

        _c_(554723, _a_(554722, _a_(554721, _n_(554720, "self", lambda: self), "exit"), "place"), anchor = 'nw', x = 475, y = 2)
        _l_(554724)
        _c_(554728, _a_(554727, _a_(554726, _n_(554725, "self", lambda: self), "canvas_menu"), "grid"), row = 0,column = 0, columnspan = 5)
        _l_(554729)

        #creation des canvas

        _n_(554730, "self", lambda: self).canvas_screen = _c_(554734, _n_(554731, "Canvas", lambda: Canvas), _n_(554732, "win", lambda: win), width =500, height =100, bg =_n_(554733, "colorb", lambda: colorb),borderwidth=0, highlightthickness=0)
        _l_(554735)
        _n_(554736, "self", lambda: self).canvas_keyb_num = _c_(554740, _n_(554737, "Canvas", lambda: Canvas), _n_(554738, "win", lambda: win), width =300, height =400, bg =_n_(554739, "colorb", lambda: colorb),borderwidth=0, highlightthickness=0)
        _l_(554741)
        _n_(554742, "self", lambda: self).canvas_keyb_op = _c_(554746, _n_(554743, "Canvas", lambda: Canvas), _n_(554744, "win", lambda: win), width =200, height =400, bg =_n_(554745, "colorb", lambda: colorb),borderwidth=0, highlightthickness=0)
        _l_(554747)

        #affchage des canvas

        _c_(554751, _a_(554750, _a_(554749, _n_(554748, "self", lambda: self), "canvas_screen"), "grid"), row = 1,column = 0, columnspan = 5)
        _l_(554752)
        _c_(554756, _a_(554755, _a_(554754, _n_(554753, "self", lambda: self), "canvas_keyb_num"), "grid"), row = 2,column = 0, columnspan = 3, rowspan = 4)
        _l_(554757)
        _c_(554761, _a_(554760, _a_(554759, _n_(554758, "self", lambda: self), "canvas_keyb_op"), "grid"), row = 2,column = 3, columnspan = 2, rowspan = 4)
        _l_(554762)

        # creation des boutons

        _n_(554763, "self", lambda: self).b1 = _c_(554776, _n_(554764, "Button", lambda: Button), _n_(554765, "win", lambda: win), text ='1',borderwidth=0, highlightthickness=0, bg = _n_(554766, "colora", lambda: colora),activebackground =_n_(554767, "colorc", lambda: colorc),foreground=_n_(554768, "colord", lambda: colord),compound="c",image = _n_(554769, "pixel", lambda: pixel),height = _n_(554770, "a", lambda: a),width = _n_(554771, "b", lambda: b) ,font = _n_(554772, "font1", lambda: font1),command=lambda: _c_(554775, _n_(554773, "Ecrire", lambda: Ecrire), '1',_n_(554774, "self", lambda: self)))
        _l_(554777)
        _n_(554778, "self", lambda: self).b2 = _c_(554791, _n_(554779, "Button", lambda: Button), _n_(554780, "win", lambda: win), text ='2',borderwidth=0, highlightthickness=0, bg = _n_(554781, "colora", lambda: colora),activebackground =_n_(554782, "colorc", lambda: colorc),foreground=_n_(554783, "colord", lambda: colord),compound="c",image = _n_(554784, "pixel", lambda: pixel),height = _n_(554785, "a", lambda: a),width = _n_(554786, "b", lambda: b) ,font = _n_(554787, "font1", lambda: font1),command=lambda: _c_(554790, _n_(554788, "Ecrire", lambda: Ecrire), '2',_n_(554789, "self", lambda: self)))
        _l_(554792)
        _n_(554793, "self", lambda: self).b3 = _c_(554806, _n_(554794, "Button", lambda: Button), _n_(554795, "win", lambda: win), text ='3',borderwidth=0, highlightthickness=0, bg = _n_(554796, "colora", lambda: colora),activebackground =_n_(554797, "colorc", lambda: colorc),foreground=_n_(554798, "colord", lambda: colord),compound="c",image = _n_(554799, "pixel", lambda: pixel),height = _n_(554800, "a", lambda: a),width = _n_(554801, "b", lambda: b) ,font = _n_(554802, "font1", lambda: font1),command=lambda: _c_(554805, _n_(554803, "Ecrire", lambda: Ecrire), '3',_n_(554804, "self", lambda: self)))
        _l_(554807)
        _n_(554808, "self", lambda: self).b4 = _c_(554821, _n_(554809, "Button", lambda: Button), _n_(554810, "win", lambda: win), text ='4',borderwidth=0, highlightthickness=0, bg = _n_(554811, "colora", lambda: colora),activebackground =_n_(554812, "colorc", lambda: colorc),foreground=_n_(554813, "colord", lambda: colord),compound="c",image = _n_(554814, "pixel", lambda: pixel),height = _n_(554815, "a", lambda: a),width = _n_(554816, "b", lambda: b) ,font = _n_(554817, "font1", lambda: font1),command=lambda: _c_(554820, _n_(554818, "Ecrire", lambda: Ecrire), '4',_n_(554819, "self", lambda: self)))
        _l_(554822)
        _n_(554823, "self", lambda: self).b5 = _c_(554836, _n_(554824, "Button", lambda: Button), _n_(554825, "win", lambda: win), text ='5',borderwidth=0, highlightthickness=0, bg = _n_(554826, "colora", lambda: colora),activebackground =_n_(554827, "colorc", lambda: colorc),foreground=_n_(554828, "colord", lambda: colord),compound="c",image = _n_(554829, "pixel", lambda: pixel),height = _n_(554830, "a", lambda: a),width = _n_(554831, "b", lambda: b) ,font = _n_(554832, "font1", lambda: font1),command=lambda: _c_(554835, _n_(554833, "Ecrire", lambda: Ecrire), '5',_n_(554834, "self", lambda: self)))
        _l_(554837)
        _n_(554838, "self", lambda: self).b6 = _c_(554851, _n_(554839, "Button", lambda: Button), _n_(554840, "win", lambda: win), text ='6',borderwidth=0, highlightthickness=0, bg = _n_(554841, "colora", lambda: colora),activebackground =_n_(554842, "colorc", lambda: colorc),foreground=_n_(554843, "colord", lambda: colord),compound="c",image = _n_(554844, "pixel", lambda: pixel),height = _n_(554845, "a", lambda: a),width = _n_(554846, "b", lambda: b) ,font = _n_(554847, "font1", lambda: font1),command=lambda: _c_(554850, _n_(554848, "Ecrire", lambda: Ecrire), '6',_n_(554849, "self", lambda: self)))
        _l_(554852)
        _n_(554853, "self", lambda: self).b7 = _c_(554866, _n_(554854, "Button", lambda: Button), _n_(554855, "win", lambda: win), text ='7',borderwidth=0, highlightthickness=0, bg = _n_(554856, "colora", lambda: colora),activebackground =_n_(554857, "colorc", lambda: colorc),foreground=_n_(554858, "colord", lambda: colord),compound="c",image = _n_(554859, "pixel", lambda: pixel),height = _n_(554860, "a", lambda: a),width = _n_(554861, "b", lambda: b) ,font = _n_(554862, "font1", lambda: font1),command=lambda: _c_(554865, _n_(554863, "Ecrire", lambda: Ecrire), '7',_n_(554864, "self", lambda: self)))
        _l_(554867)
        _n_(554868, "self", lambda: self).b8 = _c_(554881, _n_(554869, "Button", lambda: Button), _n_(554870, "win", lambda: win), text ='8',borderwidth=0, highlightthickness=0, bg = _n_(554871, "colora", lambda: colora),activebackground =_n_(554872, "colorc", lambda: colorc),foreground=_n_(554873, "colord", lambda: colord),compound="c",image = _n_(554874, "pixel", lambda: pixel),height = _n_(554875, "a", lambda: a),width = _n_(554876, "b", lambda: b) ,font = _n_(554877, "font1", lambda: font1),command=lambda: _c_(554880, _n_(554878, "Ecrire", lambda: Ecrire), '8',_n_(554879, "self", lambda: self)))
        _l_(554882)
        _n_(554883, "self", lambda: self).b9 = _c_(554896, _n_(554884, "Button", lambda: Button), _n_(554885, "win", lambda: win), text ='9',borderwidth=0, highlightthickness=0, bg = _n_(554886, "colora", lambda: colora),activebackground =_n_(554887, "colorc", lambda: colorc),foreground=_n_(554888, "colord", lambda: colord),compound="c",image = _n_(554889, "pixel", lambda: pixel),height = _n_(554890, "a", lambda: a),width = _n_(554891, "b", lambda: b) ,font = _n_(554892, "font1", lambda: font1),command=lambda: _c_(554895, _n_(554893, "Ecrire", lambda: Ecrire), '9',_n_(554894, "self", lambda: self)))
        _l_(554897)
        _n_(554898, "self", lambda: self).b_point = _c_(554911, _n_(554899, "Button", lambda: Button), _n_(554900, "win", lambda: win), text ='.',borderwidth=0, highlightthickness=0, bg = _n_(554901, "colora", lambda: colora),activebackground =_n_(554902, "colorc", lambda: colorc),foreground=_n_(554903, "colord", lambda: colord),compound="c",image = _n_(554904, "pixel", lambda: pixel),height = _n_(554905, "a", lambda: a),width = _n_(554906, "b", lambda: b) ,font = _n_(554907, "font1", lambda: font1),command=lambda: _c_(554910, _n_(554908, "Ecrire", lambda: Ecrire), '.',_n_(554909, "self", lambda: self)))
        _l_(554912)
        _n_(554913, "self", lambda: self).b0 = _c_(554926, _n_(554914, "Button", lambda: Button), _n_(554915, "win", lambda: win), text ='0',borderwidth=0, highlightthickness=0, bg = _n_(554916, "colora", lambda: colora),activebackground =_n_(554917, "colorc", lambda: colorc),foreground=_n_(554918, "colord", lambda: colord),compound="c",image = _n_(554919, "pixel", lambda: pixel),height = _n_(554920, "a", lambda: a),width = _n_(554921, "b", lambda: b) ,font = _n_(554922, "font1", lambda: font1),command=lambda: _c_(554925, _n_(554923, "Ecrire", lambda: Ecrire), '0',_n_(554924, "self", lambda: self)))
        _l_(554927)
        
        _n_(554928, "self", lambda: self).b_plus = _c_(554941, _n_(554929, "Button", lambda: Button), _n_(554930, "win", lambda: win), text ='+',borderwidth=0, highlightthickness=0, bg = _n_(554931, "colora", lambda: colora),activebackground =_n_(554932, "colorc", lambda: colorc),foreground=_n_(554933, "colord", lambda: colord),compound="c",image = _n_(554934, "pixel", lambda: pixel),height = _n_(554935, "a", lambda: a),width = _n_(554936, "b", lambda: b) ,font = _n_(554937, "font1", lambda: font1),command=lambda: _c_(554940, _n_(554938, "Ecrire", lambda: Ecrire), '+',_n_(554939, "self", lambda: self)))
        _l_(554942)
        _n_(554943, "self", lambda: self).b_moins = _c_(554956, _n_(554944, "Button", lambda: Button), _n_(554945, "win", lambda: win), text ='-',borderwidth=0, highlightthickness=0, bg = _n_(554946, "colora", lambda: colora),activebackground =_n_(554947, "colorc", lambda: colorc),foreground=_n_(554948, "colord", lambda: colord),compound="c",image = _n_(554949, "pixel", lambda: pixel),height = _n_(554950, "a", lambda: a),width = _n_(554951, "b", lambda: b) ,font = _n_(554952, "font1", lambda: font1),command=lambda: _c_(554955, _n_(554953, "Ecrire", lambda: Ecrire), '-',_n_(554954, "self", lambda: self)))
        _l_(554957)
        _n_(554958, "self", lambda: self).b_fois = _c_(554971, _n_(554959, "Button", lambda: Button), _n_(554960, "win", lambda: win), text ='*',borderwidth=0, highlightthickness=0, bg = _n_(554961, "colora", lambda: colora),activebackground =_n_(554962, "colorc", lambda: colorc),foreground=_n_(554963, "colord", lambda: colord),compound="c",image = _n_(554964, "pixel", lambda: pixel),height = _n_(554965, "a", lambda: a),width = _n_(554966, "b", lambda: b) ,font = _n_(554967, "font1", lambda: font1),command=lambda: _c_(554970, _n_(554968, "Ecrire", lambda: Ecrire), '*',_n_(554969, "self", lambda: self)))
        _l_(554972)
        _n_(554973, "self", lambda: self).b_diviser = _c_(554986, _n_(554974, "Button", lambda: Button), _n_(554975, "win", lambda: win), text ='/',borderwidth=0, highlightthickness=0, bg = _n_(554976, "colora", lambda: colora),activebackground =_n_(554977, "colorc", lambda: colorc),foreground=_n_(554978, "colord", lambda: colord),compound="c",image = _n_(554979, "pixel", lambda: pixel),height = _n_(554980, "a", lambda: a),width = _n_(554981, "b", lambda: b) ,font = _n_(554982, "font1", lambda: font1),command=lambda: _c_(554985, _n_(554983, "Ecrire", lambda: Ecrire), '/',_n_(554984, "self", lambda: self)))
        _l_(554987)
        _n_(554988, "self", lambda: self).b_del = _c_(555001, _n_(554989, "Button", lambda: Button), _n_(554990, "win", lambda: win), text ='DEL',borderwidth=0, highlightthickness=0, bg = _n_(554991, "colora", lambda: colora),activebackground =_n_(554992, "colorc", lambda: colorc),foreground=_n_(554993, "colord", lambda: colord),compound="c",image = _n_(554994, "pixel", lambda: pixel),height = _n_(554995, "a", lambda: a),width = _n_(554996, "b", lambda: b) ,font = _n_(554997, "font1", lambda: font1),command=lambda: _c_(555000, _n_(554998, "Del", lambda: Del), _n_(554999, "self", lambda: self)))
        _l_(555002)
        _n_(555003, "self", lambda: self).b_del_all = _c_(555016, _n_(555004, "Button", lambda: Button), _n_(555005, "win", lambda: win), text ='CE',borderwidth=0, highlightthickness=0, bg = _n_(555006, "colora", lambda: colora),activebackground =_n_(555007, "colorc", lambda: colorc),foreground=_n_(555008, "colord", lambda: colord),compound="c",image = _n_(555009, "pixel", lambda: pixel),height = _n_(555010, "a", lambda: a),width = _n_(555011, "b", lambda: b) ,font = _n_(555012, "font1", lambda: font1),command=lambda: _c_(555015, _n_(555013, "Del_all", lambda: Del_all), _n_(555014, "self", lambda: self)))
        _l_(555017)
        _n_(555018, "self", lambda: self).b_egale = _c_(555030, _n_(555019, "Button", lambda: Button), _n_(555020, "win", lambda: win), text ='=',borderwidth=0, highlightthickness=0, bg = _n_(555021, "colore", lambda: colore),activebackground =_n_(555022, "colorf", lambda: colorf),foreground=_n_(555023, "colord", lambda: colord),compound="c",image = _n_(555024, "pixel", lambda: pixel),height = _n_(555025, "a", lambda: a),width = 295 ,font = _n_(555026, "font1", lambda: font1),command= lambda: _c_(555029, _n_(555027, "Calcul", lambda: Calcul), _n_(555028, "self", lambda: self)))
        _l_(555031)

        #affichage des nombres

        #colone 1

        _c_(555035, _a_(555034, _a_(555033, _n_(555032, "self", lambda: self), "b7"), "grid"), column = 0, row = 2)
        _l_(555036)
        _c_(555040, _a_(555039, _a_(555038, _n_(555037, "self", lambda: self), "b4"), "grid"), column = 0, row = 3)
        _l_(555041)
        _c_(555045, _a_(555044, _a_(555043, _n_(555042, "self", lambda: self), "b1"), "grid"), column = 0, row = 4)
        _l_(555046)
        _c_(555050, _a_(555049, _a_(555048, _n_(555047, "self", lambda: self), "b_point"), "grid"), column = 0, row = 5)
        _l_(555051)

        #colone 2

        _c_(555055, _a_(555054, _a_(555053, _n_(555052, "self", lambda: self), "b8"), "grid"), column = 1, row = 2)
        _l_(555056)
        _c_(555060, _a_(555059, _a_(555058, _n_(555057, "self", lambda: self), "b5"), "grid"), column = 1, row = 3)
        _l_(555061)
        _c_(555065, _a_(555064, _a_(555063, _n_(555062, "self", lambda: self), "b2"), "grid"), column = 1, row = 4)
        _l_(555066)
        _c_(555070, _a_(555069, _a_(555068, _n_(555067, "self", lambda: self), "b0"), "grid"), column = 1, row = 5)
        _l_(555071)

        #colone 3

        _c_(555075, _a_(555074, _a_(555073, _n_(555072, "self", lambda: self), "b9"), "grid"), column = 2, row = 2)
        _l_(555076)
        _c_(555080, _a_(555079, _a_(555078, _n_(555077, "self", lambda: self), "b6"), "grid"), column = 2, row = 3)
        _l_(555081)
        _c_(555085, _a_(555084, _a_(555083, _n_(555082, "self", lambda: self), "b3"), "grid"), column = 2, row = 4)
        _l_(555086)

        #operateurs

        _c_(555090, _a_(555089, _a_(555088, _n_(555087, "self", lambda: self), "b_plus"), "grid"), column = 3, row = 2)
        _l_(555091)
        _c_(555095, _a_(555094, _a_(555093, _n_(555092, "self", lambda: self), "b_moins"), "grid"), column = 4, row = 2)
        _l_(555096)
        _c_(555100, _a_(555099, _a_(555098, _n_(555097, "self", lambda: self), "b_fois"), "grid"), column = 3, row = 3)
        _l_(555101)
        _c_(555105, _a_(555104, _a_(555103, _n_(555102, "self", lambda: self), "b_diviser"), "grid"), column = 4, row = 3)
        _l_(555106)
        _c_(555110, _a_(555109, _a_(555108, _n_(555107, "self", lambda: self), "b_del"), "grid"), column = 3, row = 4)
        _l_(555111)
        _c_(555115, _a_(555114, _a_(555113, _n_(555112, "self", lambda: self), "b_del_all"), "grid"), column = 4, row = 4)
        _l_(555116)
        _c_(555120, _a_(555119, _a_(555118, _n_(555117, "self", lambda: self), "b_egale"), "grid"), column = 2, row = 5,columnspan = 3)
        _l_(555121)

        #ecriture

        _n_(555122, "self", lambda: self).label1 = _c_(555131, _a_(555124, _n_(555123, "tk", lambda: tk), "Label"), _n_(555125, "win", lambda: win), text = '', justify = _a_(555127, _n_(555126, "tk", lambda: tk), "RIGHT"),font = _n_(555128, "font2", lambda: font2),bg =_n_(555129, "colorb", lambda: colorb),fg = _n_(555130, "colord", lambda: colord))
        _l_(555132)
        _c_(555136, _a_(555135, _a_(555134, _n_(555133, "self", lambda: self), "label1"), "place"), anchor = 'e', x = 450, y = 75)
        _l_(555137)
        _n_(555138, "self", lambda: self).b_theme = _c_(555156, _a_(555140, _n_(555139, "tk", lambda: tk), "Button"), _n_(555141, "win", lambda: win), text = 'Themes',font = _n_(555142, "font3", lambda: font3),bg =_n_(555143, "colorb", lambda: colorb),fg = _n_(555144, "colord", lambda: colord),borderwidth=0, highlightthickness=0,compound="c",image = _n_(555145, "pixel", lambda: pixel),height = 20,width = 50,activebackground =_n_(555146, "colore", lambda: colore),command= lambda: _c_(555155, _a_(555148, _n_(555147, "self", lambda: self), "openmenu"), _n_(555149, "colora", lambda: colora), _n_(555150, "colorb", lambda: colorb), _n_(555151, "colorc", lambda: colorc), _n_(555152, "colord", lambda: colord), _n_(555153, "colore", lambda: colore), _n_(555154, "colorf", lambda: colorf)))
        _l_(555157)
        _c_(555161, _a_(555160, _a_(555159, _n_(555158, "self", lambda: self), "b_theme"), "place"), anchor = 'nw', x = 5, y = 2)
        _l_(555162)

        _c_(555168, _a_(555165, _a_(555164, _n_(555163, "self", lambda: self), "canvas_menu"), "bind"), '<1>', _a_(555167, _n_(555166, "self", lambda: self), "set_xy"))
        _l_(555169)

        # bind title bar motion to the move window function

        _c_(555175, _a_(555172, _a_(555171, _n_(555170, "self", lambda: self), "canvas_menu"), "bind"), '<B1-Motion>', _a_(555174, _n_(555173, "self", lambda: self), "move_window"))
        _l_(555176)


if _n_(555179, "theme", lambda: theme) == 0:
    _l_(555186)

    Dark = _c_(555181, _n_(555180, "Theme", lambda: Theme), '#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F")
    _l_(555182)
else:
    Light = _c_(555184, _n_(555183, "Theme", lambda: Theme), '#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#915ec4")
    _l_(555185)

_c_(555189, _a_(555188, _n_(555187, "win", lambda: win), "title"), 'calculator')
_l_(555190)






#pour un future menu 

# bouton.config(state=DISABLED)
# bouton.config(state=NORMAL)

_c_(555193, _a_(555192, _n_(555191, "win", lambda: win), "resizable"), height=False,width=False)
_l_(555194)
_c_(555197, _a_(555196, _n_(555195, "win", lambda: win), "mainloop"))
_l_(555198)