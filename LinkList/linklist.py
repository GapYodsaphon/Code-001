"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

* MyLinkedList() Initializes the MyLinkedList object.
* int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
* void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
* void addAtTail(int val) Append a node of value val as the last element of the linked list.
* void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
* void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.nextptr = None
   
class MyLinkedList:
    
    def __init__(self):
        self.head = None    
        self.count=0
    
    def get(self, index: int) -> int:
    
        if self.count>index:
            curr = self.head
            for i in range(index):
                curr =curr.nextptr
            return curr.val
            
        if self.count<=0:
            return -1
        else:
            return -1



    def addAtHead(self, val: int) -> None:
        if self.count ==0:
            node = Node(val)
            self.head=node
            node.nextptr = None
        else:
            node = Node(val)
            node.nextptr = self.head
            self.head=node 

        self.count+=1
        
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.count ==0:
            self.head = node
        
        
        curr = self.head
        
        for i in range(self.count-1):
            curr = curr.nextptr
        curr.nextptr=node
        node.nextptr=None
        
        self.count+=1   
    def addAtIndex(self, index: int, val: int) -> None:
        if index <=self.count:
            node = Node(val)        
            print(self.count)
            if self.count==0:
                self.head = node
            if index ==0:
                node.nextptr=self.head
                self.head=node
                
            elif index <=self.count:

                curr =self.head
                index = index-1
                # print("ADD in INDEX :",index)
                for i in range(self.count):
                    
                    if i>=0:
                        if i-1 == index-1:
                            before_addr = curr.nextptr
                            curr.nextptr=node
                            
                        if i == index:
                            node.nextptr=before_addr
                        curr = curr.nextptr
                        
            self.count+=1    

    def deleteAtIndex(self, index: int) -> None:
        
        if self.count >=0:
            if self.count >index:
                curr = self.head
            # set index
                index = index-1
                if index>=0:
                    for i in range(self.count):
                        #before addr
                        if i-1 == index-1:
                            before_address = curr
                        curr = curr.nextptr
                    #after addr
                        
                        if i == index+1:
                            after_address = curr
                    #link before after
                    if(self.count>2):
                        before_address.nextptr=after_address
                if index ==-1:
                    curr = self.head
                    for i in range(1):
                        curr = curr.nextptr
                    self.head =curr
                self.count-=1
        

    
    def show_linklist(self):
        curr = self.head
        print("Total",self.count)
        for i in range(self.count):
            if i == (self.count-1):
                print("(",curr.val,")")
            else:
                print("(",curr.val,")","--> ",end="")
            curr = curr.nextptr

#Test Case
"""
["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
[[],[0,10],[0,20],[1,30],[0]]

# """
