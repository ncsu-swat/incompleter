# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63909122/nameerror-name-packet-is-not-defined-rlbot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Optional
    _l_(355187)

except ImportError:
    pass
try:
    from rlbot.agents.base_agent import BaseAgent, GameTickPacket, SimpleControllerState
    _l_(355189)

except ImportError:
    pass
try:
    import os
    _l_(355191)

except ImportError:
    pass
try:
    import time
    _l_(355193)

except ImportError:
    pass
try:
    import math
    _l_(355195)

except ImportError:
    pass
try:
    from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
    _l_(355197)

except ImportError:
    pass
try:
    from rlbot.utils.structures.game_data_struct import GameTickPacket
    _l_(355199)

except ImportError:
    pass
try:
    from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3 as vector3, Rotator
    _l_(355201)

except ImportError:
    pass
try:
    import random
    _l_(355203)

except ImportError:
    pass
try:
    from rlbot.agents.base_script import BaseScript
    _l_(355205)

except ImportError:
    pass
try:
    from rlbot.utils.game_state_util import GameState
    _l_(355207)

except ImportError:
    pass



DIRECTORY_LOCATION = "C:\Logs\Recorder\log"
_l_(355208)
randNum = _c_(355211, _a_(355210, _n_(355209, "random", lambda: random), "randint"), 0,9999999999) 
_l_(355212) 

# Extending the BaseScript class is purely optional. It's just convenient / abstracts you away from
# some strange classes like GameInterface
class playerRecorder(_n_(355213, "BaseScript", lambda: BaseScript)):
    _l_(355688)

    
    def __init__(self):
        _l_(355234)

        _c_(355216, _a_(355215, _n_(355214, "super", lambda: super)(), "__init__"), "playerRecorder")
        _l_(355217)
        packet = _c_(355220, _a_(355219, _n_(355218, "self", lambda: self), "get_game_tick_packet"))
        _l_(355221)
        _n_(355222, "self", lambda: self).writeFile = _c_(355232, _n_(355223, "open", lambda: open), _n_(355224, "DIRECTORY_LOCATION", lambda: DIRECTORY_LOCATION)+"\\"+"HumanLog"+_c_(355228, _n_(355225, "str", lambda: str), _a_(355227, _n_(355226, "car", lambda: car), "team"))+"-"+_c_(355231, _n_(355229, "str", lambda: str), _n_(355230, "randNum", lambda: randNum)), "w")
        _l_(355233)

    def run(self):
        _l_(355250)

        while True:
            _l_(355249)

        
            packet = _c_(355237, _a_(355236, _n_(355235, "self", lambda: self), "get_game_tick_packet"))
            _l_(355238)
        
            _c_(355241, _n_(355239, "get_output", lambda: get_output), _n_(355240, "packet", lambda: packet))
            _l_(355242)
        
            _c_(355244, _n_(355243, "sleep", lambda: sleep), 1 / 3)
            _l_(355245)
        
            _c_(355247, _n_(355246, "print", lambda: print), "test")  
            _l_(355248)  
    
    for car in _a_(355251, packet, "game_cars"):
        _l_(355259)

        if not _a_(355252, car, "is_bot"):
            _l_(355258)

            team = _a_(355253, car, "team")
            _l_(355254)
            index = _a_(355255, car, "index")
            _l_(355256)
            break
            _l_(355257)

    def get_output(self, game_tick_packet):
        _l_(355687)

       #***************************************************************    
        packet = _c_(355262, _a_(355261, _n_(355260, "self", lambda: self), "get_game_tick_packet"))
        _l_(355263)
        
        goodTeam = _c_(355267, _n_(355264, "str", lambda: str), _a_(355266, _n_(355265, "car", lambda: car), "team"))
        _l_(355268)
        
        goodLoc = _a_(355274, _a_(355273, _a_(355270, _n_(355269, "packet", lambda: packet), "game_cars")[_a_(355272, _n_(355271, "car", lambda: car), "index")], "physics"), "location")
        _l_(355275)
        goodLocX = _c_(355279, _n_(355276, "str", lambda: str), _a_(355278, _n_(355277, "goodLoc", lambda: goodLoc), "x"))
        _l_(355280)
        goodLocY = _c_(355284, _n_(355281, "str", lambda: str), _a_(355283, _n_(355282, "goodLoc", lambda: goodLoc), "y"))
        _l_(355285)
        goodLocZ = _c_(355289, _n_(355286, "str", lambda: str), _a_(355288, _n_(355287, "goodLoc", lambda: goodLoc), "z"))
        _l_(355290)
        
        goodRot = _a_(355296, _a_(355295, _a_(355292, _n_(355291, "packet", lambda: packet), "game_cars")[_a_(355294, _n_(355293, "car", lambda: car), "index")], "physics"), "rotation")
        _l_(355297)
        goodRotP = _c_(355301, _n_(355298, "str", lambda: str), _a_(355300, _n_(355299, "goodRot", lambda: goodRot), "pitch"))
        _l_(355302)
        goodRotY = _c_(355306, _n_(355303, "str", lambda: str), _a_(355305, _n_(355304, "goodRot", lambda: goodRot), "yaw"))
        _l_(355307)
        goodRotR = _c_(355311, _n_(355308, "str", lambda: str), _a_(355310, _n_(355309, "goodRot", lambda: goodRot), "roll"))
        _l_(355312)
        
        goodVel = _a_(355318, _a_(355317, _a_(355314, _n_(355313, "packet", lambda: packet), "game_cars")[_a_(355316, _n_(355315, "car", lambda: car), "index")], "physics"), "velocity")
        _l_(355319)
        goodVelX = _c_(355323, _n_(355320, "str", lambda: str), _a_(355322, _n_(355321, "goodVel", lambda: goodVel), "x"))
        _l_(355324)
        goodVelY = _c_(355328, _n_(355325, "str", lambda: str), _a_(355327, _n_(355326, "goodVel", lambda: goodVel), "y"))
        _l_(355329)
        goodVelZ = _c_(355333, _n_(355330, "str", lambda: str), _a_(355332, _n_(355331, "goodVel", lambda: goodVel), "z"))
        _l_(355334)
        
        goodAngVel = _a_(355340, _a_(355339, _a_(355336, _n_(355335, "packet", lambda: packet), "game_cars")[_a_(355338, _n_(355337, "car", lambda: car), "index")], "physics"), "angular_velocity")
        _l_(355341)
        goodAngVelX = _c_(355345, _n_(355342, "str", lambda: str), _a_(355344, _n_(355343, "goodAngVel", lambda: goodAngVel), "x"))
        _l_(355346)
        goodAngVelY = _c_(355350, _n_(355347, "str", lambda: str), _a_(355349, _n_(355348, "goodAngVel", lambda: goodAngVel), "y"))
        _l_(355351)
        goodAngVelZ = _c_(355355, _n_(355352, "str", lambda: str), _a_(355354, _n_(355353, "goodAngVel", lambda: goodAngVel), "z"))
        _l_(355356)
        
        hasWC = _c_(355363, _n_(355357, "str", lambda: str), _a_(355362, _a_(355359, _n_(355358, "packet", lambda: packet), "game_cars")[_a_(355361, _n_(355360, "car", lambda: car), "index")], "has_wheel_contact"))
        _l_(355364)
        isSS = _c_(355371, _n_(355365, "str", lambda: str), _a_(355370, _a_(355367, _n_(355366, "packet", lambda: packet), "game_cars")[_a_(355369, _n_(355368, "car", lambda: car), "index")], "is_super_sonic"))
        _l_(355372)
        jumped = _c_(355379, _n_(355373, "str", lambda: str), _a_(355378, _a_(355375, _n_(355374, "packet", lambda: packet), "game_cars")[_a_(355377, _n_(355376, "car", lambda: car), "index")], "jumped"))
        _l_(355380)
        dJumped = _c_(355387, _n_(355381, "str", lambda: str), _a_(355386, _a_(355383, _n_(355382, "packet", lambda: packet), "game_cars")[_a_(355385, _n_(355384, "car", lambda: car), "index")], "double_jumped"))
        _l_(355388)
        bst = _c_(355395, _n_(355389, "str", lambda: str), _a_(355394, _a_(355391, _n_(355390, "packet", lambda: packet), "game_cars")[_a_(355393, _n_(355392, "car", lambda: car), "index")], "boost"))        
        _l_(355396)        
        
        ballLoc = _a_(355400, _a_(355399, _a_(355398, _n_(355397, "packet", lambda: packet), "game_ball"), "physics"), "location")
        _l_(355401)
        ballLocX = _c_(355405, _n_(355402, "str", lambda: str), _a_(355404, _n_(355403, "ballLoc", lambda: ballLoc), "x"))
        _l_(355406)
        ballLocY = _c_(355410, _n_(355407, "str", lambda: str), _a_(355409, _n_(355408, "ballLoc", lambda: ballLoc), "y"))
        _l_(355411)
        ballLocZ = _c_(355415, _n_(355412, "str", lambda: str), _a_(355414, _n_(355413, "ballLoc", lambda: ballLoc), "z"))        
        _l_(355416)        
        
        ballVel = _a_(355420, _a_(355419, _a_(355418, _n_(355417, "packet", lambda: packet), "game_ball"), "physics"), "velocity")
        _l_(355421)
        ballVelX = _c_(355425, _n_(355422, "str", lambda: str), _a_(355424, _n_(355423, "ballVel", lambda: ballVel), "x"))
        _l_(355426)
        ballVelY = _c_(355430, _n_(355427, "str", lambda: str), _a_(355429, _n_(355428, "ballVel", lambda: ballVel), "y"))
        _l_(355431)
        ballVelZ = _c_(355435, _n_(355432, "str", lambda: str), _a_(355434, _n_(355433, "ballVel", lambda: ballVel), "z"))
        _l_(355436)
        
        _c_(355464, _a_(355439, _a_(355438, _n_(355437, "self", lambda: self), "writeFile"), "write"), _n_(355440, "goodTeam", lambda: goodTeam)+";"+
            _n_(355441, "goodLocX", lambda: goodLocX)+","+_n_(355442, "goodLocY", lambda: goodLocY)+","+_n_(355443, "goodLocZ", lambda: goodLocZ)+";"+
            _n_(355444, "goodRotP", lambda: goodRotP)+","+_n_(355445, "goodRotY", lambda: goodRotY)+","+_n_(355446, "goodRotR", lambda: goodRotR)+";"+
            _n_(355447, "goodVelX", lambda: goodVelX)+","+_n_(355448, "goodVelY", lambda: goodVelY)+","+_n_(355449, "goodVelZ", lambda: goodVelZ)+";"+
            _n_(355450, "goodAngVelX", lambda: goodAngVelX)+","+_n_(355451, "goodAngVelY", lambda: goodAngVelY)+","+_n_(355452, "goodAngVelZ", lambda: goodAngVelZ)+";"+
            _n_(355453, "hasWC", lambda: hasWC)+";"+_n_(355454, "isSS", lambda: isSS)+";"+_n_(355455, "jumped", lambda: jumped)+";"+_n_(355456, "dJumped", lambda: dJumped)+";"+_n_(355457, "bst", lambda: bst)+";"+
            _n_(355458, "ballLocX", lambda: ballLocX)+","+_n_(355459, "ballLocY", lambda: ballLocY)+","+_n_(355460, "ballLocZ", lambda: ballLocZ)+";"+
            _n_(355461, "ballVelX", lambda: ballVelX)+","+_n_(355462, "ballVelY", lambda: ballVelY)+","+_n_(355463, "ballVelZ", lambda: ballVelZ))
        _l_(355465)
        _c_(355469, _a_(355468, _a_(355467, _n_(355466, "self", lambda: self), "writeFile"), "write"), "\n")
        _l_(355470)
        
        
        ## WRITE OPPONENT
        badIndex = -1
        _l_(355471)
        for i in _c_(355477, _n_(355472, "range", lambda: range), _c_(355476, _n_(355473, "len", lambda: len), _a_(355475, _n_(355474, "packet", lambda: packet), "game_cars"))):
            _l_(355485)

            if _n_(355478, "i", lambda: i) != _a_(355480, _n_(355479, "car", lambda: car), "index"):
                _l_(355484)

                badIndex = _n_(355481, "i", lambda: i)
                _l_(355482)
                break
                _l_(355483)
        assert _n_(355486, "badIndex", lambda: badIndex) != _a_(355488, _n_(355487, "car", lambda: car), "index")
        _l_(355489)
        assert _n_(355490, "badIndex", lambda: badIndex) != -1
        _l_(355491)
        
        badTeam = _c_(355497, _n_(355492, "str", lambda: str), _a_(355496, _a_(355494, _n_(355493, "packet", lambda: packet), "game_cars")[_n_(355495, "badIndex", lambda: badIndex)], "team"))
        _l_(355498)
        
        badLoc = _a_(355503, _a_(355502, _a_(355500, _n_(355499, "packet", lambda: packet), "game_cars")[_n_(355501, "badIndex", lambda: badIndex)], "physics"), "location")
        _l_(355504)
        badLocX = _c_(355508, _n_(355505, "str", lambda: str), _a_(355507, _n_(355506, "badLoc", lambda: badLoc), "x"))
        _l_(355509)
        badLocY = _c_(355513, _n_(355510, "str", lambda: str), _a_(355512, _n_(355511, "badLoc", lambda: badLoc), "y"))
        _l_(355514)
        badLocZ = _c_(355518, _n_(355515, "str", lambda: str), _a_(355517, _n_(355516, "badLoc", lambda: badLoc), "z"))
        _l_(355519)
        
        badRot = _a_(355524, _a_(355523, _a_(355521, _n_(355520, "packet", lambda: packet), "game_cars")[_n_(355522, "badIndex", lambda: badIndex)], "physics"), "rotation")
        _l_(355525)
        badRotP = _c_(355529, _n_(355526, "str", lambda: str), _a_(355528, _n_(355527, "badRot", lambda: badRot), "pitch"))
        _l_(355530)
        badRotY = _c_(355534, _n_(355531, "str", lambda: str), _a_(355533, _n_(355532, "badRot", lambda: badRot), "yaw"))
        _l_(355535)
        badRotR = _c_(355539, _n_(355536, "str", lambda: str), _a_(355538, _n_(355537, "badRot", lambda: badRot), "roll"))
        _l_(355540)
        
        badVel = _a_(355545, _a_(355544, _a_(355542, _n_(355541, "packet", lambda: packet), "game_cars")[_n_(355543, "badIndex", lambda: badIndex)], "physics"), "velocity")
        _l_(355546)
        badVelX = _c_(355550, _n_(355547, "str", lambda: str), _a_(355549, _n_(355548, "badVel", lambda: badVel), "x"))
        _l_(355551)
        badVelY = _c_(355555, _n_(355552, "str", lambda: str), _a_(355554, _n_(355553, "badVel", lambda: badVel), "y"))
        _l_(355556)
        badVelZ = _c_(355560, _n_(355557, "str", lambda: str), _a_(355559, _n_(355558, "badVel", lambda: badVel), "z"))
        _l_(355561)
        
        badAngVel = _a_(355566, _a_(355565, _a_(355563, _n_(355562, "packet", lambda: packet), "game_cars")[_n_(355564, "badIndex", lambda: badIndex)], "physics"), "angular_velocity")
        _l_(355567)
        badAngVelX = _c_(355571, _n_(355568, "str", lambda: str), _a_(355570, _n_(355569, "badAngVel", lambda: badAngVel), "x"))
        _l_(355572)
        badAngVelY = _c_(355576, _n_(355573, "str", lambda: str), _a_(355575, _n_(355574, "badAngVel", lambda: badAngVel), "y"))
        _l_(355577)
        badAngVelZ = _c_(355581, _n_(355578, "str", lambda: str), _a_(355580, _n_(355579, "badAngVel", lambda: badAngVel), "z"))
        _l_(355582)
        
        badhasWC = _c_(355588, _n_(355583, "str", lambda: str), _a_(355587, _a_(355585, _n_(355584, "packet", lambda: packet), "game_cars")[_n_(355586, "badIndex", lambda: badIndex)], "has_wheel_contact"))
        _l_(355589)
        badisSS = _c_(355595, _n_(355590, "str", lambda: str), _a_(355594, _a_(355592, _n_(355591, "packet", lambda: packet), "game_cars")[_n_(355593, "badIndex", lambda: badIndex)], "is_super_sonic"))
        _l_(355596)
        badjumped = _c_(355602, _n_(355597, "str", lambda: str), _a_(355601, _a_(355599, _n_(355598, "packet", lambda: packet), "game_cars")[_n_(355600, "badIndex", lambda: badIndex)], "jumped"))
        _l_(355603)
        baddJumped = _c_(355609, _n_(355604, "str", lambda: str), _a_(355608, _a_(355606, _n_(355605, "packet", lambda: packet), "game_cars")[_n_(355607, "badIndex", lambda: badIndex)], "double_jumped"))
        _l_(355610)
        badbst = _c_(355616, _n_(355611, "str", lambda: str), _a_(355615, _a_(355613, _n_(355612, "packet", lambda: packet), "game_cars")[_n_(355614, "badIndex", lambda: badIndex)], "boost"))       
        _l_(355617)       

        _c_(355639, _a_(355620, _a_(355619, _n_(355618, "self", lambda: self), "writeFile"), "write"), _n_(355621, "badTeam", lambda: badTeam)+";"+
            _n_(355622, "badLocX", lambda: badLocX)+","+_n_(355623, "badLocY", lambda: badLocY)+","+_n_(355624, "badLocZ", lambda: badLocZ)+";"+
            _n_(355625, "badRotP", lambda: badRotP)+","+_n_(355626, "badRotY", lambda: badRotY)+","+_n_(355627, "badRotR", lambda: badRotR)+";"+
            _n_(355628, "badVelX", lambda: badVelX)+","+_n_(355629, "badVelY", lambda: badVelY)+","+_n_(355630, "badVelZ", lambda: badVelZ)+";"+
            _n_(355631, "badAngVelX", lambda: badAngVelX)+","+_n_(355632, "badAngVelY", lambda: badAngVelY)+","+_n_(355633, "badAngVelZ", lambda: badAngVelZ)+";"+
            _n_(355634, "badhasWC", lambda: badhasWC)+";"+_n_(355635, "badisSS", lambda: badisSS)+";"+_n_(355636, "badjumped", lambda: badjumped)+";"+_n_(355637, "baddJumped", lambda: baddJumped)+";"+_n_(355638, "badbst", lambda: badbst))
        _l_(355640)
        _c_(355644, _a_(355643, _a_(355642, _n_(355641, "self", lambda: self), "writeFile"), "write"), "\n")
        _l_(355645)
        
        
        ## WRITE ACTION
        _c_(355678, _a_(355648, _a_(355647, _n_(355646, "self", lambda: self), "writeFile"), "write"), _c_(355652, _n_(355649, "str", lambda: str), _a_(355651, _n_(355650, "action", lambda: action), "throttle"))+";"+_c_(355656, _n_(355653, "str", lambda: str), _a_(355655, _n_(355654, "action", lambda: action), "steer"))+";"+_c_(355660, _n_(355657, "str", lambda: str), _a_(355659, _n_(355658, "action", lambda: action), "pitch"))+";"+_c_(355664, _n_(355661, "str", lambda: str), _a_(355663, _n_(355662, "action", lambda: action), "yaw"))+";"+_c_(355669, _n_(355665, "str", lambda: str), _a_(355668, _a_(355667, _n_(355666, "action", lambda: action), "action"), "roll"))+";"+_c_(355673, _n_(355670, "str", lambda: str), _a_(355672, _n_(355671, "action", lambda: action), "jump"))+";"+_c_(355677, _n_(355674, "str", lambda: str), _a_(355676, _n_(355675, "action", lambda: action), "boost")))
        _l_(355679)
        _c_(355683, _a_(355682, _a_(355681, _n_(355680, "self", lambda: self), "writeFile"), "write"), "\n")
        _l_(355684)
        aux = _n_(355685, "action", lambda: action)
        _l_(355686)
        ##*****************************************************

        return aux