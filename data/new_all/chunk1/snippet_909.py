# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43713966/python-3-x-checkbutton-get-value-not-working-getting-an-attributeerror-chec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        from tkinter import *
        _l_(412606)

except ImportError:
        pass
try:
        import subprocess
        _l_(412608)

except ImportError:
        pass
#from tkinter.filedialog import asksaveasfilename

#save file
#saveFile = asksaveasfilename()
#print("You can write data to " + saveFile)

startup = _c_(412610, _n_(412609, "Tk", lambda: Tk))
_l_(412611)

names = ["about","accounts","admin","administrador","administrator","ads","adserver","adsl","agent","blog","channel","client","dmz","dns","dns0","dns1","dns2","dns3","external","file","forum","forums","ftp","ftpserver","host","http",
"https","ids","intern","intranet","irc","linux","log","mail","map","member","members","name","nc","ns","ntp","ntserver","office","pop","pptp","print","printer","pub","public","root","route","router","server","smtp","sql","ssh","telnet",
"voip","webaccess","webadmin","webserver","website","win","windows","www","xml"]
_l_(412612)
nslookup= _c_(412614, _n_(412613, "IntVar", lambda: IntVar))
_l_(412615)

def cmdnslookup():
        _l_(412624)

        domain='microsoft.com'
        _l_(412616)
        process = "dig "+_n_(412617, "domain", lambda: domain)+" ns > NameServerLookup.txt"
        _l_(412618)
        _c_(412622, _a_(412620, _n_(412619, "subprocess", lambda: subprocess), "Popen"), _n_(412621, "process", lambda: process), shell=True)
        _l_(412623)

def cmdmxlookup():
        _l_(412633)

        domain='microsoft.com'
        _l_(412625)
        process = "dig "+_n_(412626, "domain", lambda: domain)+" mx > MailServerLookup.txt"
        _l_(412627)
        _c_(412631, _a_(412629, _n_(412628, "subprocess", lambda: subprocess), "Popen"), _n_(412630, "process", lambda: process), shell=True)
        _l_(412632)

def cmdipForward():
        _l_(412645)

        for name in _n_(412634, "names", lambda: names):
                _l_(412644)

                domain='www.stcloudstate.edu'
                _l_(412635)
                process = "host "+_n_(412636, "name", lambda: name)+"."+_n_(412637, "domain", lambda: domain)+" | grep 'has address' >> ForwardIPLookup.txt"
                _l_(412638)
                _c_(412642, _a_(412640, _n_(412639, "subprocess", lambda: subprocess), "Popen"), _n_(412641, "process", lambda: process), shell=True)
                _l_(412643)


##def cmdipReverse():
##        
##def cmdipAdditional():
##        
##def cmdzoneTransfer():
##        
##def cmdoneSixtyOne():
##        
##def cmdsnmp():
##        
##def cmdrpc():
##        
##def cmdip():
##        


def close():
        _l_(412650)

        _c_(412648, _a_(412647, _n_(412646, "startup", lambda: startup), "destroy"))
        _l_(412649)

