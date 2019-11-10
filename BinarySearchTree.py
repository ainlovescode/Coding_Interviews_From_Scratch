class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_insert(root, newNode):
    if root.val is None:
        raise Exception("Missing root node")
    elif newNode.val is None:
        raise Exception("New node not initialised yet")            
    else:
        if newNode.val > root.val:
            if root.right is None:
                root.right = newNode
            else:
                bst_insert(root.right, newNode)
        elif newNode.val < root.val:
            if root.left is None:
                root.left = newNode
            else:
                bst_insert(root.left, newNode)
        else:
            root.val = val

'''
SAMPLE BST:
          25
     15          50
  10    20    40   60
 5 11 16 22 39 41 55 70

'''

	
def preorder(root): # root, left, right
    print(root.val)		
    if root.left != None:
        preorder(root.left)
    if root.right != None:
        preorder(root.right)
	
	
def inorder(root): # left, root, right
    if root.left != None:
        inorder(root.left)
    print(root.val)
    if root.right != None:
        inorder(root.right)

def postorder(root): # left, right, root
    if root.left != None:
        postorder(root.left)
    if root.right != None:
        postorder(root.right)
    print(root.val)

root = Node(4) 
bst_insert(root, Node(5))
bst_insert(root, Node(2)) 
bst_insert(root, Node(1)) 
bst_insert(root, Node(3))

print("Preorder traversal of binary tree is")
preorder(root) 
  
print("\nInorder traversal of binary tree is")
inorder(root) 
  
print("\nPostorder traversal of binary tree is")
postorder(root)	
	

		
