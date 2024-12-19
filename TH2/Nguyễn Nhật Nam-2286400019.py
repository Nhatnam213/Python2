class Node():
    def __init__(self, value):
        self.data = value
        self.lefttree = None
        self.righttree = None
        self.height = 1

class AVLtree():
    def getheight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getheight(root.lefttree) - self.getheight(root.righttree)

    def leftRotate(self, notBalancedTree):
        tempTreeFirst = notBalancedTree.righttree
        tempTreeSecond = tempTreeFirst.lefttree

        tempTreeFirst.lefttree = notBalancedTree
        notBalancedTree.righttree = tempTreeSecond

        notBalancedTree.height = 1 + max(self.getheight(notBalancedTree.lefttree), self.getheight(notBalancedTree.righttree))
        tempTreeFirst.height = 1 + max(self.getheight(tempTreeFirst.lefttree), self.getheight(tempTreeFirst.righttree))

        return tempTreeFirst

    def rightRotate(self, notBalancedTree):
        tempTreeFirst = notBalancedTree.lefttree
        tempTreeSecond = tempTreeFirst.righttree

        tempTreeFirst.righttree = notBalancedTree
        notBalancedTree.lefttree = tempTreeSecond

        notBalancedTree.height = 1 + max(self.getheight(notBalancedTree.lefttree), self.getheight(notBalancedTree.righttree))
        tempTreeFirst.height = 1 + max(self.getheight(tempTreeFirst.lefttree), self.getheight(tempTreeFirst.righttree))

        return tempTreeFirst

    def insertNode(self, root, value):
        if not root:
            return Node(value)

        if value < root.data:
            root.lefttree = self.insertNode(root.lefttree, value)
        else:
            root.righttree = self.insertNode(root.righttree, value)

        root.height = 1 + max(self.getheight(root.lefttree), self.getheight(root.righttree))

        balance = self.getBalance(root)

        if balance > 1:
            if value < root.lefttree.data:
                return self.rightRotate(root)
            else:
                root.lefttree = self.leftRotate(root.lefttree)
                return self.rightRotate(root)

        if balance < -1:
            if value > root.righttree.data:
                return self.leftRotate(root)
            else:
                root.righttree = self.rightRotate(root.righttree)
                return self.leftRotate(root)

        return root

    def deleteNode(self, root, key):
        if not root:
            return root

        if key < root.data:
            root.lefttree = self.deleteNode(root.lefttree, key)
        elif key > root.data:
            root.righttree = self.deleteNode(root.righttree, key)
        else:
            if not root.lefttree or not root.righttree:
                if not root.lefttree:
                    temp = root.righttree
                else:
                    temp = root.lefttree
                root = None
                return temp
            else:
                temp = self.findMinValue(root.righttree)
                root.data = temp.data
                root.righttree = self.deleteNode(root.righttree, temp.data)

            if not root:
                return root
            root.height = 1 + max(self.getheight(root.lefttree), self.getheight(root.righttree))

            balance = self.getBalance(root)

            if balance > 1:
                if key < root.lefttree.data:
                    return self.rightRotate(root)
                else:
                    root.lefttree = self.leftRotate(root.lefttree)
                    return self.rightRotate(root)

            if balance < -1:
                if key > root.righttree.data:
                    return self.leftRotate(root)
                else:
                    root.righttree = self.rightRotate(root.righttree)
                    return self.leftRotate(root)

            return root

        def findMinValue(self, root):
            current = root
            while current.lefttree:
                current = current.lefttree
            return current

        def preOrderTraversal(self, root):
            if root:
                print(root.data, end=' ')
                self.preOrderTraversal(root.lefttree)
                self.preOrderTraversal(root.righttree)

        if __name__ == "__main__":
            avl_tree = AVLtree()
            root = None

            # Chèn các giá trị vào cây
            values_to_insert = [20, 30, 41, 10, 35, 35, 50]
            for value in values_to_insert:
                root = avl_tree.insertNode(root, value)

            print("Cây AVL sau khi chèn các giá trị:")
            avl_tree.preOrderTraversal(root)

            # Xóa một giá trị khỏi cây
            value_to_delete = 20
            root = avl_tree.deleteNode(root, value_to_delete)

            print("\nCây AVL sau khi xóa giá trị", value_to_delete, ":")
            avl_tree.preOrderTraversal(root)