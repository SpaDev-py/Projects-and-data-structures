#Linked Lists

#A node basically contains a data and a next(pointer)
class Node:     #create a node class

    def __init__(self, data):   #a constructor for the class, takes in just 1 arg.
        self.data = data
        self.next = None        #next is only a symbol for a pointer that points to the next data more like an iterator or a differentiator


#A linked list contains a head 
class Linkedlist:   #linkedlist || wrapper class

    def __init__(self):
        self.head = None    #head of the ll

    def insert(self, newNode):  #insert function for adding data to the ll
        
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
        while True:
            if currentNode is None: #if the currentnode has no more data the loop ends and breaks
                break
            print(currentNode.data)     #print the data in the current list(being the head/top of the list)
            currentNode = currentNode.next  #then move to the next data



firstNode = Node('babbs')
linkedList = Linkedlist()
linkedList.insert(firstNode)

secondNode = Node('Spades')
linkedList.insert(secondNode)

linkedList.printList()






























        
