# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61714227/type-error-unsupported-operand-types-for-nonetype-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pytube import YouTube
    _l_(351599)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(351601)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(351603)

except ImportError:
    pass
try:
    from tkinter import*
    _l_(351605)

except ImportError:
    pass
try:
    import threading
    _l_(351607)

except ImportError:
    pass
try:
    import re
    _l_(351609)

except ImportError:
    pass

class Application:
    _l_(351865)

    def __init__(self,root):
        _l_(351762)

        _n_(351610, "self", lambda: self).root=_n_(351611, "root", lambda: root)
        _l_(351612)
        _c_(351616, _a_(351615, _a_(351614, _n_(351613, "self", lambda: self), "root"), "grid_rowconfigure"), 0,weight=2)
        _l_(351617)
        _c_(351621, _a_(351620, _a_(351619, _n_(351618, "self", lambda: self), "root"), "grid_columnconfigure"), 0,weight=1)
        _l_(351622)
        _c_(351626, _a_(351625, _a_(351624, _n_(351623, "self", lambda: self), "root"), "config"), bg="#ffdddd")
        _l_(351627)

        top_label=_c_(351631, _n_(351628, "Label", lambda: Label), _a_(351630, _n_(351629, "self", lambda: self), "root"),text="YouTube download manager",fg="blue",font=("ALGERIAN",70))
        _l_(351632)
        _c_(351635, _a_(351634, _n_(351633, "top_label", lambda: top_label), "grid"), pady=(0,10))
        _l_(351636)

        link_label=_c_(351640, _n_(351637, "Label", lambda: Label), _a_(351639, _n_(351638, "self", lambda: self), "root"),text="Please paste your YouTube video link",bg="black",fg="red",font=("Agency FB",30))
        _l_(351641)
        _c_(351644, _a_(351643, _n_(351642, "link_label", lambda: link_label), "grid"), pady=(0,20))
        _l_(351645)

        _n_(351646, "self", lambda: self).YoutubeEntryVar=_c_(351648, _n_(351647, "StringVar", lambda: StringVar))
        _l_(351649)

        _n_(351650, "self", lambda: self).YoutubeEntry=_c_(351656, _n_(351651, "Entry", lambda: Entry), _a_(351653, _n_(351652, "self", lambda: self), "root"),width=70,textvariable=_a_(351655, _n_(351654, "self", lambda: self), "YoutubeEntryVar"),font=("Lucida Console",25),fg="blue")
        _l_(351657)
        _c_(351661, _a_(351660, _a_(351659, _n_(351658, "self", lambda: self), "YoutubeEntry"), "grid"), pady=(0,20),ipady=5)
        _l_(351662)

        _n_(351663, "self", lambda: self).YoutubeEntryError=_c_(351667, _n_(351664, "Label", lambda: Label), _a_(351666, _n_(351665, "self", lambda: self), "root"),text="",font=("Colonna MT",20),fg="green")
        _l_(351668)
        _c_(351672, _a_(351671, _a_(351670, _n_(351669, "self", lambda: self), "YoutubeEntryError"), "grid"), pady=(0,8))
        _l_(351673)

        _n_(351674, "self", lambda: self).YoutubeFileSave=_c_(351678, _n_(351675, "Label", lambda: Label), _a_(351677, _n_(351676, "self", lambda: self), "root"),text="Choose Directory",font=("Agency FB",20),fg="black")
        _l_(351679)
        _c_(351683, _a_(351682, _a_(351681, _n_(351680, "self", lambda: self), "YoutubeFileSave"), "grid"), pady=(0,8))
        _l_(351684)

        _n_(351685, "self", lambda: self).YoutubeButton=_c_(351691, _n_(351686, "Button", lambda: Button), _a_(351688, _n_(351687, "self", lambda: self), "root"),text="Directory",font=("Colonna MT",20),command=_a_(351690, _n_(351689, "self", lambda: self), "FileDirectory"))
        _l_(351692)
        _c_(351696, _a_(351695, _a_(351694, _n_(351693, "self", lambda: self), "YoutubeButton"), "grid"), pady=(10,3),ipady=5)
        _l_(351697)

        _n_(351698, "self", lambda: self).FileLocation=_c_(351702, _n_(351699, "Label", lambda: Label), _a_(351701, _n_(351700, "self", lambda: self), "root"),text="",font=("Harlow Solid Italic",20))
        _l_(351703)
        _c_(351707, _a_(351706, _a_(351705, _n_(351704, "self", lambda: self), "FileLocation"), "grid"))
        _l_(351708)

        _n_(351709, "self", lambda: self).DownloadSelect=_c_(351713, _n_(351710, "Label", lambda: Label), _a_(351712, _n_(351711, "self", lambda: self), "root"),text="Choose the format to download",font=("Century Gothic",20))
        _l_(351714)
        _c_(351718, _a_(351717, _a_(351716, _n_(351715, "self", lambda: self), "DownloadSelect"), "grid"))
        _l_(351719)

        _n_(351720, "self", lambda: self).DownloadChoice=[("Audio MP3",1),("Video MP4",2)]
        _l_(351721)

        _n_(351722, "self", lambda: self).Choice=_c_(351724, _n_(351723, "StringVar", lambda: StringVar))
        _l_(351725)
        _c_(351729, _a_(351728, _a_(351727, _n_(351726, "self", lambda: self), "Choice"), "set"), 1)
        _l_(351730)

        for text,mode in _a_(351732, _n_(351731, "self", lambda: self), "DownloadChoice"):
            _l_(351748)

            _n_(351733, "self", lambda: self).YoutubeChoice=_c_(351741, _n_(351734, "Radiobutton", lambda: Radiobutton), _a_(351736, _n_(351735, "self", lambda: self), "root"),text=_n_(351737, "text", lambda: text),font=("Candara",10),variable=_a_(351739, _n_(351738, "self", lambda: self), "Choice"),value=_n_(351740, "mode", lambda: mode))
            _l_(351742)
            _c_(351746, _a_(351745, _a_(351744, _n_(351743, "self", lambda: self), "YoutubeChoice"), "grid"))
            _l_(351747)

        _n_(351749, "self", lambda: self).DownloadButton=_c_(351755, _n_(351750, "Button", lambda: Button), _a_(351752, _n_(351751, "self", lambda: self), "root"),text="Download",font=("Lucida Console",10),command=_a_(351754, _n_(351753, "self", lambda: self), "checkLink"))
        _l_(351756)
        _c_(351760, _a_(351759, _a_(351758, _n_(351757, "self", lambda: self), "DownloadButton"), "grid"), pady=(5,5))
        _l_(351761)

    def checkLink(self):
        _l_(351797)

        _n_(351763, "self", lambda: self).youtubeMatch=_c_(351770, _a_(351765, _n_(351764, "re", lambda: re), "match"), "https://www.youtube.com/",_c_(351769, _a_(351768, _a_(351767, _n_(351766, "self", lambda: self), "YoutubeEntryVar"), "get")))
        _l_(351771)
        if(not _a_(351773, _n_(351772, "self", lambda: self), "youtubeMatch")):
            _l_(351796)

            _c_(351777, _a_(351776, _a_(351775, _n_(351774, "self", lambda: self), "YoutubeEntryError"), "config"), text="Please choose a valid YouTube link !!")
            _l_(351778)

        elif(not _a_(351780, _n_(351779, "self", lambda: self), "FolderName")):
            _l_(351795)

            _c_(351784, _a_(351783, _a_(351782, _n_(351781, "self", lambda: self), "FileLocation"), "config"), text="Please choose a directory !!",fg="red")
            _l_(351785)

        elif(_a_(351787, _n_(351786, "self", lambda: self), "youtubeMatch") and _a_(351789, _n_(351788, "self", lambda: self), "FolderName")):
            _l_(351794)

            _c_(351792, _a_(351791, _n_(351790, "self", lambda: self), "downloadFile"))
            _l_(351793)

    def downloadFile(self):
        _l_(351840)

        _n_(351798, "self", lambda: self).newWindow=_c_(351802, _n_(351799, "Toplevel", lambda: Toplevel), _a_(351801, _n_(351800, "self", lambda: self), "root"))
        _l_(351803)
        _c_(351807, _a_(351806, _a_(351805, _n_(351804, "self", lambda: self), "root"), "withdraw"))
        _l_(351808)
        _c_(351812, _a_(351811, _a_(351810, _n_(351809, "self", lambda: self), "newWindow"), "state"), "zoomed")
        _l_(351813)
        _c_(351817, _a_(351816, _a_(351815, _n_(351814, "self", lambda: self), "newWindow"), "grid_rowconfigure"), 0,weight=2)
        _l_(351818)
        _c_(351822, _a_(351821, _a_(351820, _n_(351819, "self", lambda: self), "newWindow"), "grid_columnconfigure"), 0,weight=1)
        _l_(351823)



        _n_(351824, "self", lambda: self).app=_c_(351838, _n_(351825, "Second", lambda: Second), _a_(351827, _n_(351826, "self", lambda: self), "newWindow"),_c_(351831, _a_(351830, _a_(351829, _n_(351828, "self", lambda: self), "YoutubeEntryVar"), "get")),_a_(351833, _n_(351832, "self", lambda: self), "FolderName"),_c_(351837, _a_(351836, _a_(351835, _n_(351834, "self", lambda: self), "Choice"), "get")))
        _l_(351839)


    def FileDirectory(self):
        _l_(351864)

        _n_(351841, "self", lambda: self).FolderName=_c_(351844, _a_(351843, _n_(351842, "filedialog", lambda: filedialog), "askdirectory"))
        _l_(351845)

        if(_c_(351849, _n_(351846, "len", lambda: len), _a_(351848, _n_(351847, "self", lambda: self), "FolderName"))>0):
            _l_(351863)

            _c_(351855, _a_(351852, _a_(351851, _n_(351850, "self", lambda: self), "FileLocation"), "config"), text=_a_(351854, _n_(351853, "self", lambda: self), "FolderName"),fg="green")
            _l_(351856)
            aux = True
            _l_(351857)
            return aux
        else:
            _c_(351861, _a_(351860, _a_(351859, _n_(351858, "self", lambda: self), "FileLocation"), "config"), text="Please choose a directory !!",fg="red")
            _l_(351862)

