# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69499013/line-8-in-speak-voiceengine-getpropertyrate-100-typeerror-getproperty-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3
    _l_(627267)

except ImportError:
    pass

# This function is used to process text and speak it out
def speak (lis):
    _l_(627288)

    voiceEngine = _c_(627270, _a_(627269, _n_(627268, "pyttsx3", lambda: pyttsx3), "init")) 
    _l_(627271) 
    _c_(627274, _a_(627273, _n_(627272, "voiceEngine", lambda: voiceEngine), "getProperty"), "rate", 100)
    _l_(627275)
    #voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22" 
    #voiceEngine.setProperty('IVONA 2 Brian - British English male voice [22kHz]', voice_id ) 
    _c_(627279, _a_(627277, _n_(627276, "voiceEngine", lambda: voiceEngine), "say"), _n_(627278, "lis", lambda: lis))
    _l_(627280)
    _c_(627283, _a_(627282, _n_(627281, "voiceEngine", lambda: voiceEngine), "runAndWait")) 
    _l_(627284) 
    _a_(627286, _n_(627285, "voiceEngine", lambda: voiceEngine), "stop")
    _l_(627287)


_c_(627290, _n_(627289, "speak", lambda: speak), lis = "Hello i am alpha, your personal digital assistant. how may i be of your assistance")
_l_(627291)