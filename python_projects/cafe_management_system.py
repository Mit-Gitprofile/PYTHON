
#CAFE MANAGEMENT SYSTEM

menu={
    "pizza":50,
    "pasta":60,
    "burger":70,
    "noodel":80,
    "cold-coco":90,
    "coffee":100,
}

print("\nWelcome to our python restorent\n")
print("MENUE:-\n")
for i,p in menu.items():
    print(f"{i}:{p}")

print("\n")

total=0
orderitm=[]

itm1=input("Enter your order:")
if itm1 in menu:
    total+=menu[itm1]
    orderitm.append(itm1)
    print(f"your item {itm1} added in order")

    print("=== orders ===")
    print("\n".join(orderitm))
    print("==============")

    print(f"your amount is {total}")

else:
    print(f"your item {itm1} is not available")

while True:
    y=input("you ordered any item (yes/no):")

    if(y=="yes"):
        itm2=input("Enter your order:")
        if itm2 in menu:
            total+=menu[itm2]
            orderitm.append(itm2)
            print(f"your item {itm2} added in order")

            print("=== orders ===")
            print("\n".join(orderitm))
            print("==============")

            print(f"your amount is {total}")

        else:
            print(f"your item {itm2} is not available")

    elif(y=="no"):
        print(f"thanks for coming ..... your total bill is {total}")
        break

    else: 
        print("Enter only (yes) or (no)")