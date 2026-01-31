class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = "RED"
        self.left = None
        self.right= None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, key):
        node = RBNode(key)
        node.left = node.right = node.parent = self.NIL

        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key > x.key:
                x = x.right
            else:
                return

        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.left=node.right=self.NIL
        node.color = "RED"

        self.fix_insert(node)

    def fix_insert(self, k):
        while k !=self.root and k.parent.color=="RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.color = "RED"
                    k=k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                        k.parent.color = "BLACK"
                        k.parent.parent.color = "RED"
                        self.right_rotate(k.parent.parent)
                    else:
                        u=k.parent.parent.left
                        if u.color == "RED":
                            k.parent.color = "BLACK"
                            u.parent.color = "BLACK"
                            k.parent.parent.color= "RED"
                            k= k.parent.parent
                        else:
                            if k == k.parent.right:
                                k = k.parent
                                self.left_rotate(k)

                            k.parent.color = "BLACK"
                            k.parent.parent.color = "RED"
                            self.right_rotate(k.parent.parent)

                self.root.color="BLACK"

    def left_rotate(self,x):
        y= x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self,x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x


        y.parent = x.parent
        if x.parent == self.NIL:
            self.root= y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
    def search(self, key):
        return self._search_tree_helper(self.root, key)

    def _search_tree_helper(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def inorder_helper(self, node):
        if node != self.NIL:
            self.inorder_helper(node.left)
            print(node.key)
            self.inorder_helper(node.right)

    def list_files(self):
        print("[RBT] File List:")
        self.inorder_helper(self.root)
