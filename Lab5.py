import csv
from datetime import date
import string
from urllib.parse import SplitResult
'''
#q1
x_dim = int(input('Enter an int for x: '))
y_dim = int(input('Enter an int for y: '))
twoD_list = [[i*j for i in range(y_dim)] for j in range(x_dim)]
print('Q1: ',twoD_list)

#q1a
with open("test.txt", 'w') as f:
    for a in twoD_list:
        f.write("%s" % a)
'''
#with open("test_b.bin", 'wb') as f2: #can't write to binary file
    #for row in twoD_list:
        #binary = bin(twoD_list[row][col])
       # f2.write(binary)
'''
#q1b
print('Read Txt file:')
with open("test.txt") as foo:
    for a in foo:
        print(a)
'''
#with open("test_b.bin", "r") as fooz:
    #for a in fooz:
        #print(a)
'''

#q1c
with open('output.csv', 'w') as csv_file:
    file_Writer = csv.writer(csv_file)
    file_Writer.writerow(twoD_list)

#q2
sentence=input('Q2: Enter a sentence, seperated by a comma: ')
sentence = sentence.split(",")
sorted_array = sorted(sentence)
for b in sorted_array:
    print(b, end =',')

#q3
sentence2=input('\n\nQ3: Enter a sentence, seperated by a space: ')
sentence2 = sentence2.split(" ")
sorted_array2 = sorted(sentence2)
for b in sorted_array2:
    print(b, end =' ')

#q4
sentence3=input('\n\nQ4: Enter a sentence: ')
lower_count, upper_count = 0, 0
for a in sentence3:
    if ord(a) in range(97, 123):
        lower_count += 1
    elif ord(a) in range(65, 91):
        upper_count += 1
    else:
        continue
print('Upper count: {0} Lower Case: {1}'.format(upper_count, lower_count))

#q5
int_input=input('\nQ5: Enter a list of ints, seperated by a comma: ')
int_input = int_input.split(",")
list_ints = []
square_odds = []
for a in int_input: #adding ints to int_list
    if(a.isdigit()) and (int(a) % 2) == 1:
        list_ints.append(int(a))
        square_odds.append(int(a)**2)

print('List of Odd Ints: ', list_ints, 'List of Odd Ints Squared: ',square_odds)

#q6
sentence5=input('\n\nQ6: Enter a sentence: ')
s_list = sentence5.split()
freq_dict = {}
for s in set(s_list):
    freq_dict[s] = s_list.count(s)
items = freq_dict.items()
sorted_dict = sorted(items)
for a in range(len(sorted_dict)):
    print(sorted_dict[a][0],':', sorted_dict[a][1])

#q7
print('\nQ7:\n')
with open('data_csv.csv', 'r') as csvfile2:
    csv_content = csv.DictReader(csvfile2)
    for row in csv_content:
        print(dict(row))


#q8
print('\nQ8:\n')
sport_dict = {
    'Atlanta':
        {'soccer':
            { 
                'Name':'United Soccer Club',
                'Wins': 1,
                'Losses':0
            },
         'football':
            { 
                'Name':'Falcons',
                'Wins': 7,
                'Losses': 10
            }
            
        },

    'New England':
        {'soccer':
            { 
                'Name':'Revolution',
                'Wins':22, 
                'Losses':5
            },
          'football':
            {
                'Name':'Patriots',
                'Wins':10, 
                'Losses':7
            }
        },
    'Philidelphia':
        {'soccer':
            { 
                'Name':'Union',
                'Wins':14, 
                'Losses':8
            },
          'football':
            { 
                'Name':'Eagles',
                'Wins':9, 
                'Losses':8
            }
        },
    'Chicago':
        {'soccer':
            { 'Name':'Fire Football Club',
            'Wins':9, 
            'Losses':18
            },

            'football':
            { 
                'Name':'Bears',
                'Wins':6, 
                'Losses':11
            }
        }
}

for  k1 in sport_dict: #each teams win percent
    win_percent = sport_dict[k1]["soccer"]['Wins'] / (sport_dict[k1]["soccer"]['Wins'] - sport_dict[k1]["soccer"]['Losses'])
    print('{}\'s soccer win percentage: {}'.format(sport_dict[k1]["soccer"]['Name'], round(win_percent,2)))
    win_percent = sport_dict[k1]["football"]['Wins'] / (sport_dict[k1]["soccer"]['Wins'] - sport_dict[k1]["soccer"]['Losses'])
    print('{}\'s football win percentage: {}'.format(sport_dict[k1]["soccer"]['Name'], round(win_percent,2)))

city_team = ' ' #name of city w/ highest win percent 
high_win_percent = 0.0
win_percent = 0.0 
for  k1 in sport_dict: #highest avg winning percent
    win_percent = sport_dict[k1]["soccer"]['Wins'] / (sport_dict[k1]["soccer"]['Wins'] - sport_dict[k1]["soccer"]['Losses'])
    win_percent = win_percent + (sport_dict[k1]["football"]['Wins'] / (sport_dict[k1]["soccer"]['Wins'] - sport_dict[k1]["soccer"]['Losses']))
    if(win_percent > high_win_percent):
        high_win_percent = win_percent
        city_team = sport_dict[k1] #couldn't extract just the key
    win_percent = 0.0 
print('\nCity with highest average winning persentage: ', city_team)

#q9
bin_input=input('\nQ9: Enter a list of binary numbers, seperated by a comma: ')
bin_list = bin_input.split(",") #returns list
for a in bin_list:
    if(int(a,2) % 5 == 0):
        print(a)
'''
#q10
print('\nQ10:\n')
num_list = []
temp_string = ' '
for a in range(1000,3001):
    temp_string = str(a)
    for b in temp_string:
        if(int(b) % 2 != 0):
            break
    else:
        num_list.append(a)
