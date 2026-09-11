mylist = [2, 56, 43, 18, 29, 9]

mylist.append (66)      #removes an element tp the list
print (mylist)

mylist.remove (56)     #removes an element
print (mylist)

mylist.pop()          #removes the last element in the list
print (mylist)

mylist.sort ()       #ascending order to the list
print (mylist)

newlist = mylist.copy()
newlist.append (1001)
print (newlist)


newvalue = int(input("enter a number"))
if newvalue in mylist:
    print ("Element is in the list")
else:
    print ("Element not found")
