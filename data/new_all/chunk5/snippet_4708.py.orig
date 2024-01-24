#Source: https://stackoverflow.com/questions/51775820/showing-typeerror-unsupported-operand-types-for-int-and-nonetype
#A python program to illustrate Caesar Cipher Technique

import sys, random

class Process:

    def main():
        print("\nA python program to illustrate Caesar Cipher Technique.")
        myMode = getMode()
        if myMode == 'Encrypt':
            myMessage = input("\nEnter the Text You want to be Converted...\n\n")
            myKey = getKey()
            translated = encryptMessage(myKey, myMessage)   
            print ("\nYour Mode        : " + myMode)
            print ("\nYour Text        : " + myMessage)
            print ("\nKey              : " + myKey)
            print ("\nEncrypted Text   : " + translated)
            Testing(myKey, myMessage, translated)
            Exit()
        elif myMode == 'Decrypt':
            myMessage = input("\nEnter the Cipher Text You want to be Decrypted...\n\n")
            Key = keyVal()
            myKey = Key
            translated = decryptMessage(myKey, myMessage)
            print ("\nYour Mode        : " + myMode)
            print ("\nYour Cipher Text : " + myMessage)
            print ("\nKey              : " + myKey)
            print ("\nDecrypted Text   : " + translated)
            Exit()
        else :
            print ("\ntWrong Choice Please Try Again ... \n\n")
            main()


    def getMode():
        mode = input("\nEnter Your Choice for Caesar Cipher Technique\ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n").lower()
        if mode in 'encrypt e decrypt d'.split():
            if mode in 'encrypt e'.split():
                mode = 'Encrypt'
            elif mode in 'decrypt d'.split():
                mode = 'Decrypt'
            else:
                getMode()
        else:
            print("\nOops! Wrong Choice, Please choose Again...\n\n")
            getMode()
        myMode = mode
        return myMode


    def getKey():
        keyMode()


    def keyMode():
        keyMode = input("\nWant to give Key Manually? or Want it to be Auto Generated?\ni.e. Type ('Yes' for Manual or 'Auto' for Auto Generated Key)\n\n")
        if keyMode == 'Yes':
            keyManual()
        elif keyMode =='Auto':
            keyAuto()
        else:
            print("\nOops! Wrong Choice, Please Try Again...\n\n")


    def keyManual():
        key = 0
        minimum = 1
        maximum = 26
        keyMode = 'Manual'
        key = int (input ("\nEnter Your Choice Between %s & %s to be Shift Number as a Key:\n\n" %(minimum, maximum)))
        if (key >= minimum and key <= maximum):
            return key
        else:
            print("\nOops! Wrong Choice, Please choose between %s & %s, Try Again...\n\n" %(minimum, maximum))
            keyManual()
        myKey = int(key)


    def keyAuto():
        minimum = 1
        maximum = 26
        total = maximum + 1
        keyMode = 'Auto'
        myKey = random.randint(minimum, total)
        return myKey


    def keyVal():
        key = 0
        minimum = 1
        maximum = 26
        keyMode = 'Validation'
        key = int (input ("\nEnter the Key provided to You...\n\n"))
        if (key >= minimum and key <= maximum):
            return key
        else:
            print("\nOops! Wrong Key, Please Try Again...\n\n")
            keyVal()
        myKey = int(key)


    def Testing(myKey, myMessage, translated):
        Test = input("\nDo you want to Check what your Original Text was by Decrypting Message?\n\ni.e.(Type 'Yes'/'No')\n\n")
        if Test == 'Yes':
            myMode = 'Decrypt'
            Key = myKey
            myKey = Key
            Encrypted = translated
            myMessage = Encrypted
            translated = decryptMessage(myKey, myMessage)
            print ("\nYour Mode        : " + myMode)
            print ("\nYour Cipher Text : " + myMessage)
            print ("\nKey              : " + myKey)
            print ("\nDecrypted Text   : " + translated)
        elif Test == 'No':
            print ("\nThank You...!\n")
        else:
            print ("\nWrong Choice Please Try Again ... \n\n")
            Testing(myKey, myMessage, translated)


    def encryptMessage(key, message):
        return translateMessage(key, message, 'Encrypt')


    def decryptMessage(key, message):
        return translateMessage(key, message, 'Decrypt')


    def translateMessage(key, message, mode):
        translated = ''
        if mode == 'Decrypt':
            key = -key
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key
                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                translated += chr(num)
            else:
                translated += symbol
        return translated


    def Exit():
        Exit = input ("\nDo You want to Run the Program again? (Type 'Yes'/'No')\n\n")
        if Exit == 'Yes':
            main()
        else:
            print ("\n          --/--\--/End\--/--\-- \n\n")

Process.main()

input()