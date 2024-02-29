from ArithmeticOps.operations import multiply_by_digit, add_two_numbers, divide_by_digit


"""
Initialization of dictionaries for converting digits from bases 2-10,16 into characters and 
vice versa for performing conversions and arithmetic operations
Initialization of dictionaries for fast conversion from base 2 to bases 4,8,16 and vice versa
"""

to_base16 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
from_base16 = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16
}

table_conversion_fast_base4_base2 = {
    '0': '00', '1': '01', '2': '10', '3': '11'
}
table_conversion_fast_base8_base2 = {
    '0': '000', '1': '001', '2': '010', '3': '011', '4': '100',
    '5': '101', '6': '110', '7': '111'
}
table_conversion_fast_base16_base2 = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '0111',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

table_conversion_fast_base2_base4 = {
    '00': '0', '01': '1', '10': '2', '11': '3'
}

table_conversion_fast_base2_base8 = {
    '000': '0', '001': '1', '010': '2', '011': '3', '100': '4',
    '101': '5', '110': '6', '111': '7'
}

table_conversion_fast_base2_base16 = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8',
    '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}


def intermediate_base_conversion(a, source_base, destination_base):
    """
    Converts the given natural number 'a' from the source base to the destination base, using an intermediate base 10
    Converts 'a' from the source base to base 10 through substitution
    Converts the obtained number in base 10 to the destination base through successive divisions
    :param a: natural number, given as a string
    :param source_base: any base p, 2-10, or 16
    :param destination_base: any base q, 2-10, or 16
    :return: c - natural number equal to the number 'a' in source_base, written in destination_base
    """
    b = 0
    a = a[::-1]
    p = source_base
    for i in range(len(a) - 1, -1, -1):
        if a[i].isdigit():
            b = b + int(a[i]) * pow(p, i)
        else:
            b = b + from_base16[a[i]] * pow(p, i)

    string_c = ""
    q = destination_base
    while b != 0:
        cat = b // q
        rest = b % q
        if rest < 10:
            string_c = string_c + str(rest)
        else:
            string_c = string_c + to_base16[rest]
        b = cat

    return string_c[::-1]

def substitution_conversion(a, source_base, destination_base):
    """
    Converts the number 'a' in string form from the source base to the destination base through substitution,
    assuming the source base < destination base
    Each digit is multiplied by the source base raised to the power corresponding to its position
    (numbered from 0 to n-1 from right to left), and the products obtained are summed, with calculations done in the destination base
    The final result represents the number written in the destination base
    :param a: natural number, given as a string
    :param source_base: any base p, 2-10, or 16
    :param destination_base: any base q, 2-10, or 16
    :return: natural number equal to the number 'a' in source_base, written in destination_base
    """
    a = a[::-1]
    result = ""
    b = '0'
    p = source_base
    q = destination_base
    for i in range(0, len(a)):
        power = '1'
        for j in range(0, i):
            # Obtaining the source base raised to the power corresponding to the digit's position in the number,
            # using multiplication by a digit to perform all calculations in the given base
            power = multiply_by_digit(power, str(p), q)

        # Multiplying the obtained power by the digit of the number
        power = multiply_by_digit(power, a[i], q)

        # Adding the results together to obtain the final number written in the destination base
        b = add_two_numbers(b, power, q)
    result = b
    # Returning the final number in the destination base as a string
    return result

def successive_division_conversion(a, source_base, destination_base):
    """
    Converts the number 'a' in string form from the source base to the destination base using successive divisions,
    with calculations performed in the source base
    The number is divided by the destination base until the quotient becomes 0, using division by a digit for this purpose
    The remainders resulting from the divisions written in reverse order represent the given number in the destination base
    :param a: natural number, given as a string
    :param source_base: any base p, 2-10, or 16
    :param destination_base: any base q, 2-10, or 16
    :return: natural number equal to the number 'a' in source_base, written in destination_base
    """
    b = ""
    p = source_base
    q = destination_base
    quotient = a
    # Dividing the number by the destination base until the obtained quotient becomes 0,
    # using division by a digit to perform all calculations in the given base
    while quotient != '0':
        quotient, remainder = divide_by_digit(quotient, str(q), p)
        # Adding the remainder to the string representing the number written in the destination base
        b = b + remainder
    # Returning the reversed string to get the final number in the destination base
    return b[::-1]


