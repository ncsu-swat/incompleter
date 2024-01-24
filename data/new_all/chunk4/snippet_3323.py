# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75050989/python-pyqt5-attributeerror-type-object-qwidget-has-no-attribute-radiobutton
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(610515)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import *
    _l_(610517)

except ImportError:
    pass
try:
    from PyQt5 import uic
    _l_(610519)

except ImportError:
    pass
try:
    from PyQt5.QtGui import QColor
    _l_(610521)

except ImportError:
    pass
try:
    import requests
    _l_(610523)

except ImportError:
    pass
try:
    from random import randint as r
    _l_(610525)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(610527)

except ImportError:
    pass

class settings(_n_(610528, "QWidget", lambda: QWidget)):
    _l_(610621)

    global stngs
    _l_(610529)
    def __init__(self):
        _l_(610578)

        _c_(610534, _a_(610533, _n_(610530, "super", lambda: super)(_n_(610531, "settings", lambda: settings), _n_(610532, "self", lambda: self)), "__init__"))
        _l_(610535)
        _c_(610539, _a_(610537, _n_(610536, "uic", lambda: uic), "loadUi"), "SettingsUI.ui", _n_(610538, "self", lambda: self))
        _l_(610540)
        _c_(610543, _a_(610542, _n_(610541, "self", lambda: self), "show"))
        _l_(610544)
        _c_(610551, _a_(610548, _a_(610547, _a_(610546, _n_(610545, "self", lambda: self), "radioButton"), "clicked"), "connect"), _a_(610550, _n_(610549, "self", lambda: self), "check"))
        _l_(610552)
        _c_(610559, _a_(610556, _a_(610555, _a_(610554, _n_(610553, "self", lambda: self), "radioButton_2"), "clicked"), "connect"), _a_(610558, _n_(610557, "self", lambda: self), "check"))
        _l_(610560)
        _c_(610567, _a_(610564, _a_(610563, _a_(610562, _n_(610561, "self", lambda: self), "pushButton_2"), "clicked"), "connect"), _a_(610566, _n_(610565, "self", lambda: self), "gotomain"))
        _l_(610568)
        _c_(610576, _a_(610572, _a_(610571, _a_(610570, _n_(610569, "self", lambda: self), "fontsizeslider"), "valueChanged"), "connect"), _a_(610575, _a_(610574, _n_(610573, "self", lambda: self), "lcdNumber"), "display"))
        _l_(610577)

    def gotomain(self):
        _l_(610587)

        global stngs
        _l_(610579)
        global mn
        _l_(610580)
        stngs = 0
        _l_(610581)
        mn = 1
        _l_(610582)
        _c_(610585, _a_(610584, _n_(610583, "self", lambda: self), "close"))
        _l_(610586)
    
    def check(self):
        _l_(610620)

        global white
        _l_(610588)
        global black
        _l_(610589)
        try:
            _l_(610596)

            _n_(610590, "black", lambda: black)
            _l_(610591)
        except _n_(610592, "Exception", lambda: Exception):
            _l_(610595)

            white = 1
            _l_(610593)
            black = 0
            _l_(610594)
        if _n_(610597, "black", lambda: black) == 1:
            _l_(610603)

            _c_(610601, _a_(610600, _a_(610599, _n_(610598, "self", lambda: self), "radioButton_2"), "nextCheckState"))
            _l_(610602)
        if _c_(610607, _a_(610606, _a_(610605, _n_(610604, "self", lambda: self), "radioButton"), "isChecked")):
            _l_(610619)

            white = 1
            _l_(610608)
            black = 0
            _l_(610609)
            aux = ("white")
            _l_(610610)
            return aux
        elif _c_(610614, _a_(610613, _a_(610612, _n_(610611, "self", lambda: self), "radioButton_2"), "isChecked")):
            _l_(610618)

            black = 1
            _l_(610615)
            white = 0
            _l_(610616)
            aux = ("black")
            _l_(610617)
            return aux

