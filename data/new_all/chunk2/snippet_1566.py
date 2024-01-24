# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76857472/attributeerror-prototype-object-has-no-attribute-descriptor-while-running
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def convert_to_pubsub_message(element):
 _l_(432057)

 if _n_(432038, "element", lambda: element) is None:
  _l_(432040)

  aux = None
  _l_(432039)
  return aux
 pubsub_data = {"table": _n_(432041, "element", lambda: element)["table"], "payload": _n_(432042, "element", lambda: element)["values"]}
 _l_(432043)
 pubsub_message = {
    "data": _c_(432049, _a_(432048, _c_(432047, _a_(432045, _n_(432044, "json", lambda: json), "dumps"), _n_(432046, "pubsub_data", lambda: pubsub_data)), "encode"), "utf-8"),
    "attributes": {}
 }
 _l_(432050)
 _c_(432053, _n_(432051, "print", lambda: print), "Pub/Sub Message:", _n_(432052, "pubsub_message", lambda: pubsub_message))
 _l_(432054)
 aux = _n_(432055, "pubsub_message", lambda: pubsub_message)
 _l_(432056)
 return aux

with _c_(432061, _a_(432059, _n_(432058, "beam", lambda: beam), "Pipeline"), options=_n_(432060, "options", lambda: options)) as p:
 _l_(432085)

# Read the JSON records from GCS or any source
 records = _n_(432062, "p", lambda: p) | "Read JSON records" >> _c_(432067, _a_(432065, _a_(432064, _n_(432063, "beam", lambda: beam), "io"), "ReadFromText"), _n_(432066, "gcs_json_file", lambda: gcs_json_file))
 _l_(432068)
 # Extract payload and table name from each record
 extracted_data = (
   _n_(432069, "records", lambda: records)
   | "Extract Payload and Table" >> _c_(432074, _a_(432071, _n_(432070, "beam", lambda: beam), "ParDo"), _c_(432073, _n_(432072, "ExtractPayloadAndTable", lambda: ExtractPayloadAndTable)))
 )
 _l_(432075)
 # Send extracted payloads to Pub/Sub
 message = (
   _n_(432076, "extracted_data", lambda: extracted_data)
   | "Convert to Pub/Sub Message" >> _c_(432080, _a_(432078, _n_(432077, "beam", lambda: beam), "Map"), _n_(432079, "convert_to_pubsub_message", lambda: convert_to_pubsub_message))
   | "Send Payload to Pub/Sub" >> _c_(432083, _n_(432081, "WriteToPubSub", lambda: WriteToPubSub), topic=_n_(432082, "pubsub_topic", lambda: pubsub_topic))
 )
 _l_(432084)