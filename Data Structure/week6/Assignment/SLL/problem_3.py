class SingleLinkedList:
    class Node:
        def __init__(self, element=None, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insertAtFirst(self, e):
        newNode = self.Node(e, self._head)
        self._head = newNode
        self._size += 1

    def deleteFirst(self):
        if self.is_empty():
            raise Exception('LinkedList is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def deleteLast(self):
        if self.is_empty():
            raise Exception('LinkedList is empty')
        prv = None
        cur = self._head
        while cur._next is not None:
            cur = cur._next
            prv = prv._next if prv is not None else self._head
        if prv is None:
            self._head = None
        else:
            prv._next = None
        self._size -= 1
        return cur._element

    def unOrderedSearch(self, target):
        currNode = self._head
        while currNode is not None and currNode._element != target:
            currNode = currNode._next
        return currNode is not None

    def __str__(self):
        result = "Head-->"
        currNode = self._head
        while currNode is not None:
            result += str(currNode._element) + "-->"
            currNode = currNode._next
        return result + "None"

    def sortList(self):
        # Please write your code here
        if self.is_empty():
            return
        def merge(start,size):
            if size==1:
                return start,size,start._next
            start1,size1,end1=merge(start,size//2)
            start2,size2,end2=merge(end1,size-size//2)
            p1=1
            p2=1
            if start1._element<=start2._element:
                p1+=1
                start=start1
                start1=start1._next
            else:
                p2+=1
                start=start2
                start2=start2._next
            check=start
            while p1<=size1 and p2<=size2:
                if start1._element<=start2._element:
                    p1+=1
                    check._next=start1
                    check=check._next
                    start1=start1._next
                else:
                    p2+=1
                    check._next=start2
                    check=check._next
                    start2=start2._next
            while p1<=size1:
                check._next=start1
                check=check._next
                start1=start1._next
                p1+=1
            while p2<=size2:
                check._next=start2
                check=check._next
                start2=start2._next
                p2+=1
            return start,size,end2
        answer=merge(self._head,self._size)[0]
        temp=answer
        for _ in range(self._size-1):
            temp=temp._next
        temp._next=None
        self._head=answer

def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(5)

    print(ls1)  # Should print: Head-->5-->6-->2-->3-->None
    ls1.sortList()
    print(ls1)  # Should print: Head-->2-->3-->5-->6-->None


if __name__ == "__main__":
    main()
