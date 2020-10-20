#Linked Lists

#A node basically contains a data and a next(pointer)
class Node:     #create a node class

    def __init__(self, data):   #a constructor for the class, takes in just 1 arg.
        self.data = data
        self.next = None        #next is only a symbol for a pointer that points to the next data more like an iterator or a differentiator


#A linked list contains a head 
class Linkedlist:   #linkedlist || wrapper class

    def __init__(self):
        self.head = None    #head of the linked list
        
    def listLength(self):
        currentNode = self.head
        Length = 0
        
        while currentNode is not None:
            Length += 1
            currentNode = currentNode.next
        return Length
        
    def insertHead(self, newNode):  #this fn inserts Nodes at the beginning of a list
        
        #######--alternative irrelevant method to test if the first node is empty or not & print appropriate msg--########
        
        #if self.head is None:
            #print('Head node is empty.. please assign through the "insertEnd" method')
            #self.insertEnd(newNode)
        
        #######--alternative fn to test if the first node is empty or not & print appropriate msg--########
        
        
        temporaryNode = self.head   #--> already existing node in the linked list
        self.head = newNode         #--> new Node to be inserted in the beginning
        self.head.next = temporaryNode  #--> assign the initial head node as the next node instead
        del temporaryNode               #since its being assinged through the temp Node & temp Node currently not in use, just del
        
        
    def insertAt(self, newNode, position):  #function to add node at centre of linked list
        
        #checks for an invalid position
        if position < 0 or position > self.listLength():
            print('invalid position!')
            return #---> these return statements are very signifanct to use to terminate the whole process
                    #from continuing when the condition is met!!!
        
        #checks if the position is set at the head of the list
        if position == 0:
            self.insertHead(newNode)
            return
        
        
        #to traverse through the list for the correct position of insertion, create temp vars to start from the head and a pos. count
        currentNode = self.head
        currentPosition = 0
        
        while True:
            
            #when the right position is met, the pointer of the previous Node points to the new Node then newNode points to 
            #the current Node being the head
            if currentPosition == position:
                previousNode.next = newNode #previousNode is Node on the left of the newly node
                newNode.next = currentNode  #currentNode is Node on the right
                break
            previousNode = currentNode  #previousNode is created to store the value of a current node during traversal to not lose it
            currentNode = currentNode.next  #traversal--> moves to the next node
            currentPosition += 1    #traversal --> position controls the change in position during traversal
            
            
    def insertEnd(self, newNode):  #function inserts nodes at the end of a the linked list
        
        if self.head is None:   #before added, need to check if the head of the ll is empty
            self.head = newNode     # if its not assign a newNode as the head if the head is empty. Either the newNode is the head or the last node is the head
        else:
            lastNode = self.head    #if the head is not none then the last node should be the head
            
            #the above assignment is just to traverse the list starting from the top of the list(self.head) 
            #to arrive at the last node on the list we create a loop(lastNode.next), if it is empty it breaks out but if not then
            #assign then it traverses until the last node. if the condition is satisfied the loop breaks and assign that lastNode.next as the newNode
            
            
            
            while True:
                if lastNode.next is None:   #just giving a condition if the lastNode.next is empty then break  out of the loop
                    break   
                lastNode = lastNode.next    #else assign the lastNode as the nextNode. it keeps iterating through any added node
            lastNode.next = newNode

    def printList(self):
        
        currentNode = self.head     #set a currentNode var to the first node on the list
        if self.head is None:   #if the linked list is empty it prints the statement & returns to the begining of the prog
            print("List is empty")
            return 
        
        while True:
            if currentNode is None: #if the currentnode has no more data the loop ends and breaks
                break
            print(currentNode.data, '-->', end=' ')     #print the data in the current list(being the head/top of the list)
            #without the data part it only prints the memory location of the data
            currentNode = currentNode.next  #then move to the next data


firstNode = Node(10)
linkedList = Linkedlist()
linkedList.insertEnd(firstNode)

secondNode = Node(20)
linkedList.insertEnd(secondNode)

thirdNode = Node(15)
linkedList.insertAt(thirdNode, 1)

linkedList.printList()






























        
