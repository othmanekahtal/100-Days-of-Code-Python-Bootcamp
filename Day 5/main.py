student_heights = [180, 124, 165, 173, 189, 169, 146]
avr = 0
counter = 0
high = 0
for std in student_heights:
    high = std if std > high else high
result = 0
for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FIZZBUZZ')
        else:
            print('FIZZ')
    elif i % 5 == 0:
        print('BUZZ')
    else:
        print(i)
