class Empty(Exception):
    def __init__(self, msg):
        self.msg = msg

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

class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    """You should not modify this class."""

    #------------------------------ nested _Item class ------------------------------
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key    # compare items based on their keys

        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)

    #------------------------------ public behaviors ------------------------------
    def is_empty(self):                  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def __len__(self):
        """Return the number of items in the priority queue."""
        raise NotImplementedError('must be implemented by subclass')


class Tree:
    """You should not modify this class."""
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
        for node in self.nodes():  # use same order as nodes()
            yield node._element  # but yield each element

    def depth(self, node):
        """Return the number of levels separating a given node from the root."""
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    def _height2(self, node):  # time is linear in size of subtree
        """Return the height of the subtree rooted at the given node."""
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(node))

    def height(self, node=None):
        """Return the height of the subtree rooted at a given node.

        If node is None, return the height of the entire tree.
        """
        if node is None:
            node = self._root
        return self._height2(node)  # start _height2 recursion

    def nodes(self):
        """Generate an iteration of the tree's nodes."""
        return self.preorder()  # return entire preorder iteration

    def preorder(self):
        """Generate a preorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_preorder(self._root):  # start recursion
                yield node

    def _subtree_preorder(self, node):
        """Generate a preorder iteration of nodes in subtree rooted at node."""
        yield node  # visit node before its subtrees
        for c in self.children(node):  # for each child c
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self):
        """Generate a postorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_postorder(self._root):  # start recursion
                yield node

    def _subtree_postorder(self, node):
        """Generate a postorder iteration of nodes in subtree rooted at node."""
        for c in self.children(node):  # for each child c
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other  # yielding each to our caller
        yield node  # visit node after its subtrees

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for node in self._subtree_inorder(self._root):
                yield node

    def _subtree_inorder(self, node):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if node._left is not None:  # if left child exists, traverse its subtree
            for other in self._subtree_inorder(node._left):
                yield other
        yield node  # visit p between its subtrees
        if node._right is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(node._right):
                yield other

    def breadthfirst(self):
        """Generate a breadth-first iteration of the nodes of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()  # known nodes not yet yielded
            fringe.enqueue(self._root)  # starting with the root
            while not fringe.is_empty():
                node = fringe.dequeue()  # remove from front of the queue
                yield node  # report this node
                for c in self.children(node):
                    fringe.enqueue(c)  # add children to back of queue

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
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def sibling(self, node):
        """Return a node representing given node's sibling (or None if no sibling)."""
        parent = node._parent
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if node == parent._left:
                return parent._right  # possibly None
            else:
                return parent._left  # possibly None

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
        node._left = self.TreeNode(e, node)  # node is its parent
        return node._left

    def add_right(self, node, e):
        """Create a new right child for a given node, storing element e in the new node.

        Return the new node.
        Raise ValueError if node already has a right child.
        """
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self.TreeNode(e, node)  # node is its parent
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
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
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
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():  # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # set t2 instance to empty
            t2._size = 0


def pretty_print(tree):
    if tree.is_empty():
        return print("Levels: 0")
    levels = tree.height() + 1
    print("Levels:", levels)
    print_internal([tree._root], 1, levels)


def print_internal(this_level_nodes, current_level, max_level):
    if len(this_level_nodes) == 0 or all_elements_are_None(this_level_nodes):
        return  # Base case of recursion: out of nodes, or only None left

    floor = max_level - current_level;
    endgeLines = 2 ** max(floor - 1, 0);
    firstSpaces = 2 ** floor - 1;
    betweenSpaces = 2 ** (floor + 1) - 1;
    print_spaces(firstSpaces)
    next_level_nodes = []
    for node in this_level_nodes:
        if node is not None:
            print(node._element, end = "")
            next_level_nodes.append(node._left)
            next_level_nodes.append(node._right)
        else:
            next_level_nodes.append(None)
            next_level_nodes.append(None)
            print_spaces(1)

        print_spaces(betweenSpaces)
    print()
    for i in range(1, endgeLines + 1):
        for j in range(0, len(this_level_nodes)):
            print_spaces(firstSpaces - i)
            if this_level_nodes[j] == None:
                    print_spaces(endgeLines + endgeLines + i + 1);
                    continue
            if this_level_nodes[j]._left != None:
                    print("/", end = "")
            else:
                    print_spaces(1)
            print_spaces(i + i - 1)
            if this_level_nodes[j]._right != None:
                    print("\\", end = "")
            else:
                    print_spaces(1)
            print_spaces(endgeLines + endgeLines - i)
        print()

    print_internal(next_level_nodes, current_level + 1, max_level)


