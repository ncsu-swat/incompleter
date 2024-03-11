#Source: https://stackoverflow.com/questions/39114176/typeerror-unorderable-types-int-guessing-game
from tkinter import*
import random

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.widgets()
        self.answer = Guessing_game(starting_number = 0,
                                    ending_number = 100)

    def widgets(self):

        Label(self,
              text = "Hello welcome to new_version of the Guess My Number!"
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = "Guess the number(0-100):"
              ).grid(row = 1, column = 0, sticky = W)

        self.user_answer = Entry(self)
        self.user_answer.grid(row = 1, column = 1, sticky = W)

        Button(self,
               text = "submit",
               command = self.submit
               ).grid(row = 3, column = 0, sticky = W)

        self.txt = Text(self, width = 50, height = 20, wrap = WORD)
        self.txt.grid(row = 4, column = 0, columnspan = 4, sticky = W)

    def submit(self):

        user_answer = self.user_answer.get()    

        if user_answer != None:
           int(user_answer) 
        if int(user_answer) not in range(101):
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Your guess is not in proper range")
        elif int(user_answer) > self.answer:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Your guess is higher than the answer")
        elif int(user_answer) < self.answer:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Your guess is lower than the answer")
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Your guess is right! the number is", self.answer)

class Guessing_game(object):
    def __init__(self, starting_number, ending_number):
        self.answer = random.randint(starting_number,ending_number)

    def __str__(self):
        return self.answer
#main
root = Tk()
app = Application(root)
root.mainloop()