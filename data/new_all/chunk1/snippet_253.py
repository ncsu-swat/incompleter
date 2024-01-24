# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55012786/typeerror-close-spider-missing-1-required-positional-argument-reason
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sqlite3 as sq3
    _l_(413930)

except ImportError:
    pass
try:
    import sqlite3_functions as sq_f
    _l_(413932)

except ImportError:
    pass
try:
    import logging
    _l_(413934)

except ImportError:
    pass
try:
    from scrapy.exceptions import DropItem
    _l_(413936)

except ImportError:
    pass

class CointelegraphSpiderPipeline(_n_(413937, "object", lambda: object)):
    _l_(414066)

    """
    Doc string
    """

    def __init__(self, stats):
        _l_(413954)

        """
        Doc string
        """
        _n_(413938, "self", lambda: self).stats = _n_(413939, "stats", lambda: stats)
        _l_(413940)
        _n_(413941, "self", lambda: self).db_file = 'D:\\DCC\\Projects\\crypto_projects\\master_data.db'
        _l_(413942)
        _n_(413943, "self", lambda: self).conn = _c_(413948, _a_(413945, _n_(413944, "sq3", lambda: sq3), "connect"), _a_(413947, _n_(413946, "self", lambda: self), "db_file"))
        _l_(413949)
        _n_(413950, "self", lambda: self).table_name = 'cointelegraph'
        _l_(413951)
        _n_(413952, "self", lambda: self).commit_counter = 0
        _l_(413953)


    @_n_(413955, "classmethod", lambda: classmethod)
    def from_crawler(cls, crawler):
        _l_(413961)

        """
        Doc string
        """
        stats = _a_(413957, _n_(413956, "crawler", lambda: crawler), "stats")
        _l_(413958)
        aux = _n_(413959, "stats", lambda: stats)   #cls(crawler.stats)
        _l_(413960)   #cls(crawler.stats)
        return aux   #cls(crawler.stats)

    def open_spider(self, spider):
        _l_(413969)

        """
        Doc string
        """
        _c_(413963, _n_(413962, "print", lambda: print), "I'm starting the pipeline")
        _l_(413964)
        _c_(413967, _a_(413966, _n_(413965, "logging", lambda: logging), "INFO"), "Starting Pipeline...")
        _l_(413968)

    def process_item(self, item, spider):
        _l_(414035)

        """
        Doc string
        """
        item_checked = True
        _l_(413970)

        try:
            _l_(414034)

            # Sanity Check
            for key, value in _c_(413973, _a_(413972, _n_(413971, "item", lambda: item), "items")):
                _l_(413993)

                _c_(413975, _n_(413974, "print", lambda: print), "Inside the loop!!!")
                _l_(413976)
                if _n_(413977, "value", lambda: value) == '':
                    _l_(413992)

                    item_checked = False
                    _l_(413978)
                    raise _c_(413985, _n_(413979, "DropItem", lambda: DropItem), _c_(413984, _a_(413980, "Item '{0}:{1}' has empty data - Link: {3}", "format"), _n_(413981, "key", lambda: key), _n_(413982, "value", lambda: value), _n_(413983, "item", lambda: item)['link']))
                    _l_(413986)
                else:
                    _c_(413989, _a_(413988, _n_(413987, "logging", lambda: logging), "INFO"), "Item check OK")
                    _l_(413990)
                    item_checked = True
                    _l_(413991)

            # Insert row and increase counter
            if _n_(413994, "item_checked", lambda: item_checked):
                _l_(414014)

                _n_(413995, "self", lambda: self).conn = _c_(414005, _a_(413997, _n_(413996, "sq_f", lambda: sq_f), "insert_row"), _a_(413999, _n_(413998, "self", lambda: self), "db_file"), table_name=_a_(414001, _n_(414000, "self", lambda: self), "table_name"), conn=_a_(414003, _n_(414002, "self", lambda: self), "conn"), **_n_(414004, "item", lambda: item))
                _l_(414006)
                _n_(414007, "self", lambda: self).commit_counter += 1
                _l_(414008)
                _c_(414012, _a_(414011, _a_(414010, _n_(414009, "self", lambda: self), "conn"), "commit"))
                _l_(414013)

            # Commit every 500 inserted rows
            if _a_(414016, _n_(414015, "self", lambda: self), "commit_counter") % 500 == 0:
                _l_(414022)

                _c_(414020, _a_(414019, _a_(414018, _n_(414017, "self", lambda: self), "conn"), "commit"))
                _l_(414021)

            _c_(414025, _n_(414023, "print", lambda: print), _n_(414024, "item", lambda: item))
            _l_(414026)

        except _n_(414027, "Exception", lambda: Exception) as e:
            _l_(414033)

            _c_(414031, _a_(414029, _n_(414028, "logging", lambda: logging), "WARNING"), _n_(414030, "e", lambda: e))
            _l_(414032)




    def close_spider(self, spider):
        _l_(414065)

        """
        Doc string
        """
        _c_(414038, _a_(414037, _n_(414036, "logging", lambda: logging), "INFO"), "Commiting rows...")
        _l_(414039)
        _c_(414043, _a_(414042, _a_(414041, _n_(414040, "self", lambda: self), "conn"), "commit"))
        _l_(414044)
        _c_(414047, _a_(414046, _n_(414045, "logging", lambda: logging), "INFO"), "Saving spider stats...")
        _l_(414048)
        _c_(414054, _n_(414049, "print", lambda: print), _c_(414053, _a_(414052, _a_(414051, _n_(414050, "self", lambda: self), "stats"), "get_stats")))
        _l_(414055)
        _c_(414058, _a_(414057, _n_(414056, "logging", lambda: logging), "INFO"), "Closing pipeline..")
        _l_(414059)
        _c_(414063, _a_(414062, _a_(414061, _n_(414060, "self", lambda: self), "conn"), "close"))
        _l_(414064)