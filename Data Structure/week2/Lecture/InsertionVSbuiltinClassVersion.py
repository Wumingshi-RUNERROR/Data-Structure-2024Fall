import timeit
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def insertion_sort(data_list):
    # 1. Split data into two parts: sorted & unsorted
    #    X | X X X X X X X
    #    sorted | unsorted
    # 2. While size of unsorted part is greater than zero?    #   a. let the target element be the first element in the unsorted part
    #   b. find targets insertion point in the sorted part
    #   c. make place at insertion point by shifting all larger elements
    #   d. insert the target in its final, sorted position

    # Coding: Please sort the values in-place, i.e. no new data_list is created and final sorted values are in data_list
    for i in range(1,len(data_list)):
        target=data_list[i]
        index=i-1
        while target<data_list[index] and index>=0:
            data_list[index+1]=data_list[index]
            index-=1
        data_list[index+1]=target
    print(data_list)
    return data_list


def python_sort(data_list):
    # Use list.sort()
    # Python built in sort uses Tim-sort
    data_list.sort()
    return data_list

if __name__ == '__main__':
    data1 = []
    data2 = []
    for i in range(10000):
        value = random.randint(0,1000)
        data1.append(value)
        data2.append(value)
    print("Insertion sort 10000 elements:",
          '{:.6f}'.format(timeFunction(insertion_sort, data1)), "seconds")
    print("Built in sort 10000 elements:",
          '{:.6f}'.format(timeFunction(python_sort, data2)), "seconds")
          
     
