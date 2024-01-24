# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75272527/python3-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
token_path= './work/token.json'
_l_(461883)
kubernetes_url = 'https://192.168.39.81:8443'
_l_(461884)
client_cert_path = './work/client.crt'
_l_(461885)

f = _c_(461888, _n_(461886, "open", lambda: open), _n_(461887, "token_path", lambda: token_path))
_l_(461889)
token_json = _c_(461893, _a_(461891, _n_(461890, "json", lambda: json), "load"), _n_(461892, "f", lambda: f))
_l_(461894)
bearer_token = _n_(461895, "token_json", lambda: token_json)['status']['token']
_l_(461896)
configuration = _c_(461900, _a_(461899, _a_(461898, _n_(461897, "kubernetes", lambda: kubernetes), "client"), "Configuration"))
_l_(461901)
_a_(461903, _n_(461902, "configuration", lambda: configuration), "api_key")["authorization"] = _n_(461904, "bearer_token", lambda: bearer_token)
_l_(461905)
_a_(461907, _n_(461906, "configuration", lambda: configuration), "api_key_prefix")['authorization'] = 'Bearer'
_l_(461908)
_n_(461909, "configuration", lambda: configuration).host = _n_(461910, "kubernetes_url", lambda: kubernetes_url)
_l_(461911)
_n_(461912, "configuration", lambda: configuration).verify_ssl=False
_l_(461913)
_n_(461914, "configuration", lambda: configuration).ssl_ca_cert = _n_(461915, "client_cert_path", lambda: client_cert_path)
_l_(461916)


start_time = "5m"
_l_(461917)
end_time ="now"
_l_(461918)
query = 'rate(container_cpu_usage_seconds_total{pod="my-release-wordpress-6dc6484885-bbj2q"}[1m])*100'
_l_(461919)
resolution=1.00
_l_(461920)
max_length = 300
_l_(461921)
duration = 900
_l_(461922)
interval = 1
_l_(461923)
chaos_type = "stresschaos"
_l_(461924)
namespace = "wordpress"
_l_(461925)
experiment_name = "itec-experiment-cpu-stress-4"
_l_(461926)

df = _c_(461932, _n_(461927, "get_metric_data", lambda: get_metric_data), _n_(461928, "start_time", lambda: start_time), _n_(461929, "end_time", lambda: end_time), _n_(461930, "query", lambda: query), _n_(461931, "resolution", lambda: resolution), max_length=300)
_l_(461933)
_c_(461935, _n_(461934, "get_injection_status", lambda: get_injection_status), "stresschaos", "wordpress", "itec-experiment-cpu-stress-4")
_l_(461936)