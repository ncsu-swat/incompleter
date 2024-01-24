# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58741858/selenium-webdriver-not-closing-giving-no-attribute-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(650912)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(650914)

except ImportError:
    pass
try:
    import time
    _l_(650916)

except ImportError:
    pass
try:
    import threading
    _l_(650918)

except ImportError:
    pass
try:
    import random
    _l_(650920)

except ImportError:
    pass
try:
    import sys
    _l_(650922)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(650924)

except ImportError:
    pass
try:
    from mysql.connector import errorcode
    _l_(650926)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(650928)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(650930)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(650932)

except ImportError:
    pass
try:
    from time import strftime
    _l_(650934)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(650936)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(650938)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(650940)

except ImportError:
    pass
try:
    import datetime
    _l_(650942)

except ImportError:
    pass
try:
    from selenium.common.exceptions import *
    _l_(650944)

except ImportError:
    pass


class InstagramBot():
    _l_(651357)

    # Run page
    def Gui(self):
        _l_(651182)

    # Load application

        try:
            _l_(651181)

            root = _c_(650947, _a_(650946, _n_(650945, "tk", lambda: tk), "Tk"))
            _l_(650948)
            _c_(650951, _a_(650950, _n_(650949, "root", lambda: root), "lift"))
            _l_(650952)
            _c_(650955, _a_(650954, _n_(650953, "root", lambda: root), "title"), "Instagram Bot - Created By HudZah")
            _l_(650956)
            menubar = _c_(650959, _n_(650957, "Menu", lambda: Menu), _n_(650958, "root", lambda: root))
            _l_(650960)

            _c_(650962, _n_(650961, "print", lambda: print), "Application loading, please wait \n\n")
            _l_(650963)
            _c_(650965, _n_(650964, "print", lambda: print), "When you install this application, you agree to the abide by the Terms And Conditions stated in the installtion folder. This software is not intended to be used for the exploitation of Instagram, rather as a means of promoting your product. Any detention or suspension that is resulted due to excessive use of this Bot is in no means the fault of the publisher, but the consequences faced by the user. It should be clear that this Bot should not be misused or overused, this might result in unknown penalties to be faced by the user." + "\n Created by HudZah") 
            _l_(650966) 

            Border = 3
            _l_(650967)

            MEDIUM_FONT= ("Verdana", 12)
            _l_(650968)
            LARGE_FONT= ("Arial", 12)
            _l_(650969)


            # Creating Canvas
            canvas = _c_(650973, _a_(650971, _n_(650970, "tk", lambda: tk), "Canvas"), _n_(650972, "root", lambda: root), width=600, height=630)
            _l_(650974)
            _c_(650977, _a_(650976, _n_(650975, "canvas", lambda: canvas), "pack"))
            _l_(650978)
            MainFrame = _c_(650982, _a_(650980, _n_(650979, "tk", lambda: tk), "Frame"), _n_(650981, "root", lambda: root), bg="white")
            _l_(650983)
            _c_(650986, _a_(650985, _n_(650984, "MainFrame", lambda: MainFrame), "place"), relwidth=1, relheight=1)
            _l_(650987)

            # Adding file menu and commands
            file = _c_(650990, _n_(650988, "Menu", lambda: Menu), _n_(650989, "menubar", lambda: menubar), tearoff = 0)
            _l_(650991)
            _c_(650995, _a_(650993, _n_(650992, "menubar", lambda: menubar), "add_cascade"), label = "Run", menu = _n_(650994, "file", lambda: file))
            _l_(650996)
            _c_(651014, _a_(650998, _n_(650997, "file", lambda: file), "add_command"), label ='Run', command=lambda:_c_(651013, _a_(651000, _n_(650999, "self", lambda: self), "Threader"), _c_(651003, _a_(651002, _n_(651001, "Username", lambda: Username), "get")), _c_(651006, _a_(651005, _n_(651004, "Password", lambda: Password), "get")), _c_(651009, _a_(651008, _n_(651007, "List", lambda: List), "get")), _c_(651012, _a_(651011, _n_(651010, "PicsInput", lambda: PicsInput), "get")))) 
            _l_(651015) 
            _c_(651018, _a_(651017, _n_(651016, "file", lambda: file), "add_separator")) 
            _l_(651019) 
            _c_(651024, _a_(651021, _n_(651020, "file", lambda: file), "add_command"), label ='Exit', command = _a_(651023, _n_(651022, "root", lambda: root), "destroy")) 
            _l_(651025) 

            # Username label
            UsernameFrame = _c_(651030, _a_(651027, _n_(651026, "tk", lambda: tk), "Frame"), _n_(651028, "root", lambda: root), bg="lightgrey", bd=_n_(651029, "Border", lambda: Border))
            _l_(651031)
            _c_(651034, _a_(651033, _n_(651032, "UsernameFrame", lambda: UsernameFrame), "place"), relx=0.5, rely=0.135, relwidth=0.60,
                                relheight=0.1, anchor="n")
            _l_(651035)

            Username = _c_(651040, _a_(651037, _n_(651036, "ttk", lambda: ttk), "Entry"), _n_(651038, "UsernameFrame", lambda: UsernameFrame), font=_n_(651039, "LARGE_FONT", lambda: LARGE_FONT))
            _l_(651041)
            #Username.insert(0, "Username")
            _c_(651044, _a_(651043, _n_(651042, "Username", lambda: Username), "insert"), 0, "HudZah")
            _l_(651045)
            _c_(651048, _a_(651047, _n_(651046, "Username", lambda: Username), "place"), relwidth=1, relheight=1)
            _l_(651049)
            _c_(651052, _a_(651051, _n_(651050, "Username", lambda: Username), "focus"))
            _l_(651053)

            # Password label
            PasswordFrame = _c_(651058, _a_(651055, _n_(651054, "tk", lambda: tk), "Frame"), _n_(651056, "root", lambda: root), bg="lightgrey", bd=_n_(651057, "Border", lambda: Border))
            _l_(651059)
            _c_(651062, _a_(651061, _n_(651060, "PasswordFrame", lambda: PasswordFrame), "place"), relx=0.5, rely=0.26, relwidth=0.60,
                                relheight=0.1, anchor="n")
            _l_(651063)

            Password = _c_(651068, _a_(651065, _n_(651064, "ttk", lambda: ttk), "Entry"), _n_(651066, "PasswordFrame", lambda: PasswordFrame), show="*",  font=_n_(651067, "LARGE_FONT", lambda: LARGE_FONT))
            _l_(651069)
            #Password.insert(0, "Password")
            _c_(651072, _a_(651071, _n_(651070, "Password", lambda: Password), "insert"), 0, "HUdhayfart_123")
            _l_(651073)
            _c_(651076, _a_(651075, _n_(651074, "Password", lambda: Password), "place"), relwidth=1, relheight=1)
            _l_(651077)

            # Hashtags label
            ListFrame = _c_(651082, _a_(651079, _n_(651078, "tk", lambda: tk), "Frame"), _n_(651080, "root", lambda: root), bg="lightgrey", bd=_n_(651081, "Border", lambda: Border))
            _l_(651083)
            _c_(651086, _a_(651085, _n_(651084, "ListFrame", lambda: ListFrame), "place"), relx=0.5, rely=0.385, relwidth=0.60,
                            relheight=0.1, anchor="n")
            _l_(651087)

            List = _c_(651092, _a_(651089, _n_(651088, "ttk", lambda: ttk), "Entry"), _n_(651090, "ListFrame", lambda: ListFrame), font=_n_(651091, "LARGE_FONT", lambda: LARGE_FONT))
            _l_(651093)
            #List.insert(0, "Explore Hashtags, eg: food, nyc")
            _c_(651096, _a_(651095, _n_(651094, "List", lambda: List), "insert"), 0, "minecraft")
            _l_(651097)
            _c_(651100, _a_(651099, _n_(651098, "List", lambda: List), "place"), relwidth=1, relheight=1)
            _l_(651101)

            # Number of pictures dropdown
            PicsInput = _c_(651105, _n_(651102, "Spinbox", lambda: Spinbox), _n_(651103, "root", lambda: root), from_= 5, to = 2000, font = _n_(651104, "LARGE_FONT", lambda: LARGE_FONT))
            _l_(651106)
            _c_(651109, _a_(651108, _n_(651107, "PicsInput", lambda: PicsInput), "place"), relx=0.5, rely=0.61, relwidth=0.14,
                        relheight=0.055, anchor = "n")
            _l_(651110)


            # Run button
            button = _c_(651129, _a_(651112, _n_(651111, "ttk", lambda: ttk), "Button"), _n_(651113, "MainFrame", lambda: MainFrame), text="Run",
                            command=lambda:_c_(651128, _a_(651115, _n_(651114, "self", lambda: self), "Threader"), _c_(651118, _a_(651117, _n_(651116, "Username", lambda: Username), "get")), _c_(651121, _a_(651120, _n_(651119, "Password", lambda: Password), "get")), _c_(651124, _a_(651123, _n_(651122, "List", lambda: List), "get")), _c_(651127, _a_(651126, _n_(651125, "PicsInput", lambda: PicsInput), "get"))))
            _l_(651130)

            _c_(651133, _a_(651132, _n_(651131, "button", lambda: button), "place"), relx=0.5, rely=0.71, relwidth=0.25,
                        relheight=0.085, anchor="n")           
            _l_(651134)           

            # Quit button
            Quitbutton = _c_(651141, _a_(651136, _n_(651135, "ttk", lambda: ttk), "Button"), _n_(651137, "MainFrame", lambda: MainFrame), text="Quit",
                            command= lambda:_c_(651140, _a_(651139, _n_(651138, "self", lambda: self), "CloseThreader")))
            _l_(651142)

            _c_(651145, _a_(651144, _n_(651143, "Quitbutton", lambda: Quitbutton), "place"), relx=0.5, rely=0.81, relwidth=0.25,
                        relheight=0.085, anchor="n")
            _l_(651146)


            label = _c_(651151, _a_(651148, _n_(651147, "ttk", lambda: ttk), "Label"), _n_(651149, "root", lambda: root), text = "Created by HudZah © 2019", font=_n_(651150, "MEDIUM_FONT", lambda: MEDIUM_FONT))
            _l_(651152)
            _c_(651155, _a_(651154, _n_(651153, "label", lambda: label), "place"), relx = 0.5, rely = 0.93, anchor = "n")
            _l_(651156)

            PicsInputLabel = _c_(651161, _a_(651158, _n_(651157, "ttk", lambda: ttk), "Label"), _n_(651159, "root", lambda: root), text = "Pictures Per Hashtag", font=_n_(651160, "MEDIUM_FONT", lambda: MEDIUM_FONT))
            _l_(651162)
            _c_(651165, _a_(651164, _n_(651163, "PicsInputLabel", lambda: PicsInputLabel), "place"), relx = 0.5, rely = 0.55, relwidth = 0.3, anchor = "n")
            _l_(651166)

            # Create label to show errors to users and Info of bot when closed
            _c_(651170, _a_(651168, _n_(651167, "root", lambda: root), "config"), menu = _n_(651169, "menubar", lambda: menubar))
            _l_(651171)
            _c_(651174, _a_(651173, _n_(651172, "root", lambda: root), "mainloop")) 
            _l_(651175) 
        except _n_(651176, "Exception", lambda: Exception):
            _l_(651180)

            _c_(651178, _n_(651177, "print", lambda: print), "Failed to create gui")
            _l_(651179)

    def CheckUserInfo(self, username, password, hashtagReceived, nOfPics):
        _l_(651302)



        _c_(651186, _a_(651184, _n_(651183, "browserCount", lambda: browserCount), "append"), _n_(651185, "nOfPics", lambda: nOfPics))
        _l_(651187)
        if _n_(651188, "username", lambda: username) and _n_(651189, "username", lambda: username) != "Username":
            _l_(651280)

            pass
            _l_(651190)
            if _n_(651191, "password", lambda: password) and _c_(651194, _n_(651192, "len", lambda: len), _n_(651193, "password", lambda: password)) > 5:
                _l_(651272)

                pass
                _l_(651195)
                if _n_(651196, "hashtagReceived", lambda: hashtagReceived) and _n_(651197, "hashtagReceived", lambda: hashtagReceived) != "Explore Hashtags, eg: food, nyc":
                    _l_(651264)

                    pass
                    _l_(651198)
                    if _c_(651201, _n_(651199, "int", lambda: int), _n_(651200, "nOfPics", lambda: nOfPics)) > 0 and _c_(651204, _n_(651202, "int", lambda: int), _n_(651203, "nOfPics", lambda: nOfPics)) < 2000:
                        _l_(651256)

                        browserRunning = _c_(651209, _a_(651207, _c_(651206, _n_(651205, "Browser", lambda: Browser)), "IsBrowserRunning"), _n_(651208, "browserCount", lambda: browserCount))
                        _l_(651210)
                        _c_(651214, _n_(651211, "print", lambda: print), _n_(651212, "browserRunning", lambda: browserRunning),_n_(651213, "browserCount", lambda: browserCount))
                        _l_(651215)
                        if _n_(651216, "browserRunning", lambda: browserRunning) == False:
                            _l_(651248)

                            if _c_(651219, _a_(651218, _n_(651217, "messagebox", lambda: messagebox), "askokcancel"), 'Application','Application is running, press OK to continue') == True:
                                _l_(651240)


                                try:
                                    _l_(651238)

                                    pages = _c_(651222, _n_(651220, "int", lambda: int), _n_(651221, "nOfPics", lambda: nOfPics))/10
                                    _l_(651223)
                                    pages = _c_(651226, _n_(651224, "int", lambda: int), _n_(651225, "pages", lambda: pages))
                                    _l_(651227)
                                    if _n_(651228, "pages", lambda: pages) < 1:
                                        _l_(651231)

                                        pages = 1
                                        _l_(651229)
                                    else:
                                        pass
                                        _l_(651230)

                                except _n_(651232, "Exception", lambda: Exception):
                                    _l_(651237)

                                    _c_(651235, _a_(651234, _n_(651233, "messagebox", lambda: messagebox), "showwarning"), "Error", "An error has occured")
                                    _l_(651236)

                                infoError = False
                                _l_(651239)

                        else:
                            _c_(651243, _a_(651242, _n_(651241, "messagebox", lambda: messagebox), "showerror"), "Multiple Instances", "Only one instance of the program can be run at a time. Please wait")
                            _l_(651244)
                            _c_(651246, _n_(651245, "print", lambda: print), "Only one instance of the program can be run at a time!")
                            _l_(651247)

                    else:
                        _c_(651251, _a_(651250, _n_(651249, "messagebox", lambda: messagebox), "showwarning"), "Error", "Please enter a valid number of posts to like")
                        _l_(651252)
                        _c_(651254, _n_(651253, "print", lambda: print), "Please enter a valid number of posts to like")                      
                        _l_(651255)                      
                else:
                    _c_(651259, _a_(651258, _n_(651257, "messagebox", lambda: messagebox), "showwarning"), "Error", "Please enter your correct information.")
                    _l_(651260)
                    _c_(651262, _n_(651261, "print", lambda: print), "Please enter suitable data")
                    _l_(651263)
            else:
                _c_(651267, _a_(651266, _n_(651265, "messagebox", lambda: messagebox), "showwarning"), "Error", "Please enter your correct information.")
                _l_(651268)
                _c_(651270, _n_(651269, "print", lambda: print), "Please enter suitable data")
                _l_(651271)
        else:
            _c_(651275, _a_(651274, _n_(651273, "messagebox", lambda: messagebox), "showwarning"), 'Error', 'Please enter a username or password')
            _l_(651276)
            _c_(651278, _n_(651277, "print", lambda: print), "Please enter a username and password")
            _l_(651279)

        try:
            _l_(651301)

            if _n_(651281, "infoError", lambda: infoError) == False and _n_(651282, "browserRunning", lambda: browserRunning) == False:
                _l_(651298)

                BrowserClass = _c_(651284, _n_(651283, "Browser", lambda: Browser))
                _l_(651285)
                _c_(651293, _a_(651287, _n_(651286, "BrowserClass", lambda: BrowserClass), "Login"), _n_(651288, "username", lambda: username), _n_(651289, "password", lambda: password), _n_(651290, "hashtagReceived", lambda: hashtagReceived), _n_(651291, "nOfPics", lambda: nOfPics), _n_(651292, "pages", lambda: pages))
                _l_(651294)

            else:
                _c_(651296, _n_(651295, "print", lambda: print), "Multiple instances or wrong information\n")
                _l_(651297)
        except:
            _l_(651300)

            pass
            _l_(651299)

    def Threader(self, username, password, hashtagReceived, nOfPics):
        _l_(651317)


        #Start a new thread to run the webdriver seperately to stop the gui from freezing
        t1 = _c_(651311, _a_(651304, _n_(651303, "threading", lambda: threading), "Thread"), target = _a_(651306, _n_(651305, "self", lambda: self), "CheckUserInfo"), args = (_n_(651307, "username", lambda: username), _n_(651308, "password", lambda: password), _n_(651309, "hashtagReceived", lambda: hashtagReceived), _n_(651310, "nOfPics", lambda: nOfPics)))
        _l_(651312)
        _c_(651315, _a_(651314, _n_(651313, "t1", lambda: t1), "start"))
        _l_(651316)

    def CloseThreader(self):
        _l_(651331)


        t2 = _c_(651322, _a_(651319, _n_(651318, "threading", lambda: threading), "Thread"), target=_a_(651321, _n_(651320, "self", lambda: self), "CloseBrowser"))
        _l_(651323)
        _c_(651325, _n_(651324, "print", lambda: print), "Close threader")
        _l_(651326)
        _c_(651329, _a_(651328, _n_(651327, "t2", lambda: t2), "start"))
        _l_(651330)


    def CloseBrowser(self):
        _l_(651356)

        try:
            _l_(651355)

            driver = _a_(651334, _c_(651333, _n_(651332, "Browser", lambda: Browser)), "driver")
            _l_(651335)
            _c_(651338, _a_(651337, _n_(651336, "driver", lambda: driver), "quit"))
            _l_(651339)
            _c_(651341, _n_(651340, "print", lambda: print), "Browser quit\n")
            _l_(651342)
            browserRunning = False
            _l_(651343)
            _c_(651346, _a_(651345, _n_(651344, "browserCount", lambda: browserCount), "clear"))
            _l_(651347)
        except _n_(651348, "Exception", lambda: Exception) as e:
            _l_(651354)

            _c_(651351, _n_(651349, "print", lambda: print), _n_(651350, "e", lambda: e))
            _l_(651352)
            pass
            _l_(651353)

