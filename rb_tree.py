#!/usr/bin/env python3
"""Red-Black tree — balanced BST with color invariants."""
import sys

RED, BLACK = True, False

class Node:
    def __init__(self, key, color=RED):
        self.key, self.color = key, color
        self.left = self.right = self.parent = None

class RBTree:
    def __init__(self):
        self.NIL = Node(0, BLACK); self.root = self.NIL
    def _rot_l(self, x):
        y = x.right; x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if x.parent is None: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y
    def _rot_r(self, x):
        y = x.left; x.left = y.right
        if y.right != self.NIL: y.right.parent = x
        y.parent = x.parent
        if x.parent is None: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y
    def insert(self, key):
        n = Node(key); n.left = n.right = self.NIL
        y = None; x = self.root
        while x != self.NIL: y = x; x = x.left if n.key < x.key else x.right
        n.parent = y
        if y is None: self.root = n
        elif n.key < y.key: y.left = n
        else: y.right = n
        self._fix_insert(n)
    def _fix_insert(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == RED:
                    u.color = k.parent.color = BLACK; k.parent.parent.color = RED; k = k.parent.parent
                else:
                    if k == k.parent.left: k = k.parent; self._rot_r(k)
                    k.parent.color = BLACK; k.parent.parent.color = RED; self._rot_l(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == RED:
                    u.color = k.parent.color = BLACK; k.parent.parent.color = RED; k = k.parent.parent
                else:
                    if k == k.parent.right: k = k.parent; self._rot_l(k)
                    k.parent.color = BLACK; k.parent.parent.color = RED; self._rot_r(k.parent.parent)
            if k == self.root: break
        self.root.color = BLACK
    def inorder(self):
        res = []; self._inorder(self.root, res); return res
    def _inorder(self, n, res):
        if n != self.NIL: self._inorder(n.left, res); res.append(n.key); self._inorder(n.right, res)

def main():
    rbt = RBTree()
    for x in [7,3,18,10,22,8,11,26,2,6]: rbt.insert(x)
    print(f"Inorder: {rbt.inorder()}")
    print(f"Root: {rbt.root.key}, Color: {'B' if rbt.root.color==BLACK else 'R'}")

if __name__ == "__main__": main()
