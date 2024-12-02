def union(l1, l2):
    """
       This function returns the union of lists l1 and l2
    """

    # Please write your code here
    p1=0
    p2=0
    answer=[]
    while p1<len(l1) and p2<len(l2):
        if l1[p1]==l2[p2]:
            answer.append(l1[p1])
            p1+=1
            p2+=1
        elif l1[p1]<l2[p2]:
            answer.append(l1[p1])
            p1+=1
        else:
            answer.append(l2[p2])
            p2+=1
    while p1<len(l1):
        answer.append(l1[p1])
        p1+=1
    while p2<len(l2):
        answer.append(l2[p2])
        p2+=1
    return answer


def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = union(l1, l2)
    l.sort()
    print(l)  # should print [1,3,4,5,6,7,9]


if __name__ == '__main__':
    main()
