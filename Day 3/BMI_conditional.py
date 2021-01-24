height = float(input("enter you height in m : "))
weight = float(input("enter your weight in kg :"))
# calculate BMI :
BMI=weight/height**2
case = ""
if BMI < 18.5 :
    case="underweight"
elif BMI > 18.5 and BMI < 25:
    case = "normal weight"
elif BMI > 25 and BMI < 30 :
    case = "overweight"
elif BMI > 30 and BMI < 35 :
    case = "obese"
elif BMI > 35 :# you can replace this line into else
    case = "clinically obese"
print(f"you BMI is {round(BMI,2)}, you are slightly {case} .")