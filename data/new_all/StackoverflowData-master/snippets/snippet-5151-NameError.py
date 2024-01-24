#Source: https://stackoverflow.com/questions/75355763/pyhton-typeerror-unsupported-operand-types-for-float-and-nonetype
def divide(a, b):
    return a/b
def pow(a, b):
    return a**b
def addA(a, b):
    return a+b
def subA(a, b):
    return a-b
def mul (a, b):
    return a*b

operators = {
  '+': addA,
  '-': subA,
  '*': mul,
  '/': divide,
  '^': pow,


}
def extract_expression(s):
    start = s.index('[')
    end = s.rindex(']')
    while ']' in s:

        return s[start + 1:end]

def calculate(s):
    while '[' in s:
        sub_expression = extract_expression(s)
        result = calculate(sub_expression)
        s = s.replace('[' + sub_expression + ']', str(result))

    if s.isdigit():
        return float(s)

    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

calc = input("Type calculation:\n")
print("Answer: " + str(calculate(calc)))