def all_elements_are_None(list_of_nodes):
    for each in list_of_nodes:
        if each is not None:
            return False
    return True


def print_spaces(number):
    for i in range(number):
        print(" ", end = "")


# Task 1: Linked Representation of a heap
class HeapLinked(PriorityQueueBase, Tree):
    """A min-oriented linked-based heap implemented with a binary tree."""
    """There are TODO in this class for your work. You may define extra methods to help your implementation."""

    def __init__(self):
        """Create a new empty heap from the parent class Tree.
        Add an extra reference to the last node of that tree.
        """
        super().__init__()
        self._last = None

    # ------------------------------ nonpublic behaviors ------------------------------
    def _swap(self, x,y):
        """TODO:
        :param x,y: TreeNodes---You can assume x,y are not None.

        Swap the elements at node x and y of the Tree."""
        x._element,y._element=y._element,x._element

    def _upheap(self, x):
        """TODO:
        :param x: TreeNode---You can assume x is not None.

        Swap if heap-order property is not maintained between x and parent of x.
        Be sure to consider the case when x is the root."""
        node=x
        while True:
            parent=node._parent
            if parent is None:
                break
            if node._element<parent._element:
                node._element,parent._element=parent._element,node._element
                node=parent
            else:
                break

    def _downheap(self,y):
        """TODO:
        :param y: TreeNode---You can assume y is not None.

        Swap if heap-order property is not maintained between y and smaller child of y.
        Be sure to consider the case when y is the leaf."""
        node=y
        while True:
            left_child=node._left
            right_child=node._right
            if left_child is None and right_child is None:
                break
            elif left_child is not None and right_child is None:
                if node._element > left_child._element:
                    node._element,left_child._element=left_child._element,node._element
                    node=left_child
                else:
                    break
            else:
                smaller=left_child if left_child._element<right_child._element else right_child
                if node._element > smaller._element:
                    node._element,smaller._element=smaller._element,node._element
                    node=smaller
                else:
                    break

    # -------------------------- nonpublic mutators --------------------------
    def create_next_last(self, x):
        """TODO:
        :param x: TreeNode---last node of the current tree. You can assume x is not None.

        Create a new empty node that is the new last node if the tree increases its size by 1.
        Be sure to handle all possible cases.
        ! Complexity: O(logn).

        :return: TreeNode---a new node that is after the current last node.
        """
        left=0
        node=x
        full=False
        while True:
            if node._parent is None:
                full=True
                break
            if node._parent._right==node:
                left+=1
                node=node._parent
            else:
                node=node._parent
                break
        
        if full:
            while node._left:
                node=node._left
            temp=Tree.TreeNode(None)
            node._left=temp
            temp._parent=node
            return temp
        
        if left==0:
            temp=Tree.TreeNode(None)
            node._right=temp
            temp._parent=node
            return temp
        else:
            node=node._right
            for _ in range(left-1):
                node=node._left
            temp=Tree.TreeNode(None)
            node._left=temp
            temp._parent=node
            return temp

    def prev_last(self, x):
        """TODO:
        :param x: TreeNode---last node of the current tree. You can assume x is not None.

        Find the last node if the tree decreases its size by 1.
        You do not need to delete the current last.
        Be sure to handle all possible cases.

        ! Complexity: O(logn).
        :return: TreeNode---the node that is before the current last node.
                 None is x is the root
        """
        right=0
        node=x
        full=False
        while True:
            if node._parent is None:
                full=True
                break
            if node._parent._left==node:
                right+=1
                node=node._parent
            else:
                node=node._parent
                break

        if full:
            while node._right:
                node=node._right
            return node

        node=node._left
        for _ in range(right):
            node=node._right
        return node

    def add_root(self, e):
        """TODO:
        :param e: an abstract object to be added to self._root._element.

        Override add_root() method in Tree. Be sure your reference to the last node is updated.

        :return: the root node.
        """
        if self._size==0:
            temp=Tree.TreeNode(e)
            self._root=temp
            self._size+=1
            self._last=temp
        else:
            raise Exception('Root exists!')

    # ------------------------------ public behaviors ------------------------------
    def __len__(self):
        return self._size

    def add(self, k ,v):
        """TODO:
        Add a key-value pair to the heap.

        ! Complexity: O(logn)
        """
        if self._size==0:
            self.add_root(PriorityQueueBase._Item(k,v))
        else:
            self._size+=1
            node=self.create_next_last(self._last)
            self._last=node
            node._element=PriorityQueueBase._Item(k,v)
            self._upheap(node)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap is empty.')
        item = self._root._element
        return (item._key, item._value)

    def remove_min(self):
        """TODO:
        Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        ! Complexity: O(logn)
        """
        if self._size==0:
            raise Empty('The heap is empty')
        elif self._size==1:
            temp=(self._root._element._key,self._root._element._value)
            self._size-=1
            self._root=None
            self._last=None
            return temp
        else:
            temp=(self._root._element._key,self._root._element._value)
            self._swap(self._root,self._last)
            last_now=self._last
            self._last=self.prev_last(self._last)
            self._delete(last_now)
            self._downheap(self._root)
            return temp


