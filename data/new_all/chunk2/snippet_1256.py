# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62126379/beginner-reading-python-programming-text-a-simple-game-keeps-returning-attribut
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sys import exit
    _l_(441298)

except ImportError:
    pass
try:
    from random import randint
    _l_(441300)

except ImportError:
    pass
try:
    from textwrap import dedent
    _l_(441302)

except ImportError:
    pass


class Scene(_n_(441303, "object", lambda: object)):
    _l_(441314)


    def enter(self):
        _l_(441313)

        _c_(441305, _n_(441304, "print", lambda: print), "This scene is not yet configured.")
        _l_(441306)
        _c_(441308, _n_(441307, "print", lambda: print), "Subclass it and implement enter()")
        _l_(441309)
        aux = 1
        _l_(441312)
        exit(aux)
# Skeleton code: a base class for Scene that will have
# the common things that all scenes do.

class Engine(_n_(441315, "object", lambda: object)):
    _l_(441348)


    def __init__(self, scene_map):
        _l_(441319)

        _n_(441316, "self", lambda: self).scene_map = _n_(441317, "scene_map", lambda: scene_map)
        _l_(441318)

    def play(self):
        _l_(441347)

        current_scene = _c_(441323, _a_(441322, _a_(441321, _n_(441320, "self", lambda: self), "scene_map"), "opening_scene"))
        _l_(441324)
        last_scene = _c_(441328, _a_(441327, _a_(441326, _n_(441325, "self", lambda: self), "scene_map"), "next_scene"), 'finished')
        _l_(441329)

        while _n_(441330, "current_scene", lambda: current_scene) != _n_(441331, "last_scene", lambda: last_scene):
            _l_(441342)

            next_scene_name = _c_(441334, _a_(441333, _n_(441332, "current_scene", lambda: current_scene), "enter"))
            _l_(441335)
            current_scene = _c_(441340, _a_(441338, _a_(441337, _n_(441336, "self", lambda: self), "scene_map"), "next_scene"), _n_(441339, "next_scene_name", lambda: next_scene_name))
            _l_(441341)

        # be sure to print out the last scene
        _c_(441345, _a_(441344, _n_(441343, "current_scene", lambda: current_scene), "enter"))
        _l_(441346)


class Death(_n_(441349, "Scene", lambda: Scene)):
    _l_(441363)


    quips = [
        "You died.  You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."

    ]
    _l_(441350)

    def enter(self):
        _l_(441362)

        _c_(441360, _n_(441351, "print", lambda: print), _a_(441353, _n_(441352, "Death", lambda: Death), "quips")[_c_(441359, _n_(441354, "randint", lambda: randint), 0, _c_(441358, _n_(441355, "len", lambda: len), _a_(441357, _n_(441356, "self", lambda: self), "quips"))-1)])
        _l_(441361)


