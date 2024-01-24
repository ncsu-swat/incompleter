# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60030733/nameerror-within-inheritance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class camera(_n_(339528, "player", lambda: player)):
    _l_(339647)

    def __init__(self, stagePosX,playerposX,y):
        _l_(339549)

        _c_(339536, _a_(339532, _n_(339529, "super", lambda: super)(_n_(339530, "camera", lambda: camera),_n_(339531, "self", lambda: self)), "__init__"), _n_(339533, "playerposX", lambda: playerposX),_n_(339534, "characterPosX", lambda: characterPosX),_n_(339535, "y", lambda: y))
        _l_(339537)
        _n_(339538, "self", lambda: self).playerposX = _n_(339539, "playerposX", lambda: playerposX)
        _l_(339540)
        _n_(339541, "self", lambda: self).startscrolling = _n_(339542, "bgWidth", lambda: bgWidth) / 2
        _l_(339543)
        _n_(339544, "self", lambda: self).stagePosX = _n_(339545, "stagePosX", lambda: stagePosX)
        _l_(339546)
        _n_(339547, "self", lambda: self).rel_x = 0
        _l_(339548)


    def scroll(self,stagePosX):
        _l_(339626)

        if _a_(339551, _n_(339550, "self", lambda: self), "k")[_a_(339553, _n_(339552, "pygame", lambda: pygame), "K_LEFT")]:
            _l_(339569)

            _n_(339554, "self", lambda: self).vel = (_a_(339556, _n_(339555, "self", lambda: self), "vel")*-1)
            _l_(339557)
        elif _a_(339559, _n_(339558, "self", lambda: self), "k")[_a_(339561, _n_(339560, "pygame", lambda: pygame), "K_RIGHT")]:
            _l_(339568)

            _n_(339562, "self", lambda: self).vel = (_a_(339564, _n_(339563, "self", lambda: self), "vel")*1)
            _l_(339565)
        else:
            _n_(339566, "self", lambda: self).vel = 0
            _l_(339567)



        _n_(339570, "self", lambda: self).rel_x = _a_(339572, _n_(339571, "self", lambda: self), "stagePosX") % _n_(339573, "bgWidth", lambda: bgWidth)
        _l_(339574)
        if _a_(339576, _n_(339575, "self", lambda: self), "playerPosX") > _n_(339577, "stageWidth", lambda: stageWidth) - _a_(339579, _n_(339578, "self", lambda: self), "width"):
            _l_(339586)

            _n_(339580, "self", lambda: self).playerPosX = _a_(339582, _n_(339581, "self", lambda: self), "stageWidth") - _a_(339584, _n_(339583, "self", lambda: self), "width")  # If the player position exceeds the stage
            _l_(339585)  # If the player position exceeds the stage
        if _a_(339588, _n_(339587, "self", lambda: self), "playerposX") < 0 - _a_(339590, _n_(339589, "self", lambda: self), "width"):
            _l_(339595)

            _n_(339591, "self", lambda: self).playerposX = _a_(339593, _n_(339592, "self", lambda: self), "width")  # If the player position is far left
            _l_(339594)  # If the player position is far left
        if _a_(339597, _n_(339596, "self", lambda: self), "playerposX") < _a_(339599, _n_(339598, "self", lambda: self), "startscrolling"):
            _l_(339625)

            _n_(339600, "self", lambda: self).characterPosX = _a_(339602, _n_(339601, "self", lambda: self), "playerposX")
            _l_(339603)
        elif _a_(339605, _n_(339604, "self", lambda: self), "playerposXplayerposX") > _n_(339606, "stageWidth", lambda: stageWidth) - _a_(339608, _n_(339607, "self", lambda: self), "startscrolling"):
            _l_(339624)

            _n_(339609, "self", lambda: self).characterPosX = _a_(339611, _n_(339610, "self", lambda: self), "playerPosX") - _n_(339612, "stageWidth", lambda: stageWidth) + _a_(339614, _n_(339613, "self", lambda: self), "width")
            _l_(339615)
        else:
            _n_(339616, "self", lambda: self).characterPosX = _a_(339618, _n_(339617, "self", lambda: self), "startscrolling")
            _l_(339619)
            _n_(339620, "self", lambda: self).stagePosX +=  -_a_(339622, _n_(339621, "self", lambda: self), "vel")
            _l_(339623)






    def draw(self, win):
        _l_(339646)

        _c_(339633, _a_(339628, _n_(339627, "win", lambda: win), "blit"), _n_(339629, "bg", lambda: bg), (_a_(339631, _n_(339630, "self", lambda: self), "rel_x") - _n_(339632, "bgWidth", lambda: bgWidth), 0))
        _l_(339634)
        if _a_(339636, _n_(339635, "self", lambda: self), "rel_x") < _n_(339637, "bgWidth", lambda: bgWidth):
            _l_(339645)

            _c_(339643, _a_(339639, _n_(339638, "win", lambda: win), "blit"), _n_(339640, "bg", lambda: bg), (_a_(339642, _n_(339641, "self", lambda: self), "rel_x"), 0))
            _l_(339644)