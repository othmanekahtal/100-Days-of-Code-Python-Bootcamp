# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  total += student_heights[n];
print(f"Average of height : {round(total/len(student_heights),2)}")