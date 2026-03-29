#!/usr/bin/env python3
"""Red-Black tree — self-balancing BST with color invariants."""
import sys

RED, BLACK = True, False

class RBNode:
    __slots__ = ('key','color','left','right','parent')
    def __init__(self, key, color=RED):
        self.key, self.color = key, color
        self.left = self.right = self.parent = None

class RBTree:
    def __init__(self):
        self.NIL = RBNode(None, BLACK)
        self.root = self.NIL
        self.count = 0
    def insert(self, key):
        n = RBNode(key)
        n.left = n.right = self.NIL
        p, curr = None, self.root
        while curr != self.NIL:
            p = curr
            if key < curr.key: curr = curr.left
            elif key > curr.key: curr = curr.right
            else: return  # dup
        n.parent = p
        if not p: self.root = n
        elif key < p.key: p.left = n
        else: p.right = n
        self.count += 1
        self._fix_insert(n)
    def _fix_insert(self, n):
        while n.parent and n.parent.color == RED:
            if n.parent == n.parent.parent.left:
                u = n.parent.parent.right
                if u.color == RED:
                    n.parent.color = BLACK; u.color = BLACK
                    n.parent.parent.color = RED; n = n.parent.parent
                else:
                    if n == n.parent.right:
                        n = n.parent; self._rotL(n)
                    n.parent.color = BLACK
                    n.parent.parent.color = RED
                    self._rotR(n.parent.parent)
            else:
                u = n.parent.parent.left
                if u.color == RED:
                    n.parent.color = BLACK; u.color = BLACK
                    n.parent.parent.color = RED; n = n.parent.parent
                else:
                    if n == n.parent.left:
                        n = n.parent; self._rotR(n)
                    n.parent.color = BLACK
                    n.parent.parent.color = RED
                    self._rotL(n.parent.parent)
        self.root.color = BLACK
    def _rotL(self, x):
        y = x.right; x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y
    def _rotR(self, y):
        x = y.left; y.left = x.right
        if x.right != self.NIL: x.right.parent = y
        x.parent = y.parent
        if not y.parent: self.root = x
        elif y == y.parent.left: y.parent.left = x
        else: y.parent.right = x
        x.right = y; y.parent = x
    def __contains__(self, key):
        n = self.root
        while n != self.NIL:
            if key == n.key: return True
            n = n.left if key < n.key else n.right
        return False
    def __len__(self): return self.count
    def inorder(self):
        r = []
        def io(n):
            if n == self.NIL: return
            io(n.left); r.append(n.key); io(n.right)
        io(self.root); return r

def test():
    t = RBTree()
    for x in range(1, 21):
        t.insert(x)
    assert t.inorder() == list(range(1, 21))
    assert len(t) == 20
    assert 15 in t
    assert 25 not in t
    assert t.root.color == BLACK
    print("  rb_tree: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Red-Black tree")
