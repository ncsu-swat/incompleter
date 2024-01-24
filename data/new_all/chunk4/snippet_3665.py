# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70197401/azure-function-attributeerror-subscriptionclient-object-has-no-attribute-su
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(590819)

except ImportError:
    pass
try:
    import subprocess
    _l_(590821)

except ImportError:
    pass
try:
    import json
    _l_(590823)

except ImportError:
    pass
try:
    import os
    _l_(590825)

except ImportError:
    pass
try:
    from azure.cli.core import get_default_cli
    _l_(590827)

except ImportError:
    pass
try:
    from azure.mgmt.containerservice import ContainerServiceClient
    _l_(590829)

except ImportError:
    pass
try:
    from azure.identity import ClientSecretCredential
    _l_(590831)

except ImportError:
    pass
try:
    from azure.mgmt.subscription import SubscriptionClient
    _l_(590833)

except ImportError:
    pass
try:
    from azure.mgmt.resource import ResourceManagementClient
    _l_(590835)

except ImportError:
    pass
try:
    from azure.mgmt.containerservice.models import (ManagedClusterAgentPoolProfile, ManagedCluster)
    _l_(590837)

except ImportError:
    pass

def main(env: _n_(590838, "str", lambda: str)) -> _n_(590839, "str", lambda: str):
    _l_(590876)

    _c_(590842, _a_(590841, _n_(590840, "logging", lambda: logging), "info"), 'Python aks-upgrade function processed a request.')
    _l_(590843)
    #print("Environment:", env)
    if _n_(590844, "env", lambda: env):
        _l_(590875)

        try:
            _l_(590860)

            credential = _c_(590850, _n_(590845, "ClientSecretCredential", lambda: ClientSecretCredential), tenant_id='mytenantid',
              client_id = _a_(590847, _n_(590846, "os", lambda: os), "environ")["function_client_id"],  
              client_secret= _a_(590849, _n_(590848, "os", lambda: os), "environ")["function_client_secret"]
            )
            _l_(590851)
            
            sub_client = _c_(590854, _n_(590852, "SubscriptionClient", lambda: SubscriptionClient), credential=_n_(590853, "credential", lambda: credential))
            _l_(590855)
        except:
            _l_(590859)

            _c_(590857, _n_(590856, "print", lambda: print), "An exception occurred")
            _l_(590858)
        _c_(590862, _n_(590861, "print", lambda: print), "Listing Subscriptions....")
        _l_(590863)
        for sub in _c_(590867, _a_(590866, _a_(590865, _n_(590864, "sub_client", lambda: sub_client), "subscriptions"), "list")):
            _l_(590874)

            _c_(590872, _n_(590868, "print", lambda: print), "Sub_Name:", _a_(590870, _n_(590869, "sub", lambda: sub), "display_name"), "Environment:", _n_(590871, "env", lambda: env))
            _l_(590873)