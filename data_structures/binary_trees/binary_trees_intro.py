class Node (object):
  def __init__(self):
    self.right = None
    self.left = None
    self.value = None

class Tree (object):
  def __init__ (self):
    self.root = None

  def inOrderTraversal(self, node):
    if node is not None:
      self.inOrderTraversal(node.left)
      print(self.root.value)
      self.inOrderTraversal(node.right)
    

  def postOrderTraversal(self, node):
    self.postOrderTraversal(node.left)
    self.postOrderTraversal(node.right) 
    print(self.root.value)


  def preOrderTraversal(self, node):
    print(self.root.value)
    self.preOrderTraversal(node.left)
    self.preOrderTraversal(node.right) 

tree = Tree ()



