print("Welcome to the rollercoaster!")
height = float(input("enter your height in m :"))
bill=0;
if height >= 1.2 :
    print("You can ride the rollercoaster!")
    age = int(input("enter your age :"))
    if age > 18:
        print("Adult tickets are $12.")
        bill+=12
    elif age <= 18:
        print("Youth tickets are $7.")
        bill+=7
    else:
        print("Child tickets are $5.")
        bill+=5
    if input("Do you want a photo taken? Y or N.").upper()== "Y":
        bill+=3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")