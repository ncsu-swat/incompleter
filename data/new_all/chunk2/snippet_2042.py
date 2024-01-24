# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67377345/typeerror-unsupported-format-string-passed-to-nonetype-format-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3, datetime, sys, getopt, re
    _l_(463763)

except ImportError:
    pass
try:
    from operator import itemgetter
    _l_(463765)

except ImportError:
    pass
try:
    from table_logger import TableLogger
    _l_(463767)

except ImportError:
    pass

class buck:
    _l_(463934)

    TARIFAWS = 0.023 # 0,023 USD por GB (Primeiros 50 TB por mês)
    _l_(463768) # 0,023 USD por GB (Primeiros 50 TB por mês)


    counter = 0 
    _l_(463769) 

    def __init__(self, s3bucket):
        _l_(463866)

        _n_(463770, "buck", lambda: buck).counter = _a_(463772, _n_(463771, "buck", lambda: buck), "counter") + 1
        _l_(463773)
        _n_(463774, "self", lambda: self).name = _a_(463776, _n_(463775, "s3bucket", lambda: s3bucket), "name") 
        _l_(463777) 
        _n_(463778, "self", lambda: self).creationdate = _a_(463780, _n_(463779, "s3bucket", lambda: s3bucket), "creation_date")
        _l_(463781)
        _n_(463782, "self", lambda: self).size = _c_(463786, _a_(463784, _n_(463783, "self", lambda: self), "metricCloudwatch"), _n_(463785, "s3bucket", lambda: s3bucket),"BucketSizeBytes", "StandardStorage")
        _l_(463787)
        _n_(463788, "self", lambda: self).nbreObj = _c_(463792, _a_(463790, _n_(463789, "self", lambda: self), "metricCloudwatch"), _n_(463791, "s3bucket", lambda: s3bucket),"NumberOfObjects", "AllStorageTypes")
        _l_(463793)
        
        try:
            _l_(463807)

            _c_(463800, _a_(463797, _c_(463796, _a_(463795, _n_(463794, "boto3", lambda: boto3), "client"), 's3'), "get_bucket_encryption"), Bucket=_a_(463799, _n_(463798, "s3bucket", lambda: s3bucket), "name"))
            _l_(463801)
            _n_(463802, "self", lambda: self).number = True
            _l_(463803)
        except:
            _l_(463806)

            _n_(463804, "self", lambda: self).number = False
            _l_(463805)
        
        _n_(463808, "self", lambda: self).region = _c_(463815, _a_(463812, _c_(463811, _a_(463810, _n_(463809, "boto3", lambda: boto3), "client"), 's3'), "get_bucket_location"), Bucket=_a_(463814, _n_(463813, "s3bucket", lambda: s3bucket), "name"))['LocationConstraint'] 
        _l_(463816) 
        
        _n_(463817, "self", lambda: self).cout = _c_(463823, _n_(463818, "round", lambda: round), _a_(463820, _n_(463819, "self", lambda: self), "size") / 1024**3 * _a_(463822, _n_(463821, "self", lambda: self), "TARIFAWS"),2) 
        _l_(463824) 
                
        try:
            _l_(463838)

            _c_(463831, _a_(463828, _c_(463827, _a_(463826, _n_(463825, "boto3", lambda: boto3), "client"), 's3'), "get_bucket_replication"), Bucket=_a_(463830, _n_(463829, "s3bucket", lambda: s3bucket), "name"))
            _l_(463832)
            _n_(463833, "self", lambda: self).replica = True
            _l_(463834)
        except:
            _l_(463837)

            _n_(463835, "self", lambda: self).replica = False
            _l_(463836)

        def collObjInfo(self):
            _l_(463859)

            s3obj = _c_(463845, _a_(463842, _c_(463841, _a_(463840, _n_(463839, "boto3", lambda: boto3), "client"), 's3'), "list_objects_v2"), Bucket=_a_(463844, _n_(463843, "self", lambda: self), "name"))
            _l_(463846)
            _n_(463847, "self", lambda: self).lastupdate = None
            _l_(463848)
            _n_(463849, "self", lambda: self).typeStorage = None
            _l_(463850)
            if _n_(463851, "s3obj", lambda: s3obj)['KeyCount'] != 0:
                _l_(463858)

                _n_(463852, "self", lambda: self).lastupdate = _n_(463853, "s3obj", lambda: s3obj)['Contents'][0]['LastModified']
                _l_(463854)
                _n_(463855, "self", lambda: self).typeStorage = _n_(463856, "s3obj", lambda: s3obj)['Contents'][0]['StorageClass']
                _l_(463857)
        _c_(463862, _n_(463860, "collObjInfo", lambda: collObjInfo), _n_(463861, "self", lambda: self))
        _l_(463863)
        _n_(463864, "self", lambda: self).public = False 
        _l_(463865) 


    def __str__(self):
        _l_(463876)

        aux = _c_(463870, _n_(463867, "str", lambda: str), _a_(463869, _n_(463868, "self", lambda: self), "__class__")) + ": " + _c_(463874, _n_(463871, "str", lambda: str), _a_(463873, _n_(463872, "self", lambda: self), "__dict__"))
        _l_(463875)
        return aux

    def __getitem__(self, key):
        _l_(463887)

        if _n_(463877, "key", lambda: key) == 'region':
            _l_(463881)

            aux = _a_(463879, _n_(463878, "self", lambda: self), "region")
            _l_(463880)
            return aux
        if _n_(463882, "key", lambda: key) == 'typeStorage':
            _l_(463886)

            aux = _a_(463884, _n_(463883, "self", lambda: self), "typeStorage")
            _l_(463885)
            return aux

    def getSize(self, human=False):
        _l_(463898)

        if _n_(463888, "human", lambda: human):
            _l_(463897)

            aux = _c_(463892, _n_(463889, "humanReadable", lambda: humanReadable), _a_(463891, _n_(463890, "self", lambda: self), "size"))
            _l_(463893)
            return aux
        else:
            aux = _a_(463895, _n_(463894, "self", lambda: self), "size")
            _l_(463896)
            return aux

    def metricCloudwatch(self, bucket, nameMetric, storage):
        _l_(463933)

        cloudwatch = _c_(463901, _a_(463900, _n_(463899, "boto3", lambda: boto3), "client"), 'cloudwatch')
        _l_(463902)
        now = _c_(463906, _a_(463905, _a_(463904, _n_(463903, "datetime", lambda: datetime), "datetime"), "now"))
        _l_(463907)
        try:
            _l_(463932)

            cloudwatch_size = _c_(463923, _a_(463909, _n_(463908, "cloudwatch", lambda: cloudwatch), "get_metric_statistics"), Namespace='AWS/S3',
                MetricName=_n_(463910, "nameMetric", lambda: nameMetric),
                Dimensions=[
                    {'Name': 'BucketName', 'Value': _a_(463912, _n_(463911, "bucket", lambda: bucket), "name")},
                    {'Name': 'StorageType', 'Value': _n_(463913, "storage", lambda: storage)}
                ],
                Statistics=['Maximum'],
                Period=86400,
                StartTime=_c_(463919, _a_(463918, (_n_(463914, "now", lambda: now) - _c_(463917, _a_(463916, _n_(463915, "datetime", lambda: datetime), "timedelta"), days=1)), "isoformat")),
                EndTime=_c_(463922, _a_(463921, _n_(463920, "now", lambda: now), "isoformat"))
            )
            _l_(463924)
            if _n_(463925, "cloudwatch_size", lambda: cloudwatch_size)["Datapoints"]:
                _l_(463929)

                aux = _n_(463926, "cloudwatch_size", lambda: cloudwatch_size)["Datapoints"][0]['Maximum']
                _l_(463927)
                return aux
            else:
                aux = 0
                _l_(463928)
                return aux
        except:
            _l_(463931)

            aux = 0
            _l_(463930)
            return aux
