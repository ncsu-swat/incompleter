# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63018269/builtins-attributeerror-bytes-object-has-no-attribute-append-in-python-twis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from twisted.internet.protocol import Factory
    _l_(627978)

except ImportError:
    pass
try:
    from twisted.protocols.basic import LineReceiver
    _l_(627980)

except ImportError:
    pass
try:
    from twisted.internet import reactor
    _l_(627982)

except ImportError:
    pass
try:
    from collections import defaultdict
    _l_(627984)

except ImportError:
    pass


class MultiChatProtocol(_n_(627985, "LineReceiver", lambda: LineReceiver)):
    _l_(628364)

    
    def __init__(self, factory):
        _l_(627993)

        _n_(627986, "self", lambda: self).factory = _n_(627987, "factory", lambda: factory)
        _l_(627988)
        _n_(627989, "self", lambda: self).name = None
        _l_(627990)
        _n_(627991, "self", lambda: self).group_name = None
        _l_(627992)

    def connectionMade(self):
        _l_(628018)

        _c_(627996, _a_(627995, _n_(627994, "self", lambda: self), "sendLine"), b"Welcome to multi char server ")
        _l_(627997)
        _c_(628000, _a_(627999, _n_(627998, "self", lambda: self), "sendLine"), b"") 
        _l_(628001) 
        _c_(628008, _n_(628002, "print", lambda: print), _c_(628007, _n_(628003, "type", lambda: type), _a_(628006, _a_(628005, _n_(628004, "self", lambda: self), "factory"), "users")))
        _l_(628009)
        _c_(628016, _n_(628010, "print", lambda: print), _c_(628015, _n_(628011, "type", lambda: type), _a_(628014, _a_(628013, _n_(628012, "self", lambda: self), "factory"), "groups")))
        _l_(628017)
    def connectionLost(self, reason):
        _l_(628029)

        if _a_(628020, _n_(628019, "self", lambda: self), "name") in _a_(628023, _a_(628022, _n_(628021, "self", lambda: self), "factory"), "users"):
            _l_(628028)

            _c_(628026, _a_(628025, _n_(628024, "self", lambda: self), "broadcastMessage"), b"one member has left the channel.")
            _l_(628027)
    def lineReceived(self, line):
        _l_(628103)

        if _n_(628030, "line", lambda: line) == b'':
            _l_(628036)

            _c_(628033, _a_(628032, _n_(628031, "self", lambda: self), "sendLine"), b"write something or type /help for any")
            _l_(628034)
            aux = ""
            _l_(628035)
            return aux
        _c_(628039, _n_(628037, "print", lambda: print), "line name" , _n_(628038, "line", lambda: line))
        _l_(628040)
        
        a = _c_(628043, _a_(628042, _n_(628041, "line", lambda: line), "split"))
        _l_(628044)
        if _c_(628047, _n_(628045, "len", lambda: len), _n_(628046, "a", lambda: a)) > 1:
            _l_(628102)

            command = _n_(628048, "a", lambda: a)[0]
            _l_(628049)
            content = _n_(628050, "a", lambda: a)[1]
            _l_(628051)
            if _n_(628052, "command", lambda: command) == b"/cuser":
                _l_(628077)

                _c_(628056, _a_(628054, _n_(628053, "self", lambda: self), "save_REGISTER"), _n_(628055, "content", lambda: content))
                _l_(628057)
            elif _n_(628058, "command", lambda: command) == b"/cgroup":
                _l_(628076)

                _c_(628062, _a_(628060, _n_(628059, "self", lambda: self), "create_Group"), _n_(628061, "content", lambda: content))
                _l_(628063)
            elif _n_(628064, "command", lambda: command) == b"/join":
                _l_(628075)

                _c_(628073, _a_(628071, _c_(628070, _a_(628068, _a_(628067, _a_(628066, _n_(628065, "self", lambda: self), "factory"), "groups"), "get"), _n_(628069, "content", lambda: content), []), "append"), _n_(628072, "self", lambda: self))
                _l_(628074)
        elif _n_(628078, "line", lambda: line) == b"/ulist":
            _l_(628101)

            _c_(628081, _a_(628080, _n_(628079, "self", lambda: self), "usercount"))
            _l_(628082)
        elif _n_(628083, "line", lambda: line) == b"/glist":
            _l_(628100)

            _c_(628086, _a_(628085, _n_(628084, "self", lambda: self), "groupcount"))
            _l_(628087)
        elif _n_(628088, "line", lambda: line) == b"/help":
            _l_(628099)

            _c_(628091, _a_(628090, _n_(628089, "self", lambda: self), "handle_menu"))
            _l_(628092)
        elif _n_(628093, "line", lambda: line) == b"/quite":
            _l_(628098)

            _c_(628096, _a_(628095, _n_(628094, "self", lambda: self), "connectionLost"))
            _l_(628097)

    def join_group(self,args):
        _l_(628139)

        _c_(628106, _n_(628104, "print", lambda: print), "args for join",_n_(628105, "args", lambda: args))
        _l_(628107)
        _c_(628111, _n_(628108, "print", lambda: print), "user name for join",_a_(628110, _n_(628109, "self", lambda: self), "name"))
        _l_(628112)
        #for elem in self.factory.groups:
         #   if args == elem:
          #      elf.factory.groups[args].append(self.name)
        
        d = {}
        _l_(628113)
        y = _a_(628115, _n_(628114, "self", lambda: self), "name")
        _l_(628116)
        _c_(628123, _a_(628121, _c_(628120, _a_(628118, _n_(628117, "d", lambda: d), "setdefault"), _n_(628119, "args", lambda: args), []), "append"), _n_(628122, "y", lambda: y))
        _l_(628124)
        _c_(628127, _n_(628125, "print", lambda: print), "groups list of d ", _n_(628126, "d", lambda: d))
        _l_(628128)
        _a_(628130, _n_(628129, "self", lambda: self), "factory").groups = _n_(628131, "d", lambda: d)
        _l_(628132)
        _c_(628137, _n_(628133, "print", lambda: print), "groups list", _a_(628136, _a_(628135, _n_(628134, "self", lambda: self), "factory"), "groups"))
        _l_(628138)
    

    def save_REGISTER(self,name):
        _l_(628176)

        if _n_(628140, "name", lambda: name) in _a_(628143, _a_(628142, _n_(628141, "self", lambda: self), "factory"), "users"):
            _l_(628150)

            _c_(628147, _a_(628146, _a_(628145, _n_(628144, "self", lambda: self), "transport"), "write"), b"Name taken, please choose another.")
            _l_(628148)
            aux = ""
            _l_(628149)
            return aux
        _c_(628154, _a_(628152, _n_(628151, "self", lambda: self), "sendLine"), b"Welcome, %s!" % (_n_(628153, "name", lambda: name),))
        _l_(628155)
        _c_(628159, _a_(628157, _n_(628156, "self", lambda: self), "broadcastMessage"), b"%s has joined the channel." % (_n_(628158, "name", lambda: name),))
        _l_(628160)
        _n_(628161, "self", lambda: self).name = _n_(628162, "name", lambda: name)
        _l_(628163)
        _a_(628166, _a_(628165, _n_(628164, "self", lambda: self), "factory"), "users")[_n_(628167, "name", lambda: name)] = _n_(628168, "self", lambda: self)
        _l_(628169)
        _c_(628174, _n_(628170, "print", lambda: print), "users list",_a_(628173, _a_(628172, _n_(628171, "self", lambda: self), "factory"), "users"))
        _l_(628175)
       
    def create_Group(self,name):
        _l_(628186)

        _c_(628179, _a_(628178, _n_(628177, "self", lambda: self), "sendLine"), b"Enter group name? :")
        _l_(628180)
        _c_(628184, _a_(628182, _n_(628181, "self", lambda: self), "save_Group"), _n_(628183, "name", lambda: name))
        _l_(628185)

    def create_Group(self,name):
        _l_(628237)

        _c_(628189, _n_(628187, "print", lambda: print), "group_name", _n_(628188, "name", lambda: name))
        _l_(628190)
        _c_(628194, _n_(628191, "print", lambda: print), _a_(628193, _n_(628192, "self", lambda: self), "name"))
        _l_(628195)
        if _n_(628196, "name", lambda: name) in _a_(628199, _a_(628198, _n_(628197, "self", lambda: self), "factory"), "groups"):
            _l_(628206)

            _c_(628203, _a_(628202, _a_(628201, _n_(628200, "self", lambda: self), "transport"), "write"), b"Name taken, please choose another.")
            _l_(628204)
            aux = ""
            _l_(628205)
            return aux
        if _a_(628208, _n_(628207, "self", lambda: self), "name") in _a_(628211, _a_(628210, _n_(628209, "self", lambda: self), "factory"), "users"):
            _l_(628236)

            _c_(628215, _a_(628213, _n_(628212, "self", lambda: self), "sendLine"), b"%s group created successfully" % (_n_(628214, "name", lambda: name),))
            _l_(628216)
            _n_(628217, "self", lambda: self).group_name = _n_(628218, "name", lambda: name)
            _l_(628219)
            _a_(628222, _a_(628221, _n_(628220, "self", lambda: self), "factory"), "groups")[_n_(628223, "name", lambda: name)] = _n_(628224, "self", lambda: self)
            _l_(628225)
            #self.factory.groups[name] = self.name
            _c_(628230, _n_(628226, "print", lambda: print), "groups list",  _a_(628229, _a_(628228, _n_(628227, "self", lambda: self), "factory"), "groups"))
            _l_(628231)
        else:
            _c_(628234, _a_(628233, _n_(628232, "self", lambda: self), "sendLine"), b"you are not register with system sorry")
            _l_(628235)
            
  

    def handle_menu(self):
        _l_(628266)

        _c_(628240, _a_(628239, _n_(628238, "self", lambda: self), "sendLine"), b"")
        _l_(628241)
        _c_(628244, _a_(628243, _n_(628242, "self", lambda: self), "sendLine"), b" please select Following MENU command:")
        _l_(628245)
        _c_(628248, _a_(628247, _n_(628246, "self", lambda: self), "sendLine"), b"1) For register your name type : /cuser yourname")
        _l_(628249)
        _c_(628252, _a_(628251, _n_(628250, "self", lambda: self), "sendLine"), b"2) For create group type : /cgroup groupname")
        _l_(628253)
        _c_(628256, _a_(628255, _n_(628254, "self", lambda: self), "sendLine"), b"3) For Joined group type : /join groupname")
        _l_(628257)
        _c_(628260, _a_(628259, _n_(628258, "self", lambda: self), "sendLine"), b"4) For see list Of group type : /glist")
        _l_(628261)
        _c_(628264, _a_(628263, _n_(628262, "self", lambda: self), "sendLine"), b"5) For exit type : /quite")
        _l_(628265)

    def handle_CHAT(self, message):
        _l_(628276)

        message = b"<%s> %s" % (_a_(628268, _n_(628267, "self", lambda: self), "name"),_n_(628269, "message", lambda: message))
        _l_(628270)
        _c_(628274, _a_(628272, _n_(628271, "self", lambda: self), "broadcastMessage"), _n_(628273, "message", lambda: message))
        _l_(628275)

    def broadcastMessage(self, message):
        _l_(628291)

        for name, protocol in _c_(628281, _a_(628280, _a_(628279, _a_(628278, _n_(628277, "self", lambda: self), "factory"), "users"), "items")):
            _l_(628290)

            if _n_(628282, "protocol", lambda: protocol) != _n_(628283, "self", lambda: self):
                _l_(628289)

                _c_(628287, _a_(628285, _n_(628284, "protocol", lambda: protocol), "sendLine"), _n_(628286, "message", lambda: message))
                _l_(628288)

    def usercount(self):
        _l_(628325)


        user_count = _c_(628296, _n_(628292, "len", lambda: len), _a_(628295, _a_(628294, _n_(628293, "self", lambda: self), "factory"), "users"))                                               
        _l_(628297)                                               
        single_or_plural = b'is' if _n_(628298, "user_count", lambda: user_count) == 1 else b'are'                                                    
        _l_(628299)                                                    
        person_or_people = b'person' if _n_(628300, "user_count", lambda: user_count) == 1 else b'people'                                             
        _l_(628301)                                             
        _c_(628307, _a_(628303, _n_(628302, "self", lambda: self), "sendLine"), b"There %s %i  %s connected:" % (_n_(628304, "single_or_plural", lambda: single_or_plural), _n_(628305, "user_count", lambda: user_count), _n_(628306, "person_or_people", lambda: person_or_people), ) )                    
        _l_(628308)                    

        for client in _a_(628311, _a_(628310, _n_(628309, "self", lambda: self), "factory"), "users"):
            _l_(628320)

            if _n_(628312, "client", lambda: client) is not _n_(628313, "self", lambda: self):
                _l_(628319)

                _c_(628317, _a_(628315, _n_(628314, "self", lambda: self), "sendLine"), _n_(628316, "client", lambda: client))                                               
                _l_(628318)                                               
        _c_(628323, _a_(628322, _n_(628321, "self", lambda: self), "sendLine"), b"")
        _l_(628324)

    def groupcount(self):
        _l_(628363)

        group_count = _c_(628330, _n_(628326, "len", lambda: len), _a_(628329, _a_(628328, _n_(628327, "self", lambda: self), "factory"), "groups"))                                               
        _l_(628331)                                               
        single_or_plural = b'is' if _n_(628332, "group_count", lambda: group_count) == 1 else b'are'                                                    
        _l_(628333)                                                    
        person_or_people = b'group' if _n_(628334, "group_count", lambda: group_count) == 1 else b'groups'                                             
        _l_(628335)                                             
        _c_(628341, _a_(628337, _n_(628336, "self", lambda: self), "sendLine"), b"There %s  %i following %s we have :" % (_n_(628338, "single_or_plural", lambda: single_or_plural), _n_(628339, "group_count", lambda: group_count), _n_(628340, "person_or_people", lambda: person_or_people), ) )                    
        _l_(628342)                    

        for group in _a_(628345, _a_(628344, _n_(628343, "self", lambda: self), "factory"), "groups"):
            _l_(628354)

            if _n_(628346, "group", lambda: group) is not _n_(628347, "self", lambda: self):
                _l_(628353)

                _c_(628351, _a_(628349, _n_(628348, "self", lambda: self), "sendLine"), _n_(628350, "group", lambda: group))                                               
                _l_(628352)                                               
        _c_(628357, _a_(628356, _n_(628355, "self", lambda: self), "sendLine"), b"")
        _l_(628358)
        _c_(628361, _a_(628360, _n_(628359, "self", lambda: self), "sendLine"), b"joined above groups by command /join groupname")
        _l_(628362)

class ChatFactory(_n_(628365, "Factory", lambda: Factory)):
    _l_(628376)

    def __init__(self):
        _l_(628370)

        _n_(628366, "self", lambda: self).users = {}
        _l_(628367)
        _n_(628368, "self", lambda: self).groups = {}
        _l_(628369)
    def buildProtocol(self, addr):
        _l_(628375)

        aux = _c_(628373, _n_(628371, "MultiChatProtocol", lambda: MultiChatProtocol), _n_(628372, "self", lambda: self))
        _l_(628374)
        return aux
_c_(628381, _a_(628378, _n_(628377, "reactor", lambda: reactor), "listenTCP"), 8000, _c_(628380, _n_(628379, "ChatFactory", lambda: ChatFactory)))
_l_(628382)
_c_(628384, _n_(628383, "print", lambda: print), "Chat Server Started") 
_l_(628385) 
_c_(628388, _a_(628387, _n_(628386, "reactor", lambda: reactor), "run"))
_l_(628389)