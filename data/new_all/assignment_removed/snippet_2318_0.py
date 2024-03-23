n = int(input('Enter upper limit of range: '))
while sieve:
    prime = min(sieve)
    print(prime, end='\t')
    sieve -= set(range(prime, n + 1, prime))
print()