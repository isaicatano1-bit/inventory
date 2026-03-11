inventory = []
sales_history=[]
def add():
    name = input("name of product: ")
    for product in inventory:
        if product["name"] == name:
         print("already registed")
         return
    print("")
    price = float(input("price of the product: "))
    print("")
    quantity = int(input("quantity of product: "))
    print("")
    validation(name,price,quantity)

    product={
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(product)

    print("registred correctly")
    return

def sell(name,price,quantity):
   validation(name,price,quantity)
   name_of_product = input("name of product to buy: ")
   quantity = int(input("quantity of product to buy: "))
   for product in inventory:
        if product["name"] == name_of_product:

            if product["quantity"] >= quantity:
                total = product["price"] * quantity
                product["quantity"] -= quantity
                sale = {
                    "name": name_of_product,
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

def validation(name,price,quantity):
    try:
        if name.isdigit:
            print("only letter")
        else:
            return None
        if price <= 0 or quantity <= 0:
            print("error. not enter negative number")
            return None
    except ValueError:
        print("error. dont enter a character")

#menu
   
while True:

    print("")
    print("1. add product")
    print("2. sell product")
    print("3. view history")
    print("4 sales history")
    print("5. exit")
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
        print("goodbye")
        break

    else:
        print("invalid option")