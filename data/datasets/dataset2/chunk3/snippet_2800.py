#Source: https://stackoverflow.com/questions/73849859/attributeerror-table-n-a-m-e-object-has-no-attribute-getbestfullname-error
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add a DejaVu Unicode font (uses UTF-8)
# Supports more than 200 languages. For a coverage status see:
# http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=14)

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

for txt in text.split('\n'):
    pdf.write(8, txt)
    pdf.ln(8)

# Add a Indic Unicode font (uses UTF-8)
# Supports: Bengali, Devanagari, Gujarati, 
#           Gurmukhi (including the variants for Punjabi) 
#           Kannada, Malayalam, Oriya, Tamil, Telugu, Tibetan
pdf.add_font('gargi', fname='gargi.ttf')
pdf.set_font('gargi', size=14)
pdf.write(8, u'Hindi: नमस्ते दुनिया')
pdf.ln(20)

# Add a AR PL New Sung Unicode font (uses UTF-8)
# The Open Source Chinese Font (also supports other east Asian languages)
pdf.add_font('fireflysung', fname='fireflysung.ttf')
pdf.set_font('fireflysung', size=14)
pdf.write(8, u'Chinese: 你好世界\n')
pdf.write(8, u'Japanese: こんにちは世界\n')
pdf.ln(10)

# Add a Alee Unicode font (uses UTF-8)
# General purpose Hangul truetype fonts that contain Korean syllable 
# and Latin9 (iso8859-15) characters.
pdf.add_font('eunjin', fname='Eunjin.ttf')
pdf.set_font('eunjin', size=14)
pdf.write(8, u'Korean: 안녕하세요')
pdf.ln(20)

# Add a Fonts-TLWG (formerly ThaiFonts-Scalable) (uses UTF-8)
pdf.add_font('waree', fname='Waree.ttf')
pdf.set_font('waree', size=14)
pdf.write(8, u'Thai: สวัสดีชาวโลก')
pdf.ln(20)

# Select a standard font (uses windows-1252)
pdf.set_font('helvetica', size=14)
pdf.ln(10)
pdf.write(5, 'This is standard built-in font')

pdf.output("unicode.pdf")