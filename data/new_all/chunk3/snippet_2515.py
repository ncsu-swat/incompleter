# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73849859/attributeerror-table-n-a-m-e-object-has-no-attribute-getbestfullname-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fpdf import FPDF
    _l_(563290)

except ImportError:
    pass

pdf = _c_(563292, _n_(563291, "FPDF", lambda: FPDF))
_l_(563293)
_c_(563296, _a_(563295, _n_(563294, "pdf", lambda: pdf), "add_page"))
_l_(563297)

# Add a DejaVu Unicode font (uses UTF-8)
# Supports more than 200 languages. For a coverage status see:
# http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
_c_(563300, _a_(563299, _n_(563298, "pdf", lambda: pdf), "add_font"), 'DejaVu', fname='DejaVuSansCondensed.ttf')
_l_(563301)
_c_(563304, _a_(563303, _n_(563302, "pdf", lambda: pdf), "set_font"), 'DejaVu', size=14)
_l_(563305)

text = u"""
English: Hello World
Greek: Γειά σου κόσμος
Polish: Witaj świecie
Portuguese: Olá mundo
Russian: Здравствуй, Мир
Vietnamese: Xin chào thế giới
Arabic: مرحبا العالم
Hebrew: שלום עולם
"""
_l_(563306)

for txt in _c_(563309, _a_(563308, _n_(563307, "text", lambda: text), "split"), '\n'):
    _l_(563319)

    _c_(563313, _a_(563311, _n_(563310, "pdf", lambda: pdf), "write"), 8, _n_(563312, "txt", lambda: txt))
    _l_(563314)
    _c_(563317, _a_(563316, _n_(563315, "pdf", lambda: pdf), "ln"), 8)
    _l_(563318)

# Add a Indic Unicode font (uses UTF-8)
# Supports: Bengali, Devanagari, Gujarati, 
#           Gurmukhi (including the variants for Punjabi) 
#           Kannada, Malayalam, Oriya, Tamil, Telugu, Tibetan
_c_(563322, _a_(563321, _n_(563320, "pdf", lambda: pdf), "add_font"), 'gargi', fname='gargi.ttf')
_l_(563323)
_c_(563326, _a_(563325, _n_(563324, "pdf", lambda: pdf), "set_font"), 'gargi', size=14)
_l_(563327)
_c_(563330, _a_(563329, _n_(563328, "pdf", lambda: pdf), "write"), 8, u'Hindi: नमस्ते दुनिया')
_l_(563331)
_c_(563334, _a_(563333, _n_(563332, "pdf", lambda: pdf), "ln"), 20)
_l_(563335)

# Add a AR PL New Sung Unicode font (uses UTF-8)
# The Open Source Chinese Font (also supports other east Asian languages)
_c_(563338, _a_(563337, _n_(563336, "pdf", lambda: pdf), "add_font"), 'fireflysung', fname='fireflysung.ttf')
_l_(563339)
_c_(563342, _a_(563341, _n_(563340, "pdf", lambda: pdf), "set_font"), 'fireflysung', size=14)
_l_(563343)
_c_(563346, _a_(563345, _n_(563344, "pdf", lambda: pdf), "write"), 8, u'Chinese: 你好世界\n')
_l_(563347)
_c_(563350, _a_(563349, _n_(563348, "pdf", lambda: pdf), "write"), 8, u'Japanese: こんにちは世界\n')
_l_(563351)
_c_(563354, _a_(563353, _n_(563352, "pdf", lambda: pdf), "ln"), 10)
_l_(563355)

# Add a Alee Unicode font (uses UTF-8)
# General purpose Hangul truetype fonts that contain Korean syllable 
# and Latin9 (iso8859-15) characters.
_c_(563358, _a_(563357, _n_(563356, "pdf", lambda: pdf), "add_font"), 'eunjin', fname='Eunjin.ttf')
_l_(563359)
_c_(563362, _a_(563361, _n_(563360, "pdf", lambda: pdf), "set_font"), 'eunjin', size=14)
_l_(563363)
_c_(563366, _a_(563365, _n_(563364, "pdf", lambda: pdf), "write"), 8, u'Korean: 안녕하세요')
_l_(563367)
_c_(563370, _a_(563369, _n_(563368, "pdf", lambda: pdf), "ln"), 20)
_l_(563371)

# Add a Fonts-TLWG (formerly ThaiFonts-Scalable) (uses UTF-8)
_c_(563374, _a_(563373, _n_(563372, "pdf", lambda: pdf), "add_font"), 'waree', fname='Waree.ttf')
_l_(563375)
_c_(563378, _a_(563377, _n_(563376, "pdf", lambda: pdf), "set_font"), 'waree', size=14)
_l_(563379)
_c_(563382, _a_(563381, _n_(563380, "pdf", lambda: pdf), "write"), 8, u'Thai: สวัสดีชาวโลก')
_l_(563383)
_c_(563386, _a_(563385, _n_(563384, "pdf", lambda: pdf), "ln"), 20)
_l_(563387)

# Select a standard font (uses windows-1252)
_c_(563390, _a_(563389, _n_(563388, "pdf", lambda: pdf), "set_font"), 'helvetica', size=14)
_l_(563391)
_c_(563394, _a_(563393, _n_(563392, "pdf", lambda: pdf), "ln"), 10)
_l_(563395)
_c_(563398, _a_(563397, _n_(563396, "pdf", lambda: pdf), "write"), 5, 'This is standard built-in font')
_l_(563399)

_c_(563402, _a_(563401, _n_(563400, "pdf", lambda: pdf), "output"), "unicode.pdf")
_l_(563403)