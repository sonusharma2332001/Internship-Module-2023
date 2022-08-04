class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def addfirst(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def printl(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.next
        print("\n",self.head.next.data)
    def addlast(self,newdata):
        newnode=Node(newdata)
        n=self.head
        while n.next is not None:
            n=n.next
        n.next=newnode

    def addmiddle(self,newdata,after):
        newnode=Node(newdata)
        n=self.head
        while n.data is not after:
            n=n.next
        newnode.next=n.next
        n.next=newnode


nod=LL()
nod.addfirst(5)
nod.addfirst(7)
nod.addfirst(6)
nod.addfirst(2)
nod.addlast(10)
nod.addmiddle(1111,7)
nod.printl()
