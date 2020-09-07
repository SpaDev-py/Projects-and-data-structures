import random

class Point():
    def __init__(self, x, y):         #self describes the object itself being created
        
        self.x = 'input1'   #this method allows the vars x and y to accept and store data. input1 & 2 are allowed to be stored in the obj self itself in the props of x & y
        self.y = 'input2'
        
p = Point(6,3)          #the data being stored

print(p.x)      
print(p.y)

print()
print()

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True         #else part
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    
flight = Flight(3)
    
people = ['Harry', 'Ron', 'Hermione','draco']
for person in people:
    success = flight.add_passenger(person)
    
    if success:     #or delete the success statmnt above then type if flight.add_messenger(person) here instead
        print(f'Added {person} to flight successfully')
        
    else:
        print(f'No available seats for {person}')

print()
print()
#The coin class

class Pound():
    
    def __init__(self, rare = False):
        
        self.rare = rare
        if self.rare:
             self.value = 1.25
        else:
            self.value = 1.00
            
        self.color = 'gold'
        self.num_edge = 1
        self.diameter = 22.7 #mm
        self.thickness = 3.3 #mm
        self.heads = True
        
    def rust(self):
        self.color = 'greenish'
    
    def clean(self):
        self.color = 'gold'
        
    def flip(self):
        heads_options = [True, False]
        choices = random.choice(heads_options)
        self.heads = choices
    
    def __del__(self):
        print('coin spent')
        
coin1 = Pound(rare = True)

print(coin1.color)
coin1.rust()
print(coin1.color)
print(coin1.heads)
coin1.flip()
print(coin1.heads)
print(coin1.value)
del coin1