#Source: https://stackoverflow.com/questions/73028953/reading-file-from-a-different-project-gcloud-file-not-found-error-even-though-t
from google.cloud import bigquery
from analytics import Clients, ClientType
from datetime import datetime, date, timedelta
from pytz import timezone
from typing import List
from pyarrow import json as pyj
import pyarrow.parquet as pq
import newlinejson as nlj

bigquery_client = Clients.get_client(ClientType.STORAGE, name='w')
write_client = Clients.get_client(ClientType.BIGQUERY, name='w')
k_client = Clients.get_client(ClientType.BIGQUERY, name='w')

bucket ='update'


file_name_prefix = "al_"
target_table = k_client.get_table("w.junk.json_table1")

def get_dates() -> List[str]:
    """
    Return dates for which log files have to be checked
    """
    end = date.fromisoformat(str(datetime.date(datetime.now(timezone("EST")))))
    return [str(end - timedelta(days=1)), str(end)]

def get_bucket_files(bucket, file_name_prefix):
    # if full_path:
    path = "gs://{}/{}"
    #path = "https://storage.googleapis.com/{}/{}"
    return [
        path.format(bucket, b.name)
        for b in bigquery_client.list_blobs(bucket, prefix=file_name_prefix)
    ]

def get_latest_file() -> str:
        """
        Get all files for the current prefix between start and end date
        """
        files = []
        files_json = []

        for d in get_dates():
            prefix = file_name_prefix + d[4:] + "-" + d[:4]

            files += get_bucket_files(bucket, file_name_prefix)
            for k in files:
                filename = k.split('/')[-1]
                if 'json' in filename:
                    files_json.append(k)
            return max(files_json)

def pipeline():
    job_config = bigquery.LoadJobConfig(
#         schema=[
#             bigquery.SchemaField("name", "STRING")
#         ],
        autodetect=True,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )
    f = get_latest_file()
    print(f)
    table = pyj.read_json(f)
    # pq.write_table(target_table, table.parquet)
    # with nlj.open(f) as src:
    #     with nlj.open('out.json', 'w') as dst:
    #         for line in src:
    #                  dst.write(line)
#     k_client.load_table_from_uri(
#         f, target_table, job_config=job_config
#     ).result()


pipeline()