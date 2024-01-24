# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74770489/i-am-trying-to-add-the-tag-freefrom-tag-for-particular-compute-instances-in-oc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
core_client = _c_(425843, _a_(425841, _a_(425840, _a_(425839, _n_(425838, "oci", lambda: oci), "core"), "compute_client"), "ComputeClient"), _n_(425842, "config", lambda: config))
_l_(425844)
_c_(425848, _a_(425847, _a_(425846, _n_(425845, "core_client", lambda: core_client), "base_client"), "set_region"), 'us-phoenix-1')
_l_(425849)
vol=_c_(425854, _a_(425852, _a_(425851, _n_(425850, "oci", lambda: oci), "core"), "BlockstorageClient"), _n_(425853, "config", lambda: config))
_l_(425855)
# Send the request to service, there are more available parameters to send in the request
lista = _c_(425859, _a_(425857, _n_(425856, "core_client", lambda: core_client), "list_instances"), compartment_id=_n_(425858, "compartment_id", lambda: compartment_id),lifecycle_state="STOPPED")
_l_(425860)

for i in _a_(425862, _n_(425861, "lista", lambda: lista), "data"):
    _l_(425883)

    inst=_c_(425867, _a_(425864, _n_(425863, "core_client", lambda: core_client), "get_instance"), instance_id=_a_(425866, _n_(425865, "i", lambda: i), "id"))
    _l_(425868)
    #print(inst.data)
    update_volume_response = _c_(425876, _a_(425870, _n_(425869, "core_client", lambda: core_client), "update_instance"), update_instance_details = _c_(425875, _a_(425874, _a_(425873, _a_(425872, _n_(425871, "oci", lambda: oci), "core"), "models"), "UpdateInstanceDetails"), freefrom_tag={"shutdown": "no"}))
    _l_(425877)
    _c_(425880, _n_(425878, "print", lambda: print), _n_(425879, "update_volume_response", lambda: update_volume_response)) 
    _l_(425881) 
    break
    _l_(425882)