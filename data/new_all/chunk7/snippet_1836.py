# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51282756/typeerror-bufsize-must-be-an-integer
    #! /usr/local/bin/python3 python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, sys, re, subprocess
    _l_(433914)

except ImportError:
    pass


def read_txt(filepath, suffix=".txt"):
    _l_(433942)

    """
    Reads and returns the contents of a MCMakeProblem compatible text file,
    after replacing "#filename"-line in the contents.
    :param filepath:
    :param suffix:
    :return:
    """
    filename = _c_(433917, _a_(433916, _n_(433915, "filepath", lambda: filepath), "split"), "/")[-1][:-_c_(433920, _n_(433918, "len", lambda: len), _n_(433919, "suffix", lambda: suffix))]  # The filename without the suffix and the preceding path
    _l_(433921)  # The filename without the suffix and the preceding path
    _c_(433924, _n_(433922, "print", lambda: print), _n_(433923, "filename", lambda: filename))
    _l_(433925)
    with _c_(433928, _n_(433926, "open", lambda: open), f"{_n_(433927, 'filepath', lambda: filepath)}", 'r') as f:
        _l_(433939)

        filecontents = _c_(433931, _a_(433930, _n_(433929, "f", lambda: f), "read"))
        _l_(433932)
        filecontents = _c_(433937, _a_(433934, _n_(433933, "re", lambda: re), "sub"), r"#filename (.*)\n", f"#filename {_n_(433935, 'filename', lambda: filename)}\n", _n_(433936, "filecontents", lambda: filecontents))
        _l_(433938)
    aux = _n_(433940, "filecontents", lambda: filecontents)
    _l_(433941)
    # print(filecontents)
    return aux


def create_HTML_folder(directory="./HTMLfiles"):
    _l_(433956)

    """
    Creates a directory for a HTML file if it doesn't already exist.
    :param directory:
    :return:
    """
    try:
        _l_(433955)

        _c_(433944, _n_(433943, "print", lambda: print), "Attempting to create a folder for the HTML files...")
        _l_(433945)
        _c_(433949, _a_(433947, _n_(433946, "os", lambda: os), "mkdir"), _n_(433948, "directory", lambda: directory))
        _l_(433950)
    except:
        _l_(433954)

        _c_(433952, _n_(433951, "print", lambda: print), "The folder already exists. Moving along...")
        _l_(433953)


def redirect_HTML(htmlfile, destination="./HTMLfiles"):
    _l_(433964)

    """
    This is for cleaning purposes. Moves a give HTML file to a sub-directory.
    :param htmlfile:
    :param destination:
    :return:
    """
    _c_(433962, _a_(433958, _n_(433957, "os", lambda: os), "rename"), _n_(433959, "htmlfile", lambda: htmlfile), f"{_n_(433960, 'destination', lambda: destination)}/{_n_(433961, 'htmlfile', lambda: htmlfile)}")
    _l_(433963)


def feed_txt_to_MakeProblem(filecontents):
    _l_(433983)

    """
    Feeds the contents of a text file WITH A SINGLE PROBLEM to the MCMakeProblem-script.
    :param filecontents:
    :return:
    """
    _c_(433967, _n_(433965, "print", lambda: print), f"\nFile contents:\n"
          f"--------------\n"
          f"{_n_(433966, 'filecontents', lambda: filecontents)}\n\n")
    _l_(433968)
    try:
        _l_(433982)

        _c_(433970, _n_(433969, "print", lambda: print), "Feeding the contents of a text file to MCMakeProblem...")
        _l_(433971)
        _c_(433975, _a_(433973, _n_(433972, "subprocess", lambda: subprocess), "run"), ["./MCMakeProblem"], _n_(433974, "filecontents", lambda: filecontents), encoding="UTF8")
        _l_(433976)
    except:
        _l_(433981)

        _c_(433978, _n_(433977, "print", lambda: print), "... aaaand something went wrong")
        _l_(433979)
        raise
        _l_(433980)


