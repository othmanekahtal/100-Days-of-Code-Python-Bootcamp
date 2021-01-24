# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
name1_name_2=name1.lower()+name2.lower()
print(name1_name_2)
true_Total=0
true_Total+=name1_name_2.count("t")
true_Total+=name1_name_2.count("r")
true_Total+=name1_name_2.count("u")
true_Total+=name1_name_2.count("e")
love_Total=0
love_Total+=name1_name_2.count("l")
love_Total+=name1_name_2.count("o")
love_Total+=name1_name_2.count("v")
love_Total+=name1_name_2.count("e")
secore_love=int(str(true_Total)+str(love_Total))
if secore_love<=10 and secore_love>=90:
    print(f"Your score is {secore_love}, you go together like coke and mentos.")
elif secore_love>=40 and secore_love<=50:
    print(f"Your score is {secore_love}, you are alright together.")
else:
    print(f"Your score is {secore_love}.")