# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76131938/typeerror-can-only-concatenate-list-not-str-to-list-when-upload-to-aws-s3-b
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
AccountName = ["AWSAccountName"]
_l_(536021)

def upload_s3(AccountName,bucket,filename):
    _l_(536046)

    dir = _c_(536024, _a_(536023, _n_(536022, "os", lambda: os), "getcwd"))
    _l_(536025)
    s3 = _c_(536028, _a_(536027, _n_(536026, "boto3", lambda: boto3), "client"), 's3')
    _l_(536029)
    #prefix = 'folder_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "/" + filename
    prefix =  _n_(536030, "AccountName", lambda: AccountName) + 'folder_' + _c_(536035, _a_(536034, _c_(536033, _a_(536032, _n_(536031, "datetime", lambda: datetime), "now")), "strftime"), "%Y-%m-%d_%H-%M-%S") + "/" + _n_(536036, "filename", lambda: filename)
    _l_(536037)
    #s3object = s3.put_object(Bucket=bucket, Key=prefix)
    _c_(536044, _a_(536039, _n_(536038, "s3", lambda: s3), "upload_file"), _n_(536040, "dir", lambda: dir) + '/' +_n_(536041, "filename", lambda: filename), _n_(536042, "bucket", lambda: bucket), _n_(536043, "prefix", lambda: prefix))
    _l_(536045)

if _n_(536047, "__name__", lambda: __name__) == "__main__":
    _l_(536052)

    _c_(536050, _n_(536048, "upload_s3", lambda: upload_s3), _n_(536049, "AccountName", lambda: AccountName), "ec2-idle-workspace-list","EC2_Idle_info_cpu_NetworkIn_NetworkOut.csv")
    _l_(536051)