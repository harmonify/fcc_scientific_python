# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
# https://replit.com/@harmonify/budget-app#budget.py

from __future__ import annotations
from itertools import zip_longest
from math import floor


class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger: list[dict] = []

    def __repr__(self) -> str:
        # title
        result = f"{self.name:^30}\n".replace(" ", "*")

        # ledger
        for n in self.ledger:
            result += f"{n.get('description')[:23]:23}{n.get('amount'):>7.2f}\n"

        # total
        result += f"Total: {self.get_balance()}"

        return result

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self) -> float:
        return sum(n.get('amount') for n in self.ledger)

    def transfer(self, amount: float, category: Category) -> bool:
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        if amount > self.get_balance():
            return False
        return True

    def get_spend_total(self) -> float:
        return -sum(n.get('amount') for n in self.ledger if n.get('amount') < 0)


def create_spend_chart(categories: list[Category]) -> str:
    spends = [category.get_spend_total() for category in categories]
    spend_total = sum(spends)
    spend_percentages = [floor(s/spend_total*100) for s in spends]

    # title
    result = "Percentage spent by category\n"

    # y-axis + chart
    for i in range(100, -10, -10):
        row = f"{i:>3}| "
        for percentage in spend_percentages:
            row += "o  " if percentage >= i else "   "
        row += "\n"
        result += row

    # x-axis dashes
    result += f"    -{'-' * 3 * len(categories)}\n"

    # categories name
    for category in zip_longest(*[category.name for category in categories], fillvalue=""):
        row = "     "
        row += "".join(f"{c:3}" for c in category)
        row += "\n"
        result += row

    return result.rstrip("\n")


def main(args=None):
    # setup
    food = Category("Food")
    clothing = Category("Clothing")
    business = Category("Business")

    # food
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food")
    food.withdraw(105.55)
    food.transfer(50, clothing)

    # clothing
    clothing.deposit(900, "deposit")
    clothing.withdraw(33.40)
    clothing.transfer(100, business)

    # business
    business.deposit(900, "deposit")
    business.withdraw(10.99)
    business.deposit(100, "investment")

    print(food)
    print(clothing)
    print(business)

    print(create_spend_chart([food, clothing, business]))


if __name__ == '__main__':
    main()
