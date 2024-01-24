# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65887955/i-am-having-a-nonetype-error-on-exiting-gui
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(369862)

except ImportError:
    pass
try:
    import shutil
    _l_(369864)

except ImportError:
    pass
try:
    import sys
    _l_(369866)

except ImportError:
    pass
try:
    import math
    _l_(369868)

except ImportError:
    pass
try:
    import openpyxl
    _l_(369870)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(369872)

except ImportError:
    pass
try:
    from docx import Document
    _l_(369874)

except ImportError:
    pass
try:
    from docx.shared import Inches
    _l_(369876)

except ImportError:
    pass
try:
    from docx.oxml.table import CT_Tbl
    _l_(369878)

except ImportError:
    pass
try:
    from docx.oxml.text.paragraph import CT_P
    _l_(369880)

except ImportError:
    pass
try:
    from docx.table import Table
    _l_(369882)

except ImportError:
    pass
try:
    import PySimpleGUI as sg
    _l_(369884)

except ImportError:
    pass
try:
    import traceback
    _l_(369886)

except ImportError:
    pass

# Define the window's contents

tab1_layout =  [
          [_c_(369889, _a_(369888, _n_(369887, "sg", lambda: sg), "Text"), 'Copy/Paste the row of the SC, CA, or CC from Teams')],
          [_c_(369892, _a_(369891, _n_(369890, "sg", lambda: sg), "Text"), 'Customer name should have - rather than spaces')],
          [_c_(369895, _a_(369894, _n_(369893, "sg", lambda: sg), "Input"), key='-INPUT-')],
          [_c_(369898, _a_(369897, _n_(369896, "sg", lambda: sg), "Text"), size=(40,5), key='-OUTPUT-')],
          [_c_(369901, _a_(369900, _n_(369899, "sg", lambda: sg), "Checkbox"), 'Delete Revision History', default=True, key='-Rev-'), _c_(369904, _a_(369903, _n_(369902, "sg", lambda: sg), "Checkbox"), 'My second Checkbox!')],
         
          
          ]   
_l_(369905)   

tab2_layout = [[_c_(369908, _a_(369907, _n_(369906, "sg", lambda: sg), "T"), 'Use this page to:')],   
               [_c_(369911, _a_(369910, _n_(369909, "sg", lambda: sg), "T"), '    -Create a CC from a CA')], 
               [_c_(369914, _a_(369913, _n_(369912, "sg", lambda: sg), "T"), '    -Remove header info from a SOW to give to another SOW')], 
               [_c_(369917, _a_(369916, _n_(369915, "sg", lambda: sg), "T"), '    -Copy tables from one SOW to another')], 
               [_c_(369920, _a_(369919, _n_(369918, "sg", lambda: sg), "Radio"), 'CA to CC', "RADIO", default=True, key='-CAtoCC-', enable_events=True), _c_(369923, _a_(369922, _n_(369921, "sg", lambda: sg), "Radio"), 'Remove Customer Info', "RADIO", key='-RemoveCust-', enable_events=True), _c_(369926, _a_(369925, _n_(369924, "sg", lambda: sg), "Radio"), 'Copy Tables', "RADIO", key='-Tables-', enable_events=True)],
               [_c_(369929, _a_(369928, _n_(369927, "sg", lambda: sg), "In"), key='in1')],
               [_c_(369932, _a_(369931, _n_(369930, "sg", lambda: sg), "In"), key='in2')],
               [_c_(369935, _a_(369934, _n_(369933, "sg", lambda: sg), "Checkbox"), 'Header',disabled = True, key='-Head-'),_c_(369938, _a_(369937, _n_(369936, "sg", lambda: sg), "Checkbox"), 'Hardware',disabled = True, key='-Hard-'),_c_(369941, _a_(369940, _n_(369939, "sg", lambda: sg), "Checkbox"), 'Software', disabled = True, key='-Soft-'),_c_(369944, _a_(369943, _n_(369942, "sg", lambda: sg), "Checkbox"), 'Calibration', disabled = True, key='-Cal-'),_c_(369947, _a_(369946, _n_(369945, "sg", lambda: sg), "Checkbox"), 'Deliverables', disabled = True, key='-Deli-')],

               
               ]    
