# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61815106/getting-typeerror-cant-pickle-sslcontext-objects-in-using-ray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(409361, _n_(409360, "ray", lambda: ray), "remote")
def Prefer_Attachment_query2(listval):
    _l_(409371)

    customer_wallet=_n_(409362, "listval", lambda: listval)[0]
    _l_(409363)
    merchant_wallet=_n_(409364, "listval", lambda: listval)[1]
    _l_(409365)
    #print(x,y)
    prefquery="""MATCH (p1:CUSTOMER {WALLETID: '%s'})
                 MATCH (p2:MERCHANT {WALLETID: '%s'})
                 RETURN gds.alpha.linkprediction.preferentialAttachment(p1, p2,{relationshipQuery: "PAYMENT"}) as score"""%(_n_(409366, "customer_wallet", lambda: customer_wallet),_n_(409367, "merchant_wallet", lambda: merchant_wallet))
    _l_(409368)
    aux = _n_(409369, "prefquery", lambda: prefquery)
    _l_(409370)
    #print(prefquery)
    return aux
try:
    from timeit import default_timer as timer
    _l_(409373)

except ImportError:
    pass
try:
    import itertools
    _l_(409375)

except ImportError:
    pass
@_a_(409377, _n_(409376, "ray", lambda: ray), "remote")
def Customer_Merchant_value_pass(text):
    _l_(409508)

    minicustomer=_n_(409378, "text", lambda: text)
    _l_(409379)
    begin=_c_(409381, _n_(409380, "timer", lambda: timer))
    _l_(409382)
    sum_val=0
    _l_(409383)
    list_avg_score=[]
    _l_(409384)
    list_category_val=[]
    _l_(409385)
    dict_list=[]
    _l_(409386)
    #Avg_score=0
    with _c_(409389, _a_(409388, _n_(409387, "graphdriver", lambda: graphdriver), "session"))as session:
        _l_(409493)

        for i in _c_(409396, _a_(409391, _n_(409390, "itertools", lambda: itertools), "islice"), _n_(409392, "minicustomer", lambda: minicustomer),_c_(409395, _n_(409393, "len", lambda: len), _n_(409394, "minicustomer", lambda: minicustomer))):
            _l_(409492)

            for key in _n_(409397, "list_of_unique_merchants", lambda: list_of_unique_merchants):
                _l_(409462)

                _c_(409400, _n_(409398, "print", lambda: print), "Here at list_of_unique_merchants customer value is ",_n_(409399, "i", lambda: i))
                _l_(409401)
                _c_(409404, _n_(409402, "print", lambda: print), "BMCC_Code",_n_(409403, "key", lambda: key))
                _l_(409405)
                valuelist=_n_(409406, "list_of_unique_merchants", lambda: list_of_unique_merchants)[_n_(409407, "key", lambda: key)]
                _l_(409408)
                #print("Uniquelistfor:",key,valuelist)
                for j in  _n_(409409, "valuelist", lambda: valuelist):
                    _l_(409431)


                    #print("list len",len(valuelist))
                    #print("Here the iner of value list ",i)
                          #print("--------------------------------")
                    #print([i,j])
                    pref_attach_score_rayvalue=_c_(409414, _a_(409411, _n_(409410, "Prefer_Attachment_query2", lambda: Prefer_Attachment_query2), "remote"), [_n_(409412, "i", lambda: i),_n_(409413, "j", lambda: j)])
                    _l_(409415)
                    pref_attach_score=_c_(409419, _a_(409417, _n_(409416, "ray", lambda: ray), "get"), _n_(409418, "pref_attach_score_rayvalue", lambda: pref_attach_score_rayvalue))
                    _l_(409420)
                    #print(pref_attach_score)

                    result=_c_(409424, _a_(409422, _n_(409421, "session", lambda: session), "run"), _n_(409423, "pref_attach_score", lambda: pref_attach_score))
                    _l_(409425)
                    for line in _n_(409426, "result", lambda: result):
                        _l_(409430)

                        #print(line["score"])
                        sum_val=_n_(409427, "sum_val", lambda: sum_val)+_n_(409428, "line", lambda: line)["score"]
                        _l_(409429)


                Totalsumval=_n_(409432, "sum_val", lambda: sum_val)
                _l_(409433)
                _c_(409436, _n_(409434, "print", lambda: print), "Totalsum",_n_(409435, "Totalsumval", lambda: Totalsumval))
                _l_(409437)
                Avg_score=_n_(409438, "sum_val", lambda: sum_val)/_c_(409441, _n_(409439, "len", lambda: len), _n_(409440, "valuelist", lambda: valuelist))
                _l_(409442)
                _c_(409445, _n_(409443, "print", lambda: print), "Avg_score",_n_(409444, "Avg_score", lambda: Avg_score))
                _l_(409446)
                sum_val=0
                _l_(409447)
                _c_(409451, _a_(409449, _n_(409448, "list_avg_score", lambda: list_avg_score), "append"), _n_(409450, "Avg_score", lambda: Avg_score))
                _l_(409452)
                _c_(409456, _a_(409454, _n_(409453, "list_category_val", lambda: list_category_val), "append"), _n_(409455, "key", lambda: key))
                _l_(409457)
                avg_score_list=_n_(409458, "list_avg_score", lambda: list_avg_score)
                _l_(409459)
                category_list=_n_(409460, "list_category_val", lambda: list_category_val)
                _l_(409461)
            max_dictionary  =_c_(409467, _n_(409463, "MaxValue_calc", lambda: MaxValue_calc), _n_(409464, "i", lambda: i),_n_(409465, "category_list", lambda: category_list),_n_(409466, "avg_score_list", lambda: avg_score_list)) 
            _l_(409468) 
            #MaxValue_calc(i,category_list,avg_score_list) 

            _c_(409471, _n_(409469, "print", lambda: print), "max_dicitionary",_n_(409470, "max_dictionary", lambda: max_dictionary))
            _l_(409472)
            _c_(409476, _a_(409474, _n_(409473, "dict_list", lambda: dict_list), "append"), _n_(409475, "max_dictionary", lambda: max_dictionary))
            _l_(409477)
            rowlist=_n_(409478, "dict_list", lambda: dict_list)
            _l_(409479)
            _c_(409482, _n_(409480, "print", lambda: print), 'appended list',_n_(409481, "rowlist", lambda: rowlist))
            _l_(409483)
            _c_(409488, _n_(409484, "print", lambda: print), 'process',_c_(409487, _n_(409485, "len", lambda: len), _n_(409486, "rowlist", lambda: rowlist)))
            _l_(409489)

            #dict_list=[]
            list_avg_score=[] 
            _l_(409490) 
            list_category_val=[]
            _l_(409491)



    _c_(409496, _a_(409495, _n_(409494, "session", lambda: session), "close"))
    _l_(409497)
    end=_c_(409499, _n_(409498, "timer", lambda: timer))
    _l_(409500)
    _c_(409504, _n_(409501, "print", lambda: print), "Total time   :",(_n_(409502, "end", lambda: end)-_n_(409503, "begin", lambda: begin)))
    _l_(409505)
    aux = _n_(409506, "rowlist", lambda: rowlist)
    _l_(409507)
    return aux



datalist_rayval=_c_(409512, _a_(409510, _n_(409509, "Customer_Merchant_value_pass", lambda: Customer_Merchant_value_pass), "remote"), _n_(409511, "customerlist", lambda: customerlist))
_l_(409513)
datalist=_c_(409517, _a_(409515, _n_(409514, "ray", lambda: ray), "get"), _n_(409516, "datalist_rayval", lambda: datalist_rayval))
_l_(409518)