def sum_div(number):
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))