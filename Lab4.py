import random
import string
#q1

def divis_multiple(): # won't include 1500 or 2700
    print('Q1: All values divisible by 7 and a multiple of 5')
    #range(start, stop)
    for n in range(1500, 2701):
        if (((n % 7) == 0) and ((n % 5) == 0)):
            print(' ',n)
    return

divis_multiple()

#q2 -fix
def celsius_fahren(val, deci):
    if(deci.lower() == 'f'):
        print('{} C is {} Fahrenheit'.format(val, round((9 * val) / 5 + 32, 2)))
    elif(deci.lower() == 'c'):
       print('{} F is {} Celsius'.format(val, round((val - 32) * 5 / 9, 2)))
    else:
        print('Invalid entry');
print('\nQ2: ')
temp = float(input('Enter a temperature to convert to Celsius or Fahrenheit: '))
degree_type = input('Please enter which temperature you would like to convert to: ')[0]
celsius_fahren(val = temp, deci = degree_type)

#q3
print("\nQ3: A random number between 1 to 9 is:", random.randint(1,9))

#q4
print('\nQ4:')
for i in range(6):
    print('*' * i)
    if(i == 5):
        for j in range(1,5):
            print('*' * (i-j))

#q5
def fibonacci():
    n0, n1, nth_val = 0, 1, 0
    for n in range(0, 51):
        if(n == 0):
            print(n)
        elif(n == 1):
            print(n1)
        else:
         nth_val = n0 + n1 #(n-2)+(n-1)
         print(nth_val)
         n0=n1
         n1=nth_val

print('\nQ5: ')
fibonacci()

#q6
print('\nQ6: ')
for a in range(0, 7):
    if(a == 3) or (a == 6):
        continue
    else:
        print(a)

#q7
numbers = (1, 3, 56, 87, 3, 4, 89, 7,)
print('Q7: numbers = ', numbers)
odd_nums, even_nums = 0, 0
for n in numbers:
    if((n % 2) != 0):
        odd_nums += 1
    else:
        even_nums += 1

print('Number of even values: {}\nNumber of odd values: {}' .format(even_nums, odd_nums))

#q8
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print('\nQ8:\n')
for d in datalist:
    print(d, type(d))
#q9
print('\nQ9: ')

def fizz_buzz():
    #range(start, stop)
    for n in range(0, 51):
        if(n%3==0 and n%5==0):
            print('fizzbuzz')
        elif(n%3==0):
            print('fizz')
        elif(n%5==0):
            print('buzz')
        else:
            print(n)

fizz_buzz()

#q10
user_input= input('Q10:\nEnter a string with letters and digits: ')
digits_count = 0
letters_count = 0 
for a in user_input:
    if(a.isdigit()):
        digits_count += 1
    elif a.isalpha():
        letters_count += 1
    else:
        continue  
  
print('Letters {1} \nDigits {0}\n'.format(digits_count, letters_count))

#q11
user_input = input('Q11:\nEnter a letter from the alphabet: ')
if user_input.lower() in {'a', 'e', 'i', 'o', 'u'}:
    print('{} is a vowel.\n'.format(user_input))
else:
    print('Value entered is a consonant.\n')

#q12 -
random_string = input('Q12:\nEnter a string: ')
string_TF = False
for a in random_string:
    if (a.isalpha() == True):
        string_TF = True
    else:
        string_TF = False
print('The string is a string.\n') if (string_TF == True) else print('The string is a string.\n')
#q13
def count_alpa_numeric(u_input):
    digits_count, letters_count, other_count = 0, 0, 0
    for a in u_input:
        if(a.isdigit()):
            digits_count += 1
        elif a.isalpha():
            letters_count += 1
        else:
            other_count += 1 
    return[digits_count, letters_count, other_count]

user_input= input('Q13:\nEnter a string with letters and digits: ')
list_of_counts = count_alpa_numeric(user_input)
print('Letters {1} \nDigits {0}\nOther {2}\n'.format(list_of_counts[0], list_of_counts[1], list_of_counts[2]))

#q14
def float_verify(user_input):
    pos= user_input.find('.')
    if((pos != -1) and user_input[pos -1].isdigit() and user_input[pos + 1].isdigit()):
        return([True, float(user_input)])
    else:
        return([False, -1.0])

float_input = input('Q14:\nEnter in a string: ')
float_eval = float_verify(float_input)
print('Is {} a float? {}  what is it? {}\n'.format(float_input, float_eval[0], float_eval[1]))

#q15 - need to fix
def tip_calc(sub_total, tip_percent = 0.15):
    if( tip_percent > 0):
        tip_percent = tip_percent / 100
    
    return(sub_total * tip_percent)

subtotal = float(input('Q15:\nEnter a subtotal: '))
tip_percent = float(input('Enter a tip percent: '))
tip = tip_calc(subtotal, tip_percent)
print('The calcuted tip with a subtotal of {} and a tip percentage of {} is {}'.format(subtotal, tip_percent, tip))
tip2 = tip_calc(sub_total = subtotal)
print('The calcuted tip with a subtotal of {} and the default tip percentage is {}'.format(subtotal, tip2))
