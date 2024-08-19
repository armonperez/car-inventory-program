



in_stock_Cars = [

"toyota corolla" ,

"honda civic" , 


]


out_of_stock_cars = [ 

"Lexus LS350"

]


def question():

   answer = input("Do you want to purchase a car ?")
   while True:
      if answer == "y":
       
       print(f"We currently have the following in stock :{in_stock_Cars}")

       break
      if answer == "n":
       
       print("see you soon")

      else:
       print("Invalid input")
      return question

def buy():
    print(in_stock_Cars)
    purchase = input(f"Please select a car you would like to buy Option 1. {in_stock_Cars[0]} Option 2. {in_stock_Cars[1]}")
    if purchase == "1":
      pruchased_car = in_stock_Cars[0]
      update_list =[item for item in out_of_stock_cars] + [pruchased_car]
      in_stock_Cars.pop(0)

      print("Out of stock cars" , update_list)
      print("in stock cars", in_stock_Cars)
      return buy

def change_inventory():
    pass

buy()