def menu():
        _l_(412937)

        _c_(412653, _a_(412652, _n_(412651, "startup", lambda: startup), "title"), "Wilson Recon Tool")
        _l_(412654)

        menubar = _c_(412657, _n_(412655, "Menu", lambda: Menu), _n_(412656, "startup", lambda: startup))
        _l_(412658)
        filemenu = _c_(412661, _n_(412659, "Menu", lambda: Menu), _n_(412660, "menubar", lambda: menubar), tearoff=0)
        _l_(412662)
        _c_(412666, _a_(412664, _n_(412663, "filemenu", lambda: filemenu), "add_command"), label="Close", command=_n_(412665, "close", lambda: close))
        _l_(412667)
        _c_(412671, _a_(412669, _n_(412668, "menubar", lambda: menubar), "add_cascade"), label="file", menu=_n_(412670, "filemenu", lambda: filemenu))
        _l_(412672)
        _c_(412676, _a_(412674, _n_(412673, "startup", lambda: startup), "config"), menu=_n_(412675, "menubar", lambda: menubar))
        _l_(412677)

        topFrame = _c_(412680, _n_(412678, "Frame", lambda: Frame), _n_(412679, "startup", lambda: startup))
        _l_(412681)
        _c_(412684, _a_(412683, _n_(412682, "topFrame", lambda: topFrame), "pack"))
        _l_(412685)

        bottomFrame = _c_(412688, _n_(412686, "Frame", lambda: Frame), _n_(412687, "startup", lambda: startup))
        _l_(412689)
        _c_(412693, _a_(412691, _n_(412690, "bottomFrame", lambda: bottomFrame), "pack"), side=_n_(412692, "BOTTOM", lambda: BOTTOM))
        _l_(412694)

        about = _c_(412700, _a_(412698, _c_(412697, _n_(412695, "Label", lambda: Label), _n_(412696, "topFrame", lambda: topFrame), text="Application Description", font="ariel 10 bold"), "grid"), row=0, column=0, sticky=_n_(412699, "W", lambda: W))
        _l_(412701)
        description = _c_(412703, _n_(412702, "StringVar", lambda: StringVar))
        _l_(412704)
        _c_(412707, _a_(412706, _n_(412705, "description", lambda: description), "set"), "This is a network recon tool. It's designed to help make reconassiance easier for those not familar with terminal based tools." )
        _l_(412708)
        message = _c_(412712, _n_(412709, "Message", lambda: Message), _n_(412710, "topFrame", lambda: topFrame), textvariable=_n_(412711, "description", lambda: description), width=250)
        _l_(412713)
        _c_(412716, _a_(412715, _n_(412714, "message", lambda: message), "grid"), row=1,column=0)
        _l_(412717)


        recon = _c_(412720, _n_(412718, "Label", lambda: Label), _n_(412719, "bottomFrame", lambda: bottomFrame), text="Recon Information", font="ariel 10 bold")
        _l_(412721)
        _c_(412725, _a_(412723, _n_(412722, "recon", lambda: recon), "grid"), row=0,column=0,pady=5,sticky=_n_(412724, "W", lambda: W))
        _l_(412726)
        global nslookup
        _l_(412727)
        nslookup = _c_(412731, _n_(412728, "Checkbutton", lambda: Checkbutton), _n_(412729, "bottomFrame", lambda: bottomFrame), text="Name Server Lookup",variable=_n_(412730, "nslookup", lambda: nslookup))
        _l_(412732)
        _c_(412736, _a_(412734, _n_(412733, "nslookup", lambda: nslookup), "grid"), row=1,column=0,sticky=_n_(412735, "W", lambda: W))
        _l_(412737)
        mxlookup= _c_(412739, _n_(412738, "IntVar", lambda: IntVar))
        _l_(412740)
        mxlookup = _c_(412744, _n_(412741, "Checkbutton", lambda: Checkbutton), _n_(412742, "bottomFrame", lambda: bottomFrame), text="Mail Server Lookup",variable=_n_(412743, "mxlookup", lambda: mxlookup))
        _l_(412745)
        _c_(412749, _a_(412747, _n_(412746, "mxlookup", lambda: mxlookup), "grid"), row=2,column=0,sticky=_n_(412748, "W", lambda: W))
        _l_(412750)
        ipForward= _c_(412752, _n_(412751, "IntVar", lambda: IntVar))
        _l_(412753)
        ipForward = _c_(412757, _n_(412754, "Checkbutton", lambda: Checkbutton), _n_(412755, "bottomFrame", lambda: bottomFrame), text="Forward Domain Lookup",variable=_n_(412756, "ipForward", lambda: ipForward))
        _l_(412758)
        _c_(412762, _a_(412760, _n_(412759, "ipForward", lambda: ipForward), "grid"), row=3,column=0,sticky=_n_(412761, "W", lambda: W))
        _l_(412763)
        ipReverse= _c_(412765, _n_(412764, "IntVar", lambda: IntVar))
        _l_(412766)
        ipReverse = _c_(412770, _n_(412767, "Checkbutton", lambda: Checkbutton), _n_(412768, "bottomFrame", lambda: bottomFrame), text="Reverse Domain Lookup",variable=_n_(412769, "ipReverse", lambda: ipReverse))
        _l_(412771)
        _c_(412775, _a_(412773, _n_(412772, "ipReverse", lambda: ipReverse), "grid"), row=4,column=0,sticky=_n_(412774, "W", lambda: W))
        _l_(412776)
        ipAdditional= _c_(412778, _n_(412777, "IntVar", lambda: IntVar))
        _l_(412779)
        ipAdditional = _c_(412784, _n_(412780, "Checkbutton", lambda: Checkbutton), _n_(412781, "bottomFrame", lambda: bottomFrame), text="Additional IPs Check",variable=_n_(412782, "ipAdditional", lambda: ipAdditional), state=_n_(412783, "DISABLED", lambda: DISABLED))
        _l_(412785)
        _c_(412789, _a_(412787, _n_(412786, "ipAdditional", lambda: ipAdditional), "grid"), row=5,column=0,sticky=_n_(412788, "W", lambda: W))
        _l_(412790)
        zoneTransfer= _c_(412792, _n_(412791, "IntVar", lambda: IntVar))
        _l_(412793)
        zoneTransfer = _c_(412798, _n_(412794, "Checkbutton", lambda: Checkbutton), _n_(412795, "bottomFrame", lambda: bottomFrame), text="Zone Transfer Check",variable=_n_(412796, "zoneTransfer", lambda: zoneTransfer), state=_n_(412797, "DISABLED", lambda: DISABLED))
        _l_(412799)
        _c_(412803, _a_(412801, _n_(412800, "zoneTransfer", lambda: zoneTransfer), "grid"), row=6,column=0,sticky=_n_(412802, "W", lambda: W))
        _l_(412804)
        oneSixtyOne= _c_(412806, _n_(412805, "IntVar", lambda: IntVar))
        _l_(412807)
        oneSixtyOne = _c_(412811, _n_(412808, "Checkbutton", lambda: Checkbutton), _n_(412809, "bottomFrame", lambda: bottomFrame), text="Onesixtyone",variable=_n_(412810, "oneSixtyOne", lambda: oneSixtyOne))
        _l_(412812)
        _c_(412816, _a_(412814, _n_(412813, "oneSixtyOne", lambda: oneSixtyOne), "grid"), row=7,column=0,sticky=_n_(412815, "W", lambda: W))
        _l_(412817)
        snmp= _c_(412819, _n_(412818, "IntVar", lambda: IntVar))
        _l_(412820)
        snmp = _c_(412824, _n_(412821, "Checkbutton", lambda: Checkbutton), _n_(412822, "bottomFrame", lambda: bottomFrame), text="SNMPWalk",variable=_n_(412823, "snmp", lambda: snmp))
        _l_(412825)
        _c_(412829, _a_(412827, _n_(412826, "snmp", lambda: snmp), "grid"), row=8,column=0,sticky=_n_(412828, "W", lambda: W))
        _l_(412830)
        rpc= _c_(412832, _n_(412831, "IntVar", lambda: IntVar))
        _l_(412833)
        rpc = _c_(412838, _n_(412834, "Checkbutton", lambda: Checkbutton), _n_(412835, "bottomFrame", lambda: bottomFrame), text="RPC Client using NETBIOS",variable=_n_(412836, "rpc", lambda: rpc), state=_n_(412837, "DISABLED", lambda: DISABLED))
        _l_(412839)
        _c_(412843, _a_(412841, _n_(412840, "rpc", lambda: rpc), "grid"), row=9,column=0,sticky=_n_(412842, "W", lambda: W))
        _l_(412844)
        otherNetwork = _c_(412847, _n_(412845, "Label", lambda: Label), _n_(412846, "bottomFrame", lambda: bottomFrame), text="Other Network Information", font="ariel 10 bold")
        _l_(412848)
        _c_(412852, _a_(412850, _n_(412849, "otherNetwork", lambda: otherNetwork), "grid"), row=10,column=0,pady=5,sticky=_n_(412851, "W", lambda: W))
        _l_(412853)
        ip= _c_(412855, _n_(412854, "IntVar", lambda: IntVar))
        _l_(412856)
        ip = _c_(412860, _n_(412857, "Checkbutton", lambda: Checkbutton), _n_(412858, "bottomFrame", lambda: bottomFrame), text="Local Machine",variable=_n_(412859, "ip", lambda: ip))
        _l_(412861)
        _c_(412865, _a_(412863, _n_(412862, "ip", lambda: ip), "grid"), row=11,column=0,sticky=_n_(412864, "W", lambda: W))
        _l_(412866)

