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
                print("price must be greater than 0")
            else:
                break

        except ValueError:
            print("enter a valid number")
    while isai:
        try:
            quantity = int(input("quantity of product: "))
            if quantity <= 0:
                print("quantity must be greater than 0")
            else:
                break
        except ValueError:
            print("enter a valid number")

    product={
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(product)

    print("registred correctly")
    return
#funcion of sells
def sell():
   name = input("name of product to buy: ")
   while isai:
        try:
            quantity = int(input("quantity of product: "))
            if quantity <= 0:
                print("quantity must be greater than 0")
            else:
                break
        except ValueError:
            print("enter a valid number")
       
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

                print("sale completed")
                print("total to pay:", total)
                print("remaining stock:", product["quantity"])
                return
            
            else:
                print("not enough stock")
                return

   print("product not found")

#explain sells
def record():
    if len(sales_history) == 0:
        print("no sales yet")
    else:
        for sale in sales_history:
            print("product:", sale["name"])
            print("quantity:", sale["quantity"])
            print("total:", sale["total"])
            print("------")


def total_sales():
    total = 0

    for sale in sales_history:
        total += sale["total"]

    print("total money from sales:", total)


def view_inventory():

    if len(inventory) == 0:
        print("inventory empty")
        return

    for product in inventory:
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        print("----------------")


#menu
while isai:
   print("")
   print("1. add product")
   print("2. sell product")
   print("3. view history")
   print("4 sales history")
   print("5. view inventory")
   print("6. exit")
   print("")

   option = input("choose an option: ")

   if option == "1":
        add()

   elif option == "2":
        sell()

   elif option == "3":
        record()
   elif option == "4":
        total_sales()

   elif option == "5":
       view_inventory()
   elif option == "6":
        print("goodbye")    
        isai = False
   else:
        print("invalid option")