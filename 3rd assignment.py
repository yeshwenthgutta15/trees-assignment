class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = TreeNode(val)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def pre_order_traversal(self):
        result = []
        self._pre_order(self.root, result)
        return result

    def _pre_order(self, node, result):
        if not node:
            return
        result.append(node.val)
        self._pre_order(node.left, result)
        self._pre_order(node.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if not node:
            return
        self._in_order(node.left, result)
        result.append(node.val)
        self._in_order(node.right, result)

    def post_order_traversal(self):
        result = []
        self._post_order(self.root, result)
        return result

    def _post_order(self, node, result):
        if not node:
            return
        self._post_order(node.left, result)
        self._post_order(node.right, result)
        result.append(node.val)

    def print_leaves(self):
        leaves = []
        self._get_leaves(self.root, leaves)
        return leaves

    def _get_leaves(self, node, leaves):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        self._get_leaves(node.left, leaves)
        self._get_leaves(node.right, leaves)

    def bfs(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        if not self.root:
            return []
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def sum_left_leaves(self):
        return self._sum_left_leaves(self.root, False)

    def _sum_left_leaves(self, node, is_left):
        if not node:
            return 0
        if not node.left and not node.right:
            if is_left:
                return node.val
            else:
                return 0
        return self._sum_left_leaves(node.left, True) + self._sum_left_leaves(node.right, False)

    def sum_all_nodes(self):
        return self._sum_all_nodes(self.root)

    def _sum_all_nodes(self, node):
        if not node:
            return 0
        return node.val + self._sum_all_nodes(node.left) + self._sum_all_nodes(node.right)

    def count_subtrees_with_sum(self, target_sum):
        count = 0
        self._count_subtrees(self.root, target_sum, count)
        return count

    def _count_subtrees(self, node, target_sum, count):
        if not node:
            return 0

        left_sum = self._count_subtrees(node.left, target_sum, count)
        right_sum = self._count_subtrees(node.right, target_sum, count)

        total_sum = left_sum + right_sum + node.val

        if total_sum == target_sum:
            count[0] += 1

        return total_sum

    def max_level_sum(self):
        if not self.root:
            return 0

        max_sum = self.root.val
        queue = [self.root]

        while queue:
            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            max_sum = max(max_sum, level_sum)

        return max_sum

    def print_odd_level_nodes(self):
        if not self.root:
            return []

        result = []
        queue = [self.root]
        level = 1

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)

                if level % 2 == 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return result

tree = BinaryTree()
tree.insert(10)
tree.insert (20)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print("Height of the tree:", tree.height())
print("Pre-order traversal:", tree.pre_order_traversal())
print("In-order traversal:", tree.in_order_traversal())
print("Post-order traversal:", tree.post_order_traversal())
print("Leaves of the tree:", tree.print_leaves())
print("BFS:", tree.bfs())
print("DFS:", tree.dfs())
print("Sum of left leaves:", tree.sum_left_leaves())
print("Sum of all nodes:", tree.sum_all_nodes())
print("Count subtrees with sum 10:", tree.count_subtrees_with_sum(10))
print("Maximum level sum:", tree.max_level_sum())
print("Nodes at odd levels:", tree.print_odd_level_nodes())
