import unittest

# Your TreeNode class and max_depth function here
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Unit tests
class TestMaxDepth(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_single_node(self):
        self.assertEqual(max_depth(TreeNode(1)), 1)

    def test_balanced_tree(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(max_depth(root), 2)

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(max_depth(root), 3)

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(max_depth(root), 3)

    def test_complex_tree(self):
        root = TreeNode(1,
                        TreeNode(2, TreeNode(4), TreeNode(5)),
                        TreeNode(3, None, TreeNode(6)))
        self.assertEqual(max_depth(root), 3)

if __name__ == '__main__':
    unittest.main()
