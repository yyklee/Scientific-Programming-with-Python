def create_spend_chart(categories):
  output = "Percentage spent by category"
  x = len(categories)
  y = 100

  #calculate total & percentages for each category
  percentages = list()
  total_spent = 0
  for cat in categories:
    total_spent += cat.get_withdrawals()
  for cat in categories:
    raw = cat.get_withdrawals() / total_spent
    percentages.append(int((raw // .1) * 10))

  while y >= 0:
    output += "\n"
    #input the correct right aligned Y axis value
    output += str(y) + "| " if y == 100 else " " + str(y) + \
        "| " if y < 100 and y > 0 else "  0| "

    #loop through each category column and check if a bar value exists
    col = 0
    while col < x:
      if percentages[col] >= y:
        # print(percentages[col], y)
        output += "o  "
      else:
        output += " "*3
      col += 1

    y -= 10

  output += "\n" + " "*4 + "-" + "-"*x*3

  #label x access using double loop for names
  max_name_length = 0
  for cat in categories:
    if len(cat.name) > max_name_length:
      max_name_length = len(cat.name)

  z = 0
  while z < max_name_length:
    output += "\n" + " "*5
    for cat in categories:
      try:
        output += cat.name[z] + " "*2
      except:
        output += " "*3

    z += 1

  return output

class Category:
    #constructor for class
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}"+f"{item['amount']:>7}"+'\n'
        
        output = title + items + 'Total: ' + str(total)
        return output
        
    def deposit(self, amount, description =""):
        self.ledger.append({"amount": amount, 
                            "description": description})
        
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount),
                                "description": description})
            return True 
        else:
            return False
            
        
    def get_balance(self):
        total_cash = 0
        for item in self.ledger: 
            total_cash += item['amount']
        return total_cash
         
    def transfer(self, amount, category):
        
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to'+ category.name)
            category.deposit(amount, 'Transfer from'+ self.name) 
            return True 
        else:
            return False
    
    def check_funds(self, amount):
        
        if self.get_balance() >= amount: 
            return True  
        else: 
            return False 
    
    def get_withdrawls(self):
        total = 0 
        for item in self.ledger:
            if item['amount']<0:
                total += abs(item['amount'])
        return total


food = Category('Food')
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category('Clothing')
clothing.deposit(2000, 'initial deposit')
clothing.withdraw(10.4, "summer clothes")
clothing.withdraw(222, 'wedding')
food.transfer(50, clothing)

auto = Category('Auto')


print(food.get_withdrawls())
print(clothing.get_withdrawls())

print(create_spend_chart([food, clothing, auto]))