class Second:
    _l_(352066)

    def __init__(self,downloadWindow,youtubeLink,foldername,FileChoice):
        _l_(351973)

        _n_(351866, "self", lambda: self).downloadWindow=_n_(351867, "downloadWindow", lambda: downloadWindow)
        _l_(351868)
        _n_(351869, "self", lambda: self).youtubeLink=_n_(351870, "youtubeLink", lambda: youtubeLink)
        _l_(351871)
        _n_(351872, "self", lambda: self).foldername=_n_(351873, "foldername", lambda: foldername)
        _l_(351874)
        _n_(351875, "self", lambda: self).FileChoice=_n_(351876, "FileChoice", lambda: FileChoice)
        _l_(351877)

        _n_(351878, "self", lambda: self).yt=_c_(351882, _n_(351879, "YouTube", lambda: YouTube), _a_(351881, _n_(351880, "self", lambda: self), "youtubeLink"))
        _l_(351883)
        if(_n_(351884, "FileChoice", lambda: FileChoice)=='1'):
            _l_(351899)

            _n_(351885, "self", lambda: self).videoType=_c_(351892, _a_(351891, _c_(351890, _a_(351889, _a_(351888, _a_(351887, _n_(351886, "self", lambda: self), "yt"), "streams"), "filter"), only_audio=True), "first"))
            _l_(351893)
            _n_(351894, "self", lambda: self).MaxfileSize=_a_(351897, _a_(351896, _n_(351895, "self", lambda: self), "videoType"), "filesize")
            _l_(351898)
        if(_n_(351900, "FileChoice", lambda: FileChoice)=='2'):
            _l_(351913)

            _n_(351901, "self", lambda: self).videoType=_c_(351906, _a_(351905, _a_(351904, _a_(351903, _n_(351902, "self", lambda: self), "yt"), "streams"), "first"))
            _l_(351907)
            _n_(351908, "self", lambda: self).MaxfileSize=_a_(351911, _a_(351910, _n_(351909, "self", lambda: self), "videoType"), "filesize")
            _l_(351912)

        _n_(351914, "self", lambda: self).Loading=_c_(351918, _n_(351915, "Label", lambda: Label), _a_(351917, _n_(351916, "self", lambda: self), "downloadWindow"),text="Download in Progress.........",font=("Agency FB",40))
        _l_(351919)
        _c_(351923, _a_(351922, _a_(351921, _n_(351920, "self", lambda: self), "Loading"), "grid"))
        _l_(351924)

        _n_(351925, "self", lambda: self).percent=_c_(351929, _n_(351926, "Label", lambda: Label), _a_(351928, _n_(351927, "self", lambda: self), "downloadWindow"),text="0",font=("Agency FB",20))
        _l_(351930)
        _c_(351934, _a_(351933, _a_(351932, _n_(351931, "self", lambda: self), "percent"), "grid"))
        _l_(351935)

        _n_(351936, "self", lambda: self).progressBar=_c_(351941, _a_(351938, _n_(351937, "ttk", lambda: ttk), "Progressbar"), _a_(351940, _n_(351939, "self", lambda: self), "downloadWindow"),length=500,orient='horizontal',mode='indeterminate')
        _l_(351942)
        _c_(351946, _a_(351945, _a_(351944, _n_(351943, "self", lambda: self), "progressBar"), "grid"), pady=(50,0))
        _l_(351947)
        _c_(351951, _a_(351950, _a_(351949, _n_(351948, "self", lambda: self), "progressBar"), "start"))
        _l_(351952)

        _c_(351963, _a_(351962, _c_(351961, _a_(351954, _n_(351953, "threading", lambda: threading), "Thread"), target=_c_(351960, _a_(351957, _a_(351956, _n_(351955, "self", lambda: self), "yt"), "register_on_progress_callback"), _a_(351959, _n_(351958, "self", lambda: self), "show_Pregress"))), "start"))
        _l_(351964)

        _c_(351971, _a_(351970, _c_(351969, _a_(351966, _n_(351965, "threading", lambda: threading), "Thread"), target=_a_(351968, _n_(351967, "self", lambda: self), "downloadfile")), "start"))
        _l_(351972)

    def downloadfile(self):
        _l_(352004)

        if(_a_(351975, _n_(351974, "self", lambda: self), "FileChoice")=='1'):
            _l_(351988)

            _c_(351986, _a_(351983, _c_(351982, _a_(351981, _c_(351980, _a_(351979, _a_(351978, _a_(351977, _n_(351976, "self", lambda: self), "yt"), "streams"), "filter"), only_audio=True), "first")), "download"), _a_(351985, _n_(351984, "self", lambda: self), "foldername"))
            _l_(351987)
        if(_a_(351990, _n_(351989, "self", lambda: self), "FileChoice")=='2'):
            _l_(352003)

            _c_(352001, _a_(351998, _c_(351997, _a_(351996, _c_(351995, _a_(351994, _a_(351993, _a_(351992, _n_(351991, "self", lambda: self), "yt"), "streams"), "filter")), "first")), "download"), _a_(352000, _n_(351999, "self", lambda: self), "foldername"))
            _l_(352002)

    def show_Pregress(self,streams=None,Chunks=None,filehandle=None,bytes_remaining=None):
        _l_(352065)


        percentCount = _c_(352009, _n_(352005, "float", lambda: float), "%0.2f"% (100 - (100*(_n_(352006, "bytes_remaining", lambda: bytes_remaining)/_a_(352008, _n_(352007, "self", lambda: self), "MaxfileSize")))))
        _l_(352010)

        if(_n_(352011, "percentCount", lambda: percentCount)<100):
            _l_(352035)


            _c_(352018, _a_(352014, _a_(352013, _n_(352012, "self", lambda: self), "percent"), "config"), text=_c_(352017, _n_(352015, "str", lambda: str), _n_(352016, "percentCount", lambda: percentCount)))
            _l_(352019)

        else:
            _c_(352023, _a_(352022, _a_(352021, _n_(352020, "self", lambda: self), "progressBar"), "stop"))
            _l_(352024)
            _c_(352028, _a_(352027, _a_(352026, _n_(352025, "self", lambda: self), "Loading"), "forget"))
            _l_(352029)
            _c_(352033, _a_(352032, _a_(352031, _n_(352030, "self", lambda: self), "progressBar"), "forget"))
            _l_(352034)

        _n_(352036, "self", lambda: self).downloadfinished=_c_(352040, _n_(352037, "Label", lambda: Label), _a_(352039, _n_(352038, "self", lambda: self), "downloadWindow"),text="Download Finished",font=("ALGERIAN",20))
        _l_(352041)
        _c_(352047, _a_(352044, _a_(352043, _n_(352042, "self", lambda: self), "downloadfinished"), "grid"), _c_(352046, _n_(352045, "pady", lambda: pady), 150,0))
        _l_(352048)

        _n_(352049, "self", lambda: self).downloadfile=_c_(352056, _n_(352050, "Label", lambda: Label), _a_(352052, _n_(352051, "self", lambda: self), "downloadWindow"),text=_a_(352055, _a_(352054, _n_(352053, "self", lambda: self), "yt"), "title"),font=("ALGERIAN",20))
        _l_(352057)
        _c_(352063, _a_(352060, _a_(352059, _n_(352058, "self", lambda: self), "downloadfile"), "grid"), _c_(352062, _n_(352061, "pady", lambda: pady), 50,0))
        _l_(352064)









if _n_(352067, "__name__", lambda: __name__)=="__main__":
    _l_(352086)


    window=_c_(352069, _n_(352068, "Tk", lambda: Tk))
    _l_(352070)
    _c_(352073, _a_(352072, _n_(352071, "window", lambda: window), "title"), "YouTube Download Manager")
    _l_(352074)
    _c_(352077, _a_(352076, _n_(352075, "window", lambda: window), "state"), "zoomed")
    _l_(352078)

    app=_c_(352081, _n_(352079, "Application", lambda: Application), _n_(352080, "window", lambda: window))
    _l_(352082)

    _c_(352084, _n_(352083, "mainloop", lambda: mainloop))
    _l_(352085)