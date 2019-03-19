
# coding: utf-8

# In[63]:


import random
class myNode(object):
    def __init__(self,v=0):
        self.value=v
        self.left=None
        self.right=None
        
class myTree(object):
        def __init__(self):
            self.root=myNode(50)
            
            
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
    
def insert(root,node):
    if root is None:
        root=node
    else:
        if(root.value < node.value):
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if(root.left is None):
                root.left=node
            else:
                insert(root.left,node)
                
def test():
    numbers=[]
    for x in range(5):
        numbers.append(random.randint(1,101))
    tree1=myTree()
    
    for k in numbers:
        insert(tree1.root,myNode(k))
    inorder(tree1.root)
test()


# In[64]:


m1=myNode()
m2=myNode(60)
#m3=myNode(20)
t1=myTree()

insert(t1.root,m1)
insert(t1.root,m2)
insert(t1.root,m3)
#t1.root.right.value
inorder(t1.root)

