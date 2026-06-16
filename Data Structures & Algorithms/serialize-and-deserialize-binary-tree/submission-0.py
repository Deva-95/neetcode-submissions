# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        def preorder(root,arr):
            if not root: 
                arr.append(-1)
                return 
            arr.append(root.val)
            preorder(root.left,arr)
            preorder(root.right,arr)
        preorder(root,arr)
        return ','.join(map(str, arr))
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = list(map(int, data.split(',')))
        index = [0]

        def build():
            if arr[index[0]] == -1:
                index[0] += 1
                return None

            root = TreeNode(arr[index[0]])
            index[0] += 1
            root.left = build()
            root.right = build()
            return root

        return build()
