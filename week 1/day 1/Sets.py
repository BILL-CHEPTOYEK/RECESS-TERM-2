#store values in a single array.
#unchangeable but one can add and reomve items.
#SETS EXERCISE, LENGTH, DATA TYPE, ACCESSING ITEMS IN A SET, ADD ITEMS, ADD TWO SETS
set1={"rice", "matooke", "irish"}
lenth_of_set1=len(set1)
datatype=type(set1)
print(datatype)
print(set1)
#to access a single item in the set, sets are unordered hence we can't access individual items using indicies
#But we can check for presence of an item

if "matooke" in set1:
    print("Item exists!")
else:
    print("Item not found!")


#adding items to a set
set1.add("yams")
print(set1)
#adding two sets
#take the other set to be
set2={"broccoli","Sweet potatoes"}

general_set= set1 | set2
print(general_set)