_l_(369948)    

layout = [[_c_(369959, _a_(369950, _n_(369949, "sg", lambda: sg), "TabGroup"), [[_c_(369954, _a_(369952, _n_(369951, "sg", lambda: sg), "Tab"), 'Tab 1', _n_(369953, "tab1_layout", lambda: tab1_layout), key='Tab 1'), _c_(369958, _a_(369956, _n_(369955, "sg", lambda: sg), "Tab"), 'Tab 2', _n_(369957, "tab2_layout", lambda: tab2_layout), key='Tab 2')]], key='tab')],   
          [_c_(369962, _a_(369961, _n_(369960, "sg", lambda: sg), "Button"), 'Create'), _c_(369965, _a_(369964, _n_(369963, "sg", lambda: sg), "Button"), 'Clear'), _c_(369968, _a_(369967, _n_(369966, "sg", lambda: sg), "Button"), 'Quit')]
          ]   
_l_(369969)   

tableNames = ['Header', 'Hardware', 'Software', 'Calibration', 'Deliverables']
_l_(369970)
tableKeys = ['-Head-', '-Hard-', '-Soft-', '-Cal-', '-Deli-']
_l_(369971)

# Create the window
window = _c_(369975, _a_(369973, _n_(369972, "sg", lambda: sg), "Window"), 'SOW and CA Creator', _n_(369974, "layout", lambda: layout))
_l_(369976)
 
try:
    _l_(370040)

   
    # Display and interact with the Window using an Event Loop
    while True:
        _l_(370017)

        event, values = _c_(369979, _a_(369978, _n_(369977, "window", lambda: window), "read"))      
        _l_(369980)      
        
        
        if _n_(369981, "values", lambda: values)['-Tables-'] == True:
            _l_(369990)

            for i in _n_(369982, "tableKeys", lambda: tableKeys)  :
                _l_(369989)

                _c_(369986, _a_(369985, _n_(369983, "window", lambda: window)[_n_(369984, "i", lambda: i)], "Update"), disabled = False)
                _l_(369987)
                continue
                _l_(369988)

        if _n_(369991, "values", lambda: values)['-Tables-'] == False:
            _l_(370000)

            for i in _n_(369992, "tableKeys", lambda: tableKeys)  :
                _l_(369999)

                _c_(369996, _a_(369995, _n_(369993, "window", lambda: window)[_n_(369994, "i", lambda: i)], "Update"), disabled = True)
                _l_(369997)
                continue
                _l_(369998)

        if _n_(370001, "event", lambda: event) == 'Create' and _n_(370002, "values", lambda: values)['-in1-'] != '' and _n_(370003, "values", lambda: values)['-in2-'] != '' and _n_(370004, "values", lambda: values)['tab'] == 'Tab 2' and _n_(370005, "values", lambda: values)['CAtoCC']:
            _l_(370007)

            pass
            _l_(370006)


       # See if user wants to quit or window was closed
        if _n_(370008, "event", lambda: event) in (_a_(370010, _n_(370009, "sg", lambda: sg), "WINDOW_CLOSED"), 'Quit' ):
            _l_(370016)

            _c_(370013, _a_(370012, _n_(370011, "window", lambda: window), "close"))
            _l_(370014)
            break
            _l_(370015)


except _n_(370018, "Exception", lambda: Exception) as e:
    _l_(370039)

    _c_(370021, _a_(370020, _n_(370019, "window", lambda: window), "close"))
    _l_(370022)
    tb = _c_(370025, _a_(370024, _n_(370023, "traceback", lambda: traceback), "format_exc"))
    _l_(370026)
    _c_(370031, _a_(370028, _n_(370027, "sg", lambda: sg), "Print"), f'An error happened.  Here is the info:', _n_(370029, 'e', lambda: e), _n_(370030, 'tb', lambda: tb))
    _l_(370032)
    _c_(370037, _a_(370034, _n_(370033, 'sg', lambda: sg), 'popup_error'), f'AN EXCEPTION OCCURRED!', _n_(370035, 'e', lambda: e), _n_(370036, 'tb', lambda: tb))
    _l_(370038)