class CentralCorridor(_n_(441364, "Scene", lambda: Scene)):
    _l_(441402)


    def enter(self):
        _l_(441401)

        _c_(441368, _n_(441365, "print", lambda: print), _c_(441367, _n_(441366, "dedent", lambda: dedent), """
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew.  You are the last surviving member
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body.  He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))
        _l_(441369)

        action = _c_(441371, _n_(441370, "input", lambda: input), "> ")
        _l_(441372)

        if _n_(441373, "action", lambda: action) == "shoot!":
            _l_(441400)

            _c_(441377, _n_(441374, "print", lambda: print), _c_(441376, _n_(441375, "dedent", lambda: dedent), """
                Quick on the draw you yank out your blaster and fire
                it at the Gothon.  His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laster hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead.  Then he eats you.
                """))
            _l_(441378)
            aux = 'death'
            _l_(441379)
            return aux

        elif _n_(441380, "action", lambda: action) == "dodge!":
            _l_(441399)

            _c_(441384, _n_(441381, "print", lambda: print), _c_(441383, _n_(441382, "dedent", lambda: dedent), """
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out.  You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))
            _l_(441385)
            aux = 'death'
            _l_(441386)
            return aux

        elif _n_(441387, "action", lambda: action) == "tell a joke":
            _l_(441398)

            _c_(441391, _n_(441388, "print", lambda: print), _c_(441390, _n_(441389, "dedent", lambda: dedent), """
                Lucky for you they made you learn Gothon insults in
                the academy.  You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            _l_(441392)
            aux = 'laster_weapon_armory'
            _l_(441393)
            return aux

        else:
            _c_(441395, _n_(441394, "print", lambda: print), "DOES NOT COMPUTE!")
            _l_(441396)
            aux = 'central_corridor'
            _l_(441397)
            return aux

class LaserWeaponArmory(_n_(441403, "Scene", lambda: Scene)):
    _l_(441447)


    def enter(self):
        _l_(441446)

        _c_(441407, _n_(441404, "print", lambda: print), _c_(441406, _n_(441405, "dedent", lambda: dedent), """
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more GOthon that might be hiding. It's dead
            quiet, too quiet.  You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.  The
            code is 3 digits.
            """))
        _l_(441408)

        code = f"{_c_(441410, _n_(441409, 'randint', lambda: randint), 1,9)}{_c_(441412, _n_(441411, 'randint', lambda: randint), 1,9)}{_c_(441414, _n_(441413, 'randint', lambda: randint), 1,9)}"
        _l_(441415)
        guess = _c_(441417, _n_(441416, "input", lambda: input), "[keypad]> ")
        _l_(441418)
        guesses = 0
        _l_(441419)

        while _n_(441420, "guess", lambda: guess) != _n_(441421, "code", lambda: code) and _n_(441422, "guesses", lambda: guesses) <10:
            _l_(441430)

            _c_(441424, _n_(441423, "print", lambda: print), "BZZZZEDDD!")
            _l_(441425)
            guesses += 1
            _l_(441426)
            guess = _c_(441428, _n_(441427, "input", lambda: input), "[keypad]> ")
            _l_(441429)

        if _n_(441431, "guess", lambda: guess) == _n_(441432, "code", lambda: code):
            _l_(441445)

            _c_(441436, _n_(441433, "print", lambda: print), _c_(441435, _n_(441434, "dedent", lambda: dedent), """
                The container clicks open and the seal breaks, letting
                gas out.  You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            _l_(441437)
            aux = 'the_bridge'
            _l_(441438)
            return aux
        else:
            _c_(441442, _n_(441439, "print", lambda: print), _c_(441441, _n_(441440, "dedent", lambda: dedent), """
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together.  You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.
                """))
            _l_(441443)
            aux = 'death'
            _l_(441444)
            return aux


class Finished(_n_(441448, "Scene", lambda: Scene)):
    _l_(441454)


    def enter(self):
        _l_(441453)

        _c_(441450, _n_(441449, "print", lambda: print), "You won! Good job.")
        _l_(441451)
        aux = 'finished'
        _l_(441452)
        return aux

class Map(_n_(441455, "object", lambda: object)):
    _l_(441487)


    scenes = {
        'central_corridor': _c_(441457, _n_(441456, "CentralCorridor", lambda: CentralCorridor)),
        'laster_weapon_armory': _c_(441459, _n_(441458, "LaserWeaponArmory", lambda: LaserWeaponArmory)),
        'the_bridge': _c_(441460, TheBridge),
        'escape_pod': _c_(441461, EscapePod),
        'death': _c_(441463, _n_(441462, "Death", lambda: Death)),
        'finished': _c_(441465, _n_(441464, "Finished", lambda: Finished))
    }
    _l_(441466)

    def __init__(self, start_scene):
        _l_(441470)

        _n_(441467, "self", lambda: self).start_scene = _n_(441468, "start_scene", lambda: start_scene)
        _l_(441469)

    def next_scene(self, scene_name):
        _l_(441479)

        val = _c_(441475, _a_(441473, _a_(441472, _n_(441471, "Map", lambda: Map), "scenes"), "get"), _n_(441474, "scene_name", lambda: scene_name))
        _l_(441476)
        aux = _n_(441477, "val", lambda: val)
        _l_(441478)
        return aux

    def opening_scene(self):
        _l_(441486)

        aux = _c_(441484, _a_(441481, _n_(441480, "self", lambda: self), "next_scene"), _a_(441483, _n_(441482, "self", lambda: self), "start_scene"))
        _l_(441485)
        return aux


# Finally the code that runs the game by making a Map, handing that map to
# an Engine before calling play to make game work.
a_map = _c_(441489, _n_(441488, "Map", lambda: Map), 'central_corridor')
_l_(441490)
a_game = _c_(441493, _n_(441491, "Engine", lambda: Engine), _n_(441492, "a_map", lambda: a_map))
_l_(441494)
_c_(441497, _a_(441496, _n_(441495, "a_game", lambda: a_game), "play"))
_l_(441498)