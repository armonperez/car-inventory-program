



in_stock_Cars = {

"toyota" : "corolla" ,

"honda" : "civic" , 


}



out_of_stock_cars = {

"Lexus": "LS350"

}


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
    pass
def change_inventory():
    pass

question()