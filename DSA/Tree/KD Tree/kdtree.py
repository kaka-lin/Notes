from collections import namedtuple
from pprint import pformat

import numpy as np


class Node(namedtuple('Node', 'point left_child right_child')):
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
            left_child=self._build_kdtree(sorted_points[:median], depth + 1),
            right_child=self._build_kdtree(sorted_points[median+1:], depth + 1)
        )

    @property
    def tree(self):
        return self._tree


def main():
    points = np.array([(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)])
    kdtree = KDTree(points)
    print(kdtree.tree)


if __name__ == "__main__":
    main()
