class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def insertNode(self, child):
        if (self.data > child.data):
            if (self.leftChild is None):
                self.leftChild = child
            else:
                self.leftChild.insertNode(child)
        else:
            if (self.rightChild is None):
                self.rightChild = child
            else:
                self.rightChild.insertNode(child)

class NodeR:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.rightRightChild = None
    
    def insertNode(self, child):
        if (self.data > child.data):
            if (self.leftChild is None):
                self.leftChild = child
            else:
                self.leftChild.insertNode(child)
        else:
            if (self.rightChild is None):
                self.rightChild = child
            else:
                self.rightChild.insertNode(child)
    
    def getChildren(self):
        retQueue = []
        if (self.leftChild is not None):
            retQueue.append(self.leftChild)
        if (self.rightChild is not None):
            retQueue.append(self.rightChild)
        return retQueue
    
    def printPlease(self):
        dataHere = str(self.data) if self is not None else 'None'
        print("#### Node with data ####" + dataHere )
        rightR = str(self.rightRightChild.data) if self.rightRightChild is not None else 'None' 
        left = str(self.leftChild.data) if self.leftChild is not None else 'None'
        right = str(self.rightChild.data) if self.rightChild is not None else 'None'
        print("left : " + left + " right : " + right  + " rightRight : " + rightR )




def printThis(input):
    print("this method is defined by Pranav in his methods file => Input given is " + input)


# Returns a BST given a list of items(only integers)
def returnBST(items):
    #create a root node first
    root = Node(items.pop(0))
    for item in items:
        root.insertNode(Node(item))
    return root

def inOrderTraversal(node): #input is a bst tree root node
    #left nodes then the root and then the right nodes
    if (node.leftChild is not None):
        inOrderTraversal(node.leftChild)
    print(" node : " + str(node.data))
    if (node.rightChild is not None):
        inOrderTraversal(node.rightChild)

def preOrderTraversal(node):
    #root,left,right
    print("node => " + str(node.data))
    if (node.leftChild is not None):
        preOrderTraversal(node.leftChild)
    if (node.rightChild is not None):
        preOrderTraversal(node.rightChild)

def postOrderTraversal(node):
    #left,right,root
    if (node.leftChild is not None):
        postOrderTraversal(node.leftChild)
    if (node.rightChild is not None):
        postOrderTraversal(node.rightChild)
    print("node => " + str(node.data))

# Returns a BSTR given a list of items(only integers)
def returnBSTRight(items):
    #create a root node first
    root = NodeR(items.pop(0))
    for item in items:
        root.insertNode(NodeR(item))
    return root


def bfsPrint(queue):
    if (len(queue) == 0):
        return 
    currentNode = queue.pop(0)

    currentNode.printPlease()
    queue.extend(currentNode.getChildren())
    bfsPrint(queue)
    