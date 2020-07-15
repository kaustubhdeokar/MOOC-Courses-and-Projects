class Pants:

    def __init__(self, color,waist_size,length,price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)

class SalesPerson:

    def __init__(self, first_name,last_name,employee_id,salary,pants_sold=[],total_sales=0):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = pants_sold
        self.total_sales = total_sales
        
        
    def change_price(self, new_price):    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)

    def sell_pants(self,pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        print('here')
        arr = self.pants_sold
        for i in range(len(arr)):
            print("color: "+arr[i].color+"waist size: "+arr[i].waist_size+
            "lengtharr[i].length+arr[i].price)

def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    salesperson.sell_pants(pants_one)
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    salesperson.display_sales()

check_results()

### TODO: write a display_sales method:
#    
#    This method has no input or outputs. When this method 
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
#
###

### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#      
#      Args:
#        None
#      Returns:
#        float: total sales
#
###  


### TODO: write a calculate_commission method:
#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#