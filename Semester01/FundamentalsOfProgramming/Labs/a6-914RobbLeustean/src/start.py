# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
# Start.py
import testprogram as tests
import ui

if __name__ == "__main__":
    tests.test_all_functions()
    trans_list = [
 {"day": "2", "amount": "200", "type": "out", "description": "Groceries"},
 {"day": "7", "amount": "700", "type": "in", "description": "Salary"},
 {"day": "10", "amount": "500", "type": "out", "description": "Clothes"},
 {"day": "11", "amount": "50", "type": "out", "description": "Uber"},
 {"day": "13", "amount": "150", "type": "in", "description": "Freelance Work"},
 {"day": "14", "amount": "700", "type": "in", "description": "Salary"}, 
 {"day": "19", "amount": "60", "type": "out", "description": "Cinema"},
 {"day": "21", "amount": "80", "type": "out", "description": "Takeout"},
 {"day": "25", "amount": "120", "type": "out", "description": "Dog Food"},
 {"day": "28", "amount": "700", "type": "in", "description": "Salary"},
]
    trans_history_stk = []
    ui.perform_bank_op_from_input(trans_list, trans_history_stk)