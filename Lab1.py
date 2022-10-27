from re import I
#exercise 1
a = 'All'
b = 'work'
c = 'and' 
d = 'no'
e = 'play'
f = 'makes'
g = 'Jack'
h = 'a' 
i = 'dull'
j = 'boy'

print('Exercise 1: \n' + a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f + ' ' + g + ' ' + h + ' ' + i + ' ' + j + ' ' + '\n')


#exercise 2
#x = 6 * (1 - 2)
print('Exercise 2: \nx = 6 * (1 - 2) = ', (6*(1-2)))

#exercise 4
#bruce = 4

#exercise 5
print('Exercise 5: \n')
princ_Amount = 10000
interest_Dec = (float(input('Please enter the precent interest rate: '))) / 100
num_compound = 12 #monthly
time_Years = float (input('Please enter the number of years: '))
amount = ( princ_Amount * ( 1 + ( interest_Dec / num_compound ) ) ** ( num_compound * time_Years ) )
print('\nAccrued amount: $ ', amount)
#equation A=P(1+(r/n))^(n*t)

#exercise 6
print('\nExercise 6: \na) 5 % 2 =', (5 % 2))
print('b) 9 % 5 = ', (9 % 5))
print('c) 15 % 12 = ', (15 % 12))
print('d) 12 % 15 = ', (12 % 15))
print('e) 6 % 6 = ', (6 % 6))
print('f) 0 % 7 = ', (0 % 7))
print('g) 7 % 0 =', (7 % 0))

#exercise 7
print('\n')
time = int(input('Please enter the current time now in hours: '))
am_pm = input('Please enter whether the above time is in AM or PM using A or P: ')
am_pm.upper()
hours_ahead = int(input('Please enter the how many hours ahead the alarm is set for: '))
days_later = hours_ahead / 24 #accounts for days
hours_later = hours_ahead% 24 #takes reminder as hours
alarm_AP = ' '
#set whether alarm is AM or PM
#assuimption that char entered is either A or P
if hours_ahead < 11:
    alarm_AP = am_pm
else:
    if am_pm == 'a':
        alarm_AP = 'P'
    else:
        alarm_AP = 'A'

alarm_time = (time + hours_later) % 12
print('The current time is %s %s. The alarm will be set for %i days and %i hours later at %s %s.\n' % (time, am_pm, days_later, hours_later, alarm_time, alarm_AP))
