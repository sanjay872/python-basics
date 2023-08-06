class Element:

    def __init__(self,value):
        self.prev=None
        self.value=value
        self.next=None

class DoubleLinkedList:
    
    def __init__(self,head=None):
        self.head=head
        if self.head:
            self.length=1
        else:
            self.length=0
    
    def append(self,newElement):
        curElement=self.head
        if curElement:
            while curElement.next:
                curElement=curElement.next
            curElement.next=newElement
            newElement.prev=curElement
        else:
            self.head.next=newElement
            newElement.prev=self.head
        self.length+=1

    def insert(self,newElement,pos):
        curElement=self.head
        prevElement=curElement.prev
        if pos>=1 and pos<=self.length:
            if curElement:
                curPos=1
                while curPos<pos:
                    prevElement=curElement
                    curElement=curElement.next
                    curPos+=1
                if prevElement:
                    prevElement.next=newElement
                    newElement.prev=prevElement
                    newElement.next=curElement
                else:
                    self.head=newElement
                    newElement.next=curElement
                    curElement.prev=newElement
                self.length+=1
            else:
                print("List Empty")
        else:
            print("Invalid Position!")
    
    def delete(self,value):
        curElement=self.head
        prevElement=curElement.prev
        if curElement:
            while curElement and curElement.value!=value:
                prevElement=curElement
                curElement=curElement.next    
            if prevElement:
                if curElement:
                    if curElement.next:
                        prevElement.next=curElement.next
                        curElement.next.prev=curElement.prev
                        curElement.prev=None
                        curElement.next=None
                    else:
                        prevElement.next=None
                        curElement.prev=None
                    self.length-=1
                else:
                    print("Element not found")   
            else:    
                self.head=curElement.next
                self.head.prev=None
                self.length-=1
        else:
            print("No elements in List")
    
    def get_position(self,value):
        curElement=self.head
        if curElement:
            curPos=1
            while curElement and curElement.value!=value:
                curElement=curElement.next
                curPos+=1
            if curElement:
                return curPos
        return None
        
    def update(self,newValue,pos):
        curElement=self.head
        curPos=1
        if curElement:
            if pos>=1 and pos<=self.length:
                while curElement and curPos<pos:
                    curElement=curElement.next
                    curPos+=1
                curElement.value=newValue
            else:
                print("Invalid position")
        else:
            print("No Elements in the list")

    def extend(self,list2):
        curElement=self.head
        if curElement:
            while curElement.next:
                curElement=curElement.next
            if list2.head:
                curElement.next=list2.head
                self.length+=list2.size()
            else:
                print("No in element in given list")    
        else:
            print("No in element in current list")

    def display(self):
        curElement=self.head
        if curElement:
            while curElement:
                print(curElement.value,end=" ")
                curElement=curElement.next
            print("",end="\n")
        else:
            print("No Elements!")

    def size(self):
        return self.length
    
    def clean(self):
        self.head=None

e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)

linkedList=DoubleLinkedList(e1) #added 1
linkedList.append(e2) #added 2

linkedList.display() # display 1 2

print(linkedList.size()) # length is 2

linkedList.insert(e3,1) # changed to 3 1 2
linkedList.insert(e4,3) # changed to 3 1 4 2
linkedList.insert(e5,2) # changed to 3 5 1 4 2
#linkedList.insert(e1,7) # invalid position

#linkedList.clean()
#linkedList.insert(e1,2) # No Element in the list

linkedList.display() # display 3 5 1 4 2

linkedList.delete(3) # changed to 5 1 4 2
linkedList.delete(4) # changed to 5 1 2
linkedList.delete(2) # changed to 5 1
#linkedList.delete(6) # Element not found

print(linkedList.size()) # prints 2

linkedList.display() # display 5 1

linkedList2=DoubleLinkedList(Element(10))
linkedList2.append(Element(20))

linkedList.extend(linkedList2)
print(linkedList.size()) # prints 4
linkedList.display() # displays 5 1 10 20

print(linkedList.get_position(5)) # returns 1
print(linkedList.get_position(1)) # returns 2
print(linkedList.get_position(10)) # returns 4

linkedList.update(1,1) # changed to 1 1 10 20
linkedList.update(2,2) # changed to 1 2 10 20
linkedList.update(3,3) # changed to 1 2 3 20
linkedList.update(4,4) # changed to 1 2 3 4

linkedList.display() # displays 1 2 3 4