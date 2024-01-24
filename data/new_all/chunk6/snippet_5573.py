# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77711881/typeerrorunsupported-data-type-class-deltalake-table-deltatablehow-to-upl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from azure.storage.blob import BlobServiceClient
    _l_(345375)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(345377)

except ImportError:
    pass
try:
    import json
    _l_(345379)

except ImportError:
    pass
try:
    from deltalake.writer import write_deltalake
    _l_(345381)

except ImportError:
    pass
try:
    from deltalake import write_deltalake, DeltaTable
    _l_(345383)

except ImportError:
    pass
try:
    import asyncio
    _l_(345385)

except ImportError:
    pass
try:
    import ast
    _l_(345387)

except ImportError:
    pass
try:
    from azure.eventhub.aio import EventHubConsumerClient
    _l_(345389)

except ImportError:
    pass

BLOB_CONTAINER_NAME = "iot"
_l_(345390)
EVENT_HUB_CONNECTION_STR = "Endpoint=sb://dhbchisdbc.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=fsdojfosdjf=;EntityPath=iothub-ehub-iothubfree-kcnk-b6c03da7fe"
_l_(345391)
EVENT_HUB_NAME = "iothub-ehub-iothubfree-cdhscb-jcnj"
_l_(345392)
BLOB_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName='dygsgcsd';AccountKey=kdncs+dncsdhncs+AStVSl3cg==;EndpointSuffix=core.windows.net"
_l_(345393)


async def on_event(partition_context, event):
    _l_(345436)

    data=_c_(345399, _a_(345395, _n_(345394, "ast", lambda: ast), "literal_eval"), _c_(345398, _a_(345397, _n_(345396, "event", lambda: event), "body_as_str"), encoding="UTF-8"))
    _l_(345400)
    frame=_c_(345405, _a_(345403, _a_(345402, _n_(345401, "pd", lambda: pd), "DataFrame"), "from_dict"), _n_(345404, "data", lambda: data), orient='index')
    _l_(345406)
    #write to delta format
    _c_(345409, _n_(345407, "write_deltalake", lambda: write_deltalake), '/delta/newtable', _n_(345408, "frame", lambda: frame),mode='append')
    _l_(345410)
    # reading to delta format
    dt = _c_(345412, _n_(345411, "DeltaTable", lambda: DeltaTable), '/delta/newtable')
    _l_(345413)
   
    blob_service_client = _c_(345417, _a_(345415, _n_(345414, "BlobServiceClient", lambda: BlobServiceClient), "from_connection_string"), _n_(345416, "BLOB_STORAGE_CONNECTION_STRING", lambda: BLOB_STORAGE_CONNECTION_STRING))
    _l_(345418)
    blob_path_admin = f'/newPath'
    _l_(345419)
    blob_client_admin = _c_(345424, _a_(345421, _n_(345420, 'blob_service_client', lambda: blob_service_client), 'get_blob_client'), container=_n_(345422, 'BLOB_CONTAINER_NAME', lambda: BLOB_CONTAINER_NAME), blob=_n_(345423, 'blob_path_admin', lambda: blob_path_admin))
    _l_(345425)
    blob_client = _c_(345429, _a_(345427, _n_(345426, 'blob_client_admin', lambda: blob_client_admin), 'upload_blob'), data=_n_(345428, 'dt', lambda: dt), overwrite=True)
    _l_(345430)

    await _c_(345434, _a_(345432, _n_(345431, 'partition_context', lambda: partition_context), 'update_checkpoint'), _n_(345433, 'event', lambda: event))
    _l_(345435)

async def main():
    _l_(345450)


    client = _c_(345441, _a_(345438, _n_(345437, 'EventHubConsumerClient', lambda: EventHubConsumerClient), 'from_connection_string'), _n_(345439, 'EVENT_HUB_CONNECTION_STR', lambda: EVENT_HUB_CONNECTION_STR),
        consumer_group="$Default",
        eventhub_name=_n_(345440, 'EVENT_HUB_NAME', lambda: EVENT_HUB_NAME),
    )
    _l_(345442)
    async with _n_(345443, 'client', lambda: client):
        _l_(345449)

        await _c_(345447, _a_(345445, _n_(345444, 'client', lambda: client), 'receive'), on_event=_n_(345446, 'on_event', lambda: on_event), starting_position="-1")
        _l_(345448)

if _n_(345451, '__name__', lambda: __name__) == "__main__":
    _l_(345462)

    loop = _c_(345454, _a_(345453, _n_(345452, 'asyncio', lambda: asyncio), 'get_event_loop'))
    _l_(345455)
    _c_(345460, _a_(345457, _n_(345456, 'loop', lambda: loop), 'run_until_complete'), _c_(345459, _n_(345458, 'main', lambda: main)))
    _l_(345461)