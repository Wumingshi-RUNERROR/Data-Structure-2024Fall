class DoubleLinkedList:
    class Node:
        def __init__(self, element = None, prev = None, next = None):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = DoubleLinkedList.Node(None, None, None)
        self._trailer = DoubleLinkedList.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = DoubleLinkedList.Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        result = "Header<-->"
        currNode = self._header._next
        while currNode is not self._trailer:
            result += str(currNode._element) + "<-->"
            currNode = currNode._next
        return result + "Trailer"

    def rotate(self, n):
        # Please write your code here
        n%=self._size
        if n<=0:
            return
        original_head=self._header._next
        original_end=self._trailer._prev
        new_head=self._trailer
        for _ in range(n):
            new_head=new_head._prev
        new_end=new_head._prev
        self._header._next=new_head
        new_head._prev=self._header
        original_end._next=original_head
        original_head._prev=original_end
        new_end._next=self._trailer
        self._trailer._prev=new_end



def main():
    ls1 = DoubleLinkedList()
    ls1._insert_between(1, ls1._header, ls1._header._next)
    ls1._insert_between(2, ls1._header, ls1._header._next)
    ls1._insert_between(3, ls1._header, ls1._header._next)
    ls1._insert_between(4, ls1._header, ls1._header._next)
    ls1._insert_between(5, ls1._header, ls1._header._next)

    print(ls1)  # Should print: Header-->1-->2-->3-->4-->5-->Trailer
    ls1.rotate(2)
    print(ls1)  # Should print: Header-->4<-->5<-->1<-->2<-->3-->Trailer


if __name__ == "__main__":
    main()
