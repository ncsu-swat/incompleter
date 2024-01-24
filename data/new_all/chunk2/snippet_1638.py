# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68105958/typeerror-expected-str-bytes-or-os-pathlike-object-not-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
load_io_monthly_billing_to_snowflake = _c_(458559, _n_(458550, "SnowflakeLoadOperator", lambda: SnowflakeLoadOperator), task_id='load_io_monthly_billing_to_Snowflake',
    table=_c_(458552, _n_(458551, "IOMonthlyBillingSnowflakeTable", lambda: IOMonthlyBillingSnowflakeTable)),
    merge=False,
    partition=_c_(458558, _n_(458553, "MonthlyBillingS3PartitionLatestFile", lambda: MonthlyBillingS3PartitionLatestFile), source_resolver=_n_(458554, "get_latest_io_monthly_billing_file_from_new_prefix", lambda: get_latest_io_monthly_billing_file_from_new_prefix),
        bucket=_c_(458557, _a_(458556, _n_(458555, "Variable", lambda: Variable), "get"), 's3_bucket'),
        location_base="BTR/",
        partition_type=None
    )
)
_l_(458560)