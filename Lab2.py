import math
import numbers
#page 58 questions ----- #Q1
"""
week_value = int(input('Q1:\nPlease enter a value from 0-6 that is associated with the days of week from Sunday to Saturday:  ')) #assumes user will follow instructions

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print('The day of week you chose was %s.\n' % days_of_week[week_value])

#Q2 ---- will be using list/array called week_value from above
start_day= int(input('Q2:\nPlease enter the starting day of your vacation from 0-6 that is associated with the days of week from Sunday to Saturday:  '))

length_stay= int(input('Please enter the length of the vacation:  '))

weeks_later =  length_stay/ 7
days_later = length_stay % 7
arrival_day = (length_stay + start_day) % 7

print('Your vacation started on %s. %i days later is %i weeks and %i days later. You come back on a %s.\n' % (days_of_week[start_day], length_stay, weeks_later, days_later, days_of_week[arrival_day]))

#Q3
b = int(input('Please Enter a value for b:  '))
a = int(input('PLease enter a value for a:  '))
day = 3
print('Q3a: b > a -> %s' % (b > a))
print('Q3b: b > a -> %s' % (b > a))
print('Q3c: a < 18 and day != 3 -> %s' % ((a < 18 and day != 3) ))
print('Q3d: a < 18 and day == 3 -> %s\n' % ((a < 18 and day == 3) ))

#Q4
print('Q4a: 3 == 3 -> %s' % (3 == 3))
print('Q4b: 3 != 3 -> %s' % (3 != 3))
print('Q4c: 3 >= 4 -> %s' % (3 >= 4))
print('Q4d: not(3 < 4)-> %s\n\nQ6:' % (not(3 >= 4)))

#Q6
numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
grades = { 
    range(75,101): 'First', 
    range(70,75): 'Upper Second', 
    range(60,70): 'Second',
    range(50,60): 'Third',
    range(45,50): 'F1 Supp',
    range(0,39): 'F3'
}

for grade in grades:
    for number in numbers:
        if number in grade:
            print('The mark %d recieved the grade of %s.' % (number, grades[grade]))

#Q7
def hypotenuse(A, B):
    return(((A ** 2) + (B**2))**0.5)

side_A = int(input('\nQ7:\nPlease enter the value for A of the right-angled triangle:  '))
side_B = int(input('Please enter the value for B of the right-angled triangle:  '))
print('The hypotenuse of a right triangle with side A = %i and side B = %i is %f\n'%(side_A, side_B, hypotenuse(side_A, side_B)))

#Q8
def hypotenuse(A, B, C):
    x=(((A ** 2) + (B**2))**0.5)
    #y = C **2
    threshold = 1e-7 #difference of 0.0000001
    return (abs(x-C) < threshold)
    
side_A = float(input('Q8:\nPlease enter the value for side A:  '))
side_B = float(input('Please enter the value for side B:  '))
side_C = float(input('Please enter the hypotenuse (side C):  '))
print('The triangle is a right-triangle: %s\n' % (hypotenuse(side_A, side_B, side_C)))

#Q9
print('Q9:\nThe triangle is a right-triangle: %s\n' % (hypotenuse(C = side_C, A = side_A, B = side_B)))

#Q10
a = math.sqrt(2.0)
print('Q10:\na = %f  a*a = %f a*a == 2.0 -> %s\n' % (a, a*a,(a*a == 2.0)))

#pg 60 questions ----Q1
for x in range(1001):
    print('We like Python\'s turtles!')

#Q4
print('\n')
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for x in numbers:
    print('Value of x: ', x)
print('\n')

for x in numbers:
    print('Value of x: %i   Value of %i^2: %i' % (x,x,x**2))
print('\n')

total = 0
for x in numbers:
    total += x
print('Sum of numbers: total = %i\n' % (total))

total= 1
for x in numbers:
    total *= x
print('Product of numbers: total = %i\n' % (total))
"""

#pg 61 questions----Q1
numbers2 = [10, 3, -7, 21, 38, 43, 24, 55, -1, -15, 22, 44]
print('\nnumbers2 = ', numbers2)

count = 0
for number in numbers2:
    if(number % 2 ==1): #odd number then increment count
        count+= 1
print('\nQ1: Odd values in numbers2 = ', count)

#Q2
sum_even = 0
for number in numbers2:
    if(number % 2 == 0): #even numbers summed up
        sum_even += number
print('\nQ2: Sum of all even values in numbers2 = ', sum_even)

#Q3
sum_negatve = 0
for number in numbers2:
    if(number < 0): #negative numbers summed up
        sum_negatve += number
print('\nQ3: Sum of all negative values in numbers2 = ', sum_negatve)

#Q4
word_list = ['apple', 'PeAr', 'orange', 'Pomegranate', 'blueberries', 'BERRY']

print('\nword_list = ', word_list)
word_count = 0
for word in word_list:
    if(len(word) == 5): #looks for words with length 5, increments if T
        word_count += 1

print('\nQ4: Number of words in word_list with length 5 = ', word_count)

#Q5
numbers3 = [3, -7, 21, 43, 55, -1, -15]
print('\nnumbers2 = ', numbers2, '  numbers3 = ', numbers3)

sum_w_even = 0
for number in numbers2:
    if(number % 2 == 1): #odd values
       sum_w_even += number
    else:
        break
print('\nQ5a: Sum of all elements in numbers2 up to the 1st even number: ' , sum_w_even)

for number in numbers3:
    if(number % 2 == 1): #odd values
       sum_w_even += number
    else:
        break
print('\nQ5b: Sum of all elements in numbers3 up to the 1st even number: ' , sum_w_even)

#Q6
word_list2 = ['apple', 'PeAr', 'orange', 'Pomegranate', 'sam', 'blueberries', 'BERRY'] #is capital Sam included
print('\nword_list = ', word_list, '\n\nword_list2 = ', word_list2)

for word in word_list:
    word.lower() #accounts for capital letters, makes comparison easier

word_count = 0
for word in word_list:
    if(word != 'sam'): #while word is not sam, increment
        word_count += 1
    else: #sam found, increment then break
        word_count += 1
        break
print('\nQ6a: Number of words in words_list up to and including \'sam\': ' , word_count)

word_count = 0
for word in word_list2:
    if(word != 'sam'):
        word_count += 1
    else:
        word_count += 1
        break
print('\nQ6b: Number of words in words_list2 up to and including \'sam\': ' , word_count, '\n')

#Q7
#newton's sqrt method -> better = (approximation + n/approximation) / 2   if(abs(a-b) < threshold)
threshold = 0.001
n = int(input('Q7: Please enter a value to determine the closest squareroot: '))
approximation = n
newton_count = 0
while True:
    better = (approximation + n/approximation) / 2
    newton_count += 1
    print('current value of better = ', better)
    if(abs(approximation - better) < threshold):
        print('Final value of better is ', better)
        break
    approximation = better
print('The squareroot of %i is %f. It took %i iterations to find the squareroot.\n' % (n, better, newton_count))

#Q13
digits = input('Q13: Please enter a value to determine the number of even digits: ')
digit_length = len(digits)
count_even_digit = 0

for digit in digits:
    digit_int = int(digit)
    if (digit_int % 2 == 0):
        count_even_digit += 1

print('\nThe number of even digits in the above input is %i.\n' % (count_even_digit))