def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def longestPalindrome(s):
    if not s: return ""

    n = len(s)
    left, right, longest = 0, 0, 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if isPalindrome(substr):
                if len(substr) > longest:
                    left, right, longest = i, j, len(substr)
    return s[left:right]


if __name__ == "__main__":
    s1 = "babad"
    output1 = longestPalindrome(s1)
    print('Longest palindromic substring of "{}" is "{}"'.format(s1, output1))

    s2 = "cbbd"
    output2 = longestPalindrome(s2)
    print('Longest palindromic substring of "{}" is "{}"'.format(s2, output2))
