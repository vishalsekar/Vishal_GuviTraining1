class foodOrdering:
    def __init__(self,quantity,menu):
         self.quantity = quantity
         self.menu = menu
    
    def price_calculation(self):
         
         if self.menu == "dosa":
              rate=50

         elif self.menu =="idly":
              rate=10

         elif self.menu == "chappathi":
              rate=20

         else:
              print("Requested menu is not available")
              return 
         
         total=rate*self.quantity
         print("Total fare: ",total)
 
menu=input("Enter the menu : ")
quantity=int(input("Enter the quantity : "))

price=foodOrdering(quantity,menu)
price.price_calculation()