##        nslookup.pack()
##        mxlookup.pack()
##        ipForward.pack()
##        ipReverse.pack()
##        ipAdditional.pack()
##        zoneTransfer.pack()
##        oneSixtyOne.pack()
##        snmp.pack()
##        rpc.pack()
##        ip.pack()



        def cmdrunButton():
                _l_(412912)

                global nslookup
                _l_(412867)
                _c_(412870, _a_(412869, _n_(412868, "nslookup", lambda: nslookup), "get"))
                _l_(412871)
                _c_(412874, _a_(412873, _n_(412872, "mxlookup", lambda: mxlookup), "get"))
                _l_(412875)
                _c_(412878, _a_(412877, _n_(412876, "ipForward", lambda: ipForward), "get"))
                _l_(412879)
                _c_(412882, _a_(412881, _n_(412880, "ipReverse", lambda: ipReverse), "get"))
                _l_(412883)
                _c_(412886, _a_(412885, _n_(412884, "ipAdditional", lambda: ipAdditional), "get"))
                _l_(412887)
                _c_(412890, _a_(412889, _n_(412888, "zoneTransfer", lambda: zoneTransfer), "get"))
                _l_(412891)
                _c_(412894, _a_(412893, _n_(412892, "oneSixtyOne", lambda: oneSixtyOne), "get"))
                _l_(412895)
                _c_(412898, _a_(412897, _n_(412896, "snmp", lambda: snmp), "get"))
                _l_(412899)
                _c_(412902, _a_(412901, _n_(412900, "rpc", lambda: rpc), "get"))
                _l_(412903)
                _c_(412906, _a_(412905, _n_(412904, "ip", lambda: ip), "get"))
                _l_(412907)
                _c_(412910, _n_(412908, "print", lambda: print), _n_(412909, "nslookup", lambda: nslookup))
                _l_(412911)

        runButton = _c_(412916, _n_(412913, "Button", lambda: Button), _n_(412914, "bottomFrame", lambda: bottomFrame), text="Run", command=_n_(412915, "cmdrunButton", lambda: cmdrunButton))
        _l_(412917)
        _c_(412921, _a_(412919, _n_(412918, "runButton", lambda: runButton), "grid"), row=12, padx=3,pady=3,column=0,sticky=_n_(412920, "W", lambda: W))
        _l_(412922)
        quitButton = _c_(412926, _n_(412923, "Button", lambda: Button), _n_(412924, "bottomFrame", lambda: bottomFrame), text="Quit",command=_n_(412925, "close", lambda: close))
        _l_(412927)
        _c_(412931, _a_(412929, _n_(412928, "quitButton", lambda: quitButton), "grid"), row=12, padx=3,pady=3,column=1,sticky=_n_(412930, "E", lambda: E))
        _l_(412932)

##        runButton.pack()
##        quitButton.pack()



        _c_(412935, _a_(412934, _n_(412933, "startup", lambda: startup), "mainloop"))
        _l_(412936)
_c_(412939, _n_(412938, "menu", lambda: menu))
_l_(412940)