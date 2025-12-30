There are 4 collection day type
1, list
2, tuple
3, set
4, dictionary
list() , []
methods
- .append()     - + to join two or more list or .extend()
- .insert()     - count()  
- .remove()     - index()          - reverse()
- del  to delete item from list
- sort()    - sorted()  The difference sort only works only on lists, and modifies the orginal list is also faster while sorted work on all collection, not change the orginal, 

return new sorted list safer if you want to keep the orginal data
🔍 Side-by-side comparison
Feature	              sort()	              sorted()
Modifies              original	✅ Yes	    ❌ No
Returns new list	    ❌ No	                ✅ Yes
Works on	            Lists only	          Any iterable
Speed	                Faster	              Slightly slower
Syntax	list.sort()	sorted(iterable)

Ex
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
['banana', 'orange', 'mango', 'lemon','apple']
fruits.insert(4,'lime')
print(fruit)
['banana', 'orange', 'mango', 'lemon','lime','apple']