def fast_base2_base4_conversion(a):
    """
    Converts the natural number 'a' given as a string from base 2 to base 4 using the fast conversion table
    :param a: natural number, given as a string
    :return: natural number equal to the number 'a' in base 2, written in base 4
    """
    a = a[::-1]
    b = ""
    # Completing with 0s at the end of the number to obtain a grouping corresponding to a digit in the destination base from the fast conversion table
    while len(a) % 2 != 0:
        a = a + '0'
    for i in range(0, len(a) - 1, 2):
        base4_digit = a[i + 1] + a[i]
        b = b + table_conversion_fast_base2_base4[base4_digit]

    return b[::-1]



def fast_base4_base2_conversion(a):
    """
    Converts the natural number 'a' given as a string from base 4 to base 2 using the fast conversion table
    :param a: natural number, given as a string
    :return: natural number equal to the number 'a' in base 4, written in base 2
    """
    b = ""
    for i in range(len(a)):
        b = b + table_conversion_fast_base4_base2[a[i]]
    while b[0] == '0':
        b = b[1:]
    return b



def fast_base2_base8_conversion(a):
    """
    Converts the natural number 'a' given as a string from base 2 to base 8 using the fast conversion table
    :param a: natural number, given as a string
    :return: natural number equal to the number 'a' in base 2, written in base 8
    """
    a = a[::-1]
    b = ""
    # Completing with 0s at the end of the number to obtain a grouping corresponding to a digit in the destination base from the fast conversion table
    while len(a) % 3 != 0:
        a = a + '0'
    for i in range(0, len(a) - 2, 3):
        # Forming a group of digits in base 2 corresponding to a single digit in the destination base
        base8_digit = a[i + 2] + a[i + 1] + a[i]
        b = b + table_conversion_fast_base2_base8[base8_digit]

    return b[::-1]

def fast_base8_base2_conversion(a):
    """
    Converts the natural number 'a' given as a string from base 8 to base 2 using the fast conversion table
    :param a: natural number, given as a string
    :return: natural number equal to the number 'a' in base 8, written in base 2
    """
    b = ""
    for i in range(len(a)):
        b = b + table_conversion_fast_base8_base2[a[i]]
    while b[0] == '0':
        b = b[1:]
    return b


def fast_base2_base16_conversion(a):
    """
    Converts the natural number 'a' given as a string from base 2 to base 16 using the fast conversion table
    :param a: natural number, given as a string
    :return: natural number equal to the number 'a' in base 2, written in base 16
    """
    a = a[::-1]
    b = ""
    # Completing with 0s at the end of the number to obtain a grouping corresponding to a digit in the destination base from the fast conversion table
    while len(a) % 4 != 0:
        a = a + '0'
    for i in range(0, len(a) - 3, 4):
        base16_digit = a[i + 3] + a[i + 2] + a[i + 1] + a[i]
        b = b + table_conversion_fast_base2_base16[base16_digit]

    return b[::-1]



def fast_base16_base2_conversion(a):
    """
    Converts the natural number 'a' given as a string from base 16 to base 2 using the fast conversion table
    :param a: natural number, given as a string
    :return: natural number equal to the number 'a' in base 16, written in base 2
    """
    b = ""
    for i in range(len(a)):
        b = b + table_conversion_fast_base16_base2[a[i]]
    while b[0] == '0':
        b = b[1:]
    return b



# Conversion Tests
# print(substitution_conversion('2105', 16, 10))
# print(intermediate_base_conversion('4512', 9, 4))
# print(successive_division_conversion('27', 8, 10))
# print(base2_to_base4_quick_conversion('1001100'))
# print(base2_to_base8_quick_conversion('10000100'))
# print(base2_to_base16_quick_conversion('111100111'))
# print(base4_to_base2_quick_conversion('8764'))
# print(base16_to_base2_quick_conversion('1F9'))
# print(successive_division_conversion('FFC6', 16, 4))



# Author: Leustean Robert George - group 914