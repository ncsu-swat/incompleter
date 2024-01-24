# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65333888/attributeerror-int-object-has-no-attribute-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(449863)

except ImportError:
    pass
try:
    import random
    _l_(449865)

except ImportError:
    pass
try:
    import genanki
    _l_(449867)

except ImportError:
    pass

# Filename of the data file
data_filename = _c_(449871, _n_(449868, "str", lambda: str), _c_(449870, _n_(449869, "input", lambda: input), "Enter input file name with extension: "))
_l_(449872)

# Filename of the Anki deck to generate
deck_filename = _c_(449875, _a_(449874, _n_(449873, "data_filename", lambda: data_filename), "split"), '.')[0] + ".apkg"
_l_(449876)

# Title of the deck as shown in Anki
anki_deck_title = _c_(449879, _a_(449878, _n_(449877, "data_filename", lambda: data_filename), "split"), '.')[0]
_l_(449880)

# Name of the card model
anki_model_name = "Modelname"
_l_(449881)

# Create the deck model

model_id = _c_(449884, _a_(449883, _n_(449882, "random", lambda: random), "randrange"), 1 << 30, 1 << 31)
_l_(449885)

style = """
.card {
 font-family: arial;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
"""
_l_(449886)

anki_model = _c_(449892, _a_(449888, _n_(449887, "genanki", lambda: genanki), "Model"), _n_(449889, "model_id", lambda: model_id),
    _n_(449890, "anki_model_name", lambda: anki_model_name),
    fields=[{"name": "front"}, {"name": "back"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": '{{front}}',
            "afmt": '{{FrontSide}}<hr id="answer">{{back}}</p>',
        },
    ],
    css=_n_(449891, "style", lambda: style),
)
_l_(449893)

# The list of flashcards
anki_notes = []
_l_(449894)

with _c_(449897, _n_(449895, "open", lambda: open), _n_(449896, "data_filename", lambda: data_filename), "r", encoding="utf-8") as csv_file:
    _l_(449917)


    csv_reader = _c_(449901, _a_(449899, _n_(449898, "csv", lambda: csv), "reader"), _n_(449900, "csv_file", lambda: csv_file), delimiter=";")
    _l_(449902)

    for row in _n_(449903, "csv_reader", lambda: csv_reader):
        _l_(449916)

        anki_note = _c_(449909, _a_(449905, _n_(449904, "genanki", lambda: genanki), "Note"), model=_n_(449906, "anki_model", lambda: anki_model),
            fields=[_n_(449907, "row", lambda: row)[0], _n_(449908, "row", lambda: row)[1]]
        )
        _l_(449910)
        _c_(449914, _a_(449912, _n_(449911, "anki_notes", lambda: anki_notes), "append"), _n_(449913, "anki_note", lambda: anki_note))
        _l_(449915)

for subdeck in _c_(449926, _n_(449918, "range", lambda: range), _c_(449925, _n_(449919, "int", lambda: int), _c_(449924, _n_(449920, "round", lambda: round), (_c_(449923, _n_(449921, "len", lambda: len), _n_(449922, "anki_notes", lambda: anki_notes))/1000)+0,5))):
    _l_(449966)

    anki_deck = _c_(449937, _a_(449928, _n_(449927, "genanki", lambda: genanki), "Deck"), _n_(449929, "model_id", lambda: model_id), _n_(449930, "anki_deck_title", lambda: anki_deck_title)+" "+_c_(449933, _n_(449931, "str", lambda: str), (_n_(449932, "subdeck", lambda: subdeck)-1)*1000+1)+"-"+_c_(449936, _n_(449934, "str", lambda: str), _n_(449935, "subdeck", lambda: subdeck)*1000))
    _l_(449938)
    anki_package = _c_(449942, _a_(449940, _n_(449939, "genanki", lambda: genanki), "Package"), _n_(449941, "anki_deck", lambda: anki_deck))
    _l_(449943)

    # Add flashcards to the deck
    for anki_note in _c_(449945, _n_(449944, "range", lambda: range), 1000):
        _l_(449951)

        _c_(449949, _a_(449947, _n_(449946, "anki_deck", lambda: anki_deck), "add_note"), _n_(449948, "anki_note", lambda: anki_note))
        _l_(449950)

    # Save the deck to a file
    _c_(449955, _a_(449953, _n_(449952, "anki_package", lambda: anki_package), "write_to_file"), _n_(449954, "deck_filename", lambda: deck_filename))
    _l_(449956)
    _c_(449964, _n_(449957, "print", lambda: print), _c_(449963, _a_(449958, "Created deck with {} flashcards", "format"), _c_(449962, _n_(449959, "len", lambda: len), _a_(449961, _n_(449960, "anki_deck", lambda: anki_deck), "notes"))))
    _l_(449965)