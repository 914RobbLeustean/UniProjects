#
# Write the implementation for A5 in this file
#
import cmath
import re

def is_valid_complex_format(complex_str):
    #Regular expression to match the specified format 'a+bi'
    try:
        pattern = re.compile(r'^\s*([-+]?\d*\.?\d*)([+-]\d*\.?\d*)?i?\s*$') #regex exp
        return bool(pattern.match(complex_str)) #checking if the string matches the defined regular exp pattern
    except Exception as e:
        print(f"Error: {e}")
        return False

def number_split(number: str):

    real_part, imaginary_part = "0", "0"

    #for a or -a
    if "i" not in number:
        real_part = number
        imaginary_part = "0" #imaginary part doesnt exist so the real part is the whole nr

    else:
        #bi
        if "+" not in number and "-" not in number:
            real_part = "0"
            imaginary_part = number #since there's no - or + it means the img part is the whole nr

        #a+bi or -a+bi
        elif "+" in number[1:]:
            index = number[1:].find("+") + 1
            real_part = number[:index]
            imaginary_part = number[index:] #separting accordingly the img and real part

        # a-bi or +a-bi or -a-bi
        elif "-" in number[1:]:
            index = number[1:].find("-") + 1
            real_part = number[:index]
            imaginary_part = number[index:]#same as above but with - instead of +

        # -bi 
        elif number[0] == "-":
            real_part = "0"
            imaginary_part = number #in case the img part is neg and the real part doesnt exist

    if real_part[0] == "+":
        real_part = real_part[1:]

    if imaginary_part[0] == "+":
        if imaginary_part[1] == "i":
            imaginary_part = "1"
        else:
            imaginary_part = imaginary_part[1:] #simplyfying the signs,ex: so "+i" becomes "1" 

    if imaginary_part[-1] == "i":
        imaginary_part = imaginary_part[:-1] #if img part ends with i, we remove it for better visualization

    return real_part, imaginary_part
# 
# Write below this comment  
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def get_real(number) -> int:
    return number[0] #returning the real part of number (first element of the list)


def get_imaginary(number) -> int:
    return number[1] #returning the img part of number (2nd element of the list)


def to_str(number) -> str:
    if str(get_imaginary(number)) != "0":
        if str(get_imaginary(number))[0] != '-':
            return str(get_real(number)) + "+" + str(get_imaginary(number)) + "i"
        return str(get_real(number)) + str(get_imaginary(number)) + "i"
    return str(get_real(number))
#we first check if the img part is not zero, if it's not and it's positive as well, we
#return he string concatenation of the real and imaginary parts with a "+" sign between them

def create_number(number):
    real_part, imaginary_part = number_split(number)
    return [real_part, imaginary_part] #we use the funct. to separate real and img part, returning a list

# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values

#def get_real(number) -> int:
#     return number["real"]
#
#
#def get_imaginary(number) -> int:
#     return number["imaginary"]
#
#
# def to_str(number) -> str:
#     if str(get_imaginary(number)) != "0":
#         if str(get_imaginary(number))[0] != '-':
#             return str(get_real(number)) + "+" + str(get_imaginary(number)) + "i"
#         return str(get_real(number)) + str(get_imaginary(number)) + "i"
#     return str(get_real(number))
#
#
# def create_number(number):
#     real_part, imaginary_part = number_split(number)
#     return {"real": real_part, "imaginary": imaginary_part}


# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values

#Propriety 1 (Naive, 8)
#Length and elements of a longest subarray of numbers where both their real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111, 11-313i)
def find_longest_base10(numbers: list):
    n = len(numbers)
    max_length = start_index = stop_index = 0
    longest_base10 = []
    
    for i in range(n):
        for j in range(i + 2, n + 1):
            subsequence = numbers[i:j]

            # Check if the subsequence respects the propriety
            if has_same_base10_digits(subsequence) and len(subsequence) > max_length:
                max_length = len(subsequence)
                start_index = i
                stop_index = j

    longest_base10 = numbers[start_index:stop_index]

    return max_length, longest_base10

