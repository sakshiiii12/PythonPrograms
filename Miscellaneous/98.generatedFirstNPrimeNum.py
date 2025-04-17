#Python program to generate the first n prime numbers.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
        return True

def generatedPrime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num = num + 1
    return primes

print("The first 100 prime numbers are:",generatedPrime(100))
