"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(numberOfPrimes):
    list = []
    n = 2
    if (numberOfPrimes <= 0):
        raise ValueError(f"numberOfPrimes = {numberOfPrimes} should be a positive integer.")
    else:
        while (len(list) < numberOfPrimes):
            for i in range(2, n):
                if n % i == 0:
                    n += 1
                    break
            else:
                list.append(n)
                n += 1
    print(list)
    return list