# Task 2: Linked Representation of a heap with stored references
class HeapThreadedTree(PriorityQueueBase, Tree):
    """A min-oriented linked-based heap implemented with a binary tree."""
    """There are TODO in this class for your work. You may define extra methods to help your implementation."""
    class TreeNode(Tree.TreeNode):
        """Store references of next and previous nodes."""
        def __init__(self, element, parent=None, left=None, right=None, pred= None, succ = None):
            super().__init__(element, parent, left, right)
            self._prev = pred
            self._next = succ

    def __init__(self):
        """Create a new empty heap from the parent class Tree.
        Add an extra reference to the last node of that tree.
        """
        super().__init__()
        self._last = None

    # ------------------------------ nonpublic behaviors ------------------------------
    def _swap(self, x,y):
        """TODO:
        :param x,y: TreeNodes---You can assume x,y are not None.

        Swap the elements at node x and y of the Tree."""
        x._element,y._element=y._element,x._element

    def _upheap(self, x):
        """TODO:
        :param x: TreeNode---You can assume x is not None.

        Swap if heap-order property is not maintained between x and parent of x.
        Be sure to consider the case when x is the root."""
        node=x
        while True:
            parent=node._parent
            if parent is None:
                break
            if node._element<parent._element:
                node._element,parent._element=parent._element,node._element
                node=parent
            else:
                break

    def _downheap(self,y):
        """TODO:
        :param y: TreeNode---You can assume y is not None.

        Swap if heap-order property is not maintained between y and smaller child of y.
        Be sure to consider the case when y is the leaf."""
        node=y
        while True:
            left_child=node._left
            right_child=node._right
            if left_child is None and right_child is None:
                break
            elif left_child is not None and right_child is None:
                if node._element > left_child._element:
                    node._element,left_child._element=left_child._element,node._element
                    node=left_child
                else:
                    break
            else:
                smaller=left_child if left_child._element<right_child._element else right_child
                if node._element > smaller._element:
                    node._element,smaller._element=smaller._element,node._element
                    node=smaller
                else:
                    break

    # -------------------------- nonpublic mutators --------------------------
    def add_root(self, e):
        """TODO:
        :param e: an abstract object to be stored at self._root._element.

        Override add_root() method in Tree. Be sure references are updated.

        :return: the root node.
        """
        if self._size==0:
            temp=self.TreeNode(e)
            self._root=temp
            self._size+=1
            self._last=temp
        else:
            raise Exception('Root exists!')

    # ------------------------------ public behaviors ------------------------------
    def __len__(self):
        return self._size

    def add(self, k,v):
        """TODO:
        Add a key-value pair to the heap.

        ! Complexity: O(1) for addition, O(logn) to heapify.
        """
        if self._size==0:
            self.add_root(self._Item(k,v))
        elif self._size==1:
            self._size+=1
            node=self.TreeNode(self._Item(k,v))
            self._root._next=node
            self._root._left=node
            node._prev=self._root
            node._parent=self._root
            self._last=node
            self._upheap(node)
        else:
            self._size+=1
            node=self.TreeNode(self._Item(k,v))
            last=self._last
            last._next=node
            node._prev=last
            if last._parent._left==last:
                last._parent._right=node
                node._parent=last._parent
            else:
                last._parent._next._left=node
                node._parent=last._parent._next
            self._last=node
            self._upheap(node)
            

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap is empty.')
        item = self._root._element
        return (item._key, item._value)

    def remove_min(self):
        """TODO:
        Remove and return (k,v) tuple with minimum key.

        ! Complexity: O(1) for deletion, O(logn) to heapify.

        Raise Empty exception if empty.
        """
        if self._size==0:
            raise Empty('Heap is empty.')
        elif self._size==1:
            temp=(self._root._element._key,self._root._element._value)
            self._size-=1
            self._root=None
            self._last=None
            return temp
        else:
            temp=(self._root._element._key,self._root._element._value)
            last_update=self._last._prev
            last_now=self._last
            self._swap(self._root,last_now)
            self._delete(last_now)
            last_update._next=None
            self._last=last_update
            self._downheap(self._root)
            return temp



