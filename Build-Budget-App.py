class Category:
    
    def __init__(self,name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
        

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += transaction['amount']
        
        return balance
    
    def transfer(self, amount, category):
        if self.withdraw(amount, description=f'Transfer to {category.name}'):
    
            category.deposit(amount, description=f'Transfer from {self.name}')
            return True
        
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        lines = []
        lines.append(self.name.center(30,'*'))

        for transaction in self.ledger:
            output = f"{transaction['description'][:23]:<23}{transaction['amount']:>7.2f}"

            lines.append(output)
        
        lines.append(f'Total: {self.get_balance()}')

        return '\n'.join(lines)


def create_spend_chart(categories):
    
    title = 'Percentage spent by category'
    spent_per_category = []
    total_spent = 0
    
    for category in categories:
        category_spent = 0
        for item in category.ledger:

            if item['amount'] < 0:
                category_spent += abs(item['amount']) # Use abs() to make the number positive
                
        spent_per_category.append(category_spent)
        total_spent += category_spent
    
    percentages = []
    for spent in spent_per_category:
        if total_spent > 0:
            percent = (spent / total_spent) * 100
            rounded_percent = (percent // 10) * 10
            percentages.append(rounded_percent)
        else:
            percentages.append(0)

    chart_lines = ["Percentage spent by category"]
    
    for value in range(100, -1, -10):
        row = f"{value:>3}|"

        for pct in percentages:
            if pct >= value:
                row += " o "
            else:
                row += "   "

        row += " "
        chart_lines.append(row)

    dash_length = 4 + (3 * len(categories)) + 1
    chart_lines.append(" " * 4 + "-" * (dash_length - 4))

    category_names = [cat.name for cat in categories]
    max_name_length = max(len(name) for name in category_names)
    
    for i in range(max_name_length):
        row = " " * 4 
        for name in category_names:
            if i < len(name):
                row += f" {name[i]} "
            else:
                row += "   " 
        row += " " 
        chart_lines.append(row)

    return "\n".join(chart_lines)
    