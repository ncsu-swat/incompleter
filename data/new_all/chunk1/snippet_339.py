# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63920923/getting-error-typeerror-create-task-takes-from-1-to-2-positional-arguments-bu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from google.cloud import tasks_v2
  _l_(396476)

except ImportError:
  pass
try:
  import json
  _l_(396478)

except ImportError:
  pass


GCP_PROJECT='test'
_l_(396479)
GCP_LOCATION='europe-west6'
_l_(396480)


def enqueue_task(queue_name, payload, process_url):
  _l_(396515)

  client = _c_(396483, _a_(396482, _n_(396481, "tasks_v2", lambda: tasks_v2), "CloudTasksClient"))
  _l_(396484)
  parent = _c_(396490, _a_(396486, _n_(396485, "client", lambda: client), "queue_path"), _n_(396487, "GCP_PROJECT", lambda: GCP_PROJECT), _n_(396488, "GCP_LOCATION", lambda: GCP_LOCATION), _n_(396489, "queue_name", lambda: queue_name))
  _l_(396491)

  task = {
    'app_engine_http_request': {
      'http_method': 'POST',
      'relative_uri': _n_(396492, "process_url", lambda: process_url)
    }
  }
  _l_(396493)

  if _n_(396494, "payload", lambda: payload) is None:
    _l_(396496)

    aux = False
    _l_(396495)
    return aux

  payload = _c_(396500, _a_(396498, _n_(396497, "json", lambda: json), "dumps"), _n_(396499, "payload", lambda: payload))
  _l_(396501)
  converted_payload = _c_(396504, _a_(396503, _n_(396502, "payload", lambda: payload), "encode"))
  _l_(396505)

  _n_(396506, "task", lambda: task)['app_engine_http_request']['body'] = _n_(396507, "converted_payload", lambda: converted_payload)
  _l_(396508)
  aux = _c_(396513, _a_(396510, _n_(396509, "client", lambda: client), "create_task"), _n_(396511, "parent", lambda: parent), _n_(396512, "task", lambda: task))
  _l_(396514)
  return aux