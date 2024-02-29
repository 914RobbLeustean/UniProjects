def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_composed(num):
    while True:
        num += 1
        factors = prime_factors(num)
        if len(factors) > 1:
            return num

def prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors

def sequence_element(n):
    count = 0
    num = 1
    while count < n:
        num = next_composed(num)
        count += 1
    return num

n = int(input("Enter n: "))
result = sequence_element(n)
print(f"The {n}-th element of the sequence is: {result}")