def humanReadable(num, suffix='B'):
    _l_(463948)

    for unit in ['','K','M','G','T','P']:
        _l_(463944)

        if _c_(463937, _n_(463935, "abs", lambda: abs), _n_(463936, "num", lambda: num)) < 1024.0:
            _l_(463942)

            aux = "%3.1f%s%s" % (_n_(463938, "num", lambda: num), _n_(463939, "unit", lambda: unit), _n_(463940, "suffix", lambda: suffix))
            _l_(463941)
            return aux
        num /= 1024.0
        _l_(463943)
    aux = "%.1f%s%s" % (_n_(463945, "num", lambda: num), 'Yi', _n_(463946, "suffix", lambda: suffix))
    _l_(463947)
    return aux

def help():
    _l_(463958)

    _c_(463950, _n_(463949, "print", lambda: print), "Uso : bucket.py [OPTIONS]")
    _l_(463951)
    _c_(463953, _n_(463952, "print", lambda: print), "Exibe informações sobre buckets AWS S3, por padrão")
    _l_(463954)
    _c_(463956, _n_(463955, "print", lambda: print), "Argumentos : \n\
    --help \t\t\t ajuda\n\
    --crypted-only \t\t mostra apenas buckets criptografados\n\
    -c, --csv \t\t mostra o resultado em CSV\n\
    -s, --sorted \t\t agrupar resultados por região e grupo de armazenamento\n\
    -h, --human-readable \t exibem tamanhos de 1024\n\
    -f, --filter=filter \t filtra a lista de buckets com base na expressão regular FILTER") 
    _l_(463957) 

