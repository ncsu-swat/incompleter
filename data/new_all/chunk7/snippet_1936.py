# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/13833200/attributeerror-based-on-re-compile-pattern
##  This should be line 19
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
html_doc = """
        <title>Flickr: username</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta property="og:title" content="username" />
        <meta property="og:type" content="flickr_photos:profile" />
        <meta property="og:url" content="http://www.flickr.com/people/Something/" />
        <meta property="og:site_name" content="Flickr" />
        <meta property="og:image" content="http://farm79.staticflickr.com/1111/buddyicons/99999999@N99.jpg?1234567890#99999999@N99" />

                <li>
                <a href="/groups/theportraitgroup/">The Portrait Group</a>
                <span class="text-list-item">
        1,939,830 photos,&nbsp;125,874 members    
                </span>
        </li>
                <li>
                <a href="/groups/412762@N20/">Seagulls Gone Wild</a>
                        <span class="text-list-item">
                2,266 photos,&nbsp;464 members
                </span>
                                                        </li> """
_l_(424980)
try:
        from urllib.request import urlopen
        _l_(424982)

except ImportError:
        pass
try:
        from bs4 import BeautifulSoup
        _l_(424984)

except ImportError:
        pass
try:
        import fileinput
        _l_(424986)

except ImportError:
        pass
try:
        import re
        _l_(424988)

except ImportError:
        pass
                                ##  This should be line 46
## Strips for basic group data
Tab      = _c_(424991, _a_(424990, _n_(424989, "re", lambda: re), "compile"), "(\t){1,}")                                                    # strip tabs
_l_(424992)                                                    # strip tabs
ID       = _c_(424995, _a_(424994, _n_(424993, "re", lambda: re), "compile"), "^.*/\">")                                    # Group ID, could be ID or Href
_l_(424996)                                    # Group ID, could be ID or Href
Href     = _c_(424999, _a_(424998, _n_(424997, "re", lambda: re), "compile"), "(\s)*<a href=\"/groups/") # Strips to beginning of ID
_l_(425000) # Strips to beginning of ID
GName    = _c_(425003, _a_(425002, _n_(425001, "re", lambda: re), "compile"), "/\">(<b>)*")                                    # Strips from end of Href to GName
_l_(425004)                                    # Strips from end of Href to GName

## Persons contact info
conName  = _c_(425007, _a_(425006, _n_(425005, "re", lambda: re), "compile"), "(\s)*<meta property=\"og\:title\" content=\"")        # Contact Name 
_l_(425008)        # Contact Name 
##conName = re.compile("(\s)*<a href=\"/groups/")
conID    = _c_(425011, _a_(425010, _n_(425009, "re", lambda: re), "compile"), "(\s)*<meta property=\"og\:image.*\#")                    # Gets conName's @N ID
_l_(425012)                    # Gets conName's @N ID
conRef   = _c_(425015, _a_(425014, _n_(425013, "re", lambda: re), "compile"), "(\s)*<meta property=\"og\:url.*com/people/")
_l_(425016)

Amp   = _c_(425019, _a_(425018, _n_(425017, "re", lambda: re), "compile"), "&amp;")
_l_(425020)
Qt    = _c_(425023, _a_(425022, _n_(425021, "re", lambda: re), "compile"), "&quot;")                                                
_l_(425024)                                                
Gt    = _c_(425027, _a_(425026, _n_(425025, "re", lambda: re), "compile"), "&gt;")
_l_(425028)
Lt    = _c_(425031, _a_(425030, _n_(425029, "re", lambda: re), "compile"), "&lt;")
_l_(425032)


exfile = 1        ## 0 = use internal data, 1 = use external file
_l_(425033)        ## 0 = use internal data, 1 = use external file

InFile = _n_(425034, "html_doc", lambda: html_doc)
_l_(425035)

if _n_(425036, "exfile", lambda: exfile):
        _l_(425042)

        InFile = _c_(425038, _n_(425037, "open", lambda: open), '\Python\test\Group\group 50 min.ttxt', 'r', encoding = "utf-8", errors = "backslashreplace")
        _l_(425039)
        closein = 1        ## Only close input file if it was opened
        _l_(425040)        ## Only close input file if it was opened
else:
        closein = 0
        _l_(425041)

OutFile = _c_(425044, _n_(425043, "open", lambda: open), 'C:\Python\test\Group\Output.ttxt', 'w', encoding = "utf-8", errors = "backslashreplace")
_l_(425045)
cOutFile = _c_(425047, _n_(425046, "open", lambda: open), 'C:\Python\test\Group\ContactOutput.ttxt', 'w', encoding = "utf-8", errors = "backslashreplace")
_l_(425048)

i = 1    ## counter for debugging
_l_(425049)    ## counter for debugging

                                ##  This should be line 80
for line in _n_(425050, "InFile", lambda: InFile):
        _l_(425175)

