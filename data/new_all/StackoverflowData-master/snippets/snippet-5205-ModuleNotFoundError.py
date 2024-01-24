#Source: https://stackoverflow.com/questions/61302958/typeerror-not-supported-between-instances-of-int-and-dict
import xlrd
from xlrd import xldate_as_tuple
import datetime


data1 = xlrd.open_workbook(r'D:\\test.xlsx')
table = data1.sheets()[0]

tables = []


def import_excel(excel):
    for test in range(excel.nrows):
        array = [table.cell_value(test, 0), table.cell_value(test, 1),
                 table.cell_value(test, 2), table.cell_value(test, 3),
                 table.cell_value(test, 4)]
        tables.append(array)


if __name__ == '__main__':
    import_excel(table)
    for i in tables:
        # pass
        print(i)

num1 = tables[0]
num2 = tables[1]
num3 = tables[2]
num4 = tables[3]
num5 = tables[4]

nu1 = 1
while nu1 < num2:
    print("%d\t%d\t%d\t%d\t%d" % (nu1, num2, num3, num4, num5))
    nu1 = nu1 + 1