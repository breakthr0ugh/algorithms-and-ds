import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        cur = self.root

        while True:
            if x == cur.key:
                return
            elif x < cur.key:
                if cur.left is None:
                    cur.left = Node(x)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(x)
                    return
                cur = cur.right

    def exists(self, x):
        cur = self.root

        while cur is not None:
            if x == cur.key:
                return True
            elif x < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        return False

    def delete(self, x):
        parent = None
        cur = self.root

        while cur is not None and cur.key != x:
            parent = cur
            if x < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        if cur is None:
            return

        if cur.left is not None and cur.right is not None:
            successor_parent = cur
            successor = cur.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            cur.key = successor.key
            parent = successor_parent
            cur = successor

        child = cur.left if cur.left is not None else cur.right

        if parent is None:
            self.root = child
        elif parent.left is cur:
            parent.left = child
        else:
            parent.right = child

    def height(self):
        if self.root is None:
            return 0

        stack = [(self.root, 1)]
        max_height = 0

        while stack:
            node, depth = stack.pop()
            max_height = max(max_height, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))

            if node.right is not None:
                stack.append((node.right, depth + 1))

        return max_height

    def preorder(self):
        if self.root is None:
            return "Empty"

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(str(node.key))

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return " ".join(result)


def main():
    q = int(sys.stdin.readline())
    tree = BST()
    output = []

    for _ in range(q):
        command = sys.stdin.readline().split()
        op = command[0]

        if op == "add":
            tree.add(int(command[1]))

        elif op == "del":
            tree.delete(int(command[1]))

        elif op == "exists":
            output.append(
                "YES" if tree.exists(int(command[1])) else "NO"
            )

        elif op == "height":
            output.append(str(tree.height()))

        elif op == "print":
            output.append(tree.preorder())

    print("\n".join(output))


if __name__ == "__main__":
    main()