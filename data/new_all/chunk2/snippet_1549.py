# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75402627/how-to-handle-python-typeerror-nonetype-object-is-not-subscriptable-on-dict-valu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sites_response =_c_(440943, _a_(440939, _n_(440938, "requests", lambda: requests), "request"), "GET", _n_(440940, "url_dcim_sites", lambda: url_dcim_sites), headers=_n_(440941, "headers", lambda: headers), data=_n_(440942, "payload", lambda: payload))
_l_(440944)

sites_json = _c_(440947, _a_(440946, _n_(440945, "sites_response", lambda: sites_response), "json"))
_l_(440948)

sites_results = _n_(440949, "sites_json", lambda: sites_json)['results']
_l_(440950)

for site in _n_(440951, "sites_results", lambda: sites_results):
  _l_(440976)

  id_number = _n_(440952, "site", lambda: site)['id']
  _l_(440953)
  name = _n_(440954, "site", lambda: site)['name']
  _l_(440955)
  region_name = _n_(440956, "site", lambda: site)['region']['name']
  _l_(440957)
  status = _n_(440958, "site", lambda: site)['status']['value']
  _l_(440959)
  #print(f"ID:{id_number:5} | Hostname:{hostname:20} | IP Address:{ipaddr!s:12} | Site:{site_id:5}") 
  sites = _c_(440965, _n_(440960, "dict", lambda: dict), ID=_n_(440961, "id_number", lambda: id_number), Name=_n_(440962, "name", lambda: name), Region=_n_(440963, "region_name", lambda: region_name), Status=_n_(440964, "status", lambda: status))
  _l_(440966)
  format_sites = f"ID: {_n_(440967, 'sites', lambda: sites)['ID']:5} | Name: {_n_(440968, 'sites', lambda: sites)['Name']:20} | Region: {_n_(440969, 'sites', lambda: sites)['Region']:10} | Status: {_n_(440970, 'sites', lambda: sites)['Status']:5}"
  _l_(440971)
  _c_(440974, _n_(440972, "print", lambda: print), _n_(440973, "format_sites", lambda: format_sites))
  _l_(440975)