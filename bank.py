class Bank:
    def __init__(self):
        self.database = {}

    def create_account(self, name, details):
        self.database[name] = details


class Account:
    def __init__(self, name, password, email, bank):
        self.name = name
        self.password = password
        self.email = email
        self.details = [self.name, self.password, self.email, 0, []]  # [name, password, email, balance, transactions]
        bank.create_account(self.name, self.details)
        print("✅ Successfully created account for", self.name)
