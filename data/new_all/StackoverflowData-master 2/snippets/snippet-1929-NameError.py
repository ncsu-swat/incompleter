#Source: https://stackoverflow.com/questions/22873437/python-3-typeerror-bytes-or-integer-address-expected-instead-of-str-instance
fuse = FUSE(GoogleStorageFUSE(username, password, logfile=logfile), mount_point, **fuse_args)