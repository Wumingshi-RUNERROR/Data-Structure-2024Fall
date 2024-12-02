class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ------------------------------- queue methods -------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def __str__(self):
        result = []
        curNode = self._head
        while curNode is not None:
            result.append(str(curNode._element) + " --> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


class Tree:
    class TreeNode:
        def __init__(self, element, parent=None, left=None, right=None):
            self._parent = parent
            self._element = element
            self._left = left
            self._right = right

        def __str__(self):
            return str(self._element)

    # -------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # -------------------------- public accessors ---------------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def is_root(self, node):
        """Return True if a given node represents the root of the tree."""
        return self._root == node

    def is_leaf(self, node):
        """Return True if a given node does not have any children."""
        return self.num_children(node) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for node in self.nodes():
            yield node._element

    def nodes(self):
        """Generate an iteration of the tree's nodes."""
        return self.preorder()

    def preorder(self):
        """Generate a preorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_preorder(self._root):
                yield node

    def _subtree_preorder(self, node):
        """Generate a preorder iteration of nodes in subtree rooted at node."""
        yield node
        for c in self.children(node):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """Generate a postorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_postorder(self._root):
                yield node

    def _subtree_postorder(self, node):
        """Generate a postorder iteration of nodes in subtree rooted at node."""
        for c in self.children(node):
            for other in self._subtree_postorder(c):
                yield other
        yield node

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for node in self._subtree_inorder(self._root):
                yield node

    def _subtree_inorder(self, node):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if node._left is not None:
            for other in self._subtree_inorder(node._left):
                yield other
        yield node
        if node._right is not None:
            for other in self._subtree_inorder(node._right):
                yield other

    def breadthfirst(self):
        """Generate a breadth-first iteration of the nodes of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self._root)
            while not fringe.is_empty():
                node = fringe.dequeue()
                yield node
                for c in self.children(node):
                    fringe.enqueue(c)

    def root(self):
        """Return the root of the tree (or None if tree is empty)."""
        return self._root

    def parent(self, node):
        """Return node's parent (or None if node is the root)."""
        return node._parent

    def left(self, node):
        """Return node's left child (or None if no left child)."""
        return node._left

    def right(self, node):
        """Return node's right child (or None if no right child)."""
        return node._right

    def children(self, node):
        """Generate an iteration of nodes representing node's children."""
        if node._left is not None:
            yield node._left
        if node._right is not None:
            yield node._right

    def num_children(self, node):
        """Return the number of children of a given node."""
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def sibling(self, node):
        """Return a node representing given node's sibling (or None if no sibling)."""
        parent = node._parent
        if parent is None:
            return None
        else:
            if node == parent._left:
                return parent._right
            else:
                return parent._left

    # -------------------------- nonpublic mutators --------------------------

    def add_root(self, e):
        """Place element e at the root of an empty tree and return the root node.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self.TreeNode(e)
        return self._root

    def add_left(self, node, e):
        """Create a new left child for a given node, storing element e in the new node.
        Return the new node.
        Raise ValueError if node already has a left child.
        """
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self.TreeNode(e, node)
        return node._left

    def add_right(self, node, e):
        """Create a new right child for a given node, storing element e in the new node.
        Return the new node.
        Raise ValueError if node already has a right child.
        """
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self.TreeNode(e, node)
        return node._right

    def _replace(self, node, e):
        """Replace the element at given node with e, and return the old element."""
        old = node._element
        node._element = e
        return old

    def _delete(self, node):
        """Delete the given node, and replace it with its child, if any.
        Return the element that had been stored at the given node.
        Raise ValueError if node has two children.
        """
        if self.num_children(node) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        return node._element

    def _attach(self, node, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external node.
        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if node already has a child. (This operation requires a leaf node!)
        """
        if not self.is_leaf(node):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def preorderPrint(self, node):
        if node is None:
            return
        for each in self._subtree_preorder(node):
            print(each._element, end=" ")

    def postorderPrint(self, node):
        if node is None:
            return
        for each in self._subtree_postorder(node):
            print(each._element, end=" ")

    def inorderPrint(self, node):
        if node is None:
            return
        for each in self._subtree_inorder(node):
            print(each._element, end=" ")

    def levelorderPrint(self, node):
        queue = LinkedQueue()
        queue.enqueue(node)
        while not queue.is_empty():
            next_node = queue.dequeue()
            print(next_node._element, end=" ")
            if next_node._left:
                queue.enqueue(next_node._left)
            if next_node._right:
                queue.enqueue(next_node._right)

    def height(self, node=None):
        """Return the height of the subtree rooted at a given node.
        If node is None, return the height of the entire tree.
        """
        if node is None:
            node = self._root
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(node))

    def depth(self, node):
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(node._parent)

    def return_max(self):
        maximum = self._root._element
        for each in self:
            if each > maximum:
                maximum = each
        return maximum

    def flip_node(self, node):
        node._left, node._right = node._right, node._left

    def flip_tree(self, node=None):
        if node is None:
            node = self._root
        node._left, node._right = node._right, node._left
        if node._left:
            self.flip_tree(node._left)
        if node._right:
            self.flip_tree(node._right)

    # ------------------------------- your methods -------------------------------

    def is_isomorphic(self, other):
        # Please write your code here
        def recur(node1,node2):
            if node1 is None and node2 is None:
                return True
            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            if node1._element != node2._element:
                return False
            
            if (recur(node1._left,node2._right) and recur(node1._right,node2._left)) or (recur(node1._left,node2._left) and recur(node1._right,node2._right)):
                return True
            else:
                return False
        return recur(self._root,other._root)


def main():
    t1 = Tree()
    a = t1.add_root(1)
    b = t1.add_left(a, 3)
    c = t1.add_right(a, 2)
    d = t1.add_left(b, 4)

    t2 = Tree()
    a = t2.add_root(1)
    b = t2.add_left(a, 3)
    c = t2.add_right(a, 2)
    d = t2.add_left(b, 4)

    t2.flip_node(a)

    print(t1.is_isomorphic(t2))  # should print True


if __name__ == '__main__':
    main()