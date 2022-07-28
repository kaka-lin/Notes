import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def euclidean_distance(p1, p2):
    return math.sqrt(math.pow((p1.x - p2.x), 2) +
                     math.pow((p1.y - p2.y), 2))


# A Brute Force method to return the
# smallest distance between two points
def closest_pair_brute(P, n):
    min_dist = float('inf')
    min_pair = [(float('inf'), float('inf')), (float('inf'), float('inf'))]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(P[i], P[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = [P[i], P[j]]
    return min_pair, min_dist


def closest_pair_strip(P, n, d):
    min_dis = d
    min_pair = [(float('inf'), float('inf')), (float('inf'), float('inf'))]
    # 最多 8 個點：自己跟其他 7 個點
    for i in range(n):
        j = i + 1
        # y-axes 範圍: delta
        # runs at most 6 times
        while j < n and (P[j].y - P[i].y) < min_dis:
            min_dis = euclidean_distance(P[i], P[j])
            min_pair = [P[i], P[j]]
            j += 1
    return min_pair, min_dis


def closest_pair(Px, Py, n):
    # termination condition (base case)
    if n <= 3:
        return closest_pair_brute(Px, n)

    # Divide: (split P into left and right side)
    #   find a vertical line L
    mid = n // 2
    Pl = Px[:mid]
    Pr = Px[mid:]

    # Conquer
    left_pair, left_min = closest_pair(Pl, Py, mid)
    right_pair, right_min = closest_pair(Pr, Py, n - mid)

    # Combine
    ## 1. Find the smaller of two distances
    delta = min(left_min, right_min)

    ## 2. Remove points that are delta or more away from L.
    ##   cross_strip: contains the points, whose x-coords are at a
    ##                distance (< delta) from mid's x-coord
    cross_strip = []
    for p in Py:
        # x-axes 範圍: 2 delta
        if abs(p.x - Px[mid].x) < delta:
            cross_strip.append(p)

    ## 3. for piont pi in sorted candidates:
    ##    compute distance with other 7 points,
    ##    and update delta if a closer pair is found.
    cross_pair, cross_min = closest_pair_strip(cross_strip, len(cross_strip), delta)
    min_dist = min(cross_min, delta)
    if min_dist == left_min:
        return left_pair, left_min
    elif min_dist == right_min:
        return right_pair, right_min
    else:
        return cross_pair, cross_min


if __name__ == "__main__":
    P = [Point(2, 3), Point(12, 30),
         Point(40, 50), Point(5, 1),
         Point(12, 10), Point(3, 4)]

    Px = sorted(P, key=lambda p: p.x)
    Py = sorted(P, key=lambda p: p.y)
    n = len(P)

    min_pair, min_dist = closest_pair(Px, Py, n)
    print("The closet pair is: ({}, {}), ({}, {}), and distance is: {}".format(
        min_pair[0].x, min_pair[0].y, min_pair[1].x, min_pair[1].y, min_dist))