def main():
    _l_(464132)

    
    csv=False
    _l_(463959)
    human = False
    _l_(463960)
    group = False
    _l_(463961)
    filterCrpt = False
    _l_(463962)
    filter = None
    _l_(463963)
    
    try:
        _l_(463981)

        opts, args = _c_(463968, _a_(463965, _n_(463964, "getopt", lambda: getopt), "getopt"), _a_(463967, _n_(463966, "sys", lambda: sys), "argv")[1:], "shcf:", ["sorted", "help", "csv", "human-readable", "crypted-only", "filter:"])
        _l_(463969)
    except:
        _l_(463980)

        _c_(463971, _n_(463970, "print", lambda: print), "Comando incorreto, aqui está a ajuda: ")
        _l_(463972)
        _c_(463974, _n_(463973, "help", lambda: help))
        _l_(463975)
        _c_(463978, _a_(463977, _n_(463976, "sys", lambda: sys), "exit"), 2)
        _l_(463979)

    for opts, args in _n_(463982, "opts", lambda: opts):
        _l_(464019)

        if _n_(463983, "opts", lambda: opts) == "--help":
            _l_(464018)

            _c_(463985, _n_(463984, "help", lambda: help))
            _l_(463986)
            _c_(463989, _a_(463988, _n_(463987, "sys", lambda: sys), "exit"))
            _l_(463990)
        elif _n_(463991, "opts", lambda: opts) == "--crypted-only":
            _l_(464017)

            filterCrpt = True
            _l_(463992)
        elif _n_(463993, "opts", lambda: opts) in ("-c", "--csv"):
            _l_(464016)

            csv = True
            _l_(463994)
        elif _n_(463995, "opts", lambda: opts) in ("-s", "--sorted"):
            _l_(464015)

            group = True
            _l_(463996)
        elif _n_(463997, "opts", lambda: opts) in ("-h", "--human-readable"):
            _l_(464014)

            human = True
            _l_(463998)
        elif _n_(463999, "opts", lambda: opts) in ("-f", "--filter"):
            _l_(464013)

            if _c_(464002, _n_(464000, "len", lambda: len), _n_(464001, "args", lambda: args)):
                _l_(464012)

                filter = _n_(464003, "args", lambda: args)
                _l_(464004)
            else:
                _c_(464006, _n_(464005, "help", lambda: help))
                _l_(464007)
                _c_(464010, _a_(464009, _n_(464008, "sys", lambda: sys), "exit"), 2)
                _l_(464011)
    s3 = _c_(464022, _a_(464021, _n_(464020, "boto3", lambda: boto3), "resource"), 's3')
    _l_(464023)
    bucks = [] 
    _l_(464024) 

    listeS3Bucks = _c_(464028, _a_(464027, _a_(464026, _n_(464025, "s3", lambda: s3), "buckets"), "all"))
    _l_(464029)
    for bucket in _n_(464030, "listeS3Bucks", lambda: listeS3Bucks):
        _l_(464075)

        try:
            _l_(464046)

            if _n_(464031, "filter", lambda: filter):
                _l_(464037)

                _c_(464035, _a_(464033, _n_(464032, "re", lambda: re), "match"), _n_(464034, "filter", lambda: filter),"Test chain")
                _l_(464036)
        except:
            _l_(464045)

            _c_(464039, _n_(464038, "print", lambda: print), "Regular expression error")
            _l_(464040)
            _c_(464043, _a_(464042, _n_(464041, "sys", lambda: sys), "exit"), 2)
            _l_(464044)

        if (_n_(464047, "filter", lambda: filter) and _c_(464053, _a_(464049, _n_(464048, "re", lambda: re), "match"), _n_(464050, "filter", lambda: filter),_a_(464052, _n_(464051, "bucket", lambda: bucket), "name"))) or not _n_(464054, "filter", lambda: filter):
            _l_(464074)

            try:
                _l_(464073)

                _c_(464060, _a_(464056, _n_(464055, "bucks", lambda: bucks), "append"), _c_(464059, _n_(464057, "buck", lambda: buck), _n_(464058, "bucket", lambda: bucket))) 
                _l_(464061) 
            except:
                _l_(464072)

                _c_(464063, _n_(464062, "print", lambda: print), "Erro ao conectar ao AWS, verifique suas configurações")
                _l_(464064)
                _c_(464066, _n_(464065, "print", lambda: print), "Para obter mais informações: https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html")
                _l_(464067)
                _c_(464070, _a_(464069, _n_(464068, "sys", lambda: sys), "exit"), 2)
                _l_(464071)

    if _n_(464076, "group", lambda: group):
        _l_(464089)

        bucks = _c_(464081, _n_(464077, "sorted", lambda: sorted), _n_(464078, "bucks", lambda: bucks), key=_c_(464080, _n_(464079, "itemgetter", lambda: itemgetter), 'region'))
        _l_(464082)
        bucks = _c_(464087, _n_(464083, "sorted", lambda: sorted), _n_(464084, "bucks", lambda: bucks), key=_c_(464086, _n_(464085, "itemgetter", lambda: itemgetter), 'typeStorage'))
        _l_(464088)
    tbl = _c_(464092, _n_(464090, "TableLogger", lambda: TableLogger), columns='name,creation date,last update,size,number of objects,number,storage,public,region,cost,replica',
        csv=_n_(464091, "csv", lambda: csv), border=False) 
    _l_(464093) 
        
    for cBuck in _n_(464094, "bucks", lambda: bucks):
        _l_(464131)

        if (_n_(464095, "filterCrpt", lambda: filterCrpt) and _a_(464097, _n_(464096, "cBuck", lambda: cBuck), "number")) or not _n_(464098, "filterCrpt", lambda: filterCrpt):
            _l_(464130)

            _c_(464128, _n_(464099, "tbl", lambda: tbl), _a_(464101, _n_(464100, "cBuck", lambda: cBuck), "name"), _a_(464103, _n_(464102, "cBuck", lambda: cBuck), "creationdate"), _a_(464105, _n_(464104, "cBuck", lambda: cBuck), "lastupdate"), _c_(464109, _a_(464107, _n_(464106, "cBuck", lambda: cBuck), "getSize"), _n_(464108, "human", lambda: human)), _c_(464113, _n_(464110, "str", lambda: str), _a_(464112, _n_(464111, "cBuck", lambda: cBuck), "nbreObj")), 
            _a_(464115, _n_(464114, "cBuck", lambda: cBuck), "number"),_a_(464117, _n_(464116, "cBuck", lambda: cBuck), "typeStorage"), _a_(464119, _n_(464118, "cBuck", lambda: cBuck), "public"), _a_(464121, _n_(464120, "cBuck", lambda: cBuck), "region"), "$"+_c_(464125, _n_(464122, "str", lambda: str), _a_(464124, _n_(464123, "cBuck", lambda: cBuck), "cout")),_a_(464127, _n_(464126, "cBuck", lambda: cBuck), "replica"))
            _l_(464129)
if _n_(464133, "__name__", lambda: __name__) == "__main__":
    _l_(464137)

    _c_(464135, _n_(464134, "main", lambda: main))
    _l_(464136)