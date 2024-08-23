



in_stock_Cars = [

"toyota corolla" ,

"honda civic" , 


]


out_of_stock_cars = [ 

"Lexus LS350"

]


def question():

  
   while True: 
    
      answer = input("Do you want to purchase a car ?")
      if answer == "y":
       
       print(f"We currently have the following in stock :{in_stock_Cars[0], in_stock_Cars[1]}")

       break
      if answer == "n":
       
       print("see you soon")

      else:
       print("Invalid input")

      return question

def buy():
    print(in_stock_Cars)
    purchase = input(f"Please select a car you would like to buy Option 1. {in_stock_Cars[0]} Option 2. {in_stock_Cars[1]} :" " ")
    if purchase == "1":
      
      print(f"You purchased a {in_stock_Cars[0]}.")
      pruchased_car = in_stock_Cars[0]
      update_list =[item for item in out_of_stock_cars] + [pruchased_car]
      in_stock_Cars.pop(0)

      print("Out of stock cars" , update_list)
      print("in stock cars", in_stock_Cars)
      
    elif purchase == "2":
        print (f"You purchased a {in_stock_Cars[1]}")
        pruchased_car = in_stock_Cars[1]
        update_list =[item for item in out_of_stock_cars] + [pruchased_car]
        in_stock_Cars.pop(1)
        
        return buy

def change_inventory():
    pass

def main():
   
    question()
    buy()

main()
