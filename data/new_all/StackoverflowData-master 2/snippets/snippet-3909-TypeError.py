#Source: https://stackoverflow.com/questions/65462896/typeerror-print-takes-0-positional-arguments-but-1-was-given-highschool-edi
###Program 11 Create a binary file with name and roll no. Search for a given roll number and display the name, if not found display appropriate message.
import pickle
import sys
D={}
def main(self):
    try:
        no=input("enter the number of students")
    
        file=open("studentsdetails.dat", "wb+")
        for i in range (no):
            print("enter the information of student %d"%i)
            D["rollno"]=int(input("enter the roll number: "))
            D["Sname"]=input("enter the student name: ")
            D["marks"]=int(input("enter the marks: "))
            pickle.dump(D,file)
        file.close()
    except:
        input("there was some error,press any key to continue")
        pass
def print():
    try:
        file=open("studentsdetails.dat", "rb")
        while True:
            out=pickle.load(file)
            print(out)
    except:
            print("error try again")
            pass
def search():
    try:
        file=open("studentsdetails.dat","rb")
        se=input("enter the roll number to search")
        while True:
            if D["rollno"]==se:
                print("the rollnumber %d the data is:"%se)
                print(D)
            else:
                print("no record found")
                break
        file.close()
    except:
        print("some error occured, try again")
        pass
    

while True:
    intg=input("Enter your choice:\n1. Enter data\n2. Print Data\n3.search data\n4. Exit\n")
    if intg==("1"):
        main()
    if intg==("2"):
        print()
    if intg==("3"):
        search()
    if intg==("4"):
        break