def has_same_base10_digits(subsequence):
    for num in subsequence:
        real_digits = set(str(get_real(num))) #convert the real digits into a string and make it a set
        imag_digits = set(str(get_imaginary(num))) #same goes for img digits
        
        if not real_digits.isdisjoint(imag_digits): #checking if there are common elements between them
            return True
    
    return False


#Propriety 2 (Dynamic, 9)
#The length and elements of a longest increasing subsequence, when considering each number's modulus
def modulus_sequence(numbers: list):
    real_parts = [int(get_real(x)) for x in numbers]
    imaginary_parts = [get_imaginary(x) for x in numbers] #Extracting the real and imaginary parts
    imaginary_parts2 = []
    for number in imaginary_parts:
        if number == '-':
            imaginary_parts2.append(1) #if img part is negative we make it positive
        else:
            imaginary_parts2.append(int(number)) 

    numbers_modulus = []
    for x, y in zip(real_parts, imaginary_parts2): #pairing corresponding the real and img parts    
        numbers_modulus.append(x**2 + y**2) #sqrt(x^2 + y^2)
    return numbers_modulus


def longest_increasing_sequence(numbers: list):
    n = len(numbers) #length size stored in n
    numbers_modulus = modulus_sequence(numbers) #calculate all the modules
    lis = [1] * n #initialize everything with n, iteratively update the length of lis being a starting point

    for i in range(1, n): #iterating from the 2nd element
        for j in range(0, i): #iterating over the preceding elements
            if numbers_modulus[i] > numbers_modulus[j] and lis[i] < lis[j] + 1:
                #we check if extending lis by including the cur elem (i) would result in a longer subseq.
                lis[i] = lis[j] + 1

    max_length = max(lis) #looking for the max length and its index
    max_index = lis.index(max_length)

    #Creating the subsequence
    lis_elements = [numbers[max_index]] # lis_elements = the number at max index
    current_length = max_length - 1
    for i in range(max_index - 1, -1, -1): #we start from the element before max_index -> first
        if lis[i] == current_length and get_real(numbers[i]) < get_real(lis_elements[-1]):
            lis_elements.insert(0, numbers[i])
            current_length -= 1 #element has been added

    return max_length, lis_elements

#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def input_numbers_ui():
    complex_list = []
    try:
        numbers = str(input("Add a list of complex numbers: ")).split()
    except ValueError as ve:
        print(ve)
        return
    for number in numbers:
        complex_list.append(create_number(number))
    return complex_list


def display_numbers_ui(complex_list: list):
    for number in complex_list:
        print(to_str(number), end=" ")
    print()


def base10_sequence_ui(numbers: list):
    length, subsequence = find_longest_base10(numbers)
    print(f"The length of the longest base10 subarray is {length} and the subarray is: {[to_str(x) for x in subsequence]}.")


def longest_increasing_sequence_ui(numbers: list):
    length, subsequence = longest_increasing_sequence(numbers)
    print(f"The length of the longest increasing subsequence is {length} and the subsequence is: {[to_str(x) for x in subsequence]}.")


def print_menu():
    print("Choose your option:")
    print("1. Input a list of complex numbers (z = a + bi).")
    print("2. Display the numbers.")
    print("3. Print the length and elements of a longest subarray of numbers where both their real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111, 11-313i)")
    print("4. Print the length and elements of a longest increasing subsequence, when considering each number's modulus.")
    print("0. Exit")


def main():
    numbers = []

    while True:
        print_menu()
        option = input("> ")
        if option == "1":
            try:
                numbers.clear()
                numbers = input_numbers_ui()
            except ValueError as ve:
                print(ve)

        elif option == "2":
            display_numbers_ui(numbers)

        elif option == "3":
            base10_sequence_ui(numbers)

        elif option == "4":
            longest_increasing_sequence_ui(numbers)

        elif option == "0":
            print("Bye!")
            return

if __name__ == "__main__":
    print("Make magic happen")
    main()



