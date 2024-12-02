import ctypes


class UserDefinedDynamicArray:
    """
        paste your implementation of recitation 4 here
    """
    def __init__(self, I=None):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = x
        self._n += 1

    def _resize(self, newsize):
        A = self._make_array(newsize)
        self._capacity = newsize
        for i in range(self._n):
            A[i] = self._A[i]
        self._A = A

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def __getitem__(self, i):
        if isinstance(i, slice):
            A = UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)):
                A.append(self._A[j])
            return A
        if i < 0:
            i = self._n + i
        return self._A[i]

    def __delitem__(self, i):
        if isinstance(i, slice):
            for j in reversed(range(*i.indices(self._n))):
                del self[j]
        else:
            if i < 0:
                i = self._n + i
            for j in range(i, self._n - 1):
                self._A[j] = self._A[j + 1]
            self[-1] = None
            self._n -= 1
            # Task 8
            # Please write your code here.
            if self._n<self._capacity//2:
                self._resize(self._capacity//2)

    def __str__(self):
        return "[" \
            + "".join(str(i) + "," for i in self[:-1]) \
            + (str(self[-1]) if not self.is_empty() else "") \
            + "]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        # Task 1
        # Please write your code here.
        for i in range(self._n):
            yield self._A[i]

    def __setitem__(self, i, x):
        # Task 2
        # Please write your code here.
        if i<0:
            self._A[i+self._n]=x
        else:
            self._A[i]=x

    def extend(self, I):
        # Task 3
        # Please write your code here.
        for i in I:
            self.append(i)


    def reverse(self):
        # Task 4
        # Please write your code here.
        p1=0
        p2=self._n-1
        while p1<p2:
            self._A[p1],self._A[p2]=self._A[p2],self._A[p1]
            p1+=1
            p2-=1

    def __contains__(self, x):
        # Task 5
        # Please write your code here.
        for i in range(self._n):
            if self._A[i]==x:
                return True
        return False

    def index(self, x):
        # Task 5
        # Please write your code here.
        for i in range(self._n):
            if self._A[i]==x:
                return i
            

    def count(self, x):
        # Task 5
        # Please write your code here.
        count=0
        for i in range(self._n):
            if self._A[i]==x:
                count+=1
        return count

    def __add__(self, other):
        # Task 6
        # Please write your code here.
        
        temp1=UserDefinedDynamicArray()
        for i in range(self._n):
            temp1.append(self._A[i])
        for i in range(other._n):
            temp1.append(other._A[i])
        return temp1

    def __mul__(self, times):
        # Task 6
        # Please write your code here.
        temp1=UserDefinedDynamicArray()
        for _ in range(times-1):
            for i in range(self._n):
                temp1.append(self._A[i])
        return temp1

    __rmul__ = __mul__

    def pop(self, i=-1):
        # Task 7
        # Please write your code here.
        temp=self._A[i]
        self.__delitem__(i)
        return temp

    def remove(self, x):
        # Task 7
        # Please write your code here.
        index=self.index(x)
        self.__delitem__(index)

    def max(self):
        # Task 9
        # Please write your code here.
        maximum=self._A[0]
        for i in range(self._n):
            if self._A[i]>maximum:
                maximum=self._A[i]
        return maximum


    def min(self):
        # Task 9
        # Please write your code here.
        minimum=self._A[0]
        for i in range(self._n):
            if self._A[i]<minimum:
                minimum=self._A[i]
        return minimum

    def sort(self, order="asc"):
        # Task 10
        # Please write your code here.
        def quick_sort(array,left,right):
            if left<right:
                p1=left-1
                p2=right+1
                piv=array[left]
                while p1<p2:
                    p1+=1
                    while array[p1]<piv:
                        p1+=1
                    p2-=1
                    while array[p2]>piv:
                        p2-=1
                    if p1<p2:
                        array[p1],array[p2]=array[p2],array[p1]
                quick_sort(array,left,p2)
                quick_sort(array,p2+1,right)

        quick_sort(self._A,0,self._n-1)
        if order=='desc':
            self.reverse()


    # ___________________________________________________________________________

    def union(self, b):
        p1=0
        p2=0
        answer=[]
        while p1<len(self) and p2<len(b):
            if self[p1]==b[p2]:
                answer.append(self[p1])
                p1+=1
                p2+=1
            elif self[p1]<b[p2]:
                answer.append(self[p1])
                p1+=1
            else:
                answer.append(b[p2])
                p2+=1
        while p1<len(self):
            answer.append(self[p1])
            p1+=1
        while p2<len(b):
            answer.append(b[p2])
            p2+=1
        new_array=UserDefinedDynamicArray(answer)
        return new_array

    def intersect(self, b):
        # Please write your code here
        p1=0
        p2=0
        answer=[]
        while p1<len(self) and p2<len(b):
            if self[p1]==b[p2]:
                answer.append(self[p1])
                p1+=1
                p2+=1
            elif self[p1]<b[p2]:
                p1+=1
            else:
                p2+=1
        new_array=UserDefinedDynamicArray(answer)
        return new_array


def main():
    L1 = UserDefinedDynamicArray([1, 3, 5, 7, 9])
    L1.sort()
    L2 = UserDefinedDynamicArray([3, 4, 5, 6, 7])
    L2.sort()
    L3 = UserDefinedDynamicArray([2, 4, 6, 8, 10])
    L3.sort()

    L = L1.union(L2)
    L.sort()  # L should be same as UserDefinedDynamicArray([1,3,4,5,6,7,9])
    print(L)

    L = L2.intersect(L3)
    L.sort()  # L should be same as UserDefinedDynamicArray([4,6])
    print(L)


if __name__ == '__main__':
    main()
