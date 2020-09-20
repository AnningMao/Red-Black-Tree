import BinarySearchTree
import TreeNode
import pickle
if __name__ == "__main__":

 numberPassed=0
 numberTests=0
 print("\n\n\nTesting 1 node creation-----------------------------------------------------------")
 try:
  numberTests+=1
  myNode = TreeNode.DSATreeNode(1, "one")
  print(myNode)
  numberPassed+=1
  print("Passed")
 except:
  print("Failed")
  Exception

 print("\n\n\nTesting 2 insert------------------------------------------------------------------")
 try:
  numberTests+=1
  Tree2=BinarySearchTree.DSABinarySearchTree(10,"10")
  Tree2.insert(7, "7")
  Tree2.insert(4, "4")
  Tree2.insert(9, "9")

  Tree2.insert(16, "16")
  Tree2.insert(12, "12")
  Tree2.insert(20, "20")
  Tree2.insert(14, "14")
  Tree2.insert(19, "19")
  Tree2.insert(26, "26")
  numberPassed+=1
  print("Passed")
 except:
  print("Failed")
  Exception
 '''
                      10
            7                    16
         4     9             12      20
                               14   19 26
 '''
 print("\n\n\nTesting 3 delete leaf node--------------------------------------------------------")
 try:
  numberTests+=1
  Tree2.delete(4)
  print("result after delete")
  print(Tree2.Traverse("pre"))
  print(Tree2.Traverse("in"))
  print(Tree2.Traverse("post"))
  numberPassed+=1
  print("Passed")
 except:
  print("Failed")
  Exception
 print("\n\n\nTesting 4 delete node with two children --------------------------------------------")
 try:
  numberTests+=1
  Tree2.delete(16)
  numberPassed+=1
  print("Passed")
 except:
  print("Failed")
  Exception
 print("\n\n\nTesting 5 Traversal --------------------------------------------")
 try:
  numberTests+=1
  print("result after delete")
  print(Tree2.Traverse("pre"))
  print(Tree2.Traverse("in"))
  print(Tree2.Traverse("post"))
  numberPassed+=1
  print("Passed")
 except:
  print("Failed")
  Exception

 print("\n\n\nTesting 6 maxium/minium------------------------------------------------------------")
 try:
  numberTests+=1
  print("max is:" + str(Tree2.getMax()))
  print("min is:" + str(Tree2.getMin()))
  print("height is" + str(Tree2.getheight()))
  numberPassed+=1
  print("Passed")
 except:
  Exception

 print("\n\n\nTesting 7 height------------------------------------------------------------")
 try:
  numberTests+=1
  print("height is" + str(Tree2.getheight()))
  numberPassed+=1
  print("Passed")
 except:
  Exception

 print("\n\n\nTesting 8 balance------------------------------------------------------------")
 numberTests+=1
 print("Failed")


 print("\n\n\ntesting 9 I/O----------------------------------------------------------------------")

 try:
  numberTests+=1
  while True:
   option=input("----------------Meue-----------------"
         "\n1)read a csv file"
         "\n2)read a serialized file"
         "\n3)write a csv file"
         "\n4)write a serialized file"
         "\n5)exit")
   if option=="1":
    with open("orderresult", "rb") as dataFile:
     traverFromFile = pickle.load(dataFile)
     print("\ndisplay Object from the CVS file")
     print(traverFromFile)


   elif option=="2":
    with open("Tree", "rb") as dataFile:
     ObjectFromFile = pickle.load(dataFile)
     print("\ndisplay Object from the serialized file")
     print(ObjectFromFile.Traverse("in"))

   elif option=="3":
    with open("orderresult", "wb") as sequence:  # write traversal
     traver = []
     selection = input(" which one would you like, inorder(in), preorder(pre) or postorder(post) traversal?")
     if selection == 'in':
      traver = Tree2.Traverse("in")
     elif selection == "pre":
      traver = Tree2.Traverse("pre")
     elif selection == "post":
      traver = Tree2.Traverse("post")
     pickle.dump(traver, sequence)

   elif option=="4":
    with open("Tree", "wb") as dataFile:  # write object
     pickle.dump(Tree2, dataFile)


   elif option=="5":
    break

   else:
    print("please input a number in 1-5")

  numberPassed += 1
  print("Passed")
 except:
  print("Failed")
  Exception










 # Print test summary
 print("\nNumber PASSED: ",numberPassed, "/", numberTests)
 print("-> ", numberPassed / numberTests * 100, "%\n")








