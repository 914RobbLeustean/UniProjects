# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
import datetime
from copy import deepcopy

def push_trans_history_stk(trans_history_stk: list, transactions: list) -> list:
    """
    Pushes the current transactions list to the transaction history stack.
    :param transaction_history_stack: The transaction history stack.
    :param transactions: The list of transactions.
    :return: The transaction history stack with the current transactions list pushed.
    """
    trans_history_stk.append(transactions[:])

    return trans_history_stk

def add_transaction(transactions: list, trans_amount: int, trans_type: str, trans_desc: str, trans_history_stk: list) -> list:
    """
    Adds a transaction to the list of transactions
    
    :param transactions: The list of transactions.
    :param amount: Positive integer, the amount of the transaction.
    :param type: String, the type of the transaction.
    :param description: String, the description of the transaction.
    :param transaction_history_stack: List, the transaction history stack.
    :return: The list of transactions with the new transaction added.
    """
    if trans_amount <= 0:
        raise ValueError("Invalid amount. Must be positive")
    if trans_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. It must be either 'in' or 'out.")
    if trans_desc == "":
        raise ValueError("Invalid description.- Cannot be empty.")
    
    transaction = {
        "day": datetime.datetime.now().day % 30,
        "amount": trans_amount,
        "type": trans_type,
        "description": trans_desc,
    }

    push_trans_history_stk(trans_history_stk, transactions)
    
    transactions.append(transaction)
    
    return transactions
                        
                        
def insert_transaction(transactions: list, trans_day: int, trans_amount: int, trans_type: str, trans_desc: str, trans_history_stk: list) -> list:
    """
    Inserts a transaction for a specified date.
    
    :param transactions: The list of transactions.
    :param day: Positive integer, the day of the transaction.
    :param amount: Positive integer, the amount of the transaction.
    :param type: String, the type of the transaction.
    :param description: String, the description of the transaction.
    :param transaction_history_stack: List, the transaction history stack.
    :return: The list of transactions with the new transaction added.
    """
    
    if trans_day < 1 or trans_day > 31:
        raise ValueError("Invalid day. Must be between 1 and 31.")
    if trans_amount <= 0:
        raise ValueError("Invalid amount. Must be positive")
    if trans_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. It must be either 'in' or 'out.")
    if trans_desc == "":
        raise ValueError("Invalid description. Cannot be empty.")
    
    transaction = {
        "day": trans_day,
        "amount": trans_amount,
        "type": trans_type,
        "description": trans_desc,
    }

    push_trans_history_stk(trans_history_stk, transactions)
    
    transactions.append(transaction)
    
    return transactions

def remove_transaction_by_day(transactions: list, trans_day: int, trans_history_stk:list) -> list:
    """
    Removes all transactions for a given day.
    
    :param transactions: The list of transactions.
    :param day: The day of the transaction.
    :param trans_history_stk: The transaction history stack.
    :return: The list of transactions with the transactions for the given day removed.
    """
    
    if trans_day < 1 or trans_day > 31:
        raise ValueError("Invalid day.Please chose between 1-31.")
    
    push_trans_history_stk(trans_history_stk, transactions)
    
    #Remove all transactions from day X.
    transactions[:] = [trans for trans in transactions if trans["day"] != trans_day]
    
    return transactions

def remove_transaction_in_between_days(transactions:list, trans_start_day: int, trans_end_day: int, trans_history_stk: list) -> list:
    """
    Removes all transactions between a period of days 
    
    :param transactions: The list of transactions.
    :param start_day: The start day of the transaction.
    :param end_day: The end day of the transaction.
    :param trans_history_stk: The transaction history stack.
    :return: The list of transactions with the transactions for the given day removed.
    """
    
    if trans_start_day > trans_end_day:
        raise ValueError("Invalid days. Start day must be less than end day.")
    if trans_start_day < 1 or trans_start_day > 31:
        raise ValueError("Invalid day. Must be between 1 and 31.")
    if trans_end_day < 1 or trans_end_day > 31:
        raise ValueError("Invalid day. Must be between 1 and 31.")
    
    push_trans_history_stk(trans_history_stk, transactions)
    
    #Remove all transactions from X-Y days.
    transactions[:] = [trans for trans in transactions if int(trans["day"]) < int(trans_start_day) or int(trans["day"]) > int(trans_end_day)]

    return transactions

def remove_transactions_by_type(transactions: list, trans_type: str, trans_history_stk: list) -> list:
    """
    Removes all transactions of a given type.
    
    :param transactions: The list of transactions.
    :param trans_type: The type of the transaction.
    :param trans_history_stk: The transaction history stack.
    :return: The list of transactions with the transactions of the given type removed.
    """     
    
    if trans_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. Must be either 'in' or 'out'.")
    
    push_trans_history_stk(trans_history_stk, transactions)
    
    #Remove all transactions of the given type
    transactions[:] = [trans for trans in transactions if trans["type"] != trans_type]

    return transactions

