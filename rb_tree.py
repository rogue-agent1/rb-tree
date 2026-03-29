import argparse

RED, BLACK = True, False

class Node:
    def __init__(self, key, color=RED):
        self.key = key; self.color = color
        self.left = self.right = self.parent = None

class RBTree:
    def __init__(self):
        self.nil = Node(0, BLACK)
        self.root = self.nil
    def _rotate_left(self, x):
        y = x.right; x.right = y.left
        if y.left != self.nil: y.left.parent = x
        y.parent = x.parent
        if x.parent is None: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y
    def _rotate_right(self, x):
        y = x.left; x.left = y.right
        if y.right != self.nil: y.right.parent = x
        y.parent = x.parent
        if x.parent is None: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y
    def insert(self, key):
        node = Node(key); node.left = node.right = self.nil
        y = None; x = self.root
        while x != self.nil:
            y = x; x = x.left if node.key < x.key else x.right
        node.parent = y
        if y is None: self.root = node
        elif node.key < y.key: y.left = node
        else: y.right = node
        self._fix_insert(node)
    def _fix_insert(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == RED:
                    u.color = BLACK; k.parent.color = BLACK; k.parent.parent.color = RED; k = k.parent.parent
                else:
                    if k == k.parent.left: k = k.parent; self._rotate_right(k)
                    k.parent.color = BLACK; k.parent.parent.color = RED; self._rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == RED:
                    u.color = BLACK; k.parent.color = BLACK; k.parent.parent.color = RED; k = k.parent.parent
                else:
                    if k == k.parent.right: k = k.parent; self._rotate_left(k)
                    k.parent.color = BLACK; k.parent.parent.color = RED; self._rotate_right(k.parent.parent)
            if k == self.root: break
        self.root.color = BLACK
    def inorder(self):
        result = []
        def io(n):
            if n == self.nil: return
            io(n.left); result.append((n.key, "R" if n.color else "B")); io(n.right)
        io(self.root); return result

def main():
    p = argparse.ArgumentParser(description="Red-Black tree")
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo:
        rbt = RBTree()
        for v in [7, 3, 18, 10, 22, 8, 11, 26]: rbt.insert(v)
        print("Inorder (key, color):")
        for k, c in rbt.inorder(): print(f"  {k} ({c})")
    else: p.print_help()

if __name__ == "__main__":
    main()
