class Node:
    def __init__(self, data):
        self.value = data
        self.left_tree = None
        self.right_tree = None

    def printtree(self):
        if self.left_tree != None:
            self.left_tree.printtree()
        print(self.value)
        if self.right_tree != None:
            self.right_tree.printtree()

    def inserttree(self, data):
        if data > self.value:
            if self.right_tree == None:
                self.right_tree = Node(data)
            else:
                self.right_tree.inserttree(data)

        elif data < self.value:
            if self.left_tree == None:
                self.left_tree = Node(data)
            else:
                self.left_tree.inserttree(data)

    def search(self, data):
        if data == self.value:
            return 1
        elif data > self.value:
            if self.right_tree != None:
                return self.right_tree.search(data)
            else:
                return 0
        else:

            if self.left_tree != None:
                return self.left_tree.search(data)
            else:
                return 0


arr = [1, 8, 3, 5, 6, 2, 4, 7, 9]
root = Node(arr[0])
for i in arr[1:]:
    root.inserttree(i)
bst = root.search(12)
print(bst)