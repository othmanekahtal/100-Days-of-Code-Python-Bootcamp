# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
if year % 4 == 0 :
    if year % 100 != 0 or year % 400 == 0 :
        print("leap year")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")