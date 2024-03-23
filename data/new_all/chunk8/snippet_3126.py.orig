#Source: https://stackoverflow.com/questions/42701877/str-find-typeerror-unsupported-operand-types-for-int-and-str
from tkinter import *
master = Tk()
master.title("Caeser Cipher Program")
master.geometry("300x200")

frame1 = Frame(master)
frame2 = Frame(master)
frame3 = Frame(master)
frame4 = Frame(master)
frame5 = Frame(master)
frame6 = Frame(master)


global encryptedText
global file
global shiftKey
file = ""
encryptedText = ""
removeSpaces = ""
def Start():
    frame1.grid()
    Question = Label(frame1, text = "Would you like to encrypt or decrypt a statement?\n\n\n")
    Question.grid(row = 0, column = 1)
    ButtonPlace1 = Button(frame1, text = "Encrypt", command = EncryptChosen)
    ButtonPlace2 = Button(frame1, text = "Decrypt", command = decrypt_command)
    ButtonPlace1.place(x = 75, y = 50, anchor = "c")
    ButtonPlace2.place(x = 175, y = 50, anchor = "c")

def EncryptChosen():
 frame1.destroy()
 frame2.grid()
 Question = Label(frame2, text = "What would you like to shift it by?\t\t\t\n\n\n\n\n ")
 ButtonPlace3 = Entry(frame2)
 def SubmitEncryptionKey():
         shiftKey = ButtonPlace3.get()
         frame2.destroy()
         frame3.grid()
         Question = Label(frame3, text = "What would you like it to say?\t\t\t\n\n\n\n\n" )
         ButtonPlace5 = Entry(frame3)
         def SubmitText():
            file = ButtonPlace5.get()
            frame3.destroy()
            frame4.grid()
            Question = Label(frame4, text = "Would you like to remove spaces?\t\t\t\n\n\n\n\n")
            Question.grid(row = 0, column = 1)
            def doRemoveSpaces():
                    global spacesStatement
                    global removeSpaces
                    spacesStatement = "spaces will be removed"
                    removeSpaces = "True"
                    ReadyToEncrypt()
            ButtonPlace7 = Button(frame4, text = "Yes", command = doRemoveSpaces)
            def doNotRemoveSpaces():
                    global spacesStatement
                    global removeSpaces
                    spacesStatement = "spaces will not be removed"
                    removeSpaces = "False"
                    ReadyToEncrypt()
            ButtonPlace8 = Button(frame4, text = "No", command = doNotRemoveSpaces)
            def ReadyToEncrypt():
                    frame4.destroy()
                    frame5.grid()
                    Question = Label(frame5, text = file + "\n will be encrypted by " + shiftKey + " and \n" + spacesStatement + ".\t\t\t\n\n\n\n")
                    Question.grid(row = 0, column = 1)
                    def encryptSetup():

                            def encrypt(character):
                                alphabet = 'abcdefghijklmnopqrstuvwxyz '
                                character = character.lower()
                                if character.isalpha():
                                    position = str(alphabet).find(character) + shiftKey
                                    if position > 25:
                                        position -= 26 
                                    return alphabet[position]
                                else:
                                    return character

                            for line in file:
                              for c in line:
                                global encryptedText
                                encryptedText = encryptedText + encrypt(c)

                            if removeSpaces == "True":
                               encryptedText = encryptedText.replace(" ","")
                            frame5.destroy()
                            frame6.grid()
                            Question = Label(frame6, text = "Here is your encrypted message: \n" + encryptedText)
                            Question.grid(row = 0, column = 1)    

                    ButtonPlace9 = Button(frame5, text = "Encrypt!", command = encryptSetup)
                    ButtonPlace9.place(x=175,y=50)
            ButtonPlace7.place(x = 75, y = 50, anchor = "c")
            ButtonPlace8.place(x = 175, y = 50, anchor = "c")
         ButtonPlace6 = Button(frame3, text = "Submit", command = SubmitText)
         Question.grid(row = 0, column = 1)
         ButtonPlace5.place(x=50,y=50)
         ButtonPlace6.place(x=175,y=45)
 ButtonPlace4 = Button(frame2, text = "Submit", command = SubmitEncryptionKey)
 Question.grid(row = 0, column = 1)
 ButtonPlace3.place(x=50,y=50)
 ButtonPlace4.place(x=175,y=45)



frame1.grid()
Question = Label(frame1, text = "Would you like to encrypt or decrypt a statement?\n\n\n")
Question.grid(row = 0, column = 1)
ButtonPlace1 = Button(frame1, text = "Encrypt", command = EncryptChosen)
ButtonPlace2 = Button(frame1, text = "Decrypt", command = "")
ButtonPlace1.place(x = 75, y = 50, anchor = "c")
ButtonPlace2.place(x = 175, y = 50, anchor = "c")

master.loop()