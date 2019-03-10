import sys
sys.path.append('../')

import pranavdefinedMethods as pdm

bstNode = pdm.returnBST([15,10,20,8,12,16,25])

print("inOrder - Traversal")
# inorder traversal of the BST
pdm.inOrderTraversal(bstNode)
print("preOrder - Traversal")
#  preorder traversal of the BST
pdm.preOrderTraversal(bstNode)
print("postOrder - Traversal")
# postorder traversal of the BST
pdm.postOrderTraversal(bstNode)