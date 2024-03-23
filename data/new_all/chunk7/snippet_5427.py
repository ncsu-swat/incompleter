# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63909122/nameerror-name-packet-is-not-defined-rlbot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Optional
    _l_(341167)

except ImportError:
    pass
try:
    from rlbot.agents.base_agent import BaseAgent, GameTickPacket, SimpleControllerState
    _l_(341169)

except ImportError:
    pass
try:
    import os
    _l_(341171)

except ImportError:
    pass
try:
    import time
    _l_(341173)

except ImportError:
    pass
try:
    import math
    _l_(341175)

except ImportError:
    pass
try:
    from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
    _l_(341177)

except ImportError:
    pass
try:
    from rlbot.utils.structures.game_data_struct import GameTickPacket
    _l_(341179)

except ImportError:
    pass
try:
    from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3 as vector3, Rotator
    _l_(341181)

except ImportError:
    pass
try:
    import random
    _l_(341183)

except ImportError:
    pass
try:
    from rlbot.agents.base_script import BaseScript
    _l_(341185)

except ImportError:
    pass
try:
    from rlbot.utils.game_state_util import GameState
    _l_(341187)

except ImportError:
    pass



DIRECTORY_LOCATION = "C:\Logs\Recorder\log"
_l_(341188)
randNum = _c_(341191, _a_(341190, _n_(341189, "random", lambda: random), "randint"), 0,9999999999) 
_l_(341192) 

