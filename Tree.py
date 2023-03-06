#------------------USER_DIFINE DATA STRUCTURE-----------------------

#4. TREE

#---Tree is a non-linear but hierarchical data structure that is appropiate for storing data
#---that aren't linear connected to each other but form a hierarchy

#Example

class node:
    def __init__(self,ele):
        self.ele=ele
        self.left=None
        self.right=None


def preorder(self):
    if self:
    
        print(self.ele)
        preorder(self.left)
        preorder(self.right)

n=node('First')
n.left=node('Second')
n.right=node('Third')
preorder(n)