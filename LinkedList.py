class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            node = Node(data, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, None)
            self.tail.next = node
            self.tail = node

    def insertat(self, loc, data):
        node = Node(data, None)
        itr = self.head
        count = 0
        while itr:
            if count == loc-1:
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
            count+=1

    def getlen(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count

    def delete(self, loc):
        if loc<0 and loc>self.getlen():
            raise Exception("Invalid Index")
        if loc == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == loc-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def traverse(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr +=str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


ll = LinkedList()

ll.insert(25)
ll.insert(235)
ll.insert(55)
ll.insert(35)

ll.traverse()
print(ll.getlen())
ll.insertat(2, 68)
ll.traverse()
ll.delete(1)
print(ll.tail.data)
ll.traverse()
print(ll.getlen())