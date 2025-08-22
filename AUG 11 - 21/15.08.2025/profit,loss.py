costprice = float(input("Enter the cp:"))
sellingprice = float(input("Enter the sp:"))

if (sellingprice>costprice):
    print("Profit")
    pt=sellingprice-costprice
    print(pt)

else:
    print("no profit")