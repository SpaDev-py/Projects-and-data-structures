# This is a fraction operation algorithms that solves basic fraction arithmetics.



# Greatest common divisor : Greatest common divisor between two integers m and n is n if n divides m evenly. However if it doesn't
# then the answer is the greatest common divisor of n and the remainder of m divided n.

#  this is the euclid's algorithms for finding the greatest common divisor

def gcd(m,n):
    while m % n != 0:
        old_m = m 
        old_n = n 
        
        m = old_n
        n = old_m % old_n
    return n 

# Fraction class
# Hints: num => numerator, den => denomenator, seme and uke are just japaneese translations for top and bottom, respectively.. because why not :)
class Fractions:
    
    def __init__(self, seme, uke):  # The constructor that creates objects of this fraction class
        
        # Using a test statement to check if the objects(num and den) are both integers else it raises a TyperError
        if isinstance(seme, int) and isinstance(uke, int):
            self.num = abs(seme)    # The absolute value function converts any negative inputed int to a positive one to avoid error in calculations.
            self.den = abs(uke) 
            
            common = gcd(self.num, self.den)
            self.num = self.num // common
            self.den = self.den // common
        else:
            raise TypeError('Not an integer')
    
    # <-----------------This part is a modified constructor that already converts the fractions to their lowest forms right from the start---->
    
        # self.num = seme
        # self.den = uke
        
        # common = gcd(self.num, self.den)
        # self.num = self.num // common
        # self.den = self.den // common
        
        
    # After these then delete all the gcd (common) parts in the operator functions 
    # <-----------------This part is a modified constructor that already converts the fractions to their lowest forms right from the start---->
    
    
    def  showFrac(self):  # Just a method that prints the values of the created fraction objects
        print(self.num, '/', self.den)
    
    def __str__(self):  # Another method that prints the values of the created fractions objects but in the forms of strings
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other_fraction):  # Modifying the python addition operator to successfully add two fractions
        
        # This current step modifies the fraction in a way it might be solved on a piece of paper---- try writing it out using real digits
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        
        # This step implements the use of the euclid's algorithm to find the greatest common divisor (gcd) between two fractions.
        common = gcd(new_num, new_den)
        
        # divide both the num and den by the gcd (using the floor division //. or int division)
        return Fractions(new_num // common, new_den // common)
    
   
    
    def __sub__(self, other):   # Modify the subtract operator
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        
        common = gcd(new_num, new_den)
        
        return Fractions(new_num // common, new_den // common)
    
    # There are two types of division in python; True and floor division: True(/); returns the div in float point while floor(//) return in int form.
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        
        common = gcd(new_num, new_den)
        
        return Fractions(new_num // common, new_den // common)
    
    def __mul__(self, other):   # Modify the multiplication operator
        new_num = self.num * other.num
        new_den = self.den * other.den
        
        common = gcd(new_num, new_den)
        
        return Fractions(new_num // common, new_den // common)
    
    def __gt__(self, other):    # The greater than operator
        if self.num / self.den > other.num / other.den:
            return 'Yup it\'s greater than'
        else:
            return 'Nope it\'s not greater than'
        
    def __lt__(self, other):    # The less than operator
        if self.num / self.den < other.num / other.den:
            return 'Yup it\'s less than'
        else:
            return 'it\'s not less than'
    
    def __le__(self, other):    # The less than or equal to
        if self.num / self.den <= other.num / other.den:
            return 'Yup it\'s less than or equal to'
        else:
            return 'Naw it\'s not less than or equal to'
        
    def __ge__(self, other):    # The greater than or equal to
        if self.num / self.den >= other.num / other.den:
            return 'yup it\'s greater than or equal to'
        else:
            return 'Naw it\'s not greater than or equal to'
        
    def __eq__(self, other):    # The equality operator for testing
        if self.num/self.den == other:
           return 'Yup it\'s equal to'
        else:
            return 'Nope it\'s not equal to'
        
    def get_Num(self):  # A function that prints the numerator part of the fraction
        print(self.num)
    
    def get_Den(self):  # A function that prints the denomenator part of the fraction
        print(self.den)

    
    
        
        
    
    
frac1 = Fractions(-1,'3') # Creating objects of the fracitons class
frac2 = Fractions(1,2)
frac1.showFrac()

print()
print()

print(frac1)

print()
print()

frac3 = frac1 + frac2
print(frac3)

print(frac1 == frac2)

print()
print()

print(frac1 / frac2)