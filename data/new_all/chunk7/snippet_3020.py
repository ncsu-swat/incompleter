# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54045102/filenotfounderrorwhen-trying-to-replace-existing-csv-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
database = "E:\Stock Database\Historical Data\Historical Stock List\\"
_l_(545071)

chrome_options      = _c_(545074, _a_(545073, _n_(545072, "webdriver", lambda: webdriver), "ChromeOptions"))
_l_(545075)
prefs               = {'download.default_directory': _n_(545076, "database", lambda: database)}
_l_(545077)
_c_(545081, _a_(545079, _n_(545078, "chrome_options", lambda: chrome_options), "add_experimental_option"), name='prefs', value= _n_(545080, "prefs", lambda: prefs))
_l_(545082)
stocks              = _c_(545086, _a_(545084, _n_(545083, "webdriver", lambda: webdriver), "Chrome"), r"E:\Python Programs\chromedriver", chrome_options = _n_(545085, "chrome_options", lambda: chrome_options))
_l_(545087)

#Website
_c_(545091, _a_(545089, _n_(545088, "stocks", lambda: stocks), "get"), _n_(545090, "universe_data_site", lambda: universe_data_site))
_l_(545092)

#Navigate Web Page
_c_(545097, _a_(545096, _c_(545095, _a_(545094, _n_(545093, "stocks", lambda: stocks), "find_element_by_css_selector"), '#ui-id-4'), "click"))
_l_(545098)
_c_(545103, _a_(545102, _c_(545101, _a_(545100, _n_(545099, "stocks", lambda: stocks), "find_element_by_css_selector"), '#stocks > a.blue_button.factbutton'), "click"))
_l_(545104)
_c_(545109, _a_(545108, _c_(545107, _a_(545106, _n_(545105, "stocks", lambda: stocks), "find_element_by_css_selector"), 'body > a:nth-child(3)'), "click"))
_l_(545110)

#Download and renaiming of File
filename = 'allstocks.csv'
_l_(545111)

#removes existing file if already exists
if _c_(545117, _a_(545114, _a_(545113, _n_(545112, "os", lambda: os), "path"), "exists"), r"%s%s"%(_n_(545115, "database", lambda: database),_n_(545116, "filename", lambda: filename))) is True:
         _l_(545138)

         _c_(545122, _a_(545119, _n_(545118, "os", lambda: os), "remove"), r"%s%s"%(_n_(545120, "database", lambda: database),_n_(545121, "filename", lambda: filename)))
         _l_(545123)
         _c_(545129, _a_(545125, _n_(545124, "os", lambda: os), "rename"), r"%s"%_n_(545126, "database", lambda: database)+ "stockfactsheet.csv ",r"%s%s"%(_n_(545127, "database", lambda: database),_n_(545128, "filename", lambda: filename)))
         _l_(545130)
else:
        _c_(545136, _a_(545132, _n_(545131, "os", lambda: os), "rename"), r"%s"%_n_(545133, "database", lambda: database)+ "stockfactsheet.csv ",r"%s%s"%(_n_(545134, "database", lambda: database),_n_(545135, "filename", lambda: filename)))
        _l_(545137)