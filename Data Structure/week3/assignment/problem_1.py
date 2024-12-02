def deepest(lis):
    """
       This function finds the deepest nested element in a list
    """

    # Please write your code here
    check_repetive=[True,-1]
    def find_depth(array,depth):
        for i in array:
            if type(i) == list:
                find_depth(i,depth+1)

        if depth>check_repetive[1]:
            check_repetive[0]=True
            check_repetive[1]=depth
        elif depth==check_repetive[1]:
            check_repetive[0]=False
    
    def select(array,depth,target):
        if depth==target:
            return array
        for i in array:
            if type(i)==list:
                if select(i,depth+1,target):
                    return select(i,depth+1,target)
        return []

                
    find_depth(lis,0)
    if not check_repetive[0]:
        return []
    else:
        return select(lis,0,check_repetive[1])



def main():
    l1 = [[[1]]]
    l2 = [1, [2, [3]]]
    l3 = [[[1]], [2], [3]]

    print(deepest(l1))  # should print [1]
    print(deepest(l2))  # should print [3]
    print(deepest(l3))  # should print [1]


if __name__ == '__main__':
    main()
