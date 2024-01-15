class AccountChecker:
    def __init__(self, account):
        self.account = account

    def is_valid(self):
        return self.account == 'nhan'


class SecurityCodeChecker:
    def __init__(self, security_code):
        self.security_code = security_code

    def is_valid(self):
        return self.security_code == '123456'


class BalanceManager:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('Balance:', self.balance)

    def have_enough_money(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        self.balance -= amount
        print('Balance:', self.balance)


class BankAccount:
    def __init__(self, account, security_code):
        self.account = account
        self.security_code = security_code
        self.account_checker = AccountChecker(account)
        self.security_code_checker = SecurityCodeChecker(security_code)
        self.balance_manager = BalanceManager(balance=0)

    def deposit(self, amount):
        if (
            self.account_checker.is_valid()
            and self.security_code_checker.is_valid()
        ):
            self.balance_manager.deposit(amount)
            print('Done')
        else:
            print('Error!')

    def withdraw(self, amount):
        if (
            self.account_checker.is_valid()
            and self.security_code_checker.is_valid()
            and self.balance_manager.have_enough_money(amount)
        ):
            self.balance_manager.withdraw(amount)
            print('Done')
        else:
            print('Error!')


def main():
    bank_account = BankAccount('nhan', '123456')
    bank_account.deposit(10)
    bank_account.withdraw(5)


if __name__ == '__main__':
    main()
