def countAndSay(n: int) -> str:
    seq_dict = {1: "1", 2: "11"}
    for idx in range(3, n+1):
        prev = seq_dict[idx-1]
        ans = ''
        j = 0
        # like BFS
        while j < len(prev):
            count = 1
            while j+1 < len(prev) and prev[j] == prev[j+1]:
                count += 1
                j += 1
            ans += str(count) + str(prev[j])
            j += 1
        seq_dict[idx] = ans

    return seq_dict[n]


if __name__ == "__main__":
    for i in range(1, 7):
        print(countAndSay(i))
