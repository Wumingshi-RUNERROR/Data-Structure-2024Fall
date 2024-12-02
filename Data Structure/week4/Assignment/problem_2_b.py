def rotator(M, a, d):
    """
        a in {0, 90, 180}
        d in {"clockwise","anticlockwise"}
        You should not change the value of M in this function.
    """

    # Please write your code here
    n=len(M)
    if a==0:
        answer=[]
        for i in M:
            answer.append(i[:])
    elif a==180:
        answer=[]
        for i in reversed(range(n)):
            answer.append(M[i][::-1])
    else:
        answer=[[None]*n for _ in range(n)]
        if d=='clockwise':
            for x in range(n):
                for y in range(n):
                    answer[y][n-1-x]=M[x][y]
        else:
            for x in range(n):
                for y in range(n):
                    answer[x][y]=M[y][n-1-x]
    return answer


def main():
    mat = [ [ 1, 2, 3, 4, 5], \
            [ 6, 7, 8, 9,10], \
            [11,12,13,14,15], \
            [16,17,18,19,20], \
            [21,22,23,24,25] ]
    new_mat = rotator(mat,90,"anticlockwise")
    print(new_mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]
    new_mat = rotator(mat,0,"anticlockwise")
    print(new_mat)
    # should print [ [ 1, 2, 3, 4, 5], \
            #        [ 6, 7, 8, 9,10], \
            #        [11,12,13,14,15], \
            #        [16,17,18,19,20], \
            #        [21,22,23,24,25] ]


if __name__ == '__main__':
    main()
