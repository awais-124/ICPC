# TREES - Complete Reference for ICPC
# Binary Trees, BST, Tree Traversals, and common operations

from collections import deque

# ============ TREE NODE ============

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# ============ TREE CONSTRUCTION & OPERATIONS ============

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert in BST"""
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)


# ============ TREE TRAVERSALS ============

# Inorder (Left, Node, Right) - Sorted in BST
def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)
    return result


# Preorder (Node, Left, Right) - Useful for copying tree
def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.val)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


# Postorder (Left, Right, Node) - Useful for deletion
def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.val)
    return result


# Level Order (BFS)
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# ============ COMMON TREE OPERATIONS ============

# Find height/depth
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


# Count nodes
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Sum of all nodes
def tree_sum(node):
    if not node:
        return 0
    return node.val + tree_sum(node.left) + tree_sum(node.right)


# Find maximum value
def find_max(node):
    if not node:
        return float('-inf')
    return max(node.val, find_max(node.left), find_max(node.right))


# Check if tree is balanced
def is_balanced(node):
    if not node:
        return True
    left_h = height(node.left)
    right_h = height(node.right)

    if abs(left_h - right_h) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


# ============ BST SPECIFIC OPERATIONS ============

# Search in BST
def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    elif target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)


# Find minimum (leftmost node)
def find_min(node):
    while node and node.left:
        node = node.left
    return node.val if node else None


# Find maximum (rightmost node)
def find_max_bst(node):
    while node and node.right:
        node = node.right
    return node.val if node else None


# Delete from BST
def delete_bst(node, target):
    if not node:
        return None

    if target < node.val:
        node.left = delete_bst(node.left, target)
    elif target > node.val:
        node.right = delete_bst(node.right, target)
    else:
        # Node with only one child or no child
        if not node.left:
            return node.right
        elif not node.right:
            return node.left

        # Node with two children: get the inorder successor (smallest in right subtree)
        min_val = find_min(node.right)
        node.val = min_val
        node.right = delete_bst(node.right, min_val)

    return node


# ============ LCA (Lowest Common Ancestor) ============

def lca(node, p, q):
    """Find LCA in BST where p, q are values"""
    if not node:
        return None

    if p < node.val and q < node.val:
        return lca(node.left, p, q)
    elif p > node.val and q > node.val:
        return lca(node.right, p, q)
    else:
        return node.val


# ============ PATH OPERATIONS ============

# Find path from root to node
def find_path(node, target, path=None):
    if path is None:
        path = []

    if not node:
        return None

    path.append(node.val)

    if node.val == target:
        return path

    left_path = find_path(node.left, target, path[:])
    if left_path:
        return left_path

    right_path = find_path(node.right, target, path[:])
    if right_path:
        return right_path

    return None