class MyGUI(_n_(610622, "QMainWindow", lambda: QMainWindow)):
    _l_(610991)


    def __init__(self):
        _l_(610665)

        global black
        _l_(610623)
        global white
        _l_(610624)
        global stngs
        _l_(610625)
        stngs = 0
        _l_(610626)
        _c_(610631, _a_(610630, _n_(610627, "super", lambda: super)(_n_(610628, "MyGUI", lambda: MyGUI), _n_(610629, "self", lambda: self)), "__init__"))
        _l_(610632)
        _c_(610636, _a_(610634, _n_(610633, "uic", lambda: uic), "loadUi"), "ChatbotUI.ui", _n_(610635, "self", lambda: self))
        _l_(610637)
        _c_(610640, _a_(610639, _n_(610638, "self", lambda: self), "show"))
        _l_(610641)

        _c_(610648, _a_(610645, _a_(610644, _a_(610643, _n_(610642, "self", lambda: self), "pushButton"), "clicked"), "connect"), _a_(610647, _n_(610646, "self", lambda: self), "pressenter"))
        _l_(610649)
        _c_(610655, _a_(610653, _a_(610652, _a_(610651, _n_(610650, "self", lambda: self), "actionClose"), "triggered"), "connect"), _n_(610654, "exit", lambda: exit))
        _l_(610656)
        _c_(610663, _a_(610660, _a_(610659, _a_(610658, _n_(610657, "self", lambda: self), "actionSettings1"), "triggered"), "connect"), _a_(610662, _n_(610661, "self", lambda: self), "gotosettings"))
        _l_(610664)
    def gotosettings(self):
        _l_(610672)

        global stngs
        _l_(610666)
        stngs = 1
        _l_(610667)
        _c_(610670, _a_(610669, _n_(610668, "self", lambda: self), "close"))
        _l_(610671)

    def checkcolour():
        _l_(610689)

        check = _c_(610676, _a_(610674, _n_(610673, "settings", lambda: settings), "check"), _n_(610675, "settings", lambda: settings))
        _l_(610677)
        if _n_(610678, "check", lambda: check) == "white":
            _l_(610688)

            _c_(610680, _n_(610679, "white", lambda: white))
            _l_(610681)
        elif _n_(610682, "check", lambda: check) == "black":
            _l_(610687)

            _c_(610684, _n_(610683, "black", lambda: black))
            _l_(610685)
        else:
            raise ("Something wrong with background colour changing algorithm")
            _l_(610686)

    _c_(610690, checkcolour)
    _l_(610691)

    def black(self):
        _l_(610718)

        _c_(610694, _a_(610693, _n_(610692, "self", lambda: self), "setStyleSheet"), "background-color: black;")
        _l_(610695)
        _c_(610699, _a_(610698, _a_(610697, _n_(610696, "self", lambda: self), "pushButton"), "setStyleSheet"), "background-color : white;")
        _l_(610700)
        _c_(610704, _a_(610703, _a_(610702, _n_(610701, "self", lambda: self), "lineEdit"), "setStyleSheet"), "color: white;")
        _l_(610705)
        _c_(610709, _a_(610708, _a_(610707, _n_(610706, "self", lambda: self), "menubar"), "setStyleSheet"), "color: white;")
        _l_(610710)
        _c_(610716, _a_(610713, _a_(610712, _n_(610711, "self", lambda: self), "textBrowser"), "setTextColor"), _c_(610715, _n_(610714, "QColor", lambda: QColor), 255, 255, 255))
        _l_(610717)
    def white(self):
        _l_(610745)

        _c_(610721, _a_(610720, _n_(610719, "self", lambda: self), "setStyleSheet"), "background-color: white;")
        _l_(610722)
        _c_(610726, _a_(610725, _a_(610724, _n_(610723, "self", lambda: self), "pushButton"), "setStyleSheet"), "background-color : white;")
        _l_(610727)
        _c_(610731, _a_(610730, _a_(610729, _n_(610728, "self", lambda: self), "lineEdit"), "setStyleSheet"), "color: black;")
        _l_(610732)
        _c_(610736, _a_(610735, _a_(610734, _n_(610733, "self", lambda: self), "menubar"), "setStyleSheet"), "color: black;")
        _l_(610737)
        _c_(610743, _a_(610740, _a_(610739, _n_(610738, "self", lambda: self), "textBrowser"), "setTextColor"), _c_(610742, _n_(610741, "QColor", lambda: QColor), 0, 0, 0))
        _l_(610744)

    def pressenter(self):
        _l_(610762)

        userinput = _c_(610749, _a_(610748, _a_(610747, _n_(610746, "self", lambda: self), "lineEdit"), "text"))
        _l_(610750)
        response = _c_(610754, _a_(610752, _n_(610751, "self", lambda: self), "get_response"), _n_(610753, "userinput", lambda: userinput))
        _l_(610755)
        _c_(610760, _a_(610758, _a_(610757, _n_(610756, "self", lambda: self), "textBrowser"), "setText"), _n_(610759, "response", lambda: response))
        _l_(610761)

    def get_response(self, userinput):
        _l_(610990)

        global ait_ball_ans
        _l_(610763)
        ait_ball_ans = [
            "Yes",
            "No",
            "Question unclear, ask later",
            "Maybe",
            "Obviously not",
            "Of course"
        ]
        _l_(610764)

        #getting ip adress of user
        def get_ip():
            _l_(610773)

            response = _c_(610769, _a_(610768, _c_(610767, _a_(610766, _n_(610765, "requests", lambda: requests), "get"), 'https://api64.ipify.org?format=json'), "json"))
            _l_(610770)
            aux = _n_(610771, "response", lambda: response)["ip"]
            _l_(610772)
            return aux

        #getting location info of user
        ip_address = _c_(610775, _n_(610774, "get_ip", lambda: get_ip))
        _l_(610776)
        response = _c_(610782, _a_(610781, _c_(610780, _a_(610778, _n_(610777, "requests", lambda: requests), "get"), f'https://ipapi.co/{_n_(610779, "ip_address", lambda: ip_address)}/json/'), 'json'))
        _l_(610783)
            
        #weather api key and location info
        api_key = '14aaded169c4d6e2a5a2547d126b3f70'
        _l_(610784)
        city = _c_(610787, _a_(610786, _n_(610785, 'response', lambda: response), 'get'), "city") + ", " + _c_(610790, _a_(610789, _n_(610788, 'response', lambda: response), 'get'), "country_code")
        _l_(610791)
        qsi = _n_(610792, 'userinput', lambda: userinput)
        _l_(610793)
        qs = _c_(610798, _a_(610797, _c_(610796, _a_(610795, _n_(610794, 'qsi', lambda: qsi), 'lower')), 'split'))
        _l_(610799)
        length = _c_(610802, _n_(610800, 'len', lambda: len), _n_(610801, 'qs', lambda: qs))
        _l_(610803)

        if "what" in _n_(610804, 'qs', lambda: qs) and ("name" in _n_(610805, 'qs', lambda: qs) or "name?" in _n_(610806, 'qs', lambda: qs)) and ("your" in _n_(610807, 'qs', lambda: qs) or "ur" in _n_(610808, 'qs', lambda: qs)) and (_n_(610809, 'length', lambda: length) == 3 or _n_(610810, 'length', lambda: length) == 4):
            _l_(610987)

            _c_(610812, _n_(610811, 'print', lambda: print), "My name is chatbot, and I am a language model trained by Zayan Arshad.")
            _l_(610813)
            text = "My name is chatbot, and I am a language model trained by Zayan Arshad."
            _l_(610814)
        elif ("chatbot" in _n_(610815, 'qs', lambda: qs) or "chatbot?" in _n_(610816, 'qs', lambda: qs)) and ("you" in _n_(610817, 'qs', lambda: qs) and "are" in _n_(610818, 'qs', lambda: qs)):
            _l_(610986)

            _c_(610820, _n_(610819, 'print', lambda: print), "Yes, my name is chatbot, a language model trained by Zayan Arshad.")
            _l_(610821)
            text = "Yes, my name is chatbot, a language model trained by Zayan Arshad."
            _l_(610822)
        elif "is" in _n_(610823, 'qs', lambda: qs) and _n_(610824, 'length', lambda: length) == 4 and "chatbot" not in _n_(610825, 'qs', lambda: qs) and "name" in _n_(610826, 'qs', lambda: qs):
            _l_(610985)

            _c_(610828, _n_(610827, 'print', lambda: print), "My name is chatbot, and I am a language model trained by Zayan Arshad.")
            _l_(610829)
            text = "My name is chatbot, and I am a language model trained by Zayan Arshad."
            _l_(610830)
        elif "should" and "you" and "what" and "call" in _n_(610831, 'qs', lambda: qs):
            _l_(610984)

            _c_(610833, _n_(610832, 'print', lambda: print), "My name is chatbot, and I am a language model trained by Zayan Arshad.")
            _l_(610834)
            text = "My name is chatbot, and I am a language model trained by Zayan Arshad."
            _l_(610835)
        elif ("hello" in _n_(610836, 'qs', lambda: qs) or "hi" in _n_(610837, 'qs', lambda: qs)) or ("good" and "evening") in _n_(610838, 'qs', lambda: qs) or ("good" and "morning") in _n_(610839, 'qs', lambda: qs) or ("good" and "afternoon") in _n_(610840, 'qs', lambda: qs):
            _l_(610983)

            _c_(610842, _n_(610841, 'print', lambda: print), "Hello! Is there any way I can help you?")
            _l_(610843)
            text = "Hello! Is there any way I can help you?"
            _l_(610844)
        elif ("weather" in _n_(610845, 'qs', lambda: qs) or "weather?" in _n_(610846, 'qs', lambda: qs)) and ("what" in _n_(610847, 'qs', lambda: qs) or "pls" in _n_(610848, 'qs', lambda: qs) or "tell" in _n_(610849, 'qs', lambda: qs) or "what's" in _n_(610850, 'qs', lambda: qs) or "whats" in _n_(610851, 'qs', lambda: qs)):
            _l_(610982)

            url = f'http://api.openweathermap.org/data/2.5/weather?q={_n_(610852, "city", lambda: city)}&appid={_n_(610853, "api_key", lambda: api_key)}'
            _l_(610854)
            response = _c_(610858, _a_(610856, _n_(610855, 'requests', lambda: requests), 'get'), _n_(610857, 'url', lambda: url))
            _l_(610859)
            data = _c_(610862, _a_(610861, _n_(610860, 'response', lambda: response), 'json'))
            _l_(610863)
            conditions = _n_(610864, 'data', lambda: data)['weather'][0]['main']
            _l_(610865)
            temperature = _n_(610866, 'data', lambda: data)['main']['temp']
            _l_(610867)
            temperature_celsius = _n_(610868, 'temperature', lambda: temperature) - 273.15
            _l_(610869)
            _c_(610875, _n_(610870, 'print', lambda: print), "The weather condition is " + _n_(610871, 'conditions', lambda: conditions) + " and the temprature is " + _c_(610874, _n_(610872, 'str', lambda: str), _n_(610873, 'temperature_celsius', lambda: temperature_celsius)) + " in celcius.")
            _l_(610876)
            text = "The weather condition is " + _n_(610877, 'conditions', lambda: conditions) + " and the temprature is " + _c_(610880, _n_(610878, 'str', lambda: str), _n_(610879, 'temperature_celsius', lambda: temperature_celsius)) + " in celcius."
            _l_(610881)
        elif ("time" in _n_(610882, 'qs', lambda: qs) or "time?" in _n_(610883, 'qs', lambda: qs)) and ("what" in _n_(610884, 'qs', lambda: qs) or "pls" in _n_(610885, 'qs', lambda: qs) or "tell" in _n_(610886, 'qs', lambda: qs) or "what's" in _n_(610887, 'qs', lambda: qs) or "whats" in _n_(610888, 'qs', lambda: qs)):
            _l_(610981)

            _c_(610897, _n_(610889, 'print', lambda: print), "The time is " + _c_(610896, _n_(610890, 'str', lambda: str), _c_(610895, _a_(610894, _c_(610893, _a_(610892, _n_(610891, 'datetime', lambda: datetime), 'now')), 'time'))))
            _l_(610898)
            text = "The time is " + _c_(610905, _n_(610899, 'str', lambda: str), _c_(610904, _a_(610903, _c_(610902, _a_(610901, _n_(610900, 'datetime', lambda: datetime), 'now')), 'time')))
            _l_(610906)
        elif ("give" in _n_(610907, 'qs', lambda: qs) or "tell" in _n_(610908, 'qs', lambda: qs)) and ("joke" in _n_(610909, 'qs', lambda: qs) or "joke!" in _n_(610910, 'qs', lambda: qs)):
            _l_(610980)

            response = _c_(610913, _a_(610912, _n_(610911, 'requests', lambda: requests), 'get'), "https://sv443.net/jokeapi/v2/joke/Any")
            _l_(610914)
            data = _c_(610917, _a_(610916, _n_(610915, 'response', lambda: response), 'json'))
            _l_(610918)
            if 'setup' in _n_(610919, 'data', lambda: data):
                _l_(610938)

                setup = _n_(610920, 'data', lambda: data)['setup']
                _l_(610921)
                delivery = _n_(610922, 'data', lambda: data)['delivery']
                _l_(610923)
                _c_(610927, _n_(610924, 'print', lambda: print), _n_(610925, 'setup', lambda: setup) + "\n" + _n_(610926, 'delivery', lambda: delivery))
                _l_(610928)
                text = _n_(610929, 'setup', lambda: setup) + "\n" + _n_(610930, 'delivery', lambda: delivery)
                _l_(610931)
            else:
                joke = _n_(610932, 'data', lambda: data)['joke']
                _l_(610933)
                _c_(610936, _n_(610934, 'print', lambda: print), _n_(610935, 'joke', lambda: joke)) 
                _l_(610937) 
        elif ("give" in _n_(610939, 'qs', lambda: qs) or "tell" in _n_(610940, 'qs', lambda: qs)) and "fact" in _n_(610941, 'qs', lambda: qs):
            _l_(610979)

            response = _c_(610944, _a_(610943, _n_(610942, 'requests', lambda: requests), 'get'), "https://uselessfacts.jsph.pl/random.json?language=en")
            _l_(610945)
            data = _c_(610948, _a_(610947, _n_(610946, 'response', lambda: response), 'json'))
            _l_(610949)
            fact = _n_(610950, 'data', lambda: data)['text']
            _l_(610951)
            _c_(610954, _n_(610952, 'print', lambda: print), "Your random fact is:\n" + _n_(610953, 'fact', lambda: fact))
            _l_(610955)
            text = "Your random fact is:\n" + _n_(610956, 'fact', lambda: fact)
            _l_(610957)
        elif ("8" in _n_(610958, 'qs', lambda: qs) or "eight" in _n_(610959, 'qs', lambda: qs)) and ("ball" in _n_(610960, 'qs', lambda: qs) or "ball," in _n_(610961, 'qs', lambda: qs)):
            _l_(610978)

            ans_num = _c_(610963, _n_(610962, 'r', lambda: r), 1, 5)
            _l_(610964)
            ans = _n_(610965, 'ait_ball_ans', lambda: ait_ball_ans)[_n_(610966, 'ans_num', lambda: ans_num)]
            _l_(610967)
            _c_(610970, _n_(610968, 'print', lambda: print), _n_(610969, 'ans', lambda: ans))
            _l_(610971)
            text = _n_(610972, 'ans', lambda: ans)
            _l_(610973)
        else:
            _c_(610975, _n_(610974, 'print', lambda: print), "I'm sorry, but I am not advanced enough to answer your question or statement, a child has made me and my creator is a beginner to python and he has somehow made me. Feel free to ask me anything else or tell me something.")
            _l_(610976)
            text = "I'm sorry, but I am not advanced enough to answer your question or statement, a child has made me and my creator is a beginner to python and he has somehow made me. Feel free to ask me anything else or tell me something."  
            _l_(610977)  
        aux = _n_(610988, 'text', lambda: text)
        _l_(610989)
        return aux
