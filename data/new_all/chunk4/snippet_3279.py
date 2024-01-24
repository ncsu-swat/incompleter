# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76245831/how-do-i-resolve-error-nameerror-name-stream-is-not-defined-pyaudio-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
global stream
_l_(593189)
stream = None
_l_(593190)


global paused
_l_(593191)
paused = False    # global to track if the audio is skipped
_l_(593192)    # global to track if the audio is skipped
def on_turn(pin):
    _l_(593204)

    global paused
    _l_(593193)
    global stream
    _l_(593194)
    if _n_(593195, "stream", lambda: stream) is not None and _c_(593198, _a_(593197, _n_(593196, "stream", lambda: stream), "is_active")):
        _l_(593203)

        _c_(593200, _n_(593199, "print", lambda: print), 'audio skipped')
        _l_(593201)
        paused = False
        _l_(593202)


_c_(593210, _a_(593206, _n_(593205, "GPIO", lambda: GPIO), "add_event_detect"), 27, _a_(593208, _n_(593207, "GPIO", lambda: GPIO), "BOTH"), callback=_n_(593209, "on_turn", lambda: on_turn), bouncetime=200) #this event is when the dial is turning
_l_(593211) #this event is when the dial is turning

def bigcheck():
    _l_(593243)

    pick_up_state = _c_(593214, _a_(593213, _n_(593212, "GPIO", lambda: GPIO), "input"), 22)
    _l_(593215)
    old_pick_up_state = 1
    _l_(593216)
    if _n_(593217, "pick_up_state", lambda: pick_up_state) != _n_(593218, "old_pick_up_state", lambda: old_pick_up_state):
        _l_(593242)

        if _n_(593219, "pick_up_state", lambda: pick_up_state) == 1:
            _l_(593241)

            _c_(593221, _n_(593220, "print", lambda: print), "handset lifted")
            _l_(593222)
            is_picked_up = True
            _l_(593223)
            old_pick_up_state = 1
            _l_(593224)
        else: #the handset is put down
            _c_(593226, _n_(593225, "print", lambda: print), "handset down")
            _l_(593227)
            is_picked_up = False
            _l_(593228)
            global still_picked_up
            _l_(593229)
            still_picked_up = False
            _l_(593230)
            global has_recorded
            _l_(593231)
            has_recorded = False
            _l_(593232)
            global has_recorded_options
            _l_(593233)
            has_recorded_options = False
            _l_(593234)
            play_menu = True
            _l_(593235)
            old_pick_up_state = 0
            _l_(593236)
            _c_(593238, _n_(593237, "call", lambda: call), ["amixer", "-D", "pulse", "sset", "Master", "100%+"])
            _l_(593239)
            aux = ""
            _l_(593240)
            return aux


c=0 
_l_(593244) 
last = 1
_l_(593245)

def count(pin):
    _l_(593249)

    global c 
    _l_(593246) 
    c = _n_(593247, "c", lambda: c) + 1
    _l_(593248)
#this c and count script is used in translating the dialed number

while True:
    _l_(593297)

    
    pick_up_state = _c_(593252, _a_(593251, _n_(593250, "GPIO", lambda: GPIO), "input"), 22)
    _l_(593253)
    if _n_(593254, "pick_up_state", lambda: pick_up_state) != _n_(593255, "old_pick_up_state", lambda: old_pick_up_state):
        _l_(593274)

        if _n_(593256, "pick_up_state", lambda: pick_up_state) == 1:
            _l_(593273)

            _c_(593258, _n_(593257, "print", lambda: print), "handset lifted")
            _l_(593259)
            is_picked_up = True
            _l_(593260)
            old_pick_up_state = 1
            _l_(593261)
        else: #the handset is put down
            _c_(593263, _n_(593262, "print", lambda: print), "handset down")
            _l_(593264)
            is_picked_up = False
            _l_(593265)
            still_picked_up = False
            _l_(593266)
            has_recorded = False
            _l_(593267)
            play_menu = True
            _l_(593268)
            old_pick_up_state = 0
            _l_(593269)
            _c_(593271, _n_(593270, "call", lambda: call), ["amixer", "-D", "pulse", "sset", "Master", "100%+"])
            _l_(593272)

    if _n_(593275, "is_picked_up", lambda: is_picked_up):
        _l_(593296)

        _c_(593277, _n_(593276, "sleep", lambda: sleep), 1)
        _l_(593278)
        _c_(593280, _n_(593279, "call", lambda: call), ["amixer", "-D", "pulse", "sset", "Master", "100%+"])
        _l_(593281)
        intro = _c_(593284, _a_(593283, _n_(593282, "AudioSegment", lambda: AudioSegment), "from_wav"), "/home/brian/Music/Rotary_Recordings/Intro.wav")
        _l_(593285)
        _c_(593287, _n_(593286, "print", lambda: print), 'playing intro')
        _l_(593288)
        _c_(593291, _n_(593289, "play", lambda: play), _n_(593290, "intro", lambda: intro))
        _l_(593292)
        still_picked_up = True
        _l_(593293)
        is_picked_up = False
        _l_(593294)
        paused = True
        _l_(593295)