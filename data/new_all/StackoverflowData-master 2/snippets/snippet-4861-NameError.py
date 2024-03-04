#Source: https://stackoverflow.com/questions/44913006/nameerror-while-calling-module-declaring-default-values-in-a-class-function
def test():
    val = { 'test' : "hello"}
    keypair = statEnc()
    print(str(type(keypair)))
    encval = keypair.end2enc(val, keypair.pubcipher)
    outval = keypair.end2dec(encval, keypair.privcipher)
    print(val, outval)
    if val == eval(outval):
        return(val)
    else:
        return False

if __name__ == '__main__':
    test()