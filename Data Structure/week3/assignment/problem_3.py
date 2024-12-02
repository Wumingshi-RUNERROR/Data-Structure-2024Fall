def perm(n, i):
    """
       This function returns the ith permutation of the number n
    """

    # Please write your code here
    factorial=[1]*n
    product=1
    for j in range(1,n):
        product*=j
        factorial[j]=product
    to_select=[str(x) for x in range(1,n+1)]
    selected=[]

    def find_range(target):
        n=len(to_select)
        if n==1:
            selected.append(to_select[0])
        else:
            step=factorial[n-1]
            section=(target-1)//step
            temp=to_select.pop(section)
            selected.append(temp)
            find_range((target-1)%step+1)
    find_range(i)
    return ''.join(selected)



def main():
    print(perm(3, 2))  # should print "132"
    print(perm(4, 9))  # should print "2314"


if __name__ == '__main__':
    main()
