import math
class R_BTreeNode():
    def __init__(self,inKey,inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None
        self.color=0#0 is red 1 is black

    def __str__(self):
        return ("Key: " + str(self._key) + " Value: " + str(self._value))

    def setKey(self, key):
        self._key = key

    def getKey(self):
        return self._key

    def setValue(self, value):
        self._value = value

    def getValue(self):
        return self._value

    def setLeft(self, left):
        self._left = left

    def getLeft(self):
        return self._left

    def setRight(self, right):
        self._right = right

    def getRight(self):
        return self._right
class R_BTree():
    def __init__(self,key,value):
        newNode = R_BTreeNode(key, value)
        self._root=newNode

    def find(self,key):
        return self._findRec(key,self._root)
    def insert(self,key,value):
        return self._insertRec(key,value,self._root)
    def delete(self, key):
        return self._deletRec(key,self._root)
    def getMax(self):
        return self._maxRec(self._root)
    def getMin(self):
        return self._minRec(self._root)
    def getheight(self):
        return self._heightRec(self._root)


    def _findRec(self,key,cur):
        value=None
        if cur==None:
            print("key:"+str(key)+"not found")
        elif key==cur._key:
            value=cur._value
        elif key<cur._key:
            value=self._findRec(key,cur._left)
        else:
            value=self._findRec(key,cur._right)
        return value
    def _insertRec(self,key,value,cur):
        updateNode=cur
        if cur==None: #find null point
            newNode=R_BTreeNode(key,value)
            print(newNode)
            updateNode=newNode

        elif key==cur._key:
            raise ValueError("key:"+key+"already exist")
        elif key<cur._key:
            cur.setLeft(self._insertRec(key,value,cur._left))
        else:
            cur.setRight(self._insertRec(key,value,cur._right))
        return updateNode

#delet part
    def _deletRec(self,key,cur):
        updateNode=cur
        if cur==None:
            print("key:"+str(key)+"not found")
        elif key==cur.getKey():
            updateNode=self._deletNode(cur)
        elif key<cur.getKey():
            cur.setLeft(self._deletRec(key,cur.getLeft()))
        else:
            cur.setRight(self._deletRec(key,cur.getRight()))

        return updateNode
    def _deletNode(self,delNode):
        updateNode=None
        if delNode.getLeft()==None and delNode.getRight()==None:#no children
            print("no children")
            updateNode=None
        elif delNode.getLeft()!=None and delNode.getRight()==None:#one left-child
            updateNode=delNode.getLeft()
            print("one left-child")
        elif delNode.getRight()!=None and delNode.getLeft()==None:#one right-child
            updateNode=delNode.getRight()
            print("one right-child")
        else:# two children
            print("two children")
            updateNode=self._promoteSuccessor(delNode.getRight())
            if updateNode !=delNode.getRight():
                updateNode.setRight(delNode.getRight())
            updateNode.setLeft(delNode.getLeft())
        return updateNode
    def _promoteSuccessor(self,cur):# successor is the left most child of the right subtree
        successor=cur# this current node don't have left node
        if cur.getLeft()!=None:
            successor=self._promoteSuccessor(cur.getLeft())
            if successor==cur.getLeft():
                cur.setLeft(successor.getRight())
        return successor

#max and min
    def _minRec(self,cur):
        if (cur.getLeft()!=None):
            minKey=self._minRec(cur.getLeft())
        else:
            minKey=cur.getKey()
        return minKey
    def _maxRec(self,cur):
        if (cur.getRight()!=None):
            maxKey=self._maxRec(cur.getRight())
        else:
            maxKey=cur.getKey()
        return maxKey
    def _heightRec(self,cur):
        if cur==None:
            htSoFar=-1
        else:
            leftHt=self._heightRec(cur.getLeft())
            rightHt=self._heightRec(cur.getRight())
            if leftHt>rightHt:
                htSoFar=leftHt+1
            else:
                htSoFar=rightHt+1
        return htSoFar

#traver
    def Traverse(self,selection):

        if selection=="pre":
            print("\n\npreorder result")
            Sequence=[]
            self._preOrderTraverse(self._root,Sequence)
            return Sequence
        if selection == "in":
            Sequence = []
            print("\n\ninorder result")
            self._inOrderTraverse(self._root,Sequence)
            return Sequence
        if selection == "post":
            Sequence = []
            print("\n\npostorder result")
            self._postOrderTraverse(self._root,Sequence)
            return Sequence
    def _preOrderTraverse(self,node,Sequence):

        if node==None:
            return None
        #print(node.getValue(),end=" ")
        Sequence.append(node.getValue())
        self._preOrderTraverse(node.getLeft(),Sequence)
        self._preOrderTraverse(node.getRight(),Sequence)
    def _inOrderTraverse(self,node,Sequence):
        if node==None:
            return None
        self._inOrderTraverse(node.getLeft(),Sequence)
        #print(node.getValue(),end=" ")
        Sequence.append(node.getValue())
        self._inOrderTraverse(node.getRight(),Sequence)
    def _postOrderTraverse(self, node,Sequence):
        if node == None:
            return None
        self._postOrderTraverse(node.getLeft(),Sequence)
        self._postOrderTraverse(node.getRight(),Sequence)
        #print(node.getValue(),end=" ")
        Sequence.append(node.getValue())

#draw this tree
    #get depth
    def TreeDeep(self):
        return self._TreeDeep(self._root)
    def _TreeDeep(self, node):
        if node == None:
            return 0
        left = self._TreeDeep(node.getLeft()) + 1
        right = self._TreeDeep(node.getRight()) + 1
        return left if left > right else right
    #drawing
    def draw(self):
        Depth=self.TreeDeep()
        print(Depth)
        Sequence=[[]for i in  range(Depth+1)]
        self._drawTraverse(self._root, Sequence, 0)
        for i in range (Depth+1):
            interval=math.ceil(2**Depth/((2**i)+1))
            for ele in Sequence[i]:
                #add interval
                for j in range (interval):
                    print(" ",end="")
                #-------------
                print(ele,end="")
            print("")
        return Sequence
    def _drawTraverse(self,node,Sequence,level):

        if node==None:
            Sequence[level].append(" ")
            return None
        #print(node.getValue(),end=" ")
        Sequence[level].append(node.getValue())
        self._drawTraverse(node.getLeft(),Sequence,level+1)
        self._drawTraverse(node.getRight(),Sequence,level+1)