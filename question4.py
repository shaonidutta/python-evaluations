class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance = 0
        self.owner = owner

    def withdraw(self, amount):
        try:
            if amount> self.balance:
                raise ValueError(f"Cannot withdraw, insufficient balance")
            self.balance -= amount
        except ValueError as e:
            raise InsufficientFundsError("Withdrawal failed!") from e
        
if __name__ == "__main__":
    account= BankAccount("Shaoni", 1000)
    try: 
        account.withdraw(2000)
    except InsufficientFundsError as e:
        print(f"custorm error: {e}")