class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class cll:
    def __init__(self):
        self.start=None

    def create(self,data):
        newnode = node(data)
        if (self.start == None):
            self.start = newnode
            newnode.next=self.start
        else:
            tmp=self.start
            while(tmp.next!=self.start):
                tmp=tmp.next
            tmp.next=newnode
            newnode.next=self.start

    def swap(self):
        tmp=self.start
        first=self.start
        while(tmp.next!=self.start):
            tmp=tmp.next
        last=tmp.data
        tmp.data=first.data
        tmp=self.start
        tmp.data=last

    def display(self):
        tmp=self.start
        while(tmp.next!=self.start):
            print(tmp.data,end="->")
            tmp=tmp.next
        print(tmp.data,end="->")
        tmp=self.start
        print(f"{tmp.data}(head node)")

list=cll()
list.create(10)
list.create(2)
list.create(3)
list.create(4)
list.create(5)
list.create(6)
list.create(7)
list.create(8)
list.create(9)
list.create(1)
list.display()
list.swap()
list.display()
