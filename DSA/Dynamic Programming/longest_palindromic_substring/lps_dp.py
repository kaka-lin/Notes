def longestPalindrome(s):
    n = len(s)
    left = right = 0
    max_length = 0
    p_dp = [[0] * n for _ in range(n)]

    # Base case: Odd
    for i in range(n):
        p_dp[i][i] = True
        max_length = 1
        left = i
        right = i+1

    # Base case: Even
    for i in range(n-1):
        if s[i] == s[i+1]:
            p_dp[i][i+1] = True  # base case
            max_length = 2
            left = i
            right = i+2

    # Recursive case:
    # P(i,j) = P(i+1,j−1) and S[i] == S[j]
    # 採用『由上而下由左而右』進行搜索。
    for j in range(n):  # End
        for i in range(j-1):  # Start
            if s[i] == s[j] and p_dp[i+1][j-1]:
                p_dp[i][j] = True
                if j - i + 1 > max_length:
                    left = i
                    right = j+1
                    max_length = j - i + 1

    return s[left:right]


if __name__ == "__main__":
    s1 = "babad"
    output1 = longestPalindrome(s1)
    print('Longest palindromic substring of "{}" is "{}"'.format(s1, output1))

    s2 = "cbbd"
    output2 = longestPalindrome(s2)
    print('Longest palindromic substring of "{}" is "{}"'.format(s2, output2))
