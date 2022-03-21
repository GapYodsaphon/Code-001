


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
        if self.count<0:
            return -1
        else:
            return -1



    def addAtHead(self, val: int) -> None:

        node = Node(val)
        self.head=node
        self.count+=1
        node.nextptr = None
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        curr = self.head
        if(self.count==1):
            curr.nextptr=node
        node.nextptr=None
        self.count+=1   
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index <=self.count:

            node = Node(val)        
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
        if self.count >0:
            if self.count >index:
                curr = self.head
            # set index
                index = index-1
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
link_list = MyLinkedList()
link_list.addAtHead(1)
# link_list.show_linklist()
# link_list.addAtTail(3)
# link_list.show_linklist()
# link_list.addAtIndex(1,2)
# print(link_list.get(1))
# link_list.addAtHead(4)
# link_list.show_linklist()
link_list.deleteAtIndex(0)
# link_list.addAtIndex(1,4)
# link_list.addAtIndex(3,2)
link_list.show_linklist()

# print(link_list.get(2))


"""
["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
"""