# it is also bfs and three types of traversal like preorder(root->left->right),postorder(left->right->root),inorder(left->root->right)
class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def display(root):
    if root==None:
        return
    print(root.val)
    display(root.left)
    display(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
display(root)

