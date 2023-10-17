def count_primes(n):
    if n < 2:
        return 0

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, (n//2)+1):
        if primes[i]:
            for j in range(i*i, n+1 , i):
                primes[j] = False

    return sum(primes)

# Example usage:
n= int(input())
result = count_primes(n)
print(result)
