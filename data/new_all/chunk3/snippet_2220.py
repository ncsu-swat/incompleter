# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57343405/typeerror-unhashable-type-list-when-adding-a-count-variable-works-without
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_entry(count,balance_list, Token1_balances, Token2_balances, Token3_balances,localtime):
   _l_(577751)


   # check if in seen set
   if (_n_(577717, "count", lambda: count),_n_(577718, "Token1_balances", lambda: Token1_balances), _n_(577719, "Token2_balances", lambda: Token2_balances), _n_(577720, "Token3_balances", lambda: Token3_balances),_n_(577721, "localtime", lambda: localtime)) in _n_(577722, "seen", lambda: seen):
      _l_(577725)

      aux = _n_(577723, "balance_list", lambda: balance_list)
      _l_(577724)
      return aux

   # add to seen set
   _c_(577735, _a_(577727, _n_(577726, "seen", lambda: seen), "add"), _c_(577734, _n_(577728, "tuple", lambda: tuple), [_n_(577729, "count", lambda: count),_n_(577730, "Token1_balances", lambda: Token1_balances), _n_(577731, "Token2_balances", lambda: Token2_balances), _n_(577732, "Token3_balances", lambda: Token3_balances),_n_(577733, "localtime", lambda: localtime)]))
   _l_(577736)

   # append to results list
   _c_(577747, _a_(577738, _n_(577737, "balance_list", lambda: balance_list), "append"), {'count':_n_(577739, "count", lambda: count),_n_(577740, "Token1", lambda: Token1): _n_(577741, "Token1_balances", lambda: Token1_balances), _n_(577742, "Token2", lambda: Token2): _n_(577743, "Token2_balances", lambda: Token2_balances), _n_(577744, "Token3", lambda: Token3): _n_(577745, "Token3_balances", lambda: Token3_balances),'time':_n_(577746, "localtime", lambda: localtime)})
   _l_(577748)
   aux = _n_(577749, "balance_list", lambda: balance_list)
   _l_(577750)

   return aux


def write_to_json(lst, fn):
   _l_(577768)

   with _c_(577754, _n_(577752, "open", lambda: open), _n_(577753, "fn", lambda: fn), 'a', encoding='utf-8') as file:
      _l_(577767)

      for item in _n_(577755, "lst", lambda: lst):
         _l_(577766)

         x = _c_(577759, _a_(577757, _n_(577756, "json", lambda: json), "dumps"), _n_(577758, "item", lambda: item), indent=4)
         _l_(577760)
         _c_(577764, _a_(577762, _n_(577761, "file", lambda: file), "write"), _n_(577763, "x", lambda: x) + '\n')
         _l_(577765)


balance_list = []
_l_(577769)
seen = _c_(577771, _n_(577770, "set", lambda: set))
_l_(577772)

if _n_(577773, "__name__", lambda: __name__) == '__main__':
   _l_(577868)


   _c_(577775, _n_(577774, "print", lambda: print), '-'*40)   
   _l_(577776)   
   _c_(577778, _n_(577777, "print", lambda: print), " Service Online and logging file has been established")
   _l_(577779)
   _c_(577781, _n_(577780, "print", lambda: print), '-'*40)  
   _l_(577782)  

   n = 0 
   _l_(577783) 
   while True:
      _l_(577867)

      _c_(577787, _a_(577785, _n_(577784, "time", lambda: time), "sleep"), _n_(577786, "throttleClient", lambda: throttleClient))
      _l_(577788)
      localtime = _c_(577797, _a_(577790, _n_(577789, "time", lambda: time), "asctime"), _c_(577796, _a_(577792, _n_(577791, "time", lambda: time), "localtime"), _c_(577795, _a_(577794, _n_(577793, "time", lambda: time), "time"))) )
      _l_(577798)
      minute = _a_(577803, _c_(577802, _a_(577801, _a_(577800, _n_(577799, "datetime", lambda: datetime), "datetime"), "now")), "minute")
      _l_(577804)
      _c_(577807, _n_(577805, "print", lambda: print), 'Local current time:',_n_(577806, "localtime", lambda: localtime),'CDT\n')
      _l_(577808)
      if _n_(577809, "minute", lambda: minute) % _n_(577810, "throttleApi", lambda: throttleApi) == 0:
         _l_(577866)

         try:
            _l_(577864)


            count = _c_(577813, _n_(577811, "str", lambda: str), _n_(577812, "n", lambda: n) + 1)
            _l_(577814)
            balance_query   = _c_(577817, _a_(577816, _n_(577815, "p2p", lambda: p2p), "getBalances"))["result"]
            _l_(577818)
            Token1_balances = _c_(577822, _n_(577819, "str", lambda: str), _n_(577820, "balance_query", lambda: balance_query)[_n_(577821, "Token1", lambda: Token1)])
            _l_(577823)
            Token2_balances = _c_(577827, _n_(577824, "str", lambda: str), _n_(577825, "balance_query", lambda: balance_query)[_n_(577826, "Token2", lambda: Token2)])
            _l_(577828)
            Token3_balances = _c_(577832, _n_(577829, "str", lambda: str), _n_(577830, "balance_query", lambda: balance_query)[_n_(577831, "Token3", lambda: Token3)])
            _l_(577833)
            args1 = [_n_(577834, "count", lambda: count),_n_(577835, "Token1_balances", lambda: Token1_balances), _n_(577836, "Token2_balances", lambda: Token2_balances), _n_(577837, "Token3_balances", lambda: Token3_balances),_n_(577838, "localtime", lambda: localtime)]
            _l_(577839)
            balance_list = _c_(577843, _n_(577840, "add_entry", lambda: add_entry), _n_(577841, "balance_list", lambda: balance_list), *_n_(577842, "args1", lambda: args1))  # add entry - SUCCESS  
            _l_(577844)  # add entry - SUCCESS  
            _c_(577847, _n_(577845, "write_to_json", lambda: write_to_json), _n_(577846, "balance_list", lambda: balance_list), 'balance.json') 
            _l_(577848) 
         except _a_(577851, _a_(577850, _n_(577849, "requests", lambda: requests), "exceptions"), "ConnectionError") as e:
            _l_(577863)

            _c_(577854, _n_(577852, "print", lambda: print), _n_(577853, "ConnectionError", lambda: ConnectionError))
            _l_(577855)
            _c_(577857, _n_(577856, "print", lambda: print), '-'*20)
            _l_(577858)
            _c_(577860, _n_(577859, "print", lambda: print), "Can't log balances due to connection error")
            _l_(577861)
            pass
            _l_(577862)
      else:
        pass           
        _l_(577865)           