##    print('{}'.format(i), end = ', ') ## this is just a debugging line, to see where the program errors out
##    i += 1
        if _c_(425054, _a_(425052, _n_(425051, "Href", lambda: Href), "search"), _n_(425053, "line", lambda: line)):
                _l_(425163)

                ln = _n_(425055, "line", lambda: line)
                _l_(425056)
                ln = _c_(425061, _a_(425058, _n_(425057, "re", lambda: re), "sub"), _n_(425059, "Href", lambda: Href), "", _n_(425060, "ln", lambda: ln))
                _l_(425062)
                gID, Name = _c_(425065, _a_(425064, _n_(425063, "ln", lambda: ln), "split"), "/\">")
                _l_(425066)
                Name = _n_(425067, "Name", lambda: Name)[:-5]    ## this removes the "\n" at EOL as well
                _l_(425068)    ## this removes the "\n" at EOL as well
                if "@N" in _n_(425069, "gID", lambda: gID):
                        _l_(425074)

                        rH = ""
                        _l_(425070)
                else:        
                        rH = _n_(425071, "gID", lambda: gID)
                        _l_(425072)
                        gID = ""
                        _l_(425073)

##        sLn = '{3}\t{0}\t{1}\t{2}\n'.format(Name, gID, rH, conName)
                sLn = _c_(425080, _a_(425075, '{0}\t{1}\t{2}\n', "format"), _n_(425076, "Name", lambda: Name), _n_(425077, "gID", lambda: gID), _n_(425078, "rH", lambda: rH), _n_(425079, "conName", lambda: conName))
                _l_(425081)
                        ##  Replace HTML codes
                sLn = _c_(425086, _a_(425083, _n_(425082, "re", lambda: re), "sub"), _n_(425084, "Gt", lambda: Gt), ">", _n_(425085, "sLn", lambda: sLn))
                _l_(425087)
                sLn = _c_(425092, _a_(425089, _n_(425088, "re", lambda: re), "sub"), _n_(425090, "Lt", lambda: Lt), "<", _n_(425091, "sLn", lambda: sLn))
                _l_(425093)
                sLn = _c_(425098, _a_(425095, _n_(425094, "re", lambda: re), "sub"), _n_(425096, "Qt", lambda: Qt), "\"", _n_(425097, "sLn", lambda: sLn))
                _l_(425099)
                sLn = _c_(425104, _a_(425101, _n_(425100, "re", lambda: re), "sub"), _n_(425102, "Amp", lambda: Amp), "&", _n_(425103, "sLn", lambda: sLn))
                _l_(425105)

                _c_(425109, _a_(425107, _n_(425106, "OutFile", lambda: OutFile), "write"), _n_(425108, "sLn", lambda: sLn))
                _l_(425110)
        elif _c_(425114, _a_(425112, _n_(425111, "conName", lambda: conName), "search"), _n_(425113, "line", lambda: line)):
                _l_(425162)

                ln = _n_(425115, "line", lambda: line)
                _l_(425116)
                ln = _c_(425121, _a_(425118, _n_(425117, "re", lambda: re), "sub"), _n_(425119, "conName", lambda: conName), "", _n_(425120, "ln", lambda: ln))
                _l_(425122)
                conName = _c_(425125, _a_(425124, _n_(425123, "ln", lambda: ln), "split"), "\" />")
                _l_(425126)
        elif _c_(425130, _a_(425128, _n_(425127, "conID", lambda: conID), "search"), _n_(425129, "line", lambda: line)) is not None:
                _l_(425161)

                ln = _n_(425131, "line", lambda: line)
                _l_(425132)
                ln = _c_(425137, _a_(425134, _n_(425133, "re", lambda: re), "sub"), _n_(425135, "conID", lambda: conID), "", _n_(425136, "ln", lambda: ln))
                _l_(425138)
                conID = _c_(425141, _a_(425140, _n_(425139, "ln", lambda: ln), "split"), "\" />")
                _l_(425142)
        elif _c_(425146, _a_(425144, _n_(425143, "conRef", lambda: conRef), "search"), _n_(425145, "line", lambda: line)) is not None:
                _l_(425160)

                ln = _n_(425147, "line", lambda: line)
                _l_(425148)
                ln = _c_(425153, _a_(425150, _n_(425149, "re", lambda: re), "sub"), _n_(425151, "conRef", lambda: conRef), "", _n_(425152, "ln", lambda: ln))
                _l_(425154)
                conRef = _c_(425157, _a_(425156, _n_(425155, "ln", lambda: ln), "split"), "\" />")
                _l_(425158)
        else:
                pass
                _l_(425159)

        sLn = _c_(425168, _a_(425164, '{0}\t{1}\t{2}\n', "format"), _n_(425165, "conID", lambda: conID), _n_(425166, "conRef", lambda: conRef), _n_(425167, "conName", lambda: conName))
        _l_(425169)
        _c_(425173, _a_(425171, _n_(425170, "cOutFile", lambda: cOutFile), "write"), _n_(425172, "sLn", lambda: sLn))        ## I know, this will make a massive file with duplicated data, but deal w/ it later
        _l_(425174)        ## I know, this will make a massive file with duplicated data, but deal w/ it later

if _n_(425176, "closein", lambda: closein):
        _l_(425181)

        _c_(425179, _a_(425178, _n_(425177, "InFile", lambda: InFile), "close"))
        _l_(425180)
_c_(425184, _a_(425183, _n_(425182, "OutFile", lambda: OutFile), "close"))
_l_(425185)
_c_(425188, _a_(425187, _n_(425186, "cOutFile", lambda: cOutFile), "close"))
_l_(425189)