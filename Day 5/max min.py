# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores : ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# max function for getting the maximum value in list:
#max = max(student_scores)
# min function for getting the manimum value in list:
#min = min(student_scores)


# getting max value using loops :
max_score = student_scores[0]
for n in range(0,len(student_scores)):
    if max_score < student_scores[n]:
        max_score = student_scores[n]
print(f"The highest score in the class is: {max_score} ")

# getting min value using loops :
min_score = student_scores[0]
for n in range(0,len(student_scores)):
    if min_score>student_scores[n]:
        min_score=student_scores[n]
print(min_score)
print(f"The lowest score in the class is: {min_score} ")