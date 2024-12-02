def lengthOfLongestSubstring(s):
    check_in=[False]*26
    p1=0
    p2=0
    longest_ever=0
    length_now=0
    while p2<=len(s)-1:
        if not check_in[ord(s[p2])-97]:
            length_now+=1
            check_in[ord(s[p2])-97]=True
            p2+=1
            continue
        longest_ever=max(length_now,longest_ever)
        while check_in[ord(s[p2])-97]:
            check_in[ord(s[p1])-97]=False
            length_now-=1
            p1+=1
    longest_ever=max(longest_ever,length_now)
    return longest_ever




def main():
    s = "abcabcbb"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 3, Length of the substring “abc”

    # Example 2
    s = "bbbbb"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 1, Length of the substring “b”

    # Example 3
    s = "pwwkew"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 3, Length of the substring “wke”


if __name__ == '__main__':
    main()
