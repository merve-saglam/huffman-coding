class BTreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []
class BTree:
    def __init__(self):
     self.nodes = []

    def insert(self,key):
        if not self.search(key):
            self.nodes.append(BTreeNode(key))
            print(f"[BTree] '{key}' added.")
        else:
            print(f"[BTree] '{key}' aldready exists." )

    def search(self, key):
        for node in self.nodes:
            if node.key == key:
                return node
        return None

    def display(self):
        print("[Btree] Directory / File List:")
        for node in sorted(self.nodes, key=lambda x:x.key):
            print(" -", node.key)
