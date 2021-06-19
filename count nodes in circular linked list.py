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

    def count(self):
        tmp=self.start
        ch=0
        while(tmp.next!=self.start):
            ch=ch+1
            tmp=tmp.next
        print(ch+1,"nodes are present in this list.")


    def display(self):
        tmp=self.start
        while(tmp.next!=self.start):
            print(tmp.data,end="->")
            tmp=tmp.next
        print(tmp.data,end="->")
        tmp=self.start
        print(f"{tmp.data}(head node)")

list=cll()
list.create(1)
list.create(2)
list.create(3)
list.create(4)
list.create(5)
list.create(6)
list.create(7)
list.create(8)
list.create(9)
list.create(10)
list.display()
list.count()

