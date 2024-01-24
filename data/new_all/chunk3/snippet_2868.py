# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60446978/while-using-biopython-nameerror-name-pubmed-id-is-not-defined-even-though-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for plant, disease in _n_(527195, "plant_disease_list", lambda: plant_disease_list):
    _l_(527252)

    search_query = _c_(527199, _n_(527196, "generate_search_query", lambda: generate_search_query), _n_(527197, "plant", lambda: plant), _n_(527198, "disease", lambda: disease))
    _l_(527200)
    handle1 = _c_(527204, _a_(527202, _n_(527201, "Entrez", lambda: Entrez), "esearch"), db="pmc", term=_n_(527203, "search_query", lambda: search_query), retmax="10")
    _l_(527205)
    record1 = _c_(527209, _a_(527207, _n_(527206, "Entrez", lambda: Entrez), "read"), _n_(527208, "handle1", lambda: handle1))
    _l_(527210)
    pubmed_ids = _c_(527213, _a_(527212, _n_(527211, "record1", lambda: record1), "get"), "IdList")
    _l_(527214)
    if _n_(527215, "pubmed_id", lambda: pubmed_id) in _n_(527216, "pubmed_ids", lambda: pubmed_ids)=="":
        _l_(527251)

        _c_(527222, _n_(527217, "print", lambda: print), _c_(527221, _a_(527218, "Plant: {} Disease: {} PubmedID: DOI:", "format"), _n_(527219, "plant", lambda: plant), _n_(527220, "disease", lambda: disease)))
        _l_(527223)
    else:

     for pubmed_id in _n_(527224, "pubmed_ids", lambda: pubmed_ids):
         _l_(527250)

         handle2 = _c_(527228, _a_(527226, _n_(527225, "Entrez", lambda: Entrez), "esummary"), db="pmc", id=_n_(527227, "pubmed_id", lambda: pubmed_id))
         _l_(527229)
         records = _c_(527233, _a_(527231, _n_(527230, "Entrez", lambda: Entrez), "read"), _n_(527232, "handle2", lambda: handle2))
         _l_(527234)
         for record in _n_(527235, "records", lambda: records):
             _l_(527249)

             doi = _c_(527238, _a_(527237, _n_(527236, "record", lambda: record), "get"), "DOI")
             _l_(527239)
             _c_(527247, _n_(527240, "print", lambda: print), _c_(527246, _a_(527241, "Plant: {} Disease: {} PubmedID: {} DOI: http://doi.org/{}", "format"), _n_(527242, "plant", lambda: plant), _n_(527243, "disease", lambda: disease), _n_(527244, "pubmed_id", lambda: pubmed_id), _n_(527245, "doi", lambda: doi)))
             _l_(527248)