def main():
    _l_(611007)

    app = _c_(610993, _n_(610992, 'QApplication', lambda: QApplication), [])
    _l_(610994)
    window = _c_(610996, _n_(610995, 'MyGUI', lambda: MyGUI))
    _l_(610997)
    _c_(611000, _a_(610999, _n_(610998, 'app', lambda: app), 'exec_'))
    _l_(611001)

    if _n_(611002, 'stngs', lambda: stngs) == 1:
        _l_(611006)

        _c_(611004, _n_(611003, 'settingsfunc', lambda: settingsfunc))
        _l_(611005)

def settingsfunc():
    _l_(611027)

    _c_(611010, _a_(611009, _n_(611008, 'time', lambda: time), 'sleep'), 1)
    _l_(611011)
    app = _c_(611013, _n_(611012, 'QApplication', lambda: QApplication), [])
    _l_(611014)
    settingswindow = _c_(611016, _n_(611015, 'settings', lambda: settings))
    _l_(611017)
    _c_(611020, _a_(611019, _n_(611018, 'app', lambda: app), 'exec_'))
    _l_(611021)

    if _n_(611022, 'mn', lambda: mn) == 1:
        _l_(611026)

        _c_(611024, _n_(611023, 'main', lambda: main))
        _l_(611025)

if _n_(611028, '__name__', lambda: __name__) == '__main__':
    _l_(611032)

    _c_(611030, _n_(611029, 'main', lambda: main))
    _l_(611031)