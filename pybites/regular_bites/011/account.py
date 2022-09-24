class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self) -> int:
        """Return the number of transactions"""
        return len(self._transactions)

    def __eq__(self, other: object) -> bool:
        """Return True if the balance of the accounts are equal"""
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance == other.balance

    def __lt__(self, other: object) -> bool:
        """Return True if the balance of this account is less than the other"""
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance < other.balance

    def __le__(self, other: object) -> bool:
        """Return True if the balance of this account is less than or equal to the other"""
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance <= other.balance

    def __ge__(self, other: object) -> bool:
        """Return True if the balance of this account is greater than or equal to the other"""
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance >= other.balance

    def __gt__(self, other: object) -> bool:
        """Return True if the balance of this account is greater than the other"""
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance > other.balance

    def __getitem__(self, position: int) -> int:
        """Return the transaction at the given position"""
        return self._transactions[position]

    def __add__(self, amount: int) -> None:
        """Add the amount to the account"""
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        self._transactions.append(amount)

    def __sub__(self, amount: int) -> None:
        """Subtract the amount from the account"""
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        self._transactions.append(-amount)

    def __str__(self) -> str:
        """Return a string representation of the account"""
        return f"{self.name} account - balance: {self.balance}"
