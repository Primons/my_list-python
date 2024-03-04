mylist=[10,20,30,40]
print("My initial list:", mylist)
#add 15 at the second position 
mylist.insert(1, 15)
print("My list after inserting 15 in the second position:", mylist)
#extend
mylist.extend([50, 60, 70])
print("My list after extending:", mylist)
#remove
mylist.remove(70)
print("My list after removing the last element:", mylist)
#Sorted_list
Sortedlist= sorted(mylist)
print("Ascending order:", Sortedlist)
#Finding the index of 30
Index= Sortedlist.index(30)
print(Index)