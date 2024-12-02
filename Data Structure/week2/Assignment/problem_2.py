#1
def product_checker(A, B, m):
    def binary_search(target,array):
        left=0
        right=len(array)-1

        while left<=right:
            mid=(left+right)//2
            if array[mid]==target:
                return True
            elif array[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False



#2








    answer=[]
    for i in range(len(A)):
        if A[i]==A[i-1] and i>0:
            continue
        target=m/A[i]
        if binary_search(target,B):
            answer.append((A[i],int(target)))

    return answer


    
    


def main():
    A = [2, 4, 5, 6, 8, 10, 12]
    B = [1, 2, 4, 9, 10, 20]
    print(product_checker(A, B, 40))  # Should print [(2, 20), (4, 10), (10, 4)]

    A = [4, 5, 6, 20]
    B = [1, 2, 4, 10]
    print(product_checker(A, B, 100))  # Should print: []

    A = [1, 2, 2, 3, 5]
    B = [1, 5, 50, 50, 100]
    print(product_checker(A, B, 100))  # Should print: [(1, 100), (2, 50)]


if __name__ == '__main__':
    main()
