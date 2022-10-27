#lists
'''my_list1 = []
print("\nmy_list1 =", my_list1)

my_list2 = [1]
print("my_list2 =:", my_list2)

my_list3 = [ 'a', 3.56, 'Zebra', 700, False ]
print("\nmy_list3 =", my_list3)
print("3rd item in my_list3:", my_list3[2], "\nThe item at index -3 in my_list3:", my_list3[-3])

my_list3[2] = "bye"
print("my_list3 after changing the 3rd item:", my_list3)

my_list3[-4] = 'hello'
print("my_list3 after changing the -4th item:", my_list3, "\nThe length of the my_list3:", len(my_list3))
my_list3.pop(-5)
print("my_list3 after pop(-5):", my_list3)

#print("\nmy_list3 =", my_list3, "\nMin of my_list4:", min(my_list3), "\nMax of my_list4:", max(my_list3)) 
#error message, cannot compare elements of differing types

my_list3[:0] = ['heaven', -986]
print("\nmy_list3 after insertion at the front:", my_list3)

append_list = ['abc', 1, "ABC"]
my_list3.append(append_list)
print("my_list3 after appending to end of list:", my_list3)

my_list3.append('hello')
print("my_list3 after insertion at the end:", my_list3)

my_list3.append("world")
print("my_list3 after 2nd insertion at the end:", my_list3) 

print('\nmy_list3 before pop():', my_list3)
my_list3.pop()
print('my_list3 after pop()', my_list3)

print('\nmy_list3 before pop(4):', my_list3)
my_list3.pop(4)
print('my_list3 after pop(4)', my_list3)

print('\nmy_list3 before pop(-2):', my_list3)
my_list3.pop(-2)
print('my_list3 after pop(-2)', my_list3)

print('my_list3 length as float: %f\n' % float(len(my_list3)), 'my_list3 type:', type(my_list3))
print('\nmy_list3 order:', ord(my_list3)) #ord() does not work b/c it returns the unicode cide for a given char

#tuples
my_tuple1 = ()
print('\nmy_tuple1 =', my_tuple1)

my_tuple2 = (3)
print('my_tuple2 =', my_tuple2)

my_tuple3 = ('a', 3.56, 'Zebra', 700, False)
print('my_tuple3 =', my_tuple3)

print('3rd element in my_tuple3:', my_tuple3[2], '\nelement at  -3 in my_tuple3: ', my_tuple3[-3])

my_tuple3[3] = "bye" #error: cannot change elements w/in a tuple
print('my_tuple3 after changing 3rd item: ', my_tuple3)

my_tuple3[-4] = 'hello' #error: cannot change elements w/in a tuple
print('my_tuple3 after changing -4th item: ', my_tuple3, '\nmy_tuple3 length = ', len(my_tuple3))

print("\nmy_tuple3 =", my_tuple3, "\nMin of my_tuple3:", min(my_tuple3), "\nMax of my_tuple3:", max(my_tuple3)) 
#error message, cannot compare elements of differing types

del my_tuple3[-5] #error: cannot change elements w/in a tuple

my_tuple3[:0] = ('heaven', -986)
print('\nmy_tuple3 after insertion at front:', my_tuple3)

my_tuple4 = ('abc', 1, "ABC")
my_tuple3.append(my_tuple4)

my_tuple3.append('hello')
print("my_tuple3 after insertion at the end:", my_tuple3)

my_tuple3.append("world")
print("my_tuple3 after 2nd insertion at the end:", my_tuple3) 

print('\nmy_tuple3 before pop():', my_tuple3)
my_tuple3.pop()
print('my_tuple3 after pop()', my_tuple3)

print('\nmmy_tuple3 before pop(4):', my_tuple3)
my_tuple3.pop(4)
print('my_tuple3 after pop(4)', my_tuple3)

print('\nmy_tuple3 before pop(-2):', my_tuple3)
my_tuple3.pop(-2)
print('my_tuple3 after pop(-2)', my_tuple3)

print('my_tuple3 length as float: %f\n' % float(len(my_tuple3)), 'my_tuple3 type:', type(my_tuple3))
print('\nmy_tuple3 order:', ord(my_tuple3)) #ord() does not work b/c it returns the unicode for a given char
'''

#dictionaries
A = {
    'Yale University': 'Handsome Dan',
    'Michigan State University': 'Spartan',
    'University of Michigan': 'Wolverine',
    'University of Texas': 'Bevo',
    'Stanford University' : 'Stanford Tree',
    'Georgia Institute of Technology' : 'Buzz'
}

B = dict(
    [('Yale University', 'Handsome Dan'),
    ('Michigan State University','Spartan'),
    ('University of Michigan', 'Wolverine'),
    ('University of Texas', 'Bevo'),
    ('Stanford University' , 'Stanford Tree'),
    ('Georgia Institute of Technology' , 'Buzz')]
)

C = dict(
    yale_uni= "Handsome Dan",
    michigan_state_uni ='Spartan',
    uni_of_michigan ='Wolverine',
    uni_of_texas ='Bevo',
    standford_uni ='Stanford Tree',
    georgia_institute_of_techn ='Buzz'
    )

print('value of \'lion:', A['lion'])
A['Idaho University'] = 'Joe Vandal'
print('\nA = ', A)
B['Michigan State University'] = 'not spartan'
print('\nB = ', B)
del B["Yale University"]
print('\nB = ', B)
print('\nIs wolverine in the dictionary? ', ('wolverine' in C))
print('\nLength of A: ',len(A))
print('\nA Sorted: ', sorted(A))