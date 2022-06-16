from collections import namedtuple
from dis import dis
from pprint import pformat

import numpy as np


class Node(namedtuple('Node', 'point left right')):
    def __repr__(self):
        return pformat(tuple(self))


class KDTree():
    def __init__(self, points):
        # k dimension
        if len(points) > 0:
            self._k = len(points[0])
        else:
            self._k = None

        self._tree = self._build_kdtree(points)
        self._best = None

    def _distance(self, x, y):
        dist = np.linalg.norm(x - y, ord=2)
        return dist

    @property
    def tree(self):
        return self._tree

    def _build_kdtree(self, points, depth=0):
        if len(points) <= 0:
            return None

        # 1. Select axis based on depth so that axis cycles
        #    through all valid values
        axis = depth % self._k # 2d: (x, y, x, y, ...)

        # 2. Sort point list and choose median as pivot element
        sorted_points = sorted(points, key=lambda point: point[axis])
        median = len(sorted_points) // 2

        # 3. Create node and construct subtress
        return Node(
            point=sorted_points[median],
            left=self._build_kdtree(sorted_points[:median], depth+1),
            right=self._build_kdtree(sorted_points[median+1:], depth+1)
        )

    def find_nearest(self, point, root=None, depth=0):
        # 1. 從根節點開始搜尋
        if root is None:
            root = self._tree

        axis = depth % self._k # 2d: (x, y, x, y, ...)

        # 2. 若不是葉節點，則繼續往下走，直至達到葉節點(leaf node)
        if root.left or root.right:
            if point[axis] < root.point[axis] and root.left:
                self.find_nearest(point, root.left, depth+1)
            elif root.right:
                self.find_nearest(point, root.right, depth+1)

        # 3. 回溯，計算 target 與當前節點 (root) 之間的距離
        #    並更新當前最佳節點 (best)
        dist = self._distance(root.point, point)
        if self._best is None or dist < self._best[0]:
            self._best = (dist, root.point)

        # 4. 檢查超球面是否有穿越分割面
        #    超球面有穿越分割面:
        #      比較“目標節點”和“當前節點分割面”的距離是否比最佳節點距離更小
        if abs(point[axis] - root.point[axis]) < self._best[0]:
            # 如果 target 位於左子空間，就進右子空間搜尋
            if point[axis] < root.point[axis] and root.right:
                self.find_nearest(point, root.right, depth+1)
            # 反之亦然
            elif point[axis] >= root.point[axis] and root.left:
                self.find_nearest(point, root.left, depth+1)

        return self._best


def main():
    points = np.array([(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)])
    kdtree = KDTree(points)
    print(kdtree.tree)

    # Nearest Neighbor Search
    #target_point = np.array((2.1,3.1)) # (0.1414, (2, 3))
    target_point = np.array((2,4.5)) # (1.5 (2, 3))
    nearest_point = kdtree.find_nearest(target_point)
    print(nearest_point)


if __name__ == "__main__":
    main()
