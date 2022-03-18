class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        head = self.category.center(30, '*') + "\n"
        items = ""
        for item in self.ledger:
            spaces = 7 if len(item["description"]) > 23 else 30 - len(item["description"])
            items += item["description"][:23] + "{amount:.2f}".format(amount=item["amount"]).rjust(spaces) + "\n"
        return head + items + "Total: " + str(self.get_balance())

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, transfer_category):
        if not self.check_funds(amount):
            return False
        else:
            destination_desc = "Transfer to {des_cat}".format(des_cat=transfer_category.category)
            source_desc = "Transfer from {src_cat}".format(src_cat=self.category)
            self.withdraw(amount, destination_desc)
            transfer_category.deposit(amount, source_desc)
            return True

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False


def create_spend_chart(categories):
    no_of_categories = len(categories)
    if no_of_categories == 0:
        return "No categories found"
    title = "Percentage spent by category\n"
    barchart = ''
    total_spent = 0.00
    spent_by_cat = list()

    for cat in categories:
        spent = 0.00
        for wit in cat.ledger:
            if wit['amount'] < 0:
                spent += wit['amount']
        total_spent += abs(spent)
        spent_by_cat.append([cat.category, abs(spent)])

    for val in spent_by_cat:
        percent = val[1] / total_spent * 100
        val[1] = percent

    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for val in spent_by_cat:
            if i < val[1]:
                line += " o "
            else:
                line += "   "
        barchart += line + " \n"

    horizontal_line = "    " + "-"*(3*len(categories) + 1) + "\n"

    vertical_names = ""
    lengths = [len(cat.category) for cat in categories]
    for j in range(max(lengths)):
        vline = ''
        for cat in categories:
            try:
                vline += " " + cat.category[j] + " "
            except:
                vline += "   "

        vertical_names += "    " + vline + " \n" if j != max(lengths)-1 else "    " + vline + " "

    return title + barchart + horizontal_line + vertical_names

