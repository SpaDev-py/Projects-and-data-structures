#Hash Tables        

class HashTables:   #creates the class Hash Table
    def __init__(self):
        self.MAX = 10   #size of memory space to be used
        self.arr = [None for i in range(self.MAX)]  #an array of size of the previous length and None assigned to all the array elements
        
    def get_hash(self, key):    #Hash table values are stored in the RAM as string indexes, the string characters are converted to their acii codes and then MOD Per the mem. size, the MOD is the memory index location to store the string value
        h = 0

        if isinstance(key, int):    # checks if the key is an integer 
            key = str(key)  # then converts it to strings because integers cannot be hashed

        for char in key:
            h += ord(char)
        return h % self.MAX 
    
    def set_item(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        
    def get_item(self, key):
        h = self.get_hash(key)
        return self.arr[h]
        
    def __setitem__(self, key, val):    #function to add a key and its value into the arr
        h = self.get_hash(key)  #gets the ascii of the key for mem storage
        self.arr[h] = val       #sets the arr at that ascii to its corresponding value
        
    def __getitem__(self, key): #retrieve the passed in key
        h = self.get_hash(key)  #converts/gets the ascii AKA mem location of that key and locates it 
        return self.arr[h]      #returns the located corresponding value
    
    def __delitem__(self, key):   #deletion funciton that accepts the key to be located
        h = self.get_hash(key)   #gets the ascii code of that key
        self.arr[h] = None      #it doesnt directly delete it only sets it to None
        

t = HashTables()    #create object of the hash class to be used

t['march 9'] = 130
t['April 4'] = 'spades'

print(t.arr)
del t['march 9']
print()
print(t.arr)
print()

t[4] = 'midas'
print(t.arr)


# Hash table (dictionary) has inbuilt functions like;
# __delitem__
# __setitem__
# __getitem__
