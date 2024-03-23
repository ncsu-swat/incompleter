def isValidIP(s):
    if s.count('.') != 3:
        return 'Invalid Ip address'
    for ele in l:
        if int(ele) < 0 or int(ele) > 255:
            return 'Invalid Ip address'
    return 'Valid Ip address'
print(isValidIP('666.1.2.2'))