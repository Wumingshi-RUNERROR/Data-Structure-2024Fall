class Solution:
    def same(self, i1, i2):

        def is_same_tree(arr1, arr2):
            if not arr1 and not arr2:
                return True
            if len(arr1) != len(arr2):
                return False
            
            if arr1[0] != arr2[0]:
                return False
            
            root = arr1[0]
            left1 = [x for x in arr1[1:] if x < root]
            right1 = [x for x in arr1[1:] if x >= root]
            left2 = [x for x in arr2[1:] if x < root]
            right2 = [x for x in arr2[1:] if x >= root]
            
            return is_same_tree(left1, left2) and is_same_tree(right1, right2)
        
        return is_same_tree(i1, i2)


def main():
    i1 = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]
    i2 = [15, 10, 12, 8, 25, 30, 6, 20, 18, 9, 22]

    res = Solution().same(i1, i2)
    print(res)  # Should print true


if __name__ == '__main__':
    main()
