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

    def isPalindrome(self):
        # Please write your code here
        def helper(right, length):
            if length == 0:
                return (True, right)
            if length == 1:
                return (True, right._next)
            is_pal, next_node = helper(right._next, length - 2)
            if not is_pal or next_node is None:
                return (False, next_node)
            is_pal = (right._element == next_node._element)
            return (is_pal, next_node._next)
        
        if self.is_empty():
            return True
        return helper(self._head, self._size)[0]
            



def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(1)

    print(ls1)  # Should print: Head-->1-->2-->2-->1-->None
    print(ls1.isPalindrome())  # Should print: True


if __name__ == "__main__":
    main()
