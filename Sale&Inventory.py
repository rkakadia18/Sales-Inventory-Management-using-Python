#Inventory System
#dictionary for product catalog
from datetime import datetime
Product_Catalog = {
    "J001": {
        "name":"Diamond Necklace",
        "price_per_unit":150,
        "current_stock":20,
    },
    "J002" : {
        "name":"Gold Hoop Earrings",
        "price_per_unit":300,
        "current_stock":40,
    },
    "J003" : {
        "name":"Sapphire Ring",
        "price_per_unit":100,
        "current_stock":25,
    },
    "J004" : {
        "name":"Ruby Bracelet",
        "price_per_unit":500,
        "current_stock":50,
    },
    "J005" : {
        "name": "Pearl Earrings",
        "price_per_unit":75,
        "current_stock":45,
    },
    "J006" : {
        "name" : "Platinum Wedding Band",
        "price_per_unit" : 700,
        "current_stock" : 22,
    }

}

def view_catalog():
    print("\nProduct Catalog:")
    print("Product_ID\tName\tPrice_per_unit\tQuantity")
    for pid,details in Product_Catalog.items():
        print(f'{pid} | {details["name"]} | {details["price_per_unit"]} | {details["current_stock"]}')

view_catalog()

 #Sale history list
sale_history = []

def make_sale():
    view_catalog()
    SaleProduct = input("Enter the ProductID of the item sold:")
    SaleQuantity = int(input("Enter the quantity sold:"))
    if SaleProduct in Product_Catalog:
        try:
            if Product_Catalog[SaleProduct]["current_stock"] >= SaleQuantity:
                Total_Sale_Amount = SaleQuantity*Product_Catalog[SaleProduct]["price_per_unit"]
                #Update stock qty 
                Product_Catalog[SaleProduct]["current_stock"]=Product_Catalog[SaleProduct]["current_stock"]-SaleQuantity

                Sale_record = {
                    "SaleID" : len(sale_history)+1,
                    "Date_time_of_sale" : datetime.datetime.now(),
                    "ProductID" : SaleProduct,
                    "Quantity_sold" : SaleQuantity,
                    "TotalSale": Total_Sale_Amount
                }
                sale_history.append(Sale_record)
                print(f'Your sale was successfully accepted!{Sale_record}')
            else:
                print('Stock Quantity not available')
        except Exception as e:
                  print(f'An error occured:{e}')
            
    
    else:
        print('Invalid ProductID')

def update_price(Product_Catalog):
    try:
        productid = input("Enter the product ID for the item that needs a price change")
        if productid.upper in Product_Catalog: 
             NewPrice = float(input(f"Enter the new price for {Product_Catalog[productid]['name']}"))
             if NewPrice > 0 : 
                  Product_Catalog[productid]['price_per_unit'] = NewPrice
                  print(f"Price for {Product_Catalog[productid]['name']} was changed to ${NewPrice}")
             else: 
                print("Value should be positive")
        else: 
             print('Invalid ProductID')
             
    except Exception as e: 
         print(f'error{e}') 
         


update_price(Product_Catalog)




             
                  
          


 

     
    





          





