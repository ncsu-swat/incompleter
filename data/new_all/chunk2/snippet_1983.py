# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73376735/python-telebot-issue-typeerror-telebot-send-message-missing-1-required-posit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import telebot;
    _l_(474595)

except ImportError:
    pass

bot = _c_(474598, _a_(474597, _n_(474596, "telebot", lambda: telebot), "TeleBot"), '*there was my Telegram bot token*');
_l_(474599)

name = '';
_l_(474600)
surname = '';
_l_(474601)
age = 0;
_l_(474602)

@_c_(474605, _a_(474604, _n_(474603, "bot", lambda: bot), "message_handler"), commands=['start'])
def start_message(message):
    _l_(474613)

    _c_(474611, _a_(474607, _n_(474606, "bot", lambda: bot), "send_message"), _a_(474610, _a_(474609, _n_(474608, "message", lambda: message), "chat"), "id"),"Hi! I'm another bot for practicing skill :)")
    _l_(474612)

@_c_(474616, _a_(474615, _n_(474614, "bot", lambda: bot), "message_handler"), content_types=['text'])
def get_text_messages(message):
    _l_(474660)

    if _a_(474618, _n_(474617, "message", lambda: message), "text") == "hi":
        _l_(474659)

        _c_(474624, _a_(474620, _n_(474619, "bot", lambda: bot), "send_message"), _a_(474623, _a_(474622, _n_(474621, "message", lambda: message), "from_user"), "id"), "How can I help you?")
        _l_(474625)
    elif _a_(474627, _n_(474626, "message", lambda: message), "text") == "/help":
        _l_(474658)

        _c_(474633, _a_(474629, _n_(474628, "bot", lambda: bot), "send_message"), _a_(474632, _a_(474631, _n_(474630, "message", lambda: message), "from_user"), "id"), "Registration - /reg")
        _l_(474634)
    elif _a_(474636, _n_(474635, "message", lambda: message), "text") == '/reg':
        _l_(474657)

        _c_(474642, _a_(474638, _n_(474637, "bot", lambda: bot), "send_message"), _a_(474641, _a_(474640, _n_(474639, "message", lambda: message), "from_user"), "id"), "Nice! Lets sign you up! What is your name?");
        _l_(474643)
        _c_(474648, _a_(474645, _n_(474644, "bot", lambda: bot), "register_next_step_handler"), _n_(474646, "message", lambda: message), _n_(474647, "get_name", lambda: get_name));
        _l_(474649)
    else:
        _c_(474655, _a_(474651, _n_(474650, "bot", lambda: bot), "send_message"), _a_(474654, _a_(474653, _n_(474652, "message", lambda: message), "from_user"), "id"), "Sorry, I don't understand that. Write /help")
        _l_(474656)
def get_name(message):
    _l_(474678)

    global name;
    _l_(474661)
    name = _a_(474663, _n_(474662, "message", lambda: message), "text");
    _l_(474664)
    _c_(474670, _a_(474666, _n_(474665, "bot", lambda: bot), "send_message"), _a_(474669, _a_(474668, _n_(474667, "message", lambda: message), "from_user"), "id"), 'Okay! What is your surname?');
    _l_(474671)
    _c_(474676, _a_(474673, _n_(474672, "bot", lambda: bot), "register_next_step_handler"), _n_(474674, "message", lambda: message), _n_(474675, "get_surname", lambda: get_surname));
    _l_(474677)
def get_surname(message):
    _l_(474693)

    global surname;
    _l_(474679)
    surname = _a_(474681, _n_(474680, "message", lambda: message), "text");
    _l_(474682)
    _c_(474685, _a_(474684, _n_(474683, "bot", lambda: bot), "send_message"), 'What is your age?');
    _l_(474686)
    _c_(474691, _a_(474688, _n_(474687, "bot", lambda: bot), "register_next_step_handler"), _n_(474689, "message", lambda: message), _n_(474690, "get_age", lambda: get_age));
    _l_(474692)
def get_age(message):
    _l_(474724)

    global age;
    _l_(474694)
    while _n_(474695, "age", lambda: age) == 0:
        _l_(474711)

        try:
            _l_(474710)

            age = _c_(474699, _n_(474696, "int", lambda: int), _a_(474698, _n_(474697, "message", lambda: message), "text"))
            _l_(474700)
        except _n_(474701, "Exception", lambda: Exception):
            _l_(474709)

            _c_(474707, _a_(474703, _n_(474702, "bot", lambda: bot), "send_message"), _a_(474706, _a_(474705, _n_(474704, "message", lambda: message), "from_user"), "id"), 'Oops! I need only number.');
            _l_(474708)
    _c_(474722, _a_(474713, _n_(474712, "bot", lambda: bot), "send_message"), _a_(474716, _a_(474715, _n_(474714, "message", lambda: message), "from_user"), "id"), 'You are '+_c_(474719, _n_(474717, "str", lambda: str), _n_(474718, "age", lambda: age))+'yo, your full name is '+_n_(474720, "name", lambda: name)+' '+_n_(474721, "surname", lambda: surname)+'?')        
    _l_(474723)        

_c_(474727, _a_(474726, _n_(474725, "bot", lambda: bot), "delete_webhook"))
_l_(474728)
_c_(474731, _a_(474730, _n_(474729, "bot", lambda: bot), "infinity_polling"))
_l_(474732)