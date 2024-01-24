# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74698367/nameerror-name-lemma-from-key-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class _WordNetObject:
    _l_(460145)


    def lemma(self, name, lang="eng"):
        _l_(459571)

        """Return lemma object that matches the name"""
        # cannot simply split on first '.',
        # e.g.: '.45_caliber.a.01..45_caliber'
        separator = _c_(459543, _a_(459542, _c_(459541, _a_(459539, _n_(459538, "SENSENUM_RE", lambda: SENSENUM_RE), "search"), _n_(459540, "name", lambda: name)), "end"))
        _l_(459544)

        synset_name, lemma_name = _n_(459545, "name", lambda: name)[: _n_(459546, "separator", lambda: separator) - 1], _n_(459547, "name", lambda: name)[_n_(459548, "separator", lambda: separator):]
        _l_(459549)

        synset = _c_(459553, _a_(459551, _n_(459550, "self", lambda: self), "synset"), _n_(459552, "synset_name", lambda: synset_name))
        _l_(459554)
        for lemma in _c_(459558, _a_(459556, _n_(459555, "synset", lambda: synset), "lemmas"), _n_(459557, "lang", lambda: lang)):
            _l_(459565)

            if _a_(459560, _n_(459559, "lemma", lambda: lemma), "_name") == _n_(459561, "lemma_name", lambda: lemma_name):
                _l_(459564)

                aux = _n_(459562, "lemma", lambda: lemma)
                _l_(459563)
                return aux
        raise _c_(459569, _n_(459566, "WordNetError", lambda: WordNetError), f"no lemma {_n_(459567, 'lemma_name', lambda: lemma_name)!r} in {_n_(459568, 'synset_name', lambda: synset_name)!r}")
        _l_(459570)

    def lemma_from_key(self, key):
        _l_(459635)

        # Keys are case sensitive and always lower-case
        key = _c_(459574, _a_(459573, _n_(459572, "key", lambda: key), "lower"))
        _l_(459575)

        lemma_name, lex_sense = _c_(459578, _a_(459577, _n_(459576, "key", lambda: key), "split"), "%")
        _l_(459579)
        pos_number, lexname_index, lex_id, _, _ = _c_(459582, _a_(459581, _n_(459580, "lex_sense", lambda: lex_sense), "split"), ":")
        _l_(459583)
        pos = _a_(459585, _n_(459584, "self", lambda: self), "_pos_names")[_c_(459588, _n_(459586, "int", lambda: int), _n_(459587, "pos_number", lambda: pos_number))]
        _l_(459589)

        # open the key -> synset file if necessary
        if _a_(459591, _n_(459590, "self", lambda: self), "_key_synset_file") is None:
            _l_(459597)

            _n_(459592, "self", lambda: self)._key_synset_file = _c_(459595, _a_(459594, _n_(459593, "self", lambda: self), "open"), "index.sense")
            _l_(459596)

        # Find the synset for the lemma.
        synset_line = _c_(459602, _n_(459598, "_binary_search_file", lambda: _binary_search_file), _a_(459600, _n_(459599, "self", lambda: self), "_key_synset_file"), _n_(459601, "key", lambda: key))
        _l_(459603)
        if not _n_(459604, "synset_line", lambda: synset_line):
            _l_(459609)

            raise _c_(459607, _n_(459605, "WordNetError", lambda: WordNetError), "No synset found for key %r" % _n_(459606, "key", lambda: key))
            _l_(459608)
        offset = _c_(459614, _n_(459610, "int", lambda: int), _c_(459613, _a_(459612, _n_(459611, "synset_line", lambda: synset_line), "split"))[1])
        _l_(459615)
        synset = _c_(459620, _a_(459617, _n_(459616, "self", lambda: self), "synset_from_pos_and_offset"), _n_(459618, "pos", lambda: pos), _n_(459619, "offset", lambda: offset))
        _l_(459621)
        # return the corresponding lemma
        for lemma in _a_(459623, _n_(459622, "synset", lambda: synset), "_lemmas"):
            _l_(459630)

            if _a_(459625, _n_(459624, "lemma", lambda: lemma), "_key") == _n_(459626, "key", lambda: key):
                _l_(459629)

                aux = _n_(459627, "lemma", lambda: lemma)
                _l_(459628)
                return aux
        raise _c_(459633, _n_(459631, "WordNetError", lambda: WordNetError), "No lemma found for for key %r" % _n_(459632, "key", lambda: key))
        _l_(459634)

    #############################################################
    # Loading Synsets
    #############################################################
    def synset(self, name):
        _l_(459714)

        # split name into lemma, part of speech and synset number
        lemma, pos, synset_index_str = _c_(459640, _a_(459639, _c_(459638, _a_(459637, _n_(459636, "name", lambda: name), "lower")), "rsplit"), ".", 2)
        _l_(459641)
        synset_index = _c_(459644, _n_(459642, "int", lambda: int), _n_(459643, "synset_index_str", lambda: synset_index_str)) - 1
        _l_(459645)

        # get the offset for this synset
        try:
            _l_(459688)

            offset = _a_(459647, _n_(459646, "self", lambda: self), "_lemma_pos_offset_map")[_n_(459648, "lemma", lambda: lemma)][_n_(459649, "pos", lambda: pos)][_n_(459650, "synset_index", lambda: synset_index)]
            _l_(459651)
        except _n_(459652, "KeyError", lambda: KeyError) as e:
            _l_(459661)

            message = "no lemma %r with part of speech %r"
            _l_(459653)
            raise _c_(459658, _n_(459654, "WordNetError", lambda: WordNetError), _n_(459655, "message", lambda: message) % (_n_(459656, "lemma", lambda: lemma), _n_(459657, "pos", lambda: pos))) from _n_(459659, "e", lambda: e)
            _l_(459660)
        except _n_(459662, "IndexError", lambda: IndexError) as e:
            _l_(459687)

            n_senses = _c_(459668, _n_(459663, "len", lambda: len), _a_(459665, _n_(459664, "self", lambda: self), "_lemma_pos_offset_map")[_n_(459666, "lemma", lambda: lemma)][_n_(459667, "pos", lambda: pos)])
            _l_(459669)
            message = "lemma %r with part of speech %r has only %i %s"
            _l_(459670)
            if _n_(459671, "n_senses", lambda: n_senses) == 1:
                _l_(459680)

                tup = _n_(459672, "lemma", lambda: lemma), _n_(459673, "pos", lambda: pos), _n_(459674, "n_senses", lambda: n_senses), "sense"
                _l_(459675)
            else:
                tup = _n_(459676, "lemma", lambda: lemma), _n_(459677, "pos", lambda: pos), _n_(459678, "n_senses", lambda: n_senses), "senses"
                _l_(459679)
            raise _c_(459684, _n_(459681, "WordNetError", lambda: WordNetError), _n_(459682, "message", lambda: message) % _n_(459683, "tup", lambda: tup)) from _n_(459685, "e", lambda: e)
            _l_(459686)

        # load synset information from the appropriate file
        synset = _c_(459693, _a_(459690, _n_(459689, "self", lambda: self), "synset_from_pos_and_offset"), _n_(459691, "pos", lambda: pos), _n_(459692, "offset", lambda: offset))
        _l_(459694)

        # some basic sanity checks on loaded attributes
        if _n_(459695, "pos", lambda: pos) == "s" and _a_(459697, _n_(459696, "synset", lambda: synset), "_pos") == "a":
            _l_(459704)

            message = (
                "adjective satellite requested but only plain "
                "adjective found for lemma %r"
            )
            _l_(459698)
            raise _c_(459702, _n_(459699, "WordNetError", lambda: WordNetError), _n_(459700, "message", lambda: message) % _n_(459701, "lemma", lambda: lemma))
            _l_(459703)
        assert _a_(459706, _n_(459705, "synset", lambda: synset), "_pos") == _n_(459707, "pos", lambda: pos) or (_n_(459708, "pos", lambda: pos) == "a" and _a_(459710, _n_(459709, "synset", lambda: synset), "_pos") == "s")
        _l_(459711)
        aux = _n_(459712, "synset", lambda: synset)
        _l_(459713)

        # Return the synset object.
        return aux

    def _data_file(self, pos):
        _l_(459742)

        """
        Return an open file pointer for the data file for the given
        part of speech.
        """
        if _n_(459715, "pos", lambda: pos) == _n_(459716, "ADJ_SAT", lambda: ADJ_SAT):
            _l_(459719)

            pos = _n_(459717, "ADJ", lambda: ADJ)
            _l_(459718)
        if _c_(459724, _a_(459722, _a_(459721, _n_(459720, "self", lambda: self), "_data_file_map"), "get"), _n_(459723, "pos", lambda: pos)) is None:
            _l_(459737)

            fileid = "data.%s" % _a_(459726, _n_(459725, "self", lambda: self), "_FILEMAP")[_n_(459727, "pos", lambda: pos)]
            _l_(459728)
            _a_(459730, _n_(459729, "self", lambda: self), "_data_file_map")[_n_(459731, "pos", lambda: pos)] = _c_(459735, _a_(459733, _n_(459732, "self", lambda: self), "open"), _n_(459734, "fileid", lambda: fileid))
            _l_(459736)
        aux = _a_(459739, _n_(459738, "self", lambda: self), "_data_file_map")[_n_(459740, "pos", lambda: pos)]
        _l_(459741)
        return aux

    def synset_from_pos_and_offset(self, pos, offset):
        _l_(459805)

        """
        - pos: The synset's part of speech, matching one of the module level
          attributes ADJ, ADJ_SAT, ADV, NOUN or VERB ('a', 's', 'r', 'n', or 'v').
        - offset: The byte offset of this synset in the WordNet dict file
          for this pos.

        >>> from nltk.corpus import wordnet as wn
        >>> print(wn.synset_from_pos_and_offset('n', 1740))
        Synset('entity.n.01')
        """
        # Check to see if the synset is in the cache
        if _n_(459743, "offset", lambda: offset) in _a_(459745, _n_(459744, "self", lambda: self), "_synset_offset_cache")[_n_(459746, "pos", lambda: pos)]:
            _l_(459752)

            aux = _a_(459748, _n_(459747, "self", lambda: self), "_synset_offset_cache")[_n_(459749, "pos", lambda: pos)][_n_(459750, "offset", lambda: offset)]
            _l_(459751)
            return aux

        data_file = _c_(459756, _a_(459754, _n_(459753, "self", lambda: self), "_data_file"), _n_(459755, "pos", lambda: pos))
        _l_(459757)
        _c_(459761, _a_(459759, _n_(459758, "data_file", lambda: data_file), "seek"), _n_(459760, "offset", lambda: offset))
        _l_(459762)
        data_file_line = _c_(459765, _a_(459764, _n_(459763, "data_file", lambda: data_file), "readline"))
        _l_(459766)
        # If valid, the offset equals the 8-digit 0-padded integer found at the start of the line:
        line_offset = _n_(459767, "data_file_line", lambda: data_file_line)[:8]
        _l_(459768)
        if _c_(459771, _a_(459770, _n_(459769, "line_offset", lambda: line_offset), "isalnum")) and _n_(459772, "offset", lambda: offset) == _c_(459775, _n_(459773, "int", lambda: int), _n_(459774, "line_offset", lambda: line_offset)):
            _l_(459798)

            synset = _c_(459780, _a_(459777, _n_(459776, "self", lambda: self), "_synset_from_pos_and_line"), _n_(459778, "pos", lambda: pos), _n_(459779, "data_file_line", lambda: data_file_line))
            _l_(459781)
            assert _a_(459783, _n_(459782, "synset", lambda: synset), "_offset") == _n_(459784, "offset", lambda: offset)
            _l_(459785)
            _a_(459787, _n_(459786, "self", lambda: self), "_synset_offset_cache")[_n_(459788, "pos", lambda: pos)][_n_(459789, "offset", lambda: offset)] = _n_(459790, "synset", lambda: synset)
            _l_(459791)
        else:
            synset = None
            _l_(459792)
            raise _c_(459796, _n_(459793, "WordNetError", lambda: WordNetError), f"No WordNet synset found for pos={_n_(459794, 'pos', lambda: pos)} at offset={_n_(459795, 'offset', lambda: offset)}."
            )
            _l_(459797)
        _c_(459801, _a_(459800, _n_(459799, "data_file", lambda: data_file), "seek"), 0)
        _l_(459802)
        aux = _n_(459803, "synset", lambda: synset)
        _l_(459804)
        return aux

    @_c_(459806, deprecated, "Use public method synset_from_pos_and_offset() instead")
    def _synset_from_pos_and_offset(self, *args, **kwargs):
        _l_(459813)

        """
        Hack to help people like the readers of
        https://stackoverflow.com/a/27145655/1709587
        who were using this function before it was officially a public method
        """
        aux = _c_(459811, _a_(459808, _n_(459807, "self", lambda: self), "synset_from_pos_and_offset"), *_n_(459809, "args", lambda: args), **_n_(459810, "kwargs", lambda: kwargs))
        _l_(459812)
        return aux

    def _synset_from_pos_and_line(self, pos, data_file_line):
        _l_(460136)

        # Construct a new (empty) synset.
        synset = _c_(459816, _n_(459814, "Synset", lambda: Synset), _n_(459815, "self", lambda: self))
        _l_(459817)

        # parse the entry for this synset
        try:
            _l_(460070)


            # parse out the definitions and examples from the gloss
            columns_str, gloss = _c_(459822, _a_(459821, _c_(459820, _a_(459819, _n_(459818, "data_file_line", lambda: data_file_line), "strip")), "split"), "|")
            _l_(459823)
            definition = _c_(459829, _a_(459828, _c_(459827, _a_(459825, _n_(459824, "re", lambda: re), "sub"), r"[\"].*?[\"]", "", _n_(459826, "gloss", lambda: gloss)), "strip"))
            _l_(459830)
            examples = _c_(459834, _a_(459832, _n_(459831, "re", lambda: re), "findall"), r'"([^"]*)"', _n_(459833, "gloss", lambda: gloss))
            _l_(459835)
            for example in _n_(459836, "examples", lambda: examples):
                _l_(459843)

                _c_(459841, _a_(459839, _a_(459838, _n_(459837, "synset", lambda: synset), "_examples"), "append"), _n_(459840, "example", lambda: example))
                _l_(459842)

            _n_(459844, "synset", lambda: synset)._definition = _c_(459847, _a_(459846, _n_(459845, "definition", lambda: definition), "strip"), "; ")
            _l_(459848)

            # split the other info into fields
            _iter = _c_(459853, _n_(459849, "iter", lambda: iter), _c_(459852, _a_(459851, _n_(459850, "columns_str", lambda: columns_str), "split")))
            _l_(459854)

            def _next_token():
                _l_(459859)

                aux = _c_(459857, _n_(459855, "next", lambda: next), _n_(459856, "_iter", lambda: _iter))
                _l_(459858)
                return aux

            # get the offset
            _n_(459860, "synset", lambda: synset)._offset = _c_(459864, _n_(459861, "int", lambda: int), _c_(459863, _n_(459862, "_next_token", lambda: _next_token)))
            _l_(459865)

            # determine the lexicographer file name
            lexname_index = _c_(459869, _n_(459866, "int", lambda: int), _c_(459868, _n_(459867, "_next_token", lambda: _next_token)))
            _l_(459870)
            _n_(459871, "synset", lambda: synset)._lexname = _a_(459873, _n_(459872, "self", lambda: self), "_lexnames")[_n_(459874, "lexname_index", lambda: lexname_index)]
            _l_(459875)

            # get the part of speech
            _n_(459876, "synset", lambda: synset)._pos = _c_(459878, _n_(459877, "_next_token", lambda: _next_token))
            _l_(459879)

            # create Lemma objects for each lemma
            n_lemmas = _c_(459883, _n_(459880, "int", lambda: int), _c_(459882, _n_(459881, "_next_token", lambda: _next_token)), 16)
            _l_(459884)
            for _ in _c_(459887, _n_(459885, "range", lambda: range), _n_(459886, "n_lemmas", lambda: n_lemmas)):
                _l_(459927)

                # get the lemma name
                lemma_name = _c_(459889, _n_(459888, "_next_token", lambda: _next_token))
                _l_(459890)
                # get the lex_id (used for sense_keys)
                lex_id = _c_(459894, _n_(459891, "int", lambda: int), _c_(459893, _n_(459892, "_next_token", lambda: _next_token)), 16)
                _l_(459895)
                # If the lemma has a syntactic marker, extract it.
                m = _c_(459899, _a_(459897, _n_(459896, "re", lambda: re), "match"), r"(.*?)(\(.*\))?$", _n_(459898, "lemma_name", lambda: lemma_name))
                _l_(459900)
                lemma_name, syn_mark = _c_(459903, _a_(459902, _n_(459901, "m", lambda: m), "groups"))
                _l_(459904)
                # create the lemma object
                lemma = _c_(459912, _n_(459905, "Lemma", lambda: Lemma), _n_(459906, "self", lambda: self), _n_(459907, "synset", lambda: synset), _n_(459908, "lemma_name", lambda: lemma_name), _n_(459909, "lexname_index", lambda: lexname_index), _n_(459910, "lex_id", lambda: lex_id), _n_(459911, "syn_mark", lambda: syn_mark))
                _l_(459913)
                _c_(459918, _a_(459916, _a_(459915, _n_(459914, "synset", lambda: synset), "_lemmas"), "append"), _n_(459917, "lemma", lambda: lemma))
                _l_(459919)
                _c_(459925, _a_(459922, _a_(459921, _n_(459920, "synset", lambda: synset), "_lemma_names"), "append"), _a_(459924, _n_(459923, "lemma", lambda: lemma), "_name"))
                _l_(459926)

            # collect the pointer tuples
            n_pointers = _c_(459931, _n_(459928, "int", lambda: int), _c_(459930, _n_(459929, "_next_token", lambda: _next_token)))
            _l_(459932)
            for _ in _c_(459935, _n_(459933, "range", lambda: range), _n_(459934, "n_pointers", lambda: n_pointers)):
                _l_(459987)

                symbol = _c_(459937, _n_(459936, "_next_token", lambda: _next_token))
                _l_(459938)
                offset = _c_(459942, _n_(459939, "int", lambda: int), _c_(459941, _n_(459940, "_next_token", lambda: _next_token)))
                _l_(459943)
                pos = _c_(459945, _n_(459944, "_next_token", lambda: _next_token))
                _l_(459946)
                lemma_ids_str = _c_(459948, _n_(459947, "_next_token", lambda: _next_token))
                _l_(459949)
                if _n_(459950, "lemma_ids_str", lambda: lemma_ids_str) == "0000":
                    _l_(459986)

                    _c_(459957, _a_(459954, _a_(459952, _n_(459951, "synset", lambda: synset), "_pointers")[_n_(459953, "symbol", lambda: symbol)], "add"), (_n_(459955, "pos", lambda: pos), _n_(459956, "offset", lambda: offset)))
                    _l_(459958)
                else:
                    source_index = _c_(459961, _n_(459959, "int", lambda: int), _n_(459960, "lemma_ids_str", lambda: lemma_ids_str)[:2], 16) - 1
                    _l_(459962)
                    target_index = _c_(459965, _n_(459963, "int", lambda: int), _n_(459964, "lemma_ids_str", lambda: lemma_ids_str)[2:], 16) - 1
                    _l_(459966)
                    source_lemma_name = _a_(459970, _a_(459968, _n_(459967, "synset", lambda: synset), "_lemmas")[_n_(459969, "source_index", lambda: source_index)], "_name")
                    _l_(459971)
                    lemma_pointers = _a_(459973, _n_(459972, "synset", lambda: synset), "_lemma_pointers")
                    _l_(459974)
                    tups = _n_(459975, "lemma_pointers", lambda: lemma_pointers)[_n_(459976, "source_lemma_name", lambda: source_lemma_name), _n_(459977, "symbol", lambda: symbol)]
                    _l_(459978)
                    _c_(459984, _a_(459980, _n_(459979, "tups", lambda: tups), "append"), (_n_(459981, "pos", lambda: pos), _n_(459982, "offset", lambda: offset), _n_(459983, "target_index", lambda: target_index)))
                    _l_(459985)

            # read the verb frames
            try:
                _l_(460061)

                frame_count = _c_(459991, _n_(459988, "int", lambda: int), _c_(459990, _n_(459989, "_next_token", lambda: _next_token)))
                _l_(459992)
            except _n_(459993, "StopIteration", lambda: StopIteration):
                _l_(459995)

                pass
                _l_(459994)
            else:
                for _ in _c_(459998, _n_(459996, "range", lambda: range), _n_(459997, "frame_count", lambda: frame_count)):
                    _l_(460060)

                    # read the plus sign
                    plus = _c_(460000, _n_(459999, "_next_token", lambda: _next_token))
                    _l_(460001)
                    assert _n_(460002, "plus", lambda: plus) == "+"
                    _l_(460003)
                    # read the frame and lemma number
                    frame_number = _c_(460007, _n_(460004, "int", lambda: int), _c_(460006, _n_(460005, "_next_token", lambda: _next_token)))
                    _l_(460008)
                    frame_string_fmt = _n_(460009, "VERB_FRAME_STRINGS", lambda: VERB_FRAME_STRINGS)[_n_(460010, "frame_number", lambda: frame_number)]
                    _l_(460011)
                    lemma_number = _c_(460015, _n_(460012, "int", lambda: int), _c_(460014, _n_(460013, "_next_token", lambda: _next_token)), 16)
                    _l_(460016)
                    # lemma number of 00 means all words in the synset
                    if _n_(460017, "lemma_number", lambda: lemma_number) == 0:
                        _l_(460059)

                        _c_(460022, _a_(460020, _a_(460019, _n_(460018, "synset", lambda: synset), "_frame_ids"), "append"), _n_(460021, "frame_number", lambda: frame_number))
                        _l_(460023)
                        for lemma in _a_(460025, _n_(460024, "synset", lambda: synset), "_lemmas"):
                            _l_(460040)

                            _c_(460030, _a_(460028, _a_(460027, _n_(460026, "lemma", lambda: lemma), "_frame_ids"), "append"), _n_(460029, "frame_number", lambda: frame_number))
                            _l_(460031)
                            _c_(460038, _a_(460034, _a_(460033, _n_(460032, "lemma", lambda: lemma), "_frame_strings"), "append"), _n_(460035, "frame_string_fmt", lambda: frame_string_fmt) % _a_(460037, _n_(460036, "lemma", lambda: lemma), "_name"))
                            _l_(460039)
                    # only a specific word in the synset
                    else:
                        lemma = _a_(460042, _n_(460041, "synset", lambda: synset), "_lemmas")[_n_(460043, "lemma_number", lambda: lemma_number) - 1]
                        _l_(460044)
                        _c_(460049, _a_(460047, _a_(460046, _n_(460045, "lemma", lambda: lemma), "_frame_ids"), "append"), _n_(460048, "frame_number", lambda: frame_number))
                        _l_(460050)
                        _c_(460057, _a_(460053, _a_(460052, _n_(460051, "lemma", lambda: lemma), "_frame_strings"), "append"), _n_(460054, "frame_string_fmt", lambda: frame_string_fmt) % _a_(460056, _n_(460055, "lemma", lambda: lemma), "_name"))
                        _l_(460058)

        # raise a more informative error with line text
        except _n_(460062, "ValueError", lambda: ValueError) as e:
            _l_(460069)

            raise _c_(460066, _n_(460063, "WordNetError", lambda: WordNetError), f"line {_n_(460064, 'data_file_line', lambda: data_file_line)!r}: {_n_(460065, 'e', lambda: e)}") from _n_(460067, "e", lambda: e)
            _l_(460068)

        # set sense keys for Lemma objects - note that this has to be
        # done afterwards so that the relations are available
        for lemma in _a_(460072, _n_(460071, "synset", lambda: synset), "_lemmas"):
            _l_(460107)

            if _a_(460074, _n_(460073, "synset", lambda: synset), "_pos") == _n_(460075, "ADJ_SAT", lambda: ADJ_SAT):
                _l_(460088)

                head_lemma = _a_(460079, _c_(460078, _a_(460077, _n_(460076, "synset", lambda: synset), "similar_tos"))[0], "_lemmas")[0]
                _l_(460080)
                head_name = _a_(460082, _n_(460081, "head_lemma", lambda: head_lemma), "_name")
                _l_(460083)
                head_id = "%02d" % _a_(460085, _n_(460084, "head_lemma", lambda: head_lemma), "_lex_id")
                _l_(460086)
            else:
                head_name = head_id = ""
                _l_(460087)
            tup = (
                _a_(460090, _n_(460089, "lemma", lambda: lemma), "_name"),
                _a_(460092, _n_(460091, "WordNetCorpusReader", lambda: WordNetCorpusReader), "_pos_numbers")[_a_(460094, _n_(460093, "synset", lambda: synset), "_pos")],
                _a_(460096, _n_(460095, "lemma", lambda: lemma), "_lexname_index"),
                _a_(460098, _n_(460097, "lemma", lambda: lemma), "_lex_id"),
                _n_(460099, "head_name", lambda: head_name),
                _n_(460100, "head_id", lambda: head_id),
            )
            _l_(460101)
            _n_(460102, "lemma", lambda: lemma)._key = _c_(460105, _a_(460104, ("%s%%%d:%02d:%02d:%s:%s" % _n_(460103, "tup", lambda: tup)), "lower"))
            _l_(460106)

        # the canonical name is based on the first lemma
        lemma_name = _c_(460112, _a_(460111, _a_(460110, _a_(460109, _n_(460108, "synset", lambda: synset), "_lemmas")[0], "_name"), "lower"))
        _l_(460113)
        offsets = _a_(460115, _n_(460114, "self", lambda: self), "_lemma_pos_offset_map")[_n_(460116, "lemma_name", lambda: lemma_name)][_a_(460118, _n_(460117, "synset", lambda: synset), "_pos")]
        _l_(460119)
        sense_index = _c_(460124, _a_(460121, _n_(460120, "offsets", lambda: offsets), "index"), _a_(460123, _n_(460122, "synset", lambda: synset), "_offset"))
        _l_(460125)
        tup = _n_(460126, "lemma_name", lambda: lemma_name), _a_(460128, _n_(460127, "synset", lambda: synset), "_pos"), _n_(460129, "sense_index", lambda: sense_index) + 1
        _l_(460130)
        _n_(460131, "synset", lambda: synset)._name = "%s.%s.%02i" % _n_(460132, "tup", lambda: tup)
        _l_(460133)
        aux = _n_(460134, "synset", lambda: synset)
        _l_(460135)

        return aux

    def synset_from_sense_key(self, sense_key):
        _l_(460144)

        """
        Retrieves synset based on a given sense_key. Sense keys can be
        obtained from lemma.key()

        From https://wordnet.princeton.edu/documentation/senseidx5wn:
        A sense_key is represented as::

            lemma % lex_sense (e.g. 'dog%1:18:01::')

        where lex_sense is encoded as::

            ss_type:lex_filenum:lex_id:head_word:head_id

        :lemma:       ASCII text of word/collocation, in lower case
        :ss_type:     synset type for the sense (1 digit int)
                      The synset type is encoded as follows::

                          1    NOUN
                          2    VERB
                          3    ADJECTIVE
                          4    ADVERB
                          5    ADJECTIVE SATELLITE
        :lex_filenum: name of lexicographer file containing the synset for the sense (2 digit int)
        :lex_id:      when paired with lemma, uniquely identifies a sense in the lexicographer file (2 digit int)
        :head_word:   lemma of the first word in satellite's head synset
                      Only used if sense is in an adjective satellite synset
        :head_id:     uniquely identifies sense in a lexicographer file when paired with head_word
                      Only used if head_word is present (2 digit int)

        >>> import nltk
        >>> from nltk.corpus import wordnet as wn
        >>> print(wn.synset_from_sense_key("drive%1:04:03::"))
        Synset('drive.n.06')

        >>> print(wn.synset_from_sense_key("driving%1:04:03::"))
        Synset('drive.n.06')
        """
        aux = _c_(460142, _a_(460141, _c_(460140, _a_(460138, _n_(460137, "self", lambda: self), "lemma_from_key"), _n_(460139, "sense_key", lambda: sense_key)), "synset"))#line 1680
        _l_(460143)#line 1680
        return aux#line 1680