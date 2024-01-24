# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70197401/azure-function-attributeerror-subscriptionclient-object-has-no-attribute-su
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(628430)

except ImportError:
    pass
try:
    import subprocess
    _l_(628432)

except ImportError:
    pass
try:
    import json
    _l_(628434)

except ImportError:
    pass
try:
    import os
    _l_(628436)

except ImportError:
    pass
try:
    from azure.cli.core import get_default_cli
    _l_(628438)

except ImportError:
    pass
try:
    from azure.mgmt.containerservice import ContainerServiceClient
    _l_(628440)

except ImportError:
    pass
try:
    from azure.identity import ClientSecretCredential
    _l_(628442)

except ImportError:
    pass
try:
    from azure.mgmt.subscription import SubscriptionClient
    _l_(628444)

except ImportError:
    pass
try:
    from azure.mgmt.resource import ResourceManagementClient
    _l_(628446)

except ImportError:
    pass
try:
    from azure.mgmt.containerservice.models import (ManagedClusterAgentPoolProfile, ManagedCluster)
    _l_(628448)

except ImportError:
    pass

def main(env: _n_(628449, "str", lambda: str)) -> _n_(628450, "str", lambda: str):
    _l_(628487)

    _c_(628453, _a_(628452, _n_(628451, "logging", lambda: logging), "info"), 'Python aks-upgrade function processed a request.')
    _l_(628454)
    #print("Environment:", env)
    if _n_(628455, "env", lambda: env):
        _l_(628486)

        try:
            _l_(628471)

            credential = _c_(628461, _n_(628456, "ClientSecretCredential", lambda: ClientSecretCredential), tenant_id='mytenantid',
              client_id = _a_(628458, _n_(628457, "os", lambda: os), "environ")["function_client_id"],  
              client_secret= _a_(628460, _n_(628459, "os", lambda: os), "environ")["function_client_secret"]
            )
            _l_(628462)
            
            sub_client = _c_(628465, _n_(628463, "SubscriptionClient", lambda: SubscriptionClient), credential=_n_(628464, "credential", lambda: credential))
            _l_(628466)
        except:
            _l_(628470)

            _c_(628468, _n_(628467, "print", lambda: print), "An exception occurred")
            _l_(628469)
        _c_(628473, _n_(628472, "print", lambda: print), "Listing Subscriptions....")
        _l_(628474)
        for sub in _c_(628478, _a_(628477, _a_(628476, _n_(628475, "sub_client", lambda: sub_client), "subscriptions"), "list")):
            _l_(628485)

            _c_(628483, _n_(628479, "print", lambda: print), "Sub_Name:", _a_(628481, _n_(628480, "sub", lambda: sub), "display_name"), "Environment:", _n_(628482, "env", lambda: env))
            _l_(628484)