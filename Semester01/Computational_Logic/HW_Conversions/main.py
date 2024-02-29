from algorithms.conversions import *
from ArithmeticOps.operations import *

to_baza16 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
from_base16 = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16
}


def run_number_conversion():
    number = input("Enter the number you want to convert:")
    source_base = input("Enter the source base in which the given number is written:")
    destination_base = input("Enter the base to which you want to convert the given number:")
    if int(source_base) < 2 or (int(source_base) > 10 and int(source_base) < 16):
        print("Invalid source base entered!")
        return
    if int(destination_base) < 2 or (int(destination_base) > 10 and int(destination_base) < 16):
        print("Invalid destination base entered!")
        return
    for i in range(0, len(number)):
        if from_base16[number[i]] >= int(source_base):
            print("The given number is incorrectly represented in the source base!")
            return
    if int(source_base) == 2 and int(destination_base) in [4, 8, 16]:
        print("Quick conversions will be used")
        if int(destination_base) == 4:
            print(fast_base2_base4_conversion(number))
        elif int(destination_base) == 8:
            print(fast_base2_base8_conversion(number))
        elif int(destination_base) == 16:
            print(fast_base2_base16_conversion(number))

    elif int(destination_base) == 2 and int(source_base) in [4, 8, 16]:
        print("Quick conversions will be used")
        if int(source_base) == 4:
            print(fast_base4_base2_conversion(number))
        elif int(source_base) == 8:
            print(fast_base8_base2_conversion(number))
        elif int(source_base) == 16:
            print(fast_base16_base2_conversion(number))

    elif int(source_base) < int(destination_base):
        print("It is recommended to use conversion by substitution or by an intermediate base")
        print("1 - conversion by substitution")
        print("2 - conversion by intermediate base")
        option = input(">>>")
        option = option.strip()
        if option == '1':
            print(substitution_conversion(number, int(source_base), int(destination_base)))
        elif option == '2':
            print(intermediate_base_conversion(number, int(source_base), int(destination_base)))
        else:
            print("Invalid command!")
    elif int(source_base) > int(destination_base):
        print("It is recommended to use conversion by successive divisions or by an intermediate base")
        print("1 - conversion by successive divisions")
        print("2 - conversion by intermediate base")
        option = input(">>>")
        option = option.strip()
        if option == '1':
            print(successive_division_conversion(number, int(source_base), int(destination_base)))
        elif option == '2':
            print(intermediate_base_conversion(number, int(source_base), int(destination_base)))
        else:
            print("Invalid command!")
    else:
        print("The given conversion cannot be performed!")


def run_intermediate_base_conversion():
    number = input("Enter the number you want to convert:")
    source_base = input("Enter the source base in which the given number is written:")
    destination_base = input("Enter the base to which you want to convert the given number:")
    if int(source_base) < 2 or (int(source_base) > 10 and int(source_base) < 16):
        print("Invalid source base entered!")
        return
    if int(destination_base) < 2 or (int(destination_base) > 10 and int(destination_base) < 16):
        print("Invalid destination base entered!")
        return
    for i in range(0, len(number)):
        if from_base16[number[i]] >= int(source_base):
            print("The given number is incorrectly represented in the source base!")
            return
    print("The number converted to the destination base is equal to:")
    print(intermediate_base_conversion(number, int(source_base), int(destination_base)))



def run_substitution_conversion():
    number = input("Enter the number you want to convert:")
    source_base = input("Enter the source base in which the given number is written:")
    destination_base = input("Enter the base to which you want to convert the given number:")
    if int(source_base) < 2 or (int(source_base) > 10 and int(source_base) < 16):
        print("Invalid source base entered!")
        return
    if int(destination_base) < 2 or (int(destination_base) > 10 and int(destination_base) < 16):
        print("Invalid destination base entered!")
        return
    for i in range(0, len(number)):
        if from_base16[number[i]] >= int(source_base):
            print("The given number is incorrectly represented in the source base!")
            return
    print("The number converted to the destination base is equal to:")
    print(substitution_conversion(number, int(source_base), int(destination_base)))



def run_successive_division_conversion():
    number = input("Enter the number you want to convert:")
    source_base = input("Enter the source base in which the given number is written:")
    destination_base = input("Enter the base to which you want to convert the given number:")
    if int(source_base) < 2 or (int(source_base) > 10 and int(source_base) < 16):
        print("Invalid source base entered!")
        return
    if int(destination_base) < 2 or (int(destination_base) > 10 and int(destination_base) < 16):
        print("Invalid destination base entered!")
        return
    for i in range(0, len(number)):
        if from_base16[number[i]] >= int(source_base):
            print("The given number is incorrectly represented in the source base!")
            return
    print("The number converted to the destination base is equal to:")
    print(successive_division_conversion(number, int(source_base), int(destination_base)))



