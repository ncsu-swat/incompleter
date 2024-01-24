# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70819746/python-builtins-attributeerror-tuple-object-has-no-attribute-win32-process
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, wmi, time
    _l_(537759)

except ImportError:
    pass
connect = _c_(537762, _a_(537761, _n_(537760, "wmi", lambda: wmi), "WMI"))
_l_(537763)
empty = []
_l_(537764)
excluding = ['svchost.exe', 'lsass.exe', 'explorer.exe', 'sihost.exe', 'System', 'ntoskrnl.exe', 'winnit.exe', 'dwm.exe', 'smss.exe', 'services.exe', 'winlogon.exe', 'csrss.exe', 'RuntimeBroker.exe', 'ApplicationFrameHost.exe', 'ctfmon.exe', 'spoolsv.exe', 'SecurityHealthService.exe', 'System Idle Process', 'Registry', 'wininit.exe', 'fontdrvhost.exe', 'IntelCpHDCPSvc.exe', 'IntelCpHeciSvc.exe', 'igfxCUIService.exe', 'Memory Compression', 'hasplms.exe', 'armsvc.exe', 'IPROSetMonitor.exe', 'FNPLicensingService64.exe', 'jhi_service.exe', 'klnagent.exe', 'avp.exe', 'AdAppMgrSvc.exe', 'veyon-service.exe', 'sqlwriter.exe', 'WmiPrvSE.exe', 'hasplmv.exe', 'avpui.exe', 'PresentationFontCache.exe', 'taskhostw.exe', 'igfxEM.exe', 'rundll32.exe', 'veyon-server.exe', 'veyon-worker.exe', 'ShellExperienceHost.exe', 'SearchUI.exe', 'smartscreen.exe', 'chrome.exe', 'jusched.exe', 'GenuineService.exe', 'avpsus.exe', 'SgrmBroker.exe', 'WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe', 'SystemSettingsBroker.exe', 'jucheck.exe', 'cmd.exe', 'conhost.exe', 'dllhost.exe']
_l_(537765)
process_dictionary = {}
_l_(537766)
while 1:
    _l_(537807)

    for process in _c_(537769, _a_(537768, _n_(537767, "connect", lambda: connect), "Win32_Process")):
        _l_(537790)

        connect = _c_(537773, _n_(537770, "str", lambda: str), _a_(537772, _n_(537771, "process", lambda: process), "ProcessId")), _a_(537775, _n_(537774, "process", lambda: process), "Name")
        _l_(537776)
        if _a_(537778, _n_(537777, "process", lambda: process), "Name") not in _n_(537779, "excluding", lambda: excluding):
            _l_(537789)

            prNm = _a_(537781, _n_(537780, "process", lambda: process), "Name")
            _l_(537782)
            _n_(537783, "process_dictionary", lambda: process_dictionary)[_n_(537784, "prNm", lambda: prNm)] = _c_(537787, _a_(537786, _n_(537785, "time", lambda: time), "time"))
            _l_(537788)
    for i in _c_(537793, _a_(537792, _n_(537791, "process_dictionary", lambda: process_dictionary), "keys")):
        _l_(537798)

        _c_(537796, _n_(537794, "print", lambda: print), _n_(537795, "i", lambda: i))
        _l_(537797)
    _c_(537801, _n_(537799, "print", lambda: print), _n_(537800, "process_dictionary", lambda: process_dictionary))
    _l_(537802)
    _c_(537805, _a_(537804, _n_(537803, "time", lambda: time), "sleep"), 10)
    _l_(537806)