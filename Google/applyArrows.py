import sys
sys.path.append('../')

import pranavdefinedMethods as pdm

bstNodeR = pdm.returnBSTRight([15,10,20,8,12,16,25])

def applyArrows(listNodes):
    childQueue = []
    if (len(listNodes) == 0):
        return 
    for index,node in enumerate(listNodes):
        if (index != len(listNodes)-1):
            # print("apply arrow for " + str(node.data) + " => "+ str(listNodes[index+1].data))
            node.rightRightChild = listNodes[index+1]
        childQueue.extend(node.getChildren())
    applyArrows(childQueue)


applyArrows([bstNodeR])

pdm.bfsPrint([bstNodeR])

