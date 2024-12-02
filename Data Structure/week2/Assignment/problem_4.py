'''
def findMedianSortedArrays(nums1, nums2):
    def find_k_smallest(k):
        p1=-1
        p2=-1
        length1=len(nums1)
        length2=len(nums2)
        while True:
            if p2==length2-1:
                return nums1[p1+k]
            if p1==length1-1:
                return nums2[p2+k]
            if k==1:
                return min(nums1[p1+1],nums2[p2+1])
            
            step=min(k//2,length1-1-p1,length2-1-p2)
            if nums1[p1+step]<=nums2[p2+step]:
                p1+=step
            else:
                p2+=step
            k-=step
    
    numbers=len(nums1)+len(nums2)
    if numbers%2==0:
        return (find_k_smallest(numbers//2)+find_k_smallest(numbers//2+1))/2
    else:
        return find_k_smallest((numbers+1)//2)
'''


def findMedianSortedArrays(nums1,nums2):
    if len(nums1)>=len(nums2):
        longer=nums1
        shorter=nums2
    else:
        longer=nums2
        shorter=nums1
    long_length=len(longer)
    short_length=len(shorter)
    sum=long_length+short_length
    index_short=short_length-1
    index_long=(long_length+short_length+1)//2-short_length-1
    while True:
        if index_long==-1:
            left_num_longer=-float("inf")
        else:
            left_num_longer=longer[index_long]
        if index_short==-1:
            left_num_shorter=-float('inf')
        else:
            left_num_shorter=shorter[index_short]
        try: 
            right_num_shorter=shorter[index_short+1]
        except:
            right_num_shorter=float('inf')
        try: 
            right_num_longer=longer[index_long+1]
        except:
            right_num_longer=float('inf')
        
        if left_num_longer<=right_num_shorter and left_num_shorter<=right_num_longer:
            if sum%2==0:
                return (max(left_num_longer,left_num_shorter)+min(right_num_longer,right_num_shorter))/2
            else:
                return max(left_num_longer,left_num_shorter)
        else:
            index_long+=1
            index_short-=1



def main():
    # Example 1
    nums1 = [1, 3, 5, 7]
    nums2 = [2]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)  # Should print 3

    # Example 2
    nums1 = [1, 2]
    nums2 = [4, 5]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)  # Median is (2 + 4) / 2 = 3.0
                   # Should print 3


if __name__ == '__main__':
    main()