for b in num_list:
    print(b, end=",")     


#q11
sentence6=input('\n\nQ11: Enter a sentence: ')
letter_count, digit_count = 0, 0
for a in sentence6:
    if (ord(a) in range(97, 123) or ord(a) in range(65, 91)):
        letter_count += 1
    elif ord(a) in range(48, 58):
        digit_count += 1
    else:
        continue
print('Letter Count: {0}, Digit Count: {1}'.format(letter_count, digit_count))

#q12
password_input=input('\nQ12: Enter a list of passwords, seperated by a comma: ')
password_list = password_input.split(",")

#q13
print('\n\nQ13:')

basic_string = "Professor Robert Mann"
a = basic_string.isalpha()
b = basic_string.islower()
c = basic_string.isupper()
d = basic_string.isdigit()
e = basic_string.startswith('Hello')
f = basic_string.endswith('Mann')
print('isAlpha()= {} islower()= {}, isupper()= {}, isdidgit()= {}, startswith(\"Hello\")= {}, endswith(\'Mann\')= {}'.format(a, b, c, d, e, f))

basic_string2 = "---Intro to Python---"
g = basic_string2.lower()
h = basic_string2.upper()
i = basic_string2.title()
j = basic_string2.lstrip('-')
k = basic_string2.rstrip('-')
l = basic_string2.strip('-')
print('\n\nlower()= {}, upper()= {}, title()= {}, lstrip()= {}, rstrip()= {}, strip()= {}'.format(g,h,i,j,k,l))

m = basic_string2.ljust(30)
print(m)
n = basic_string2.rjust(45)
print(n)
o = basic_string2.center(20)
print(o)

print('\nOrdinal of %:', ord('%'), 'Char of 94:', chr(94))

string_val =  "delicious"
print('\nstring_val[0]=',string_val[0],'string_val[-1]=', string_val[-1], 'string_val[1]=', string_val[1], 'string_val[2]=', string_val[2])
print('string_val[5:]=',string_val[5:], 'string_val[7]=', string_val[7], 'string_val[3:5]=', string_val[3:5], 'string_val[-1:]=',string_val[-1:], 'string_val[:-1]=',string_val[:-1], '\n')

print('^'*36,'\n', 'Hello World!'*5)
rand_string = """ Students  will  gain  an  ability  to  write  small  programs  in  a  modern  programming language
Students will learn to use Python packages and toolkits
Students will learn to develop analytic/data science applications"""
print('\nrand_string = {0}\nlen(rand_string)={1}'.format(rand_string, len(rand_string)))

Phone_number = '\n1-800-555-1212'
x = Phone_number.replace('-','(',1)
x = Phone_number.replace('-',')',1)
x = Phone_number.replace('-','.',1)
print(x)

Quote="These are the times that try men/'s souls."
Date = "02/14/2019"
date_list = Date.split("/")
num_date = []
for a in date_list:
    num_date.append(int(a))
print('date:%(MM)02d/%(DD)02d/%(YYYY)04d\n' % {'MM':num_date [0], 'DD': num_date [1], 'YYYY': num_date  [2]})