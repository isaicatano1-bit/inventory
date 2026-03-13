isai = True
inventory = []
sales_history=[]
#add products
def add():
    name = input("name of product: ")
    for product in inventory:
        if product["name"] == name:
         print("already registed")
         return
    print("")
    while isai:
        try:
            price = float(input("price of the product: "))
            if price <= 0:
                print("ERROR, price must be greater than 0")
                print("")
            else:
                break

        except ValueError:
            print("ERROR, enter a valid number")
            print("")
    while isai:
        try:
            quantity = int(input("quantity of product: "))
            if quantity <= 0:
                print("ERROR, quantity must be greater than 0")
                print("")
            else:
                break
        except ValueError:
            print("ERROR, enter a valid number")
            print("")

    product={
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(product)

    print("registred correctly")
    print("------------------------------")
    return


#funcion of sells
def sell():
   name = input("name of product to buy: ").lower()
   while isai:
        try:
            quantity = int(input("quantity of product: "))
            if quantity <= 0:
                print("ERROR, quantity must be greater than 0")
                print("")
            else:
                break
        except ValueError:
            print("ERROR, enter a valid number")
            print("")
   for product in inventory:
        if product["name"] == name:

            if product["quantity"] >= quantity:
                total = product["price"] * quantity
                product["quantity"] -= quantity
                sale = {
                    "name": name,
                    "quantity": quantity,
                    "total": total
                }

                sales_history.append(sale)
                print("-----------------------------")
                print("sale completed")
                print("product:", name)
                print("price:", product["price"])
                print("total to pay:", total)
                print("remaining stock:", product["quantity"])
                return
            
            else:
                print("not enough stock")
                return

   print("product not found")

#menu
while isai:
   print("")
   print("1. add product")
   print("2. sell product")
   print("3. exit")
   print("")

   option = input("choose an option: ")

   if option == "1":
        add()

   elif option == "2":
        sell()

   elif option == "3":
        print("goodbye")    
        isai = False
   else:
        print("invalid option")

#this code is a simple inventory system, only have two functions, add products and sell products,
#the function sell, show the total to pay, the price of the product and the remainig stock.