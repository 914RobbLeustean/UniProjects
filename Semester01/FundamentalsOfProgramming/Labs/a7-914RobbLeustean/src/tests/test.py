from repository.memory_repository import RepositoryException
from services.expense_service import ExpenseService

class Test:
   def __init__(self, repository) -> None:
      self.expense_service = ExpenseService(repository)
      
   def test_add_expenses(self):
      expense_data = self.expense_service.get_all_expenses()
      initial_expense_count = len(expense_data)
      
      self.expense_service.add_expense(1, 100, "food")
      assert len(self.expense_service.get_all_expenses() == initial_expense_count + 1)
      
      self.expense_service.add_expense(2, 200, "utilities")
      assert len(self.expense_service.get_all_expenses() == initial_expense_count + 2)
      
      self.expense_service.add_expense(3, 300, "gym membership")
      assert len(self.expense_service.get_all_expenses() == initial_expense_count + 3)
      
      
      try:
         self.expense_service.add_expense(3, 300, "gym membership")
      except RepositoryException:
         pass
      assert len(self.expense_service.get_all_expenses() == initial_expense_count + 3)
      
   def run_test(self):
      self.test_add_expenses()
      