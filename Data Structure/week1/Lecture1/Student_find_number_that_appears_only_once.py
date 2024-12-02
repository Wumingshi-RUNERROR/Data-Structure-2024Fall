def find(lissy):
    result=0
    for num in lissy:
        result^=num
        print(result,end=' ')
    print()
    return result

def main():
    l1 = [7,1,5,3,6,4,7,1,5,6,4]
    l2 = [7,6,4,3,2,1,1,2,3,4,5,6,7]
    print(find(l1)) # expect: 3
    print(find(l2)) # expect: 5

if __name__ == '__main__':
    main()
