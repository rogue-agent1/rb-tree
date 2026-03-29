#!/usr/bin/env python3
"""rb_tree - Red-Black tree implementation."""
import sys

RED, BLACK = True, False

class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = self.right = self.parent = None

class RBTree:
    def __init__(self):
        self.NIL = RBNode(None, BLACK)
        self.root = self.NIL
        self.size = 0

    def _rot_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rot_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = RBNode(key)
        node.left = node.right = self.NIL
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            x = x.left if key < x.key else x.right
        node.parent = y
        if y is None:
            self.root = node
        elif key < y.key:
            y.left = node
        else:
            y.right = node
        self.size += 1
        self._fix_insert(node)

    def _fix_insert(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._rot_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._rot_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_left(z.parent.parent)
        self.root.color = BLACK

    def search(self, key):
        n = self.root
        while n != self.NIL:
            if key == n.key: return True
            n = n.left if key < n.key else n.right
        return False

    def inorder(self):
        result = []
        def traverse(n):
            if n != self.NIL:
                traverse(n.left)
                result.append(n.key)
                traverse(n.right)
        traverse(self.root)
        return result

    def _black_height(self, node=None):
        if node is None:
            node = self.root
        if node == self.NIL:
            return 1
        lh = self._black_height(node.left)
        rh = self._black_height(node.right)
        if lh != rh:
            return -1
        return lh + (1 if node.color == BLACK else 0)

def test():
    t = RBTree()
    for v in [7, 3, 18, 10, 22, 8, 11, 26]:
        t.insert(v)
    assert t.inorder() == sorted([7,3,18,10,22,8,11,26])
    assert t.size == 8
    assert t.root.color == BLACK
    assert t._black_height() > 0
    assert t.search(10)
    assert not t.search(99)
    t2 = RBTree()
    for i in range(50):
        t2.insert(i)
    assert t2.size == 50
    assert t2._black_height() > 0
    assert t2.inorder() == list(range(50))
    print("All tests passed!")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("rb_tree: Red-Black tree. Use --test")
