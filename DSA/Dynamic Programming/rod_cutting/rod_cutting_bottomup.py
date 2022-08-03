# Bottom-Up with Tabulation
def rod_cut(p, n):
    revenue = {0: 0}
    # compute r[1], r[2], ..., r[n]
    for i in range(1, n+1):
        profit = 0  # or float('-inf')
        for j in range(1, i+1):
            # 長度為 j 的桿子成本為 price[j-1]
            # ex: j=1(m) => price[0]
            profit = max(profit, p[j-1] + revenue[i - j])
        revenue[i] = profit
    return revenue[n]


if __name__ == '__main__':
    # 1m, 2m, ..., Nm
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    # the length of rod
    for i in range(1, len(price)+1):
        r = rod_cut(price, i)
        print("The maximum revenue of {}m is: {}".format(i, r))
