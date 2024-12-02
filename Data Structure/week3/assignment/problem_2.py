def summer(dic):
    """
       This function returns the sum of all positive integers in of nested dictionaries
    """

    # Please write your code here
    sum=0
    for i in dic:
        if type(dic[i])==int:
            sum+=max(0,dic[i])
        elif type(dic[i])==dict:
            sum+=summer(dic[i])
    return sum


def main():
    d1 = {"a": 2, "b": {"c": 3, "d": {"e": 2}}}
    d2 = {"nn": {"lil": 2}, "mm": 'car'}

    print(summer(d1))  # should print 7
    print(summer(d2))  # should print 2


if __name__ == '__main__':
    main()
