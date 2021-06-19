class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class cll:
    def __init__(self):
        self.start=None

    def create(self, data):
        newnode = node(data)
        if (self.start == None):
            self.start = newnode
            newnode.next = self.start
        else:
            tmp=self.start
            while (tmp.next != self.start):
                tmp = tmp.next
            tmp.next = newnode
            newnode.next = self.start

    def check(self): #### you can also check by putting this funtion in any not circular linked list
        tmp=self.start
        if tmp==None:
            print("list is circular.")
        else:
            tmp=self.start
            while True:
                if (tmp.next==None):
                    print("list is not circular.")
                    break
                if (tmp.next==self.start):
                    print("list is circular.")
                    break
                tmp=tmp.next

    def display(self):
        tmp=self.start
        while(tmp.next!=self.start):
            print(tmp.data,end="->")
            tmp=tmp.next
        print(tmp.data,end="->")
        tmp=self.start
        print(f"{tmp.data}(head node)")


list=cll()
list.check()
list.create(1)
list.create(2)
list.create(3)
list.create(4)
list.create(5)
list.display()
list.check()