# Task 3: Linear probing without the _AVAIL object
from collections.abc import MutableMapping
from random import randrange, seed         # used to pick MAD parameters


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""
    """You should not modify this class."""
    #------------------------------- nested _Item class -------------------------------
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key   # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)       # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key    # compare items based on their keys


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression.

    ### Note: MAD: Multiply-Add-Divide
    From Mathemical analysis (group theory),
    this compression function will spread integer (more) evenly over the range [0..(N-1)]
    if we use a prime number for p.

    Keys must be hashable and non-None.
    """
    """You should not modify this class."""
    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map.

        cap     initial table size (default 11)
        p       positive prime used for MAD (default 109345121)
        """
        self._table = cap * [ None ]
        self._n = 0                                   # number of entries in the map
        self._prime = p                               # prime for MAD compression
        self._scale = 1 + randrange(p-1)              # scale from 1 to p-1 for MAD
        self._shift = randrange(p)                    # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)             # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)                 # subroutine maintains self._n
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)      # number 2*len(self._table) - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)                    # may raise KeyError
        self._n -= 1

    def _resize(self, c):
        """Resize bucket array to capacity c and rehash all items."""
        old = list(self.items())       # use iteration to record existing items
        self._table = c * [None]       # then reset table to desired capacity
        self._n = 0                    # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v                  # reinsert old key-value pair


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    def _find_slot(self, j, k):
        """TODO:
        :param j: index.
        :param k: key.

        Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes the NULL slot for insertion.
        """
        index=j
        count=0
        while True:
            if count==len(self._table):
                return False,None
            if self._table[index] is None:
                return False,index
            elif self._table[index]._key==k:
                return True,index
            else:
                index=(index+1)%len(self._table)
                count+=1

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)  # insert new item
            self._n += 1  # size has increased
        else:
            self._table[s]._value = v  # overwrite existing

    def _bucket_delitem(self, j, k):
        """TODO:
        :param j: index
        :param k: key

        Search for key k in bucket at index j. If it exists, delete it by searching for a proper replacement.
        Be sure you deal with indices that are affected by replacement.

        Raise KeyError if k does not exist.
        """
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        else:
            self._table[j]=None
            slots=len(self._table)
            p1=j#index available to put
            p2=(j+1)%slots#numbers to adjust
            count=0
            while True:
                if count==slots:
                    break
                count+=1
                if self._table[p2] is None:
                    break
                else:
                    temp=self._hash_function(self._table[p2]._key)
                    if p1<temp<=p2:
                        p2=(p2+1)%slots
                        continue
                    elif p1>p2 and (temp>p1 or temp<=p2):
                        p2=(p2+1)%slots
                        continue
                    else:
                        self._table[p1],self._table[p2]=self._table[p2],None
                        p1=p2
                        p2=(p2+1)%slots



    def __iter__(self):
        for j in range(len(self._table)):  # scan entire table
            if self._table[j] is not None:
                yield self._table[j]._key

    def __str__(self):
        result = []
        result.append("[")
        for j in range(len(self._table)):  # scan entire table
            if self._table[j] is not None:
                result.append("(" + str(self._table[j]._key) + " " + str(self._table[j]._value) + "), ")
            else:
                result.append("None, ")
        result.append("]")
        return "".join(result)