def read_html_for_assignments(htmlfile, suffix=".html"):
    _l_(434006)

    """
    Reads and returns the assignment text and MathCheck-code from a MakeProblem-generated HTML-file.
    :param htmlfile:
    :param suffix:
    :return:
    """
    assignments = _c_(433987, _a_(433985, _n_(433984, "re", lambda: re), "findall"), "<tr><td class=ifrl>[\s\S]+?\d+.[\s\S]+?</textarea>", _n_(433986, "htmlfile", lambda: htmlfile))
    _l_(433988)
    assignment = _c_(433994, _a_(433989, "", "join"), _c_(433993, _a_(433991, _n_(433990, "re", lambda: re), "findall"), r'\d+\.(?:(?:\s+)?[A-Ö][\s\S]+?[.?])+', _n_(433992, "assignments", lambda: assignments)))
    _l_(433995)
    mccode = _c_(433999, _a_(433997, _n_(433996, "re", lambda: re), "findall"), "verbose_off\s*[\s\S]*?</textarea>", _n_(433998, "assignment", lambda: assignment))[0][:-_c_(434001, _n_(434000, "len", lambda: len), "\n</textarea>"):]
    _l_(434002)
    aux = _n_(434003, "assignment", lambda: assignment), _n_(434004, "mccode", lambda: mccode)
    _l_(434005)

    return aux


def write_txt(contents, destination):
    _l_(434017)

    """
    Writes the given contents to a destination file.
    :param contents:
    :param destination:
    :return:
    """
    with _c_(434009, _n_(434007, "open", lambda: open), _n_(434008, "destination", lambda: destination), "w") as f:
        _l_(434015)

        _c_(434013, _a_(434011, _n_(434010, "f", lambda: f), "write"), _n_(434012, "contents", lambda: contents))
        _l_(434014)
    aux = ""
    _l_(434016)
    return aux


def generate(filename, destination):
    _l_(434056)

    _c_(434019, _n_(434018, "print", lambda: print), "\nGenerating a problem...\n")
    _l_(434020)
    # filename = str(filename)
    filecontents = _c_(434023, _n_(434021, "read_txt", lambda: read_txt), _n_(434022, "filename", lambda: filename))
    _l_(434024)
    _c_(434026, _n_(434025, "create_HTML_folder", lambda: create_HTML_folder))
    _l_(434027)
    _c_(434030, _n_(434028, "feed_txt_to_MakeProblem", lambda: feed_txt_to_MakeProblem), _n_(434029, "filecontents", lambda: filecontents))  # A html-file is put out by this line
    _l_(434031)  # A html-file is put out by this line
    _c_(434033, _n_(434032, "create_HTML_folder", lambda: create_HTML_folder))
    _l_(434034)
    _c_(434037, _n_(434035, "redirect_HTML", lambda: redirect_HTML), f"./{_n_(434036, 'filename', lambda: filename)}1.html")  # The created html-file is moved to a sub-folder
    _l_(434038)  # The created html-file is moved to a sub-folder
    assignment, mccode = _c_(434041, _n_(434039, "read_html_for_assignments", lambda: read_html_for_assignments), f"./HTMLfiles/{_n_(434040, 'filename', lambda: filename)}1.html")
    _l_(434042)

    _c_(434046, _n_(434043, "write_txt", lambda: write_txt), _n_(434044, "assignment", lambda: assignment), f"{_n_(434045, 'destination', lambda: destination)}/instructions.txt")
    _l_(434047)
    _c_(434051, _n_(434048, "write_txt", lambda: write_txt), _n_(434049, "mccode", lambda: mccode), f"{_n_(434050, 'destination', lambda: destination)}/mccode.txt")
    _l_(434052)
    _c_(434054, _n_(434053, "print", lambda: print), "... done.")
    _l_(434055)


testfile = "./TxtFiles/testi.txt"
_l_(434057)
testdest = "./tehtavat/testi/00/"
_l_(434058)

_c_(434060, _n_(434059, "print", lambda: print))
_l_(434061)
_c_(434063, _n_(434062, "print", lambda: print))
_l_(434064)
filename = _n_(434065, "testfile", lambda: testfile)  # sys.argv[1]
_l_(434066)  # sys.argv[1]
_c_(434069, _n_(434067, "print", lambda: print), _n_(434068, "filename", lambda: filename))
_l_(434070)
destination = _n_(434071, "testdest", lambda: testdest)  # sys.argv[2]
_l_(434072)  # sys.argv[2]
_c_(434075, _n_(434073, "print", lambda: print), _n_(434074, "destination", lambda: destination))
_l_(434076)
_c_(434080, _n_(434077, "generate", lambda: generate), _n_(434078, "filename", lambda: filename), _n_(434079, "destination", lambda: destination))
_l_(434081)