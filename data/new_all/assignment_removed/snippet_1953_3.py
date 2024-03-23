import re
ipv4 = '^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\.(\n            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\.(\n            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\.(\n            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
ipv6 = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|\n        ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:)\n        {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1\n        ,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}\n        :){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{\n        1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA\n        -F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a\n        -fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0\n        -9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,\n        4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}\n        :){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9\n        ])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0\n        -9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]\n        |1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]\n        |1{0,1}[0-9]){0,1}[0-9]))'

def find(Ip):
    if re.search(ipv4, Ip):
        print('IPv4')
    elif re.search(ipv6, Ip):
        print('IPv6')
    else:
        print('Neither')
if __name__ == '__main__':
    Ip = '192.0.2.126'
    find(Ip)
    Ip = '3001:0da8:75a3:0000:0000:8a2e:0370:7334'
    find(Ip)
    find(Ip)