# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def palindromeAt(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    return s[l+1:r]


def longestPalindrome(s: str) -> str:
    ans = ""
    for i in range(len(s)):
        odd = palindromeAt(s, i, i)  # 單數框
        even = palindromeAt(s, i, i+1)  # 偶數框
        ans = max(ans, odd, even, key=len)
    return ans


if __name__ == "__main__":
    s1 = "babad"
    output1 = longestPalindrome(s1)
    print('Longest palindromic substring of "{}" is "{}"'.format(s1, output1))

    s2 = "cbbd"
    output2 = longestPalindrome(s2)
    print('Longest palindromic substring of "{}" is "{}"'.format(s2, output2))
