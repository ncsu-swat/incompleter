#Source: https://stackoverflow.com/questions/42926039/attributeerror-user-questions-object-has-no-attribute
import os
from tkinter import *
import time
import sys

root = Tk()
root.attributes("-fullscreen", True)

class User_Questions:
    def __init__(self, master):

        self.master = master
        master.title("MIT")

        global frame
        frame = Frame(master)
        frame.pack()

        self.choosen_questions = []
        self.choosen_answers = []

        self.choosen_questions_file = open(os.path.expanduser("~/Desktop/Bradfield/Project/" + str(test_choice) + "/Questions.txt"))
        self.choosen_answers_file = open(os.path.expanduser("~/Desktop/Bradfield/Project/" + str(test_choice) + "/Answers.txt"))

        for line in self.choosen_questions_file:
           self.new_question = line.replace("\n","")
           self.choosen_questions.append(self.new_question)

        for line in self.choosen_answers_file:
           self.new_answer = line.replace("\n","")
           self.choosen_answers.append(self.new_answer)

        self.correct_answers = 0

        self.question_label = Label(frame, text = self.choosen_questions[0].replace("1. ",""),  font = "Helvetica", fg = "blue")
        self.question_label.pack()

        self.answer_entry = Entry(frame, text = "", font = "Helvetica")
        self.answer_entry.pack()

        self.answer_entry.bind('<Return>', self.question)

        self.check_test_exists_button = Button(frame, text="SUBMIT", font = "Helvetica", command=self.question)
        self.check_test_exists_button.pack()

        self.back_button = Button(frame, text="GO BACK", font = "Helvetica", command=self.go_back)
        self.back_button.pack()

        self.quit_button = Button(frame, text="QUIT", font = "Helvetica", command=master.destroy)
        self.quit_button.pack()

        def question(self, event):
            for i in range(1, len(self.choosen_questions)):
                return(self.choosen_questions[i+1].replace(i+". ",""))

        def go_back(self):
            frame.destroy()
            my_gui = User_Choose_Test(root)