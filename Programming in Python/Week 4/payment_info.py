class Payslip:  # Changed the class name to follow Python naming conventions
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = Payslip("Nathan", "no", 1000)  # Fixed the variable name here
roger = Payslip("Roger", "no", 3000)

print(nathan.status(), "\n", roger.status())

nathan.pay()
print("After payment")
print(nathan.status(), "\n", roger.status())