def main():
    print("#-------------------------- Task 1 Linked Representation of a heap... --------------------------")
    heap1 = HeapLinked()

    heap1.add(12, 'v')
    heap1.add(2, 'v')
    for i in range(10):
        heap1.add(i, 'v')
    print(len(heap1), ', Expect: 12')
    pretty_print(heap1)

    print('The current min is', heap1.min(), ', Expect: (0,"v")')
    print(len(heap1), ', Expect: 12')
    print('the first removed min is', heap1.remove_min(), ', Expect: (0,"v")')
    print('the next removed min is', heap1.remove_min(), ', Expect: (1,"v")')
    print('the next removed min is', heap1.remove_min(), ', Expect: (2,"v")')
    print('the next removed min is', heap1.remove_min(), ', Expect: (2,"v")')
    print(len(heap1), ', Expect: 8')
    pretty_print(heap1)

    for i in range(7):
        heap1.remove_min()
    print('the last removed min is', heap1.remove_min(), ', Expect: (12,"v")')
    print(heap1.is_empty(), ', Expect: True')


    print("#-------------------------- Task 2 Linked Representation of a heap with references... --------------------------")
    heap2 = HeapThreadedTree()

    heap2.add(12, 'v')
    heap2.add(2, 'v')
    for i in range(10):
        heap2.add(i, 'v')
    print(len(heap2), ', Expect: 12')
    pretty_print(heap2)

    print('The current min is', heap2.min(), ', Expect: (0,"v")')
    print(len(heap2), ' Expect: 12')
    print('the first removed min is', heap2.remove_min(), ', Expect: (0,"v")')
    print('the next removed min is', heap2.remove_min(), ', Expect: (1,"v")')
    print('the next removed min is', heap2.remove_min(), ', Expect: (2,"v")')
    print('the next removed min is', heap2.remove_min(), ', Expect: (2,"v")')
    print(len(heap2), ', Expect: 8')
    pretty_print(heap2)

    for i in range(7):
        heap2.remove_min()
    print('the last removed min is', heap2.remove_min(), ', Expect: (12,"v")')
    print(heap2.is_empty(), ', Expect: True')


    print("#-------------------------- Task 3 Linear probing without the _AVAIL object... --------------------------")
    seed(2021)      # change the seed when you do testings

    table = ProbeHashMap()
    values = ["Ezreal", "Blizcrank", "Annie", "Teemo", "Zed", "Hack", "DS2021"]
    for i in range(len(values)):
        table[i] = values[i]  # __setitem__ in HashMapBase, key value pair, key=i
        print(table)
    del table[3]
    table[5] = "Hacker"
    print(table)

    table[7] = "collider1"  # introducing collisions, works when seed(2021)
    table[21] = "collider2"
    table[35] = "collider3"
    print(table)

    del table[7]   # expect: all colliders shifted forward
    print(table)

    del table[21]   # expect: all colliders shifted forward
    print(table)


if __name__== '__main__':
    main()