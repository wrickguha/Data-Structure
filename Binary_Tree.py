class Node:
    def __init__(self,data)->None:
        self.left = None
        self.right = None
        self.data = data

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            ## Add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)


        else:
            ## Add data to right subtree    

            if self.right:
                self.right.add_child(data)
            else:
                self.right= Node(data)

    def in_order_traversal(self):
        elements = []
        
        # Visit left tree 
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Visit root node
        elements.append(self.data)

        # Visit Right tree
        if self.right:
            elements += self.right.in_order_traversal()


        return elements

def build_tree(elements):
    root = Node(elements[0])

    for i in range(1,len(elements)):
         root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [3,2,1,4,5,9,7,8]
    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())


"""
    def show(self):
        if self.left:
            self.left.show()

        print(self.data)

        if self.right:
            self.right.show()

root = Node(100)
r_left = Node(99)
r_right = Node(101) 

root.left = r_left
root.right = r_right

root.show()
"""

"""

## Inorder traversal

def print_inorder(root):

    if root:
        # First Occur on left
        printInorder(root.left)

        # Then print data of node
        print(root.val)

        # Now recur on right child
        printInorder(root.right)
"""



"""

# Preorder Traversal

def printPreorder(root):

    if root:
        # First print the data of node
        print(root,val)

        # Then recur on left child
        printPreorder(root.left)

        #Finally recur on right child
        printPreorder(root.right)

"""


"""
#Post Order Traversal

def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # then recur on right child
        printPostorder(root.right)

        # the data of the node
        print(root.val)


"""

