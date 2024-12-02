def rotator(M,a,d):
    """
        a in {0, 90, 180}
        d in {"clockwise","anticlockwise"}
        You should change the value of M in this function
    """

    # Please write your code here
    n=len(M)
    if a==0:
        return
    elif a==180:
        temp=n//2
        for x in range(temp):
            for y in range(n):
                M[x][y],M[n-1-x][n-1-y]=M[n-1-x][n-1-y],M[x][y]
        if n%2==1:
            for y in range(temp):
                M[temp][y],M[temp][n-1-y]=M[temp][n-1-y],M[temp][y]
    else:
        if d=='anticlockwise':
            for x in range((n+1)//2):
                for y in range(x,n-1-x):
                    M[x][y],M[y][n-1-x],M[n-1-x][n-1-y],M[n-1-y][x]=M[y][n-1-x],M[n-1-x][n-1-y],M[n-1-y][x],M[x][y]
        else:
            for x in range((n+1)//2):
                for y in range(x,n-1-x):
                    M[y][n-1-x],M[n-1-x][n-1-y],M[n-1-y][x],M[x][y]=M[x][y],M[y][n-1-x],M[n-1-x][n-1-y],M[n-1-y][x]



def main():
    mat = [ [ 1, 2, 3, 4, 5], \
            [ 6, 7, 8, 9,10], \
            [11,12,13,14,15], \
            [16,17,18,19,20], \
            [21,22,23,24,25] ]
    rotator(mat,90,"anticlockwise")
    print(mat) 
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]
    rotator(mat,0,"anticlockwise")
    print(mat) 
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]


if __name__ == '__main__':
    main()
