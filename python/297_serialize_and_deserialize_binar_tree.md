# 297. Serialize and Deserialize Binary Tree

#### Discription

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.


#### Example:

```
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```

#### Clarification:

The above format is the same as [how LeetCode serializes a binary tree](https://support.leetcode.com/hc/en-us/sections/360002895993-Technical-Questions). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

#### Note:

Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## Solution:

Youtube: [Serialize & Deserialize A Binary Tree - Crafting Recursive Solutions To Interview Problems](https://www.youtube.com/watch?v=suj1ro8TIVY)

- Runtime: 100 ms (97.46%)
- Memory Usage: 18.1 MB (58.35%)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""

        if root is None:
            return 'X'

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return "{},{},{}".format(root.val, left, right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""

        def deserializeHelper():
            val = next(datas)

            if val == 'X':
                return None

            node = TreeNode(int(val))
            node.left = deserializeHelper()
            node.right = deserializeHelper()

            return node

        datas = iter(data.split(','))
        return deserializeHelper()

    """
    def deserialize(self, data: str) -> TreeNode:
        datas = data.split(',')
        return self.deserializeHelper(datas)

    def deserializeHelper(self, datas: List) -> TreeNode:
        val = datas.pop(0)

        if val == 'X':
            return None

        node = TreeNode(int(val))
        node.left = self.deserializeHelper(datas)
        node.right = self.deserializeHelper(datas)

        return node
    """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

### Time complexity

### Space complexity
