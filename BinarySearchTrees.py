
# coding: utf-8

# In[63]:


import random
class Node(object):
    def __init__(self,v=0):
        self.value=v
        self.left=None
        self.right=None
        
class Tree(object):
    def __init__(self):
        self.root=Node()
        
        
def insert(root,node):
    if root:
        if(root.value < node.value):
            if root.right:
                insert(root.right,node)
            else:
                root.right=node
        else:
            if root.left:
                insert(root.left,node)
            else:
                root.left=node
        
    else:
        root=node


                
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.value,end=" ")
        preorder(root.left)
        preorder(root.right)
    
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=" ")
        
def test():
    numbers=[]
    for x in range(5):
        numbers.append(random.randint(1,101))
    tree1=Tree()
    
    for k in numbers:
        insert(tree1.root,Node(k))
    inorder(tree1.root)
    print()
    preorder(tree1.root)
    print()
    postorder(tree1.root)

