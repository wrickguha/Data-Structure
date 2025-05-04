class Node:
    def __init__(self,data= None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print(lstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count =0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next 
                break
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index ==0:
            self.insert_at_begining(data)
            return
        count =0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll= Linked_List()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(79)
    ll.insert_at_end(9)
    ll.insert_values(['banana','mango','grapes','orange'])
    ll.print()
    ll.remove_at(2)
    print("Length: ",ll.get_length())
    ll.insert_at(0,'figs')
    ll.insert_at(2,'guava')

    ll.print()