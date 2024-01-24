#Source: https://stackoverflow.com/questions/47372780/how-to-debug-typeerror-object-of-type-stringvar-has-no-len-in-python
##


# Functions

def validate_password(first_pwd, second_pwd):
    """
    validates if password is acceptable
    """

    min_length = 8

    number_of_tests = 6
    test1 = 0 #Both entered passwords are identical.
    test2 = 0 #The password is >= 8 characters in length.
    test3 = 0 #if first and last chars are alpha then both must be different
    test4 = 0 #There are no more than 2 vowels in the password.
    test5 = 0 #The password has at least 1 alphabetic character
              #in either upper or lower case.
    test6 = 0 #Not all alphabetic characters are in the same
              #case (either all upper or all lower).

    # test1
    if first_pwd == second_pwd:
        test1 = 1

    password = first_pwd
    pwd_length = len(password)

    # test2
    if pwd_length >= 8:
        test2 = 1

    # test3

    same = 0

    if password[0].isalpha() and password[pwd_length-1].isalpha():
        if password[0] == password[pwd_length-1].upper():
            same = 1
        if password[0] == password[pwd_length-1].lower():
            same = 1
        if same == 0:
            test3 = 1

    else:
        test3 = 1


    # test4
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    max_vowels = 2
    for vowel in vowels:
        count = count + password.count(vowel)

    if count <= max_vowels:
        test4 = 1

    alpha_chars = []

    # test5
    for char in password:
        if char.isalpha():
            alpha_chars.append(char)
            test5 = 1


    # test6
    alpha_count = len(alpha_chars)
    upper_count = 0
    lower_count = 0
    for char in alpha_chars:
        if char == char.upper():
            upper_count = upper_count + 1
        if char == char.lower():
            lower_count = lower_count + 1

    if alpha_count != upper_count and \
       alpha_count != lower_count:
        test6 = 1

    test_count = test1 + test2 + test3 + test4 \
                 + test5 + test6

    if test_count == number_of_tests:
           return True



    return False

# Program Code

from tkinter import *

root_window = Tk()

# window title
root_window.title("Title")

# window size
root_window.geometry("400x200")

# label asking for password
pwd_label = Label(root_window, text="Please enter your password")
pwd_label.pack()

# pwd entry boxes

pwd1 = StringVar()
pwd1_text = Entry(root_window,textvariable=pwd1) 
pwd1_text.pack()

pwd2 = StringVar()
pwd2_text = Entry(root_window,textvariable=pwd2) 
pwd2_text.pack()

# pwd check button
check_btn = Button(root_window,text="Change Password",command=lambda: validate_password(pwd1, pwd2)) 
check_btn.pack() 




root_window.mainloop()

##