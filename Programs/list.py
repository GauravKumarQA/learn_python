#Initialiselist
list=["One","Two","Three"]
print(list)
list2=[1,"Two1",3.0]
print(list2)

#Access list element
print(list[1])
print(list[0:2])
print(list2[:1])


#Contains in the list
if list2[1] in  list:
    print(str(list2[1]) + " Is present in list : " + str(list))
else:    
    print(str(list2[1]) + " Is not present in list : " + str(list))
    
#Changing a value in the list    
list2[1]=2
print(list2)    

#Replacing values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["replace blackcurrant", " replace watermelon"]
print(thislist)

#insert()-> Inserting value without replacing
thislist.insert(2,"insert grapes")
print(thislist)

#append() -> to add any value
thislist.append("i am appended")
print(thislist)

#extend() ->add two list or any iterable object [tuple set dictionary etc..]
appendTuple=("I","am","tuple by extend")
thislist.extend(appendTuple)
print(thislist)

#remove() -> remove specific items
thislist.remove("orange")
print("orange has been removed" + str(thislist))

#pop() -> remove item by index or remove last item
thislist.pop(0);
print("0 index item removed" + str(thislist))
thislist.pop()
print("last item has been removed by pop function without param" + str(thislist))

#del keyword -> to remove item by index
del thislist[0]
print("Remove 0 index value by del keyword" + str(thislist))

#clear() -> clear whole list
thislist.clear()
print("List has been cleared : " + str(thislist))

#del delete the list by del keyword
del thislist
print("List has been deleted by del listName")

#sort() -> sort a list 
listOfNumbers = [1,2,3,4,5]
listOfNumbers.sort()
print(listOfNumbers)
#sorting of string values
listOfString = ["A","a","B","b","c"]
listOfString.sort()
print(str(listOfString) + "sort method will sort capital first." )

#reverse() -> reverse a list
listOfString.reverse()
print("List of string has been reveresed " + str(listOfString))

#copy() -> copy a list to another list i.e equals only share address
list1 = [1]
list2 = list1.copy()
list1.clear()
print(list2)



