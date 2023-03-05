from utils.display import clear_screen

class AccountsScreen:
    def __init__(self, accounts):
        self.accounts = accounts

    def display(self):
        clear_screen()
        print("Accounts:")
        for account in self.accounts:
            print(f"- {account['name']}: {account['balance']} {account['currency']}")