def run_addition():
    base = input("Enter the base in which the given numbers are represented and where the addition will take place:")
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    for i in range(0, len(num1)):
        if from_base16[num1[i]] >= int(base):
            print("The given number is incorrectly represented in the source base!")
            return
    for i in range(0, len(num2)):
        if from_base16[num2[i]] >= int(base):
            print("The given number is incorrectly represented in the source base!")
            return
    print("The result of adding the two numbers in the given base is:")
    print(add_two_numbers(num1, num2, int(base)))


def run_subtraction():
    base = input("Enter the base in which the given numbers are represented and where the subtraction will take place:")
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    for i in range(0, len(num1)):
        if from_base16[num1[i]] >= int(base):
            print("The given number is incorrectly represented in the source base!")
            return
    for i in range(0, len(num2)):
        if from_base16[num2[i]] >= int(base):
            print("The given number is incorrectly represented in the source base!")
            return

    if int(num1) < int(num2):
        print("The first number is smaller than the second, subtraction cannot be performed!")
        return

    print("The result of subtracting the second number from the first in the given base is:")
    print(subtract_two_numbers(num1, num2, int(base)))



def run_multiplication():
    base = input("Enter the base in which the number and the given digit for multiplication will be represented:")
    num = input("Enter the number:")
    digit = input("Enter the digit:")
    for i in range(0, len(num)):
        if from_base16[num[i]] >= int(base):
            print("The given number is incorrectly represented in the source base!")
            return
    if from_base16[digit] >= int(base):
        print("The digit does not exist in the given base!")
        return
    print("The result of multiplying the number by the given digit is:")
    print(multiply_by_digit(num, digit, int(base)))



def run_division():
    base = input("Enter the base in which the number and the given digit for division will be represented:")
    num = input("Enter the number:")
    digit = input("Enter the digit:")
    for i in range(0, len(num)):
        if from_base16[num[i]] >= int(base):
            print("The given number is incorrectly represented in the source base!")
            return
    if from_base16[digit] >= int(base):
        print("The digit does not exist in the given base!")
        return
    print("The result of dividing the number by the given digit is:")
    quotient, remainder = divide_by_digit(num, digit, int(base))
    print(quotient, "remainder", remainder)



def help():
    print("Welcome to the number conversion application!")
    print("This app supports multiple methods for converting numbers into different bases (2-10 or 16):")
    print("- Successive divisions, substitution, and utilizing an intermediate base (implicitly base 10)")
    print("- Rapid conversions between base 2 and bases 4, 8, 16, and vice versa")
    print("Moreover, it enables fundamental arithmetic operations like addition, subtraction, and multiplication/division by a digit in any specified base.")
    print("Here are the available commands:")
    print("[convert_number] - Enter a number, source base, and destination base for conversion. It will suggest suitable methods based on your input.")
    print("[base_intermediate_conversion] - Execute the algorithm to convert a number using an intermediate base.")
    print("[substitution_conversion] - Execute the algorithm to convert a number using the substitution method (recommended for converting from a smaller base to a larger one).")
    print("[successive_division_conversion] - Execute the algorithm to convert a number using successive divisions (recommended for converting from a larger base to a smaller one).")
    print("[addition] - Add 2 numbers entered by the user, both written in any mentioned base.")
    print("[subtraction] - Subtract 2 numbers entered by the user, both written in any mentioned base.")
    print("[multiplication] - Multiply a given number in any mentioned base by a given digit.")
    print("[division] - Divide a given number in any mentioned base by a given digit and display the quotient and remainder.")
    print("[exit] - Exit the application")
    print("App made by Robert George Leustean - Group 914")




commands = {
    "convert_number":run_number_conversion,
    "intermediate_base_conversion": run_intermediate_base_conversion,
    "substitution_conversion": run_substitution_conversion,
    "successive_division_conversion": run_successive_division_conversion,
    "addition": run_addition,
    "subtraction": run_subtraction,
    "multiplication": run_multiplication,
    "division": run_division
}



def run():
    help()
    while True:
        command = input(">>>")
        command = command.strip()
        if command == "":
            continue
        elif command == "exit":
            return
        elif command in commands:
            try:
                commands[command]()
            except ValueError as ve:
                print(str(ve))
        else:
            print("Invalid command!")



run()

# Author: Leustean Robert George - group 914