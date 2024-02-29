# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#UI.py
import re
import functions
import random
import termtables as tt

def show_menu():
    print("Welcome to the Bank Account System!")
    print("Available commands:")
    print("- add <value> <type> <description>")
    print("- insert <day> <value> <type> <description>")
    print("- remove <day>")
    print("- remove <start day> to <end day>")
    print("- remove <type>")
    print("- replace <day> <type> <description> with <value>")
    print("- list")
    print("- list <type>")
    print("- list [ < | = | > ] <value>")
    print("- list balance <day>")
    print("- filter <type>")
    print("- filter <type> <value>")
    print("- Undo the last transaction")
    

def perform_bank_op_from_input(trans_list: list, trans_history_stk: list) -> int:
    """
     This function performs the bank operations based on the given command.
     
    :param trans_history_stk: The list of transaction history stack.
    :param transactions_list: The list of transactions.
    :return: The operation the user asked for.
    """
    show_menu()
    while True:
        user_input = input("Enter a command: ").strip().split()

        if not user_input:
            print("Please enter a valid command!")
            continue

        command = user_input[0]
        
        # (A) Function/s
        if command == 'add':
            if len(user_input) >= 4:
                try:
                    amount = int(user_input[1])
                    trans_type = user_input[2]
                    desc = ' '.join(user_input[3:])
                    functions.add_transaction(trans_list, amount ,trans_type, desc, trans_history_stk)
                    print(f"Added transaction: 'amount': {amount}, 'type': {trans_type}, 'desc': {desc}")
                except ValueError:
                    print("Invalid command parameters. Please provide valid parameters.")  
            else:
                print("Insufficient parameters for 'add' command.")
                
        elif command == 'insert':
            if len(user_input) >= 5:
                try:
                    day = int(user_input[1])
                    amount = int(user_input[2])
                    trans_type = user_input[3]
                    desc = ' '.join(user_input[4:])
                    functions.insert_transaction(trans_list,day, amount ,trans_type, desc, trans_history_stk)
                    print(f"Added transaction: 'day': {day}, 'amount': {amount}, 'type': {trans_type}, 'desc': {desc}")
                except (ValueError, IndexError):
                    print("Invalid command parameters. Please provide valid parameters.")
            else:
                print("Insufficient parameters for 'insert' command.")
        
        #(B) Function/s
        elif command == 'remove':
            try:
                if len(user_input) == 1:
                    raise ValueError("Insufficient parameters for 'remove' command.")
                if len(user_input) == 2:
                    if isinstance(user_input[1], int) and 1 <= int(user_input[1]) <= 31:
                        day = int(user_input[1])
                        functions.remove_transaction_by_day(trans_list, day, trans_history_stk)
                        print(f"Removed all transactions for day {day}")
                    elif isinstance(user_input[1], str) and (user_input[1] == 'out' or user_input[1] == 'in'):
                        type = user_input[1]
                        functions.remove_transactions_by_type(trans_list, trans_type, trans_history_stk)
                        print(f"Removed all transactions by type {type}")
                    else:
                        raise ValueError("Invalid Inputs.")
                if len(user_input) == 4:
                    start_day = int(user_input[1])
                    end_day = int(user_input[3])
                    functions.remove_transaction_in_between_days(trans_list, start_day, end_day, trans_history_stk)
                    print(f"Removed all transactions from day {start_day} to {end_day}")
            except ValueError as e:
                print(e)
        elif command == 'replace':
            try:
                if len(user_input) < 6:
                    raise ValueError("Insufficient parameters for the 'replace' command.")
                if len(user_input) >= 6:
                    day = int(user_input[1])
                    type = user_input[2]
                    new_amount = int(user_input[-1])
                    desc = ' '.join(user_input[3:-2])  
                    functions.replace_transaction_by_amount(trans_list, day, type, desc, new_amount, trans_history_stk)
                    print(f"Replaced transaction: 'day': {day}, 'type': {type}, 'desc': '{desc}' with {new_amount} RON ")
            except ValueError as e:
                print(e)
         
        #(C) Functions/s
        elif command == 'list':
            if len(user_input) == 1:
                if trans_list:
                            header_of_table = ["Day", "Amount", "Type", "Description"]
                            data_to_display = [[t["day"], t["amount"], t["type"], t["description"]]
                                for t in functions.list_all_transactions(trans_list)]

                            tt.print(data_to_display,header=header_of_table,padding=(0, 1, 0, 1),)
                else:
                    print("There are no transactions to display.")
            elif len(user_input) == 2:
                try:
                    type = user_input[1]
                    if trans_list:
                        if(type == 'in' or type == 'out'):
                                header_of_table = ["Day", "Amount", "Type", "Description"]
                                data_to_display = [[t["day"], t["amount"], t["type"], t["description"]]
                                    for t in functions.list_all_transactions_by_type(trans_list, type)]

                                tt.print(data_to_display,header=header_of_table,padding=(0, 1, 0, 1),)       
                        else:
                            raise ValueError("Invalid Input.")
                    else:
                        print("There are no transactions to display.")
                except ValueError as e:
                    print(e)
            elif len(user_input) == 3:
                try:
                    operation = user_input[1]
                    if trans_list:
                        if(operation == '<' or operation == '>' or operation == '='):
                            amount = int(user_input[2])
                            header_of_table = ["Day", "Amount", "Type", "Description"]
                            data_to_display = [[t["day"], t["amount"], t["type"], t["description"]]
                                    for t in functions.list_all_transactions_by_amount(trans_list, amount, operation)]

                            tt.print(data_to_display,header=header_of_table,padding=(0, 1, 0, 1),)
                                
                        elif(operation == 'balance'):
                            day = int(user_input[2])
                            print(f"The sum of the amounts until day {day} is {functions.list_account_balance_by_day(trans_list, day)}")
                        else:
                            raise ValueError("Invalid Input.")
                    else:
                        print("There are no transactions to display.")             
                except ValueError as e:
                    print(e)
        
        #(D) Function/s
        elif command == 'filter':
            try:
                if len(user_input) < 2 or len(user_input) > 3:
                    raise ValueError("Insufficient parameters for 'filter' command.")
                elif len(user_input) == 2:
                    type = user_input[1]
                    trans_list = functions.filter_transactions_by_type(trans_list, type, trans_history_stk)
                elif len(user_input) == 3:
                    type = user_input[1]
                    amount = int(user_input[2])
                    trans_list = functions.filter_transactions_by_smaller_amount(trans_list,type,amount,trans_history_stk,)
                else:
                    raise ValueError("Invalid parameters for 'filter' command.") 
            except ValueError as e:
                print(e)
                           
        #(E) Function/s
        elif command == 'undo':
            try:
                trans_list = functions.undo_last_transaction(trans_list, trans_history_stk)
                print("Last transaction was undone.")
            except ValueError as error:
                print(str(error))
        
        else:
            print("Invalid command. Choose again.")
    

