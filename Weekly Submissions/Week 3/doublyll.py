class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doubly_ll:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref

    def print_ll_reverse(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref

            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref

    def addd(self,data):
        n=self.head
        if n is None:
            new_node=Node(data)
            n = new_node
        else:
            print("linked list is not empty")

    def adbeg(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            n=self.head
            n.pref=new_node
            new_node.nref=n


ll=doubly_ll()
ll.addd(45)
ll.adbeg(69)
ll.adbeg(6)
ll.print_ll_reverse()


