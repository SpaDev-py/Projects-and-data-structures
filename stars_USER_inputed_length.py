
def diamond():
    length = int(input('Enter the length of the star: '))
    
    def dia_up():
        hashs = '*'
        hashes_times = 1
        spaces = ' '
        spaces_times = length
        
        for i in range(length):
            print(spaces * spaces_times, hashs * hashes_times)
            hashes_times += 2
            spaces_times -= 1
            
            
    def dia_down():
        hashes = '*'
        hashes_times = (length * 2) + 1 #the down part starts with 21 stars but could use 20 and then change the space_times value to = 1
        
        spaces = ' '
        spaces_times = 0    #used zero so no any space is created from the down part
        
        for i in range(length + 1): #added 1 so it allows the display of the last star when it decrements down to 1. it doesnt print it when the iteration repeatition is same as the length
            print(spaces_times * spaces, hashes * hashes_times)
            spaces_times += 1
            hashes_times -= 2
            
            
    dia_up()
    dia_down()
    print()
    print()
    exit = input('do you want to exit?(y/n): ').lower()
    if exit == 'n':
        diamond()
        
diamond()

    

        
        
