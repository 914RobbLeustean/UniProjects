"""
Initialization of dictionaries for converting digits from bases 2-10,16 into characters and vice versa for performing conversions and arithmetic operations
"""

to_base16 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
from_base16 = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16
}


def multiply_by_digit(number, digit, base):
    """
    Performs the multiplication operation of the number 'number' by the given digit in an arbitrary base, following the algorithm:
    an an-1 ... a1 a0 (p) *
                      b (p)
    _______________________
    cn+1 cn ... c1 c0 (p)

    i=0,n , t0=0

    ci := (ti+ai*b) mod p
    ti+1:=(ti+ai*b) div p
    cn+1 := tn+1

    :param number: natural number, given as a string
    :param digit: natural number <= 9 (or <= F in the case of calculations in base 16)
    :param base: arbitrary base p, 2-10 or 16
    :return: the result of multiplying the number 'number' by the given digit, in the specified base
    """
    result = ""
    number = number[::-1]
    quotient = 0
    remainder = 0
    for i in range(len(number)):
        product = from_base16[number[i]] * from_base16[digit]
        product += quotient
        quotient = product // base
        remainder = product % base
        result = result + to_base16[remainder]
    if quotient != 0:
        result = result + to_base16[quotient]
    return result[::-1]


def divide_by_digit(number, digit, base):
    """
    Performs the division operation of the number 'number' by the given digit in an arbitrary base, following the algorithm:
    an an-1 ... a1 a0 (p) : b (p) = cn cn-1 ... c1 c0 (p) remainder r(p)

    i=n,0 , tn=0

    (ti*p+ai):b = ci remainder ti-1
    r := t -1

    :param number: natural number, given as a string
    :param digit: natural number <= 9 (or <= F in the case of calculations in base 16)
    :param base: arbitrary base p, 2-10 or 16
    :return: the result of dividing the number 'number' by the given digit, in the specified base
    """
    result_quotient = ""
    result_remainder = ""
    quotient = 0
    remainder = 0
    for i in range(len(number)):
        d = remainder * base + from_base16[number[i]]
        quotient = d // from_base16[digit]
        remainder = d % from_base16[digit]
        result_quotient = result_quotient + to_base16[quotient]
    result_remainder = to_base16[remainder]

    if len(result_quotient) > 1:
        while result_quotient[0] == '0':
            result_quotient = result_quotient[1:]

    return result_quotient, result_remainder


def add_two_numbers(number1, number2, base):
    """
    Performs the addition of two numbers in a given base, following the algorithm:

    an an-1 ... a1 a0 (p) +
    bm bm-1 ... b1 b0 (p)
    _____________________
    ck ck-1 ... c1 c0 (p)

    i=0,max(m,n) we assume that we will complete the shorter number with 0s, t0=0

    ci := (ai+bi+ti) mod p
    ti+1 := (ai+bi+ti) div p
    k= max(m,n)+1, cmax(m,n)+1=t max(m,n)+1

    :param number1: natural number, given as a string
    :param number2: natural number, given as a string
    :param base: arbitrary base p, 2-10 or 16
    :return: the result of adding the two numbers in the given base
    """
    number1 = number1[::-1]
    number2 = number2[::-1]
    if len(number1) > len(number2):
        length_diff = len(number1) - len(number2)
        for i in range(length_diff):
            number2 = number2 + '0'
    else:
        length_diff = len(number2) - len(number1)
        for i in range(length_diff):
            number1 = number1 + '0'

    length = len(number1)
    result = ""
    quotient = 0
    remainder = 0
    for i in range(length):
        s = from_base16[number1[i]] + from_base16[number2[i]]
        s += quotient
        quotient = s // base
        remainder = s % base
        result = result + to_base16[remainder]
    if quotient != 0:
        result = result + to_base16[quotient]

    return result[::-1]


def subtract_two_numbers(number1, number2, base):
    """
    Performs the subtraction of two numbers in a given base, following the algorithm:

    Precondition: number1 >= number2
    an an-1 ... a1 a0 (p) -
    bm bm-1 ... b1 b0 (p)
    _____________________
    cn cn-1 ... c1 c0 (p)

    i=0,n we assume that we will complete the shorter number with 0s, t0=0

    ci := p+ai-bi+ti , if ai+ti <bi, ti+1=-1
    ci := ai-bi+ti otherwise, ti+1=0

    :param number1: natural number, given as a string
    :param number2: natural number, given as a string
    :param base: arbitrary base p, 2-10 or 16
    :return: the result of subtracting the two numbers in the given base
    """
    number1 = number1[::-1]
    number2 = number2[::-1]
    if len(number1) > len(number2):
        length_diff = len(number1) - len(number2)
        for i in range(length_diff):
            number2 = number2 + '0'

    length = len(number1)
    result = ""
    borrow = 0
    for i in range(length):
        difference = from_base16[number1[i]] - borrow
        difference = difference - from_base16[number2[i]]
        if difference >= 0:
            result = result + to_base16[difference]
            borrow = 0
        else:
            result = result + to_base16[base - abs(difference)]
            borrow = 1

    while result[-1] == '0':
        result = result[:-1]
    return result[::-1]

# Operations Tests

# print(add_two_numbers('60FF6E', 'C6A44', 16))
# print(multiply_by_digit('F44E', '5', 16))
# print(divide_by_digit("D19E", '7', 16))
# print(divide_by_digit("213", '9', 10))
# print(subtract_two_numbers('10011', '11111', 2))
# print(subtract_two_numbers('A2E2', '9DEF', 16))

# Author: Leustean Robert George - group 914