class Browser():
    _l_(651726)


    def Login(self, username, password, hashtagReceived, nOfPics, pages):
        _l_(651533)


        browserRunning = True
        _l_(651358)
        _n_(651359, "self", lambda: self).username = _n_(651360, "username", lambda: username)
        _l_(651361)
        _n_(651362, "self", lambda: self).password = _n_(651363, "password", lambda: password)
        _l_(651364)
        hashtags = []
        _l_(651365)
        hashtags = _c_(651368, _a_(651367, _n_(651366, "hashtagReceived", lambda: hashtagReceived), "split"), ",")
        _l_(651369)
        hashtagsOut = False
        _l_(651370)
        i = 0
        _l_(651371)



        try:
            _l_(651474)

            _n_(651372, "self", lambda: self).driver = _c_(651375, _a_(651374, _n_(651373, "webdriver", lambda: webdriver), "Chrome"))
            _l_(651376)
            driver = _a_(651378, _n_(651377, "self", lambda: self), "driver")
            _l_(651379)
            _c_(651382, _a_(651381, _n_(651380, "driver", lambda: driver), "get"), "https://www.instagram.com/")
            _l_(651383)
            _c_(651386, _a_(651385, _n_(651384, "time", lambda: time), "sleep"), 5)
            _l_(651387)


            LoginButton = _c_(651390, _a_(651389, _n_(651388, "driver", lambda: driver), "find_element_by_xpath"), "//a[@href='/accounts/login/?source=auth_switcher']")
            _l_(651391)
            _c_(651394, _a_(651393, _n_(651392, "LoginButton", lambda: LoginButton), "click"))
            _l_(651395)

            _c_(651398, _a_(651397, _n_(651396, "time", lambda: time), "sleep"), 5)
            _l_(651399)


            UsernameElem = _c_(651402, _a_(651401, _n_(651400, "driver", lambda: driver), "find_element_by_xpath"), "//input[@name='username']")
            _l_(651403)
            _c_(651406, _a_(651405, _n_(651404, "UsernameElem", lambda: UsernameElem), "clear"))
            _l_(651407)
            _c_(651412, _a_(651409, _n_(651408, "UsernameElem", lambda: UsernameElem), "send_keys"), _a_(651411, _n_(651410, "self", lambda: self), "username"))
            _l_(651413)


            PasswordElem = _c_(651416, _a_(651415, _n_(651414, "driver", lambda: driver), "find_element_by_xpath"), "//input[@name='password']")
            _l_(651417)
            _c_(651420, _a_(651419, _n_(651418, "PasswordElem", lambda: PasswordElem), "clear"))
            _l_(651421)
            _c_(651426, _a_(651423, _n_(651422, "PasswordElem", lambda: PasswordElem), "send_keys"), _a_(651425, _n_(651424, "self", lambda: self), "password"))
            _l_(651427)
            _c_(651432, _a_(651429, _n_(651428, "PasswordElem", lambda: PasswordElem), "send_keys"), _a_(651431, _n_(651430, "Keys", lambda: Keys), "RETURN"))
            _l_(651433)

            _c_(651436, _a_(651435, _n_(651434, "time", lambda: time), "sleep"), 2)
            _l_(651437)

        except _n_(651438, "WebDriverException", lambda: WebDriverException) or _n_(651439, "NoSuchWindowException", lambda: NoSuchWindowException):
            _l_(651450)

            _c_(651441, _n_(651440, "print", lambda: print), "Browser has been closed by manual intervention \n")
            _l_(651442)
            browserRunning = False
            _l_(651443)
            _c_(651447, _a_(651446, _c_(651445, _n_(651444, "InstagramBot", lambda: InstagramBot)), "CloseThreader"))
            _l_(651448)
            pass
            _l_(651449)

        else:

            try:
                _l_(651473)

                loginCheck = _c_(651453, _a_(651452, _n_(651451, "driver", lambda: driver), "find_element_by_id"), "slfErrorAlert")
                _l_(651454)


            except _n_(651455, "NoSuchElementException", lambda: NoSuchElementException):
                _l_(651458)

                infoValidity = True
                _l_(651456)
                pass
                _l_(651457)

            else:
                _c_(651462, _a_(651461, _a_(651460, _n_(651459, "tk", lambda: tk), "messagebox"), "showerror"), "Login Error", "Please re-verify your login details")
                _l_(651463)
                _c_(651465, _n_(651464, "print", lambda: print), "Login details are incorrect \n")
                _l_(651466)
                _c_(651470, _a_(651469, _c_(651468, _n_(651467, "InstagramBot", lambda: InstagramBot)), "CloseThreader"))
                _l_(651471)
                infoValidity = False
                _l_(651472)

        if _n_(651475, "infoValidity", lambda: infoValidity) == True:
            _l_(651532)

            for hashtag in _n_(651476, "hashtags", lambda: hashtags):
                _l_(651502)


                # Choose a tag from the list of tags         
                hashtag = _c_(651479, _a_(651478, _n_(651477, "hashtag", lambda: hashtag), "replace"), " ", "")
                _l_(651480)

                if _n_(651481, "i", lambda: i) != _c_(651484, _n_(651482, "len", lambda: len), _n_(651483, "hashtags", lambda: hashtags)) and _n_(651485, "hashtagsOut", lambda: hashtagsOut) == False:
                    _l_(651501)

                    _c_(651491, _a_(651487, _n_(651486, "self", lambda: self), "LikePhoto"), _n_(651488, "hashtag", lambda: hashtag), _n_(651489, "nOfPics", lambda: nOfPics), _n_(651490, "pages", lambda: pages))
                    _l_(651492)
                    i = _n_(651493, "i", lambda: i) + 1
                    _l_(651494)

                else:
                    _c_(651498, _a_(651497, _c_(651496, _n_(651495, "InstagramBot", lambda: InstagramBot)), "CloseThreader"))
                    _l_(651499)
                    hashtagsOut = True
                    _l_(651500)

            if _n_(651503, "i", lambda: i) != _c_(651506, _n_(651504, "len", lambda: len), _n_(651505, "hashtags", lambda: hashtags)):
                _l_(651520)

                _c_(651510, _a_(651509, _c_(651508, _n_(651507, "InstagramBot", lambda: InstagramBot)), "CloseThreader"))
                _l_(651511)
                _c_(651513, _n_(651512, "print", lambda: print), "Browser crashed")
                _l_(651514)
                _c_(651517, _a_(651516, _n_(651515, "time", lambda: time), "sleep"), 3)
                _l_(651518)

            else:
                hashtagsOut = True
                _l_(651519)

            if _n_(651521, "hashtagsOut", lambda: hashtagsOut):
                _l_(651531)

                _c_(651524, _a_(651523, _n_(651522, "messagebox", lambda: messagebox), "showinfo"), "Complete", "Program has completed")
                _l_(651525)
                _c_(651529, _a_(651528, _c_(651527, _n_(651526, "InstagramBot", lambda: InstagramBot)), "CloseThreader"))
                _l_(651530)

    def LikePhoto(self, hashtag, NumOfPics, pages):
        _l_(651712)


        try:
            _l_(651711)

            driver = _a_(651535, _n_(651534, "self", lambda: self), "driver") 
            _l_(651536) 
            _c_(651540, _a_(651538, _n_(651537, "driver", lambda: driver), "get"), "https://www.instagram.com/explore/tags/" + _n_(651539, "hashtag", lambda: hashtag) + "/")
            _l_(651541)
            _c_(651544, _a_(651543, _n_(651542, "time", lambda: time), "sleep"), 3)
            _l_(651545)
            PicLinks = []
            _l_(651546)
            _c_(651549, _n_(651547, "print", lambda: print), "Check : Number of pages are", _n_(651548, "pages", lambda: pages))
            _l_(651550)

            currentUrl = _a_(651552, _n_(651551, "driver", lambda: driver), "current_url")
            _l_(651553)

            if _n_(651554, "currentUrl", lambda: currentUrl) != "https://www.instagram.com/explore/tags/" + _n_(651555, "hashtag", lambda: hashtag) + "/":
                _l_(651565)

                _c_(651559, _a_(651557, _n_(651556, "driver", lambda: driver), "get"), "https://www.instagram.com/explore/tags/" + _n_(651558, "hashtag", lambda: hashtag) + "/")
                _l_(651560)
                _c_(651563, _a_(651562, _n_(651561, "time", lambda: time), "sleep"), 5)
                _l_(651564)


            for i in _c_(651568, _n_(651566, "range", lambda: range), 0,_n_(651567, "pages", lambda: pages)):
                _l_(651608)


                _c_(651571, _a_(651570, _n_(651569, "driver", lambda: driver), "execute_script"), "window.scrollTo(0, document.body.scrollHeight);")
                _l_(651572)
                _c_(651575, _a_(651574, _n_(651573, "time", lambda: time), "sleep"), 2)
                _l_(651576)


                Links = _c_(651579, _a_(651578, _n_(651577, "driver", lambda: driver), "find_elements_by_tag_name"), 'a')
                _l_(651580)

                Links = [_c_(651583, _a_(651582, _n_(651581, "elem", lambda: elem), "get_attribute"), 'href') for elem in _n_(651584, "Links", lambda: Links)
                        if ".com/p/" in _c_(651587, _a_(651586, _n_(651585, "elem", lambda: elem), "get_attribute"), "href")]
                _l_(651588)

                for Link in _n_(651589, "Links", lambda: Links):
                    _l_(651598)

                    if _n_(651590, "Link", lambda: Link) not in _n_(651591, "PicLinks", lambda: PicLinks):
                        _l_(651597)

                        _c_(651595, _a_(651593, _n_(651592, "PicLinks", lambda: PicLinks), "append"), _n_(651594, "Link", lambda: Link))
                        _l_(651596)

                _c_(651606, _n_(651599, "print", lambda: print), "Check: Total N.of pic hrefs stored after array : " + _c_(651604, _n_(651600, "str", lambda: str), _c_(651603, _n_(651601, "len", lambda: len), _n_(651602, "PicLinks", lambda: PicLinks))) + " , in " + _n_(651605, "hashtag", lambda: hashtag))
                _l_(651607)

            LikedPhotos = 0 # FIX LOST CONNECTION and LIKED TOTAL LIKED PICS
            _l_(651609) # FIX LOST CONNECTION and LIKED TOTAL LIKED PICS


            for i in _c_(651614, _n_(651610, "range", lambda: range), 0, _c_(651613, _n_(651611, "len", lambda: len), _n_(651612, "PicLinks", lambda: PicLinks))):
                _l_(651621)

                _c_(651619, _n_(651615, "print", lambda: print), "Num" , _n_(651616, "i", lambda: i) , ": " ,  _n_(651617, "PicLinks", lambda: PicLinks)[_n_(651618, "i", lambda: i)])
                _l_(651620)

            UniquePhotos = _c_(651624, _n_(651622, "int", lambda: int), _n_(651623, "NumOfPics", lambda: NumOfPics))
            _l_(651625)
            _c_(651628, _n_(651626, "print", lambda: print), _n_(651627, "UniquePhotos", lambda: UniquePhotos))
            _l_(651629)

            # For all the images in the array, like each one
            for i in _c_(651634, _n_(651630, "range", lambda: range), 0,_c_(651633, _n_(651631, "int", lambda: int), _n_(651632, "NumOfPics", lambda: NumOfPics))):
                _l_(651691)

                try:
                    _l_(651652)

                    _c_(651639, _a_(651636, _n_(651635, "driver", lambda: driver), "get"), _n_(651637, "PicLinks", lambda: PicLinks)[_n_(651638, "i", lambda: i)])
                    _l_(651640)
                    _c_(651643, _a_(651642, _n_(651641, "time", lambda: time), "sleep"), 4)
                    _l_(651644)

                except _n_(651645, "Exception", lambda: Exception) as e:
                    _l_(651651)

                    _c_(651648, _n_(651646, "print", lambda: print), _n_(651647, "e", lambda: e))
                    _l_(651649)
                    pass
                    _l_(651650)

                try:
                    _l_(651664)

                    _c_(651655, _a_(651654, _n_(651653, "driver", lambda: driver), "execute_script"), "window.scrollTo(0, document.body.scrollHeight);")
                    _l_(651656)

                except _n_(651657, "NoSuchElementException", lambda: NoSuchElementException) as e:
                    _l_(651663)

                    _c_(651660, _n_(651658, "print", lambda: print), _n_(651659, "e", lambda: e))
                    _l_(651661)
                    pass
                    _l_(651662)

                _c_(651670, _a_(651666, _n_(651665, "time", lambda: time), "sleep"), _c_(651669, _a_(651668, _n_(651667, "random", lambda: random), "randint"), 3, 9))
                _l_(651671)

                _c_(651676, _a_(651675, _c_(651674, _a_(651673, _n_(651672, "driver", lambda: driver), "find_element_by_xpath"), '//span[@aria-label="Like"]'), "click"))
                _l_(651677)


                _c_(651680, _a_(651679, _n_(651678, "time", lambda: time), "sleep"), 1)
                _l_(651681)
                UniquePhotos = _n_(651682, "UniquePhotos", lambda: UniquePhotos) - 1
                _l_(651683)
                LikedPhotos = _n_(651684, "LikedPhotos", lambda: LikedPhotos) + 1
                _l_(651685)
                _c_(651689, _n_(651686, "print", lambda: print), "Picture liked : ",_n_(651687, "LikedPhotos", lambda: LikedPhotos) , " Pictures left : ", _n_(651688, "UniquePhotos", lambda: UniquePhotos))
                _l_(651690)

        except _n_(651692, "NoSuchWindowException", lambda: NoSuchWindowException) or _n_(651693, "WebDriverException", lambda: WebDriverException) or _n_(651694, "NoSuchFrameException", lambda: NoSuchFrameException) as e:
            _l_(651700)

            _c_(651697, _n_(651695, "print", lambda: print), _n_(651696, "e", lambda: e))
            _l_(651698)
            browserRunning = False
            _l_(651699)

        finally:
            _l_(651710)

            _c_(651702, _n_(651701, "print", lambda: print), "LikePhotos function is now over\n")
            _l_(651703)
            _c_(651707, _a_(651706, _c_(651705, _n_(651704, "InstagramBot", lambda: InstagramBot)), "CloseThreader"))
            _l_(651708)
            browserRunning = False
            _l_(651709)

    def IsBrowserRunning(self, browserCount):
        _l_(651725)

        if _c_(651715, _n_(651713, "len", lambda: len), _n_(651714, "browserCount", lambda: browserCount)) > 1:
            _l_(651724)

            _c_(651720, _n_(651716, "print", lambda: print), _c_(651719, _n_(651717, "len", lambda: len), _n_(651718, "browserCount", lambda: browserCount)))
            _l_(651721)
            aux = True
            _l_(651722)
            return aux

        else:
            aux = False
            _l_(651723)
            return aux




if _n_(651727, "__name__", lambda: __name__) == "__main__":
    _l_(651749)

    _c_(651729, _n_(651728, "print", lambda: print), "Run from main \n")
    _l_(651730)

    NewLimit = 3000
    _l_(651731)
    _c_(651735, _a_(651733, _n_(651732, "sys", lambda: sys), "setrecursionlimit"), _n_(651734, "NewLimit", lambda: NewLimit))
    _l_(651736)
    global browserCount
    _l_(651737)
    browserCount = []
    _l_(651738)


    IG = _c_(651740, _n_(651739, "InstagramBot", lambda: InstagramBot))
    _l_(651741)
    _c_(651744, _a_(651743, _n_(651742, "IG", lambda: IG), "Gui"))
    _l_(651745)

else:
    _c_(651747, _n_(651746, "print", lambda: print), "Run from import")
    _l_(651748)
# if IG.CheckUserInfo() == False:
#     print("yes")