class Node:
    def __init__(self,data):
        self.data = data
        self.refa = None

class LL:
    def __init__(self):
        self.head= None

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.refa

    def addstart(self,new_data):
        new_node= Node(new_data)
        new_node.refa=self.head
        self.head=new_node

    def delstart(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head=self.head.refa

    def addend(self,nedta):
        new_node=Node(nedta)
        if self.head is None:
            self.head=new_node
        else:
            while self.head.refa is not None:
                self.head=self.head.refa
            self.head.refa=new_node

    def delend(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n.refa.refa is not None:
                n=n.refa
            n.refa=None

    def addafter(self,predata,newdata):
        new_node= Node(newdata)
        n= self.head
        while n.refa is not None:
            if n.data==predata:
                break
            n=n.refa
        if n.refa is None:
            print("node is not present")
        else:
            new_node.refa=n.refa
            n.refa=new_node

    def delafter(self,predata):
        n = self.head
        while n.refa is not None:
            if n.data == predata:
                break
            n = n.refa
        if n.refa is None:
            print("node is not present")
        else:
            n.refa = n.refa.refa


    def adbefore(self,predata,newdata):
            new_node= Node(newdata)
            n= self.head
            while n.refa is not None:
                if n.refa.data==predata:
                    break
                n=n.refa
            if n.refa is None:
                print("node is not present")
            else:
                new_node.refa=n.refa
                n.refa=new_node

 # def delbefore(self,predata):
#   this is not possible by singly linked list

    def reversell(self):
        pre=None
        while self.head:
            curr=self.head.refa
            self.head.refa=pre
            pre=self.head
            self.head=curr
        self.head=pre

ll=LL()
ll.addstart(9696)
ll.addend(400)
ll.addstart(433)
ll.addstart(4494)
ll.addafter(433,500)
ll.adbefore(500,400)
ll.print_LL()
print('\n')
# ll.delend()
# ll.print_LL()
# print('\n')
# ll.delstart()
# ll.print_LL()
# print('\n')
# ll.delafter(400)
# ll.print_LL()
# print('\n')
ll.reversell()
ll.print_LL()
print('\n')
