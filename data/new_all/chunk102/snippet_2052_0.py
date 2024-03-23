from functools import reduce

def oddTimes(input):
    print(reduce(lambda a, b: a ^ b, input))
if __name__ == '__main__':
    oddTimes(input)