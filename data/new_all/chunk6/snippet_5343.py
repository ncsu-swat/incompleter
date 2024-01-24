# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63873612/how-come-i-get-childhood-takes-no-arguments-when-i-execute-it-but-when-i-delete
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ex45f import live
    _l_(357130)

except ImportError:
    pass
class childhood(_n_(357131, "live", lambda: live)):
    _l_(357191)


    def development(self):
        _l_(357190)

        _n_(357132, "intelligent", lambda: intelligent)["low", "average", "high"]
        _l_(357133)
        if _c_(357137, _a_(357135, _n_(357134, "random", lambda: random), "choice"), _n_(357136, "intelligent", lambda: intelligent)) == _n_(357138, "low", lambda: low):
            _l_(357148)

            aux = "You are dumb"
            _l_(357139)
            return aux
        elif _c_(357143, _a_(357141, _n_(357140, "random", lambda: random), "choice"), _n_(357142, "intelligent", lambda: intelligent)) == _n_(357144, "average", lambda: average):
            _l_(357147)

            aux = "You are average"
            _l_(357145)
            return aux
        else:
            aux = "You are smart"
            _l_(357146)
            return aux

        if _n_(357149, "school", lambda: school) == "yes" and _n_(357150, "intelligent", lambda: intelligent) == _n_(357151, "high", lambda: high):
            _l_(357189)

            aux = 'You will have an fantastic life'
            _l_(357152)
            return aux
        elif _n_(357153, "school", lambda: school) == "no" and _n_(357154, "intelligent", lambda: intelligent) == _n_(357155, "high", lambda: high):
            _l_(357188)

            aux = "You will have an average life"
            _l_(357156)
            return aux
        elif _n_(357157, "school", lambda: school) == "maybe" and _n_(357158, "intelligent", lambda: intelligent) == _n_(357159, "high", lambda: high):
            _l_(357187)

            aux = "You will have an good life"
            _l_(357160)
            return aux
        elif _n_(357161, "school", lambda: school) == "yes" and _n_(357162, "intelligent", lambda: intelligent) == _n_(357163, "average", lambda: average):
            _l_(357186)

            aux = "You will have an good life"
            _l_(357164)
            return aux
        elif _n_(357165, "school", lambda: school) == "no" and _n_(357166, "intelligent", lambda: intelligent) == _n_(357167, "average", lambda: average):
            _l_(357185)

            aux = "You will have an bad life"
            _l_(357168)
            return aux
        elif _n_(357169, "school", lambda: school) == "maybe" and _n_(357170, "intelligent", lambda: intelligent) == _n_(357171, "average", lambda: average):
            _l_(357184)

            aux = "You will have an average life"
            _l_(357172)
            return aux
        elif _n_(357173, "school", lambda: school) == "yes" and _n_(357174, "intelligent", lambda: intelligent) == _n_(357175, "low", lambda: low):
            _l_(357183)

            aux = "You will have an average life"
            _l_(357176)
            return aux
        elif _n_(357177, "school", lambda: school) == "no" and _n_(357178, "intelligent", lambda: intelligent) == _n_(357179, "low", lambda: low):
            _l_(357182)

            aux = "You will have an horrible life"
            _l_(357180)
            return aux
        else:
            aux = "You will have an bad life"
            _l_(357181)
            return aux
#Zoek op how random choice antwoord bij betrekt
like_school = """Do you like school?
Possible answers: yes, no or maybe
> """
_l_(357192)
school = _c_(357195, _n_(357193, "input", lambda: input), _n_(357194, "like_school", lambda: like_school))
_l_(357196)
q = _c_(357199, _n_(357197, "childhood", lambda: childhood), _n_(357198, "school", lambda: school))
_l_(357200)
_c_(357203, _a_(357202, _n_(357201, "q", lambda: q), "development"))
_l_(357204)