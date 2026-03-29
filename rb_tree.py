#!/usr/bin/env python3
"""Red-Black Tree - Self-balancing BST with color-based invariants."""
import sys

RED, BLACK = True, False

class Node:
    def __init__(self, key, color=RED):
        self.key = key; self.color = color; self.left = self.right = self.parent = None

class RBTree:
    def __init__(self): self.NIL = Node(None, BLACK); self.root = self.NIL; self.size = 0
    def insert(self, key):
        node = Node(key); node.left = node.right = self.NIL
        parent = None; current = self.root
        while current != self.NIL:
            parent = current
            current = current.left if key < current.key else current.right
        node.parent = parent
        if not parent: self.root = node
        elif key < parent.key: parent.left = node
        else: parent.right = node
        self.size += 1; self._fix_insert(node)
    def _fix_insert(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK; y.color = BLACK; z.parent.parent.color = RED; z = z.parent.parent
                else:
                    if z == z.parent.right: z = z.parent; self._rot_l(z)
                    z.parent.color = BLACK; z.parent.parent.color = RED; self._rot_r(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK; y.color = BLACK; z.parent.parent.color = RED; z = z.parent.parent
                else:
                    if z == z.parent.left: z = z.parent; self._rot_r(z)
                    z.parent.color = BLACK; z.parent.parent.color = RED; self._rot_l(z.parent.parent)
        self.root.color = BLACK
    def _rot_l(self, x):
        y = x.right; x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y
    def _rot_r(self, y):
        x = y.left; y.left = x.right
        if x.right != self.NIL: x.right.parent = y
        x.parent = y.parent
        if not y.parent: self.root = x
        elif y == y.parent.left: y.parent.left = x
        else: y.parent.right = x
        x.right = y; y.parent = x
    def inorder(self):
        r = []
        def dfs(n):
            if n != self.NIL: dfs(n.left); r.append((n.key, "R" if n.color else "B")); dfs(n.right)
        dfs(self.root); return r
    def black_height(self):
        h = 0; n = self.root
        while n != self.NIL: 
            if n.color == BLACK: h += 1
            n = n.left
        return h

def main():
    t = RBTree()
    for x in [7, 3, 18, 10, 22, 8, 11, 26, 2, 6]: t.insert(x)
    print(f"=== Red-Black Tree ({t.size} nodes, bh={t.black_height()}) ===")
    print(f"Root: {t.root.key} ({'R' if t.root.color else 'B'})")
    for key, color in t.inorder(): print(f"  {key} ({color})")

if __name__ == "__main__":
    main()
