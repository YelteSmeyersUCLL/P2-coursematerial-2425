class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        else:
            return Money(
                self.amount + other.amount, self.currency
            )
    
    def __sub__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        else:
            return Money(
                self.amount - other.amount, self.currency
            )
    
    def __mul__(self, times):
        return Money(
            self.amount * times, self.currency
        )
    
    def __repr__(self):
        return f"Money{self.amount, self.currency}"
    


first = Money(10, "EUR")
second = Money(20, "EUR")

print(first * 50)