def replace_transaction_by_amount(transactions:list, transaction_day: int, transaction_type: str, transaction_description: str, 
                                  amount: int, trans_history_stk: list) -> list:
    """
    Replace the amount for the <type> transaction having the <desc> description from <day> with <amount>   
    
    :param transactions: The list of transactions.
    :param trans_type: The type of the transaction.
    :param trans_history_stk: The transaction history stack.
    :param amount: positive integer, the sum of the transaction.
    :return: The list of transactions with the transactions of the given type removed.
    """
    if transaction_day < 1 or transaction_day > 31:
        raise ValueError("Invalid day. Must be between 1 and 31.")
    if amount <= 0:
        raise ValueError("Invalid amount. Must be positive")
    if transaction_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. It must be either 'in' or 'out.")
    if transaction_description == "":
        raise ValueError("Invalid description. Cannot be empty.")
    
    transaction = {"day": transaction_day, "amount": amount, "type":transaction_type, "description": transaction_description,}
    
    push_trans_history_stk(trans_history_stk, transactions)
    
    #Replace the transaction by given X amount.
    for transaction in transactions:
        if (
            transaction["day"] == transaction_day
            and transaction["type"] == transaction_type
            and transaction["description"] == transaction_description
        ):
            transaction["amount"] = amount
            break
    else:
        raise ValueError("Transaction not found.")

    return transactions
    
def list_all_transactions(transactions: list) -> list:
    """
    Lists all transactions.

    :param transactions: The list of transactions.
    :return: The list of transactions.
    """
    return transactions

def list_all_transactions_by_type(transactions: list, transaction_type: str) -> list:
    """
    Lists all transactions of a given type.

    :param transactions: The list of transactions.
    :param transaction_type: The type of the transaction.
    :return: The list of transactions of the given type.
    """
    if transaction_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. Must be either 'in' or 'out'.")

    return [transaction for transaction in transactions if transaction["type"] == transaction_type]

def list_all_transactions_by_amount(transactions: list, transaction_amount: int, transaction_operator: str) -> list:
    """
    Lists all transactions of a given amount.

    :param transactions: The list of transactions.
    :param amount: The amount of the transaction.
    :return: The list of transactions of the given amount.
    """
    if transaction_amount <= 0:
        raise ValueError("Invalid amount. Must be positive.")

    if transaction_operator not in ["<", "=", ">"]:
        raise ValueError("Invalid operator. Must be either '<', '=' or '>'.")

    if transaction_operator == "<":
        return [transaction for transaction in transactions if int(transaction["amount"]) < int(transaction_amount)]
    elif transaction_operator == "=":
        return [transaction for transaction in transactions if int(transaction["amount"]) == int(transaction_amount)]
    elif transaction_operator == ">":
        return [transaction for transaction in transactions if int(transaction["amount"]) > int(transaction_amount)]

    return []

def list_account_balance_by_day(transactions: list, transaction_day: int) -> int:
    """
    Lists the account balance for a given day.

    :param transactions: The list of transactions.
    :param day: The day of the transaction.
    :return: The account balance for the given day.
    """
    if int(transaction_day) < 1 or int(transaction_day) > 31:
        raise ValueError("Invalid day. Must be between 1 and 31.")

    return sum(int(transaction["amount"]) if transaction["type"] == "in" else -int(transaction["amount"]) for transaction in transactions 
               if int(transaction["day"]) <= int(transaction_day))

def filter_transactions_by_type(transactions: list, transaction_type: str, trans_history_stk: list) -> list:
    """
    Filters transactions by type.

    :param transactions: The list of transactions.
    :param transaction_type: String, the type of the transaction.
    :param transaction_history_stack: The transaction history stack.
    :return: The list of transactions of the given type.
    """
    if transaction_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. Must be either 'in' or 'out'.")

    push_trans_history_stk(trans_history_stk, transactions)

    for transaction_index in range(len(transactions) - 1, -1, -1):
        if transactions[transaction_index]["type"] != transaction_type:
            transactions.pop(transaction_index)

    return transactions

def filter_transactions_by_smaller_amount(transactions: list,transaction_type: str,transaction_amount: int, trans_history_stk: list) -> list:
    """
    Filters transactions by amount.

    :param transactions: The list of transactions.
    :param transaction_type: The type of the transaction.
    :param amount: The amount of the transaction.
    :param transaction_history_stack: The transaction history stack.
    :return: The list of transactions of the given amount.
    """
    if transaction_type not in ["in", "out"]:
        raise ValueError("Invalid transaction type. Must be either 'in' or 'out'.")

    if transaction_amount <= 0:
        raise ValueError("Invalid amount. Must be positive.")

    push_trans_history_stk(trans_history_stk, transactions)

    transactions[:] = [transaction for transaction in transactions if transaction["type"] == transaction_type and transaction["amount"] < transaction_amount]

    return transactions

def undo_last_transaction(transactions: list, trans_history_stk: list) -> list:
    """
    Undo the last operation / transaction.
    
    :param transactions: The list of transactions.
    :param trans_history_stk: The transaction history stack.
    :return: The list of transactions with the  last transactions erased.
    """
    
    if len(trans_history_stk) == 0:
        raise ValueError("No more transactions left to be undone.")
    
    last_state = trans_history_stk.pop()
    transactions.clear()
    transactions.extend(last_state)
    
    return transactions