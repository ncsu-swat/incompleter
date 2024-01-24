# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64211907/incomprehensible-name-error-using-class-variables-within-a-class-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(536961)

except ImportError:
    pass
try:
    from better_profanity import profanity
    _l_(536963)

except ImportError:
    pass


class Profanity(_n_(536964, "object", lambda: object)):
    _l_(537092)


    # Wordlist file paths for languages
    eng = "/home/mareike/sw_filter/wordlists/google_profanity_wordlist_eng.txt"
    _l_(536965)
    deu = "/home/mareike/sw_filter/wordlists/profanity_wordlist_deu.txt"
    _l_(536966)
    # Further language variables...

    

    def __init__(self, transcript_filename, wordlist_language):
        _l_(536973)

        _n_(536967, "self", lambda: self).transcript_filename = _n_(536968, "transcript_filename", lambda: transcript_filename)
        _l_(536969)
        _n_(536970, "self", lambda: self).wordlist_language = _n_(536971, "wordlist_language", lambda: wordlist_language)
        _l_(536972)
    def load_transcript(self):
        _l_(536989)

        f = _c_(536977, _n_(536974, "open", lambda: open), _a_(536976, _n_(536975, "self", lambda: self), "transcript_filename"), "r")
        _l_(536978)
        file = _c_(536981, _a_(536980, _n_(536979, "f", lambda: f), "read"))
        _l_(536982)
        _c_(536985, _a_(536984, _n_(536983, "f", lambda: f), "close"))
        _l_(536986)
        aux = _n_(536987, "file", lambda: file)
        _l_(536988)

        return aux
    

    def load_wordlist(self):
        _l_(537005)

        f = _c_(536993, _n_(536990, "open", lambda: open), _a_(536992, _n_(536991, "self", lambda: self), "wordlist_language"), "r")
        _l_(536994)
        file = _c_(536997, _a_(536996, _n_(536995, "f", lambda: f), "read"))
        _l_(536998)
        _c_(537001, _a_(537000, _n_(536999, "f", lambda: f), "close"))
        _l_(537002)
        aux = _n_(537003, "file", lambda: file)
        _l_(537004)

        return aux


    def preprocess(self):
        _l_(537075)

        # Remove noisy punctuation
        prep_transcript = _c_(537010, _a_(537009, _c_(537008, _a_(537007, _n_(537006, "transcript", lambda: transcript), "replace"), '--', ''), "replace"), '>', '')
        _l_(537011)
        prep_transcript = _c_(537016, _a_(537015, _c_(537014, _a_(537013, _n_(537012, "prep_transcript", lambda: prep_transcript), "replace"), '[', ''), "replace"), ']', '')
        _l_(537017)
        prep_transcript = _c_(537022, _a_(537021, _c_(537020, _a_(537019, _n_(537018, "prep_transcript", lambda: prep_transcript), "replace"), '(', ''), "replace"), ')', '')
        _l_(537023)
        prep_transcript = _c_(537026, _a_(537025, _n_(537024, "prep_transcript", lambda: prep_transcript), "replace"), "'", '')
        _l_(537027)
        prep_transcript = _c_(537030, _a_(537029, _n_(537028, "prep_transcript", lambda: prep_transcript), "replace"), '.', '')
        _l_(537031)
        prep_transcript = _c_(537034, _a_(537033, _n_(537032, "prep_transcript", lambda: prep_transcript), "replace"), ';', '')
        _l_(537035)
        prep_transcript = _c_(537038, _a_(537037, _n_(537036, "prep_transcript", lambda: prep_transcript), "replace"), '!', '')
        _l_(537039)
        prep_transcript = _c_(537042, _a_(537041, _n_(537040, "prep_transcript", lambda: prep_transcript), "replace"), '?', '')
        _l_(537043)
        prep_transcript = _c_(537046, _a_(537045, _n_(537044, "prep_transcript", lambda: prep_transcript), "replace"), '-', ' ')
        _l_(537047)
        prep_transcript = _c_(537053, _a_(537049, _n_(537048, "re", lambda: re), "sub"), r":\B", "", _n_(537050, "prep_transcript", lambda: prep_transcript), flags = _a_(537052, _n_(537051, "re", lambda: re), "MULTILINE"))
        _l_(537054)
        prep_transcript = _c_(537060, _a_(537056, _n_(537055, "re", lambda: re), "sub"), r",\D\b", " ", _n_(537057, "prep_transcript", lambda: prep_transcript), flags = _a_(537059, _n_(537058, "re", lambda: re), "MULTILINE"))
        _l_(537061)
        prep_transcript = _c_(537067, _a_(537063, _n_(537062, "re", lambda: re), "sub"), r",\n", "\n", _n_(537064, "prep_transcript", lambda: prep_transcript), flags = _a_(537066, _n_(537065, "re", lambda: re), "MULTILINE"))
        _l_(537068)

        # Lowercase text
        prep_transcript = _c_(537071, _a_(537070, _n_(537069, "prep_transcript", lambda: prep_transcript), "lower"))
        _l_(537072)
        aux = _n_(537073, "prep_transcript", lambda: prep_transcript)
        _l_(537074)

        return aux


    def apply_filter(self, prep_transcript):
        _l_(537091)

        if _n_(537076, "__name__", lambda: __name__) == "__main__":
            _l_(537088)

            _c_(537081, _a_(537078, _n_(537077, "profanity", lambda: profanity), "load_censor_words_from_file"), _a_(537080, _n_(537079, "self", lambda: self), "wordlist_language"))                                                                                                             
            _l_(537082)                                                                                                             
            censored_transcript = _c_(537086, _a_(537084, _n_(537083, "profanity", lambda: profanity), "censor"), _n_(537085, "prep_transcript", lambda: prep_transcript))
            _l_(537087)
        aux = _n_(537089, "censored_transcript", lambda: censored_transcript)
        _l_(537090)

        return aux


p = _c_(537095, _n_(537093, "Profanity", lambda: Profanity), "sample_transcript.txt", _n_(537094, "eng", lambda: eng))
_l_(537096)

transcript = _c_(537099, _a_(537098, _n_(537097, "p", lambda: p), "load_transcript"))
_l_(537100)
wordlist = _c_(537103, _a_(537102, _n_(537101, "p", lambda: p), "load_wordlist"))
_l_(537104)
prep_transcript = _c_(537107, _a_(537106, _n_(537105, "p", lambda: p), "preprocess"))
_l_(537108)

censored_transcript = _c_(537112, _a_(537110, _n_(537109, "p", lambda: p), "apply_filter"), _n_(537111, "prep_transcript", lambda: prep_transcript))
_l_(537113)
_c_(537116, _n_(537114, "print", lambda: print), _n_(537115, "censored_transcript", lambda: censored_transcript))
_l_(537117)