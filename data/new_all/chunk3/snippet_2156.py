# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849825/typeerror-kollision-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class score():
    _l_(576096)

    def __init__(self, pbaum):
        _l_(576079)

        schrift = _c_(576074, _a_(576073, _a_(576072, _n_(576071, "pygame", lambda: pygame), "font"), "SysFont"), "OCR A" , 30 , True ) 
        _l_(576075) 
        _n_(576076, "self", lambda: self).Baum = _n_(576077, "pbaum", lambda: pbaum)
        _l_(576078)

    def anzeigen(self):
        _l_(576095)

        score = 0
        _l_(576080)

        _n_(576081, "self", lambda: self).text = _c_(576087, _a_(576083, _n_(576082, "schrift", lambda: schrift), "render"), "Score: " + _c_(576086, _n_(576084, "str", lambda: str), _n_(576085, "score", lambda: score))  , 0 , (0,0,0))
        _l_(576088)
        _c_(576093, _a_(576090, _n_(576089, "screen", lambda: screen), "blit"), _a_(576092, _n_(576091, "self", lambda: self), "text") , (550 , 10))  
        _l_(576094)  

#Objekt der Klasse Schlitten erzeugen
spieler1 = _c_(576099, _n_(576097, "Schlitten", lambda: Schlitten), 350,400,_n_(576098, "screen", lambda: screen))
_l_(576100)
Score = _c_(576103, _n_(576101, "score", lambda: score), _n_(576102, "Baum", lambda: Baum))
_l_(576104)
#Objekt der Klasse Baum erzeugen
Baum1 = _c_(576108, _n_(576105, "Baum", lambda: Baum), 500,0 ,_n_(576106, "screen", lambda: screen) , _n_(576107, "Schlitten", lambda: Schlitten))
_l_(576109)
Baum2 = _c_(576113, _n_(576110, "Baum", lambda: Baum), 300,-525 , _n_(576111, "screen", lambda: screen) , _n_(576112, "Schlitten", lambda: Schlitten))
_l_(576114)
Baum3 = _c_(576118, _n_(576115, "Baum", lambda: Baum), 100,-1050 , _n_(576116, "screen", lambda: screen), _n_(576117, "Schlitten", lambda: Schlitten))
_l_(576119)



schrift = _c_(576123, _a_(576122, _a_(576121, _n_(576120, "pygame", lambda: pygame), "font"), "SysFont"), "comicsans" , 30 , True ) 
_l_(576124) 
# -------- Haupt-Schleife -----------
while not _n_(576125, "done", lambda: done):
    _l_(576216)

    # Ändert den Wert von done auf True, falls Spiel-Fenster geschlossen wird
    for event in _c_(576129, _a_(576128, _a_(576127, _n_(576126, "pygame", lambda: pygame), "event"), "get")):
        _l_(576136)

        if _a_(576131, _n_(576130, "event", lambda: event), "type") == _a_(576133, _n_(576132, "pygame", lambda: pygame), "QUIT"):
            _l_(576135)

            done = True
            _l_(576134)



    # --- hier Zeichenbefehle ergänzen---

    # Screen mit weiß fuellen
    _c_(576139, _a_(576138, _n_(576137, "screen", lambda: screen), "fill"), (255,255,255))
    _l_(576140)

    _c_(576145, _a_(576144, _a_(576143, _a_(576142, _n_(576141, "pygame", lambda: pygame), "mixer"), "music"), "set_volume"), 0.1)
    _l_(576146)



    _c_(576149, _a_(576148, _n_(576147, "Score", lambda: Score), "anzeigen"))
    _l_(576150)


    # Schlitten zeichnen
    _c_(576153, _a_(576152, _n_(576151, "spieler1", lambda: spieler1), "zeichne_dich"))
    _l_(576154)
    _c_(576157, _a_(576156, _n_(576155, "spieler1", lambda: spieler1), "movemint"))
    _l_(576158)




    # Baeume zeichnen
    _c_(576161, _a_(576160, _n_(576159, "Baum1", lambda: Baum1), "zeichne"))
    _l_(576162)
    _c_(576165, _a_(576164, _n_(576163, "Baum1", lambda: Baum1), "bewegung"))
    _l_(576166)
    _c_(576169, _a_(576168, _n_(576167, "Baum1", lambda: Baum1), "spawn"))
    _l_(576170)
    _c_(576173, _a_(576172, _n_(576171, "Baum1", lambda: Baum1), "collision"))
    _l_(576174)




    _c_(576177, _a_(576176, _n_(576175, "Baum2", lambda: Baum2), "zeichne"))
    _l_(576178)
    _c_(576181, _a_(576180, _n_(576179, "Baum2", lambda: Baum2), "bewegung"))
    _l_(576182)
    _c_(576185, _a_(576184, _n_(576183, "Baum2", lambda: Baum2), "spawn"))
    _l_(576186)
    _c_(576189, _a_(576188, _n_(576187, "Baum2", lambda: Baum2), "collision"))
    _l_(576190)




    _c_(576193, _a_(576192, _n_(576191, "Baum3", lambda: Baum3), "zeichne"))
    _l_(576194)
    _c_(576197, _a_(576196, _n_(576195, "Baum3", lambda: Baum3), "bewegung"))
    _l_(576198)
    _c_(576201, _a_(576200, _n_(576199, "Baum3", lambda: Baum3), "spawn"))
    _l_(576202)
    _c_(576205, _a_(576204, _n_(576203, "Baum3", lambda: Baum3), "collision"))
    _l_(576206)









    # Maximale fps angeben
    _c_(576209, _a_(576208, _n_(576207, "clock", lambda: clock), "tick"), 60)
    _l_(576210)

    # Bildschirm updaten um gezeichnete Objekte darzustellen
    _c_(576214, _a_(576213, _a_(576212, _n_(576211, "pygame", lambda: pygame), "display"), "flip"))
    _l_(576215)

# Pygame beenden, nachdem Haupt-Schleife beendet wurde
_c_(576219, _a_(576218, _n_(576217, "pygame", lambda: pygame), "quit"))
_l_(576220)