class Category:
    def __init__(self, cat_name):

        self.cat_name = cat_name
        self.ledger = []

    def check_funds(self, amount):

        funds = [operation["amount"] for operation in self.ledger]

        if sum(funds) >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description=""):

        self.ledger.append({"amount": amount, "description": description})

        return None

    def withdraw(self, amount, description=""):

        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):

        funds = [operation["amount"] for operation in self.ledger]

        return sum(funds)

    def transfer(self, amount, destiny_category):

        if self.check_funds(amount) == True:

            self.withdraw(
                amount, description=f"Transfer to {destiny_category.cat_name}")
            destiny_category.deposit(
                amount, description=f"Transfer from {self.cat_name}")
            return True

        else:
            return False

    def __str__(self):

        title = self.cat_name.center(30, '*')
        operations = ""

        for operation in self.ledger:

            round_amount = "{:.2f}".format(operation["amount"])
            operations += ("{desc}{amount}\n".format(
                desc=operation['description'][0:23],
                amount=str(round_amount).rjust(
                    30 - len(operation['description'][0:23]))))

        total = "Total: {:.2f}".format(self.get_balance())

        return f"{title}\n{operations}{total}"


def create_spend_chart(categories):

    title = "Percentage spent by category"

    def calculate_percentages():
        expenses = {}
        for category in categories:

            expenses[category.cat_name] = sum([
                operation["amount"] for operation in category.ledger
                if (operation["amount"] < 0
                    and "Transfer" not in operation["description"])
            ])

        expenses_percentages = [
            int((expense / sum(expenses.values()) * 100) / 10) * 10
            for expense in expenses.values()
        ]

        return expenses_percentages

    def draw_markers(expenses_percentages=calculate_percentages()):

        expenses_markers = [""] * len(expenses_percentages)

        for i, percentage in enumerate(expenses_percentages):
            value_markers = ""
            for percentage_decile in range(0, percentage + 10, 10):

                value_markers += ("{marker}".format(marker="o"))

            expenses_markers[i] = value_markers

        filled_expenses_markers = [
            ((" " * (10 - len(expense_marker) + 1)) + expense_marker)
            for expense_marker in expenses_markers
        ]
        column_markers = ""
        i = 0
        while True:
            for j, marker in enumerate(filled_expenses_markers):

                if j == 0:
                    column_markers += f"{marker[i]}  "
                elif j != len(filled_expenses_markers) - 1:
                    column_markers += f"{marker[i]}  "
                else:
                    column_markers += f"{marker[i]}  \n"

            i += 1
            if i < 11:
                continue
            else:
                break

        return column_markers

    def draw_y_axis(column_markers=draw_markers()):

        y_values = sorted([y for y in range(0, 110, 10)], reverse=True)
        y_axis = ""

        i = 0
        j = 10
        while True:

            for y_value in y_values:
                y_axis += ("{value}| {markers}").format(
                    value=str(y_value).rjust(3), markers=column_markers[i:j])

                if y_value == 0:
                    break
                else:
                    i += 10
                    j += 10
                    continue
            break
        return y_axis

    def draw_x_axis():

        x_axis_line = "{dashes}".format(
            dashes=(("-" * 3 * len(categories)) +
                    "-").rjust((3 * len(categories) + 1) + 4))
        x_axis_labels = ""
        category_max_length = max(
            len(category.cat_name) for category in categories)
        filled_categories = [
            category.cat_name +
            (" " * (category_max_length - len(category.cat_name)))
            for category in categories
        ]  #we fill each category to the  max length category to avoid range problems while iterating

        i = 0
        while True:

            for category in filled_categories:
                if category == filled_categories[0]:
                    x_axis_labels += f"{category[i].rjust(6)}  "
                elif category != filled_categories[-1]:
                    x_axis_labels += f"{category[i]}  "
                elif i != category_max_length - 1:
                    x_axis_labels += f"{category[i]}  \n"
                else:
                    x_axis_labels += f"{category[i]}  "

            i += 1
            if i < category_max_length:
                continue
            else:
                break

        return x_axis_line, x_axis_labels

    return f"{title}\n{draw_y_axis()}{draw_x_axis()[0]}\n{draw_x_axis()[1]}"