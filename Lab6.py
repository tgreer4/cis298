#Fraction Class
#overload add, subtract, multiply, divide
import math
import copy

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numer = numerator
        self.denom = denominator

    def reduce_fraction(self):
        gcd = math.gcd(self.numer , self.denom)
        self.numer = int(self.numer / gcd) 
        self.denom = int(self.denom / gcd)
    
    #overloaded operators
    def __add__(self,value):
        if(isinstance(value,Fraction)): #check if val is Fraction instance or not
            other = copy.deepcopy(value)
        
        else: #otherwise a list with int
            other = Fraction(numerator = int(value[0]))
        
        if(self.denom == other.denom): #checks whether denom is same or not, adds the numers
            self.numer += other.numer

        else: #(a/b)+(c/d)=ad + bc / bd
            self.numer = (self.numer * other.denom) + (self.denom * other.numer)
            self.denom *= other.denom
        
        self.reduce_fraction()
        return str(self.numer) + '/' + str(self.denom)

    def __sub__(self, value):
        if(isinstance(value,Fraction)): #check if val is Fraction instance or not
            other = copy.deepcopy(value)
        
        else: #otherwise a list with int
            other = Fraction(numerator = int(value[0]))

        if(self.denom == other.denom): #checks whether denom is same or not, subtracts the numerators
            self.numer -= other.numer

        else:  #a/b - c/d = ((a*d) - (b*c)) / (b * d)
            self.numer = (self.numer * other.denom) - (self.denom * other.numer)
            self.denom *= other.denom

        self.reduce_fraction()
        return (str(self.numer) + '/' + str(self.denom))

    def __mul__(self, value): #a/b * c/d = (a*d) / (b*c)
        if(isinstance(value,Fraction)): #check if val is Fraction instance or not
            other = copy.deepcopy(value)

        else: #otherwise a list with int
            other = Fraction(numerator = int(value[0]))

        self.numer *= other.numer
        self.denom *= other.denom

        self.reduce_fraction()
        return (str(self.numer) + '/' + str(self.denom))

    def __truediv__(self, value): #a/b / c/d = a/b * d/c
        if(isinstance(value,Fraction)): #check if val is Fraction instance or not
            other = copy.deepcopy(value)

        else: #otherwise a list with int
            other = Fraction(numerator = int(value[0]))
        
        temp_var = other.numer #flip other fraction
        other.numer = other.denom
        other.denom = temp_var

        self * other

        self.reduce_fraction()
        return (str(self.numer) + '/' + str(self.denom))
        
def valid_input(input): #determines if input is valid
    divis_count = input.count('/') #finds num of /
    
    if(divis_count == 1 ): 
        val = input.split('/') #return list of input
        return(all(i.isdigit() for i in val), val) #returns a tuple
    
    elif(divis_count == 0):
        return(input.isdigit(), input)
    
    else:
        return False

decision = input("Enter whether you would like to  add(a), substract(s), multiply(m), divide(d), or quit (q): ").lower()
while(decision in ['a', 's', 'm', 'd']):
    try:
        user_input = input("Enter in a fraction. No decimals.: ")
        valid, x = valid_input(user_input) #returns tuple of valid input and input as list
        if(valid ==  False):
            raise ValueError('Input is not a fraction or integer.')
        my_fraction = Fraction(numerator = int(x[0]), denominator = int(x[1])) #left val is always a Fraction
       
        user_input2 = input("Enter in another fraction or integer. No decimals.: ")
        valid, x = valid_input(user_input2) #returns tuple of valid input and input as list
        if(valid ==  False):
            raise ValueError('Input is not a fraction or integer.')
        
        if(len(x) > 1):
            my_fraction2 = Fraction(int(x[0]), int(x[1]))
        else:
            my_fraction2 = x

        if decision == 'a':     #operations loop
            print("{ui1} + {ui2} = {total}".format(ui1=user_input, ui2=user_input2, total = my_fraction + my_fraction2))

        elif decision == 's':
            print("{ui1} - {ui2} = {total}".format(ui1=user_input, ui2=user_input2, total = my_fraction - my_fraction2))

        elif decision == 'm':
            print("{ui1} * {ui2} = {total}".format(ui1=user_input, ui2=user_input2, total = my_fraction * my_fraction2))

        else: 
            print("{ui1} / {ui2} = {total}".format(ui1=user_input, ui2=user_input2, total = my_fraction / my_fraction2))

    except ValueError as except_val:
        print(except_val, "Invaild input, try again.")
    
    decision = input("Enter whether you would like to  add(a), substract(s), multiply(m), divide(d), or quit (q)\n").lower()

print("The user has decided to quit.")