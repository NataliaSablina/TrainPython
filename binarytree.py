class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()



    # def __eq__(self, other):
    #     if self.data == other.data:
    #         if self.left is None or self.right is None or other.right is None or other.right is None:
    #             self.data.__eq__(other.data)
    #             return True
    #         elif self.left == other.left and self.right == other.right:
    #             if self.left is None or self.right is None or other.right is None or other.right is None:
    #                 self.data.__eq__(other.data)
    #                 return True
    #             self.left.__eq__(other.left)
    #             self.right.__eq__(other.right)
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    def __eq__(self, other):
        this = input(self.print_tree())
        other = other.print_tree()
        sorted_this = this.sort()
        sorted_other = other.sort()
        if sorted_this == sorted_other:
            return True
        return False


root = Node(12)
root.insert(6)
root.insert(13)
root.insert(18)
root.insert(2)

root.print_tree()
print("-------------------")
root1 = Node(12)
root1.insert(6)
root1.insert(13)
root1.insert(19)

root1.print_tree()
print(root == root1)