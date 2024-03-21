import csv
marks = [['RollNo', 'Maths', 'Python'], [1000, 80, 85], [2000, 85, 89], [3000, 82, 90], [4000, 83, 98], [5000, 82, 90]]
with open('my_csv.csv', 'w', newline='') as file:
    writer.writerows(marks)
with open('my_csv.csv', newline='') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
    output = []
    for row in reader:
        output.append(row[:])
for rows in output:
    print(rows)