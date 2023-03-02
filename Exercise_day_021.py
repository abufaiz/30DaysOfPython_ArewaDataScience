# 30DaysOfPython Exercises 

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def total_income(self):
        return sum(income[0] for income in self.incomes)

    def total_expense(self):
        return sum(expense[0] for expense in self.expenses)

    def account_info(self):
        print(f"Account holder: {self.firstname} {self.lastname}")
        print(f"Total income: {self.total_income()}")
        print(f"Total expenses: {self.total_expense()}")
        print(f"Account balance: {self.account_balance()}")

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()
    
account = PersonAccount("John", "Doe")
account.add_income(1000, "Salary")
account.add_income(500, "Bonus")
account.add_expense(300, "Rent")
account.add_expense(200, "Food")
account.account_info()
