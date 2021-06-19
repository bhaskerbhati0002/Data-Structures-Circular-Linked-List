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

    def delete(self,value):
        ch=0
        tmp=self.start
        while(tmp.next.data!=value):
            tmp=tmp.next
        tmp.next=tmp.next.next

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
list.create(8)
list.create(4)
list.create(5)
list.display()
list.delete(8)
print("link list after deletion:")
list.display()
