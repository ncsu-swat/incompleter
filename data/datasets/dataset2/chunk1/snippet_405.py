#Source: https://stackoverflow.com/questions/43403992/typeerror-not-supported-between-instances-of-list-and-int
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 97.0, 98.0, 100.0],
    "quizzes": [98.0, 99.0, 99.0],
    "tests": [100.0, 100.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 35.0, 45.0, 22.0],
    "quizzes": [0.0, 60.0, 58.0],
    "tests": [65.0, 58.0]
}
students = [lloyd,alice,tyler]
def average(numbers):
    total= sum(numbers)
    total = float(total)
    return total / len(numbers) 

def get_average(student):
    homework= average(student["homework"])
    quizzes= average(student["quizzes"])
    tests= average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_student_average(gruppo):
    for student in gruppo:
        results= []
        results.append(get_average(student))
        print (student["name"])
        print (results)
        print (get_letter_grade(results))

get_student_average(students)