# Extending the BaseScript class is purely optional. It's just convenient / abstracts you away from
# some strange classes like GameInterface
class playerRecorder(_n_(341193, "BaseScript", lambda: BaseScript)):
    _l_(341668)

    
    def __init__(self):
        _l_(341214)

        _c_(341196, _a_(341195, _n_(341194, "super", lambda: super)(), "__init__"), "playerRecorder")
        _l_(341197)
        packet = _c_(341200, _a_(341199, _n_(341198, "self", lambda: self), "get_game_tick_packet"))
        _l_(341201)
        _n_(341202, "self", lambda: self).writeFile = _c_(341212, _n_(341203, "open", lambda: open), _n_(341204, "DIRECTORY_LOCATION", lambda: DIRECTORY_LOCATION)+"\\"+"HumanLog"+_c_(341208, _n_(341205, "str", lambda: str), _a_(341207, _n_(341206, "car", lambda: car), "team"))+"-"+_c_(341211, _n_(341209, "str", lambda: str), _n_(341210, "randNum", lambda: randNum)), "w")
        _l_(341213)

    def run(self):
        _l_(341230)

        while True:
            _l_(341229)

        
            packet = _c_(341217, _a_(341216, _n_(341215, "self", lambda: self), "get_game_tick_packet"))
            _l_(341218)
        
            _c_(341221, _n_(341219, "get_output", lambda: get_output), _n_(341220, "packet", lambda: packet))
            _l_(341222)
        
            _c_(341224, _n_(341223, "sleep", lambda: sleep), 1 / 3)
            _l_(341225)
        
            _c_(341227, _n_(341226, "print", lambda: print), "test")  
            _l_(341228)  
    
    for car in _a_(341231, packet, "game_cars"):
        _l_(341239)

        if not _a_(341232, car, "is_bot"):
            _l_(341238)

            team = _a_(341233, car, "team")
            _l_(341234)
            index = _a_(341235, car, "index")
            _l_(341236)
            break
            _l_(341237)

    def get_output(self, game_tick_packet):
        _l_(341667)

       #***************************************************************    
        packet = _c_(341242, _a_(341241, _n_(341240, "self", lambda: self), "get_game_tick_packet"))
        _l_(341243)
        
        goodTeam = _c_(341247, _n_(341244, "str", lambda: str), _a_(341246, _n_(341245, "car", lambda: car), "team"))
        _l_(341248)
        
        goodLoc = _a_(341254, _a_(341253, _a_(341250, _n_(341249, "packet", lambda: packet), "game_cars")[_a_(341252, _n_(341251, "car", lambda: car), "index")], "physics"), "location")
        _l_(341255)
        goodLocX = _c_(341259, _n_(341256, "str", lambda: str), _a_(341258, _n_(341257, "goodLoc", lambda: goodLoc), "x"))
        _l_(341260)
        goodLocY = _c_(341264, _n_(341261, "str", lambda: str), _a_(341263, _n_(341262, "goodLoc", lambda: goodLoc), "y"))
        _l_(341265)
        goodLocZ = _c_(341269, _n_(341266, "str", lambda: str), _a_(341268, _n_(341267, "goodLoc", lambda: goodLoc), "z"))
        _l_(341270)
        
        goodRot = _a_(341276, _a_(341275, _a_(341272, _n_(341271, "packet", lambda: packet), "game_cars")[_a_(341274, _n_(341273, "car", lambda: car), "index")], "physics"), "rotation")
        _l_(341277)
        goodRotP = _c_(341281, _n_(341278, "str", lambda: str), _a_(341280, _n_(341279, "goodRot", lambda: goodRot), "pitch"))
        _l_(341282)
        goodRotY = _c_(341286, _n_(341283, "str", lambda: str), _a_(341285, _n_(341284, "goodRot", lambda: goodRot), "yaw"))
        _l_(341287)
        goodRotR = _c_(341291, _n_(341288, "str", lambda: str), _a_(341290, _n_(341289, "goodRot", lambda: goodRot), "roll"))
        _l_(341292)
        
        goodVel = _a_(341298, _a_(341297, _a_(341294, _n_(341293, "packet", lambda: packet), "game_cars")[_a_(341296, _n_(341295, "car", lambda: car), "index")], "physics"), "velocity")
        _l_(341299)
        goodVelX = _c_(341303, _n_(341300, "str", lambda: str), _a_(341302, _n_(341301, "goodVel", lambda: goodVel), "x"))
        _l_(341304)
        goodVelY = _c_(341308, _n_(341305, "str", lambda: str), _a_(341307, _n_(341306, "goodVel", lambda: goodVel), "y"))
        _l_(341309)
        goodVelZ = _c_(341313, _n_(341310, "str", lambda: str), _a_(341312, _n_(341311, "goodVel", lambda: goodVel), "z"))
        _l_(341314)
        
        goodAngVel = _a_(341320, _a_(341319, _a_(341316, _n_(341315, "packet", lambda: packet), "game_cars")[_a_(341318, _n_(341317, "car", lambda: car), "index")], "physics"), "angular_velocity")
        _l_(341321)
        goodAngVelX = _c_(341325, _n_(341322, "str", lambda: str), _a_(341324, _n_(341323, "goodAngVel", lambda: goodAngVel), "x"))
        _l_(341326)
        goodAngVelY = _c_(341330, _n_(341327, "str", lambda: str), _a_(341329, _n_(341328, "goodAngVel", lambda: goodAngVel), "y"))
        _l_(341331)
        goodAngVelZ = _c_(341335, _n_(341332, "str", lambda: str), _a_(341334, _n_(341333, "goodAngVel", lambda: goodAngVel), "z"))
        _l_(341336)
        
        hasWC = _c_(341343, _n_(341337, "str", lambda: str), _a_(341342, _a_(341339, _n_(341338, "packet", lambda: packet), "game_cars")[_a_(341341, _n_(341340, "car", lambda: car), "index")], "has_wheel_contact"))
        _l_(341344)
        isSS = _c_(341351, _n_(341345, "str", lambda: str), _a_(341350, _a_(341347, _n_(341346, "packet", lambda: packet), "game_cars")[_a_(341349, _n_(341348, "car", lambda: car), "index")], "is_super_sonic"))
        _l_(341352)
        jumped = _c_(341359, _n_(341353, "str", lambda: str), _a_(341358, _a_(341355, _n_(341354, "packet", lambda: packet), "game_cars")[_a_(341357, _n_(341356, "car", lambda: car), "index")], "jumped"))
        _l_(341360)
        dJumped = _c_(341367, _n_(341361, "str", lambda: str), _a_(341366, _a_(341363, _n_(341362, "packet", lambda: packet), "game_cars")[_a_(341365, _n_(341364, "car", lambda: car), "index")], "double_jumped"))
        _l_(341368)
        bst = _c_(341375, _n_(341369, "str", lambda: str), _a_(341374, _a_(341371, _n_(341370, "packet", lambda: packet), "game_cars")[_a_(341373, _n_(341372, "car", lambda: car), "index")], "boost"))        
        _l_(341376)        
        
        ballLoc = _a_(341380, _a_(341379, _a_(341378, _n_(341377, "packet", lambda: packet), "game_ball"), "physics"), "location")
        _l_(341381)
        ballLocX = _c_(341385, _n_(341382, "str", lambda: str), _a_(341384, _n_(341383, "ballLoc", lambda: ballLoc), "x"))
        _l_(341386)
        ballLocY = _c_(341390, _n_(341387, "str", lambda: str), _a_(341389, _n_(341388, "ballLoc", lambda: ballLoc), "y"))
        _l_(341391)
        ballLocZ = _c_(341395, _n_(341392, "str", lambda: str), _a_(341394, _n_(341393, "ballLoc", lambda: ballLoc), "z"))        
        _l_(341396)        
        
        ballVel = _a_(341400, _a_(341399, _a_(341398, _n_(341397, "packet", lambda: packet), "game_ball"), "physics"), "velocity")
        _l_(341401)
        ballVelX = _c_(341405, _n_(341402, "str", lambda: str), _a_(341404, _n_(341403, "ballVel", lambda: ballVel), "x"))
        _l_(341406)
        ballVelY = _c_(341410, _n_(341407, "str", lambda: str), _a_(341409, _n_(341408, "ballVel", lambda: ballVel), "y"))
        _l_(341411)
        ballVelZ = _c_(341415, _n_(341412, "str", lambda: str), _a_(341414, _n_(341413, "ballVel", lambda: ballVel), "z"))
        _l_(341416)
        
        _c_(341444, _a_(341419, _a_(341418, _n_(341417, "self", lambda: self), "writeFile"), "write"), _n_(341420, "goodTeam", lambda: goodTeam)+";"+
            _n_(341421, "goodLocX", lambda: goodLocX)+","+_n_(341422, "goodLocY", lambda: goodLocY)+","+_n_(341423, "goodLocZ", lambda: goodLocZ)+";"+
            _n_(341424, "goodRotP", lambda: goodRotP)+","+_n_(341425, "goodRotY", lambda: goodRotY)+","+_n_(341426, "goodRotR", lambda: goodRotR)+";"+
            _n_(341427, "goodVelX", lambda: goodVelX)+","+_n_(341428, "goodVelY", lambda: goodVelY)+","+_n_(341429, "goodVelZ", lambda: goodVelZ)+";"+
            _n_(341430, "goodAngVelX", lambda: goodAngVelX)+","+_n_(341431, "goodAngVelY", lambda: goodAngVelY)+","+_n_(341432, "goodAngVelZ", lambda: goodAngVelZ)+";"+
            _n_(341433, "hasWC", lambda: hasWC)+";"+_n_(341434, "isSS", lambda: isSS)+";"+_n_(341435, "jumped", lambda: jumped)+";"+_n_(341436, "dJumped", lambda: dJumped)+";"+_n_(341437, "bst", lambda: bst)+";"+
            _n_(341438, "ballLocX", lambda: ballLocX)+","+_n_(341439, "ballLocY", lambda: ballLocY)+","+_n_(341440, "ballLocZ", lambda: ballLocZ)+";"+
            _n_(341441, "ballVelX", lambda: ballVelX)+","+_n_(341442, "ballVelY", lambda: ballVelY)+","+_n_(341443, "ballVelZ", lambda: ballVelZ))
        _l_(341445)
        _c_(341449, _a_(341448, _a_(341447, _n_(341446, "self", lambda: self), "writeFile"), "write"), "\n")
        _l_(341450)
        
        
        ## WRITE OPPONENT
        badIndex = -1
        _l_(341451)
        for i in _c_(341457, _n_(341452, "range", lambda: range), _c_(341456, _n_(341453, "len", lambda: len), _a_(341455, _n_(341454, "packet", lambda: packet), "game_cars"))):
            _l_(341465)

            if _n_(341458, "i", lambda: i) != _a_(341460, _n_(341459, "car", lambda: car), "index"):
                _l_(341464)

                badIndex = _n_(341461, "i", lambda: i)
                _l_(341462)
                break
                _l_(341463)
        assert _n_(341466, "badIndex", lambda: badIndex) != _a_(341468, _n_(341467, "car", lambda: car), "index")
        _l_(341469)
        assert _n_(341470, "badIndex", lambda: badIndex) != -1
        _l_(341471)
        
        badTeam = _c_(341477, _n_(341472, "str", lambda: str), _a_(341476, _a_(341474, _n_(341473, "packet", lambda: packet), "game_cars")[_n_(341475, "badIndex", lambda: badIndex)], "team"))
        _l_(341478)
        
        badLoc = _a_(341483, _a_(341482, _a_(341480, _n_(341479, "packet", lambda: packet), "game_cars")[_n_(341481, "badIndex", lambda: badIndex)], "physics"), "location")
        _l_(341484)
        badLocX = _c_(341488, _n_(341485, "str", lambda: str), _a_(341487, _n_(341486, "badLoc", lambda: badLoc), "x"))
        _l_(341489)
        badLocY = _c_(341493, _n_(341490, "str", lambda: str), _a_(341492, _n_(341491, "badLoc", lambda: badLoc), "y"))
        _l_(341494)
        badLocZ = _c_(341498, _n_(341495, "str", lambda: str), _a_(341497, _n_(341496, "badLoc", lambda: badLoc), "z"))
        _l_(341499)
        
        badRot = _a_(341504, _a_(341503, _a_(341501, _n_(341500, "packet", lambda: packet), "game_cars")[_n_(341502, "badIndex", lambda: badIndex)], "physics"), "rotation")
        _l_(341505)
        badRotP = _c_(341509, _n_(341506, "str", lambda: str), _a_(341508, _n_(341507, "badRot", lambda: badRot), "pitch"))
        _l_(341510)
        badRotY = _c_(341514, _n_(341511, "str", lambda: str), _a_(341513, _n_(341512, "badRot", lambda: badRot), "yaw"))
        _l_(341515)
        badRotR = _c_(341519, _n_(341516, "str", lambda: str), _a_(341518, _n_(341517, "badRot", lambda: badRot), "roll"))
        _l_(341520)
        
        badVel = _a_(341525, _a_(341524, _a_(341522, _n_(341521, "packet", lambda: packet), "game_cars")[_n_(341523, "badIndex", lambda: badIndex)], "physics"), "velocity")
        _l_(341526)
        badVelX = _c_(341530, _n_(341527, "str", lambda: str), _a_(341529, _n_(341528, "badVel", lambda: badVel), "x"))
        _l_(341531)
        badVelY = _c_(341535, _n_(341532, "str", lambda: str), _a_(341534, _n_(341533, "badVel", lambda: badVel), "y"))
        _l_(341536)
        badVelZ = _c_(341540, _n_(341537, "str", lambda: str), _a_(341539, _n_(341538, "badVel", lambda: badVel), "z"))
        _l_(341541)
        
        badAngVel = _a_(341546, _a_(341545, _a_(341543, _n_(341542, "packet", lambda: packet), "game_cars")[_n_(341544, "badIndex", lambda: badIndex)], "physics"), "angular_velocity")
        _l_(341547)
        badAngVelX = _c_(341551, _n_(341548, "str", lambda: str), _a_(341550, _n_(341549, "badAngVel", lambda: badAngVel), "x"))
        _l_(341552)
        badAngVelY = _c_(341556, _n_(341553, "str", lambda: str), _a_(341555, _n_(341554, "badAngVel", lambda: badAngVel), "y"))
        _l_(341557)
        badAngVelZ = _c_(341561, _n_(341558, "str", lambda: str), _a_(341560, _n_(341559, "badAngVel", lambda: badAngVel), "z"))
        _l_(341562)
        
        badhasWC = _c_(341568, _n_(341563, "str", lambda: str), _a_(341567, _a_(341565, _n_(341564, "packet", lambda: packet), "game_cars")[_n_(341566, "badIndex", lambda: badIndex)], "has_wheel_contact"))
        _l_(341569)
        badisSS = _c_(341575, _n_(341570, "str", lambda: str), _a_(341574, _a_(341572, _n_(341571, "packet", lambda: packet), "game_cars")[_n_(341573, "badIndex", lambda: badIndex)], "is_super_sonic"))
        _l_(341576)
        badjumped = _c_(341582, _n_(341577, "str", lambda: str), _a_(341581, _a_(341579, _n_(341578, "packet", lambda: packet), "game_cars")[_n_(341580, "badIndex", lambda: badIndex)], "jumped"))
        _l_(341583)
        baddJumped = _c_(341589, _n_(341584, "str", lambda: str), _a_(341588, _a_(341586, _n_(341585, "packet", lambda: packet), "game_cars")[_n_(341587, "badIndex", lambda: badIndex)], "double_jumped"))
        _l_(341590)
        badbst = _c_(341596, _n_(341591, "str", lambda: str), _a_(341595, _a_(341593, _n_(341592, "packet", lambda: packet), "game_cars")[_n_(341594, "badIndex", lambda: badIndex)], "boost"))       
        _l_(341597)       

        _c_(341619, _a_(341600, _a_(341599, _n_(341598, "self", lambda: self), "writeFile"), "write"), _n_(341601, "badTeam", lambda: badTeam)+";"+
            _n_(341602, "badLocX", lambda: badLocX)+","+_n_(341603, "badLocY", lambda: badLocY)+","+_n_(341604, "badLocZ", lambda: badLocZ)+";"+
            _n_(341605, "badRotP", lambda: badRotP)+","+_n_(341606, "badRotY", lambda: badRotY)+","+_n_(341607, "badRotR", lambda: badRotR)+";"+
            _n_(341608, "badVelX", lambda: badVelX)+","+_n_(341609, "badVelY", lambda: badVelY)+","+_n_(341610, "badVelZ", lambda: badVelZ)+";"+
            _n_(341611, "badAngVelX", lambda: badAngVelX)+","+_n_(341612, "badAngVelY", lambda: badAngVelY)+","+_n_(341613, "badAngVelZ", lambda: badAngVelZ)+";"+
            _n_(341614, "badhasWC", lambda: badhasWC)+";"+_n_(341615, "badisSS", lambda: badisSS)+";"+_n_(341616, "badjumped", lambda: badjumped)+";"+_n_(341617, "baddJumped", lambda: baddJumped)+";"+_n_(341618, "badbst", lambda: badbst))
        _l_(341620)
        _c_(341624, _a_(341623, _a_(341622, _n_(341621, "self", lambda: self), "writeFile"), "write"), "\n")
        _l_(341625)
        
        
        ## WRITE ACTION
        _c_(341658, _a_(341628, _a_(341627, _n_(341626, "self", lambda: self), "writeFile"), "write"), _c_(341632, _n_(341629, "str", lambda: str), _a_(341631, _n_(341630, "action", lambda: action), "throttle"))+";"+_c_(341636, _n_(341633, "str", lambda: str), _a_(341635, _n_(341634, "action", lambda: action), "steer"))+";"+_c_(341640, _n_(341637, "str", lambda: str), _a_(341639, _n_(341638, "action", lambda: action), "pitch"))+";"+_c_(341644, _n_(341641, "str", lambda: str), _a_(341643, _n_(341642, "action", lambda: action), "yaw"))+";"+_c_(341649, _n_(341645, "str", lambda: str), _a_(341648, _a_(341647, _n_(341646, "action", lambda: action), "action"), "roll"))+";"+_c_(341653, _n_(341650, "str", lambda: str), _a_(341652, _n_(341651, "action", lambda: action), "jump"))+";"+_c_(341657, _n_(341654, "str", lambda: str), _a_(341656, _n_(341655, "action", lambda: action), "boost")))
        _l_(341659)
        _c_(341663, _a_(341662, _a_(341661, _n_(341660, "self", lambda: self), "writeFile"), "write"), "\n")
        _l_(341664)
        aux = _n_(341665, "action", lambda: action)
        _l_(341666)
        ##*****************************************************

        return aux