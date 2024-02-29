# Solve the problem from the second set here

def product_of_PF(n):
    if n <= 1:
        return 0  #No proper factors for n that's <= 1

    product = 1

    for i in range(2, n // 2 + 1): #we iterate from 2 to n / 2 since no prime factors are biggger than n / 2
        if n % i == 0:
            product = product * i #we add every prime factor to the product

    return product

print(product_of_PF(20))