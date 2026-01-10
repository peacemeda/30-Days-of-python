#Exercise 1

#1 created day_2 repo and variable.py file
#2 Day2: 30 Days of python programming
first_name = 'Medhanie'
last_name = 'Meshesha'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'Los Angeles'
age = 43
year = 2025
is_married = True
is_true = 1
is_light = False
days, language = 30, 'python'


#Exercise 2

"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

#1 data type
print(type(10))
#2
print(len(first_name))
#3
print(len(first_name) == len(last_name))
#4
num_one, num_two = 5, 4

#5
total = num_one + num_two
print(total)
#6
diff = num_one - num_two
print('6, Num_one - Num_two: ', diff)
#7
product = num_one * num_two
print('7, Num_one * Num_two: ', product)
#8
division = num_one / num_two
print('8, Num_one / Num_two: ', division)
#9
reminder = num_one % num_two
print('9, Num_one % Num_two: ', reminder)
#10
exp = num_one ** num_two
print('10, Num_one ** Num_two: ', exp)
#11
floor_division = num_one // num_two
print('11, Num_one // Num_two: ', floor_division)
#12 
radius = 30
#area of a circle pi * r^2
import math

area = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print(f'12,i Area of a circle is  {area:.2f} metersquare.')
print(f'12,ii The circumfernce of a circle is {circum_of_circle:.2f} meter')
radius = int(input('Enter the radius: '))
area = math.pi * radius ** 2
print(f'12,iii Area of a circle after user input  {area:.2f} metersquare.')

#13
first_name = input('Enter your First Name ')
last_name = input('Enter your Last Name: ')
country = input('Enter your Country: ')
age = int(input('Enter your age: '))
print(f'The first Name is {first_name} Last Name is {last_name} country is {country} and age {age}')

#14 
help('keywords')

#Exercise 3

"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
#1
age = 20
#2
height = 5.7
#3
compile_num = 1 + 3j
#4
base = float(input('Enter base: '))
height = float(input('Enter height '))
area_triangle = 0.5 * base * height
print(f'The area of a triangle is: {area_triangle:.2f}')

#5
side_a = float(input('Enter the first side: '))
side_b = float(input('Enter the first side: '))
side_c= float(input('Enter the first side: '))
print(f'The perimeter of a triangle is {side_a + side_b + side_c:.2f}')

#6
length = float(input('Enter lenght a rectangle: '))
width = float(input('Enter width of rectangle: '))
print(f'The length is {length} and width of a triangel is {width}. area is lenght x width is {length * width} and perimeter  2 x (length * width) is {2 * length * width}')
#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input('Enter the radius: '))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print(f'The area of a circle {area:.2f} and the circumference of a circle is {circumference:.2f}')

#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y = mx + b
m1 = 2
b = -2
y = b
x = -b /m1
print(f'The x-intercept is {x} and y-intercept is {y} and slope is {m1}')

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
values =list(zip((2,2), (6,10)))
x1, x2, y1, y2 = values[0][0], values[0][1], values[1][0], values[1][1]
print(f'{x1} {x2} {y1} {y2} ')

m2 = (y2 - y1)/(x2- x1)
# d = √((x_2 - x_1)² + (y_2 - y_1)²)
d = math.sqrt(pow((x2 -x1),2) + pow((y2 - y1),2))
print(f'The slope is {m2:.2f} and the Euclidean distance is {d:.2f}')

# 9 compare the slopes in 8 and 9

print(f'comparing slope 1 and 2 {m1 == m2} ')
#11 calculate y for y = x^2 + 6x + 9


#12 find the length of python
print(len('python'))
print(len('python') > len('dragon'))

#13
print('on','python' and 'on' in 'dragon')

#14
print('jargon' in 'I hope this course is not full of jargon')

#15

#16 Find the length of the text python and convert the value to float and convert it to string
leng = len('python')
print(leng)
leng = float(len('python'))
print(str(leng))

#17
num = int(input('Enter number: '))
if num % 2 == 0:
  print('Even')
else:
  print('Not even')

#18
if 7//3 == int(2.7):
  print('True')

#19
if 10 == '10':
  print('True')
else:
  print('False')

#20
int(9.8) == 10

#21
hour = float(input('Enter hours: '))
rates = float(input('Enter rate per hour: '))
hourly_rate = hour * rates
print('Your weekly earning is: ',hourly_rate)

#22
year_lived = float(input('Enter the number of years you live '))
year_per_second = year_lived * 365 * 24 * 3600
print(f'You have lived for {year_per_second} seconds.')

#23 write python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
for num in range(1, 6):
  print(num, 1 , num**2, num**3)

# Exercise 4

"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
w = ['Thirty', 'Days', 'Of', 'Python']
r = ' '.join(w)
print(r)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

w = ['Coding', 'For' , 'All']
r = ' '.join(w)
print(r)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

  #4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
print(company.strip('Coding'))

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
print(company.startswith('Coding'))
print(company.index('Coding'))
print(company.count('Coding') > 0)
print('Coding' in company)

# 11 Replacing the Coding For all to Python for all
word = 'Coding For all'
print(word.replace('Coding', 'Python'))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
word = 'Python for Everone'
print(word.replace('Everone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
word = 'Coding For All'

 #14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech.split(','))

#15 What is the character at index 0 in the string Coding For All.
word = 'Coding For All'
print(word[0])

#16 What character is at index 10 in "Coding For All" string.
word = 'Coding For All'
char = word[10]
print(repr(char))

#17 What character is at index 10 in "Coding For All" string.

word = 'Coding For All'
char = word[10]
print(repr(char))

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
lang = 'Python For Everone'
acr = ''.join(char[0].upper() for char in lang.split())
print(acr)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
text = 'Coding For ALl'
acr1 = ''.join(word[0].upper() for word in text.split())

#20 Use index to determine the position of the first occurrence of C in Coding For All.
text = 'Coding For All'
print(text.find('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
text = 'Coding For All'
print(text.index('F'))

#22Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = 'Coding For All People.'
print(text.rindex('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.split('because'))

#26 

#27

#28 Does ''Coding For All' start with a substring Coding?
text = 'Coding For All'
print(text.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?
text = 'Coding For All'
print(text.endswith('Coding'))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '   Coding For All      '
print(text.strip(' '))

#31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

text = '30DaysOfPython'
text1 = 'thirty_days_of_python'

print(text.isidentifier())
print(text1.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

text = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
word = ' # '.join('text')
print('#',word)

#33 Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')

#35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %d meters square.'%(radius, area))

# 36 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print(f'{8} + {6} = {8+6}')
print(f'{8} - {6} = {8-6}')
print(f'{8} * {6} = {8*6}')
print(f'{8} / {6} = {8/6:.2f}')
print(f'{8} % {6} = {8%6}')
print(f'{8} // {6} = {8//6}')
print(f'{8} ** {6} = {8**6}')


# Exercise 5

"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

# Declare an empty list
lst = list()
lst1 = []

#1 Declare a list with more than 5 items
lst = [1,2,'age','item',True,0]

#2 Find the length of your list
len(lst)

#3 Get the first item, the middle item and the last item of the list
print(lst[0])
print(lst[3])
print(lst[-1])

#4Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixted_data_types = ['medhanie',40, 1.71,'is_married','4906 w 63rd st, Los Angeles']
#5 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companie = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
#6 Print the list using print()
print(it_companie)
#7 Print the number of companies in the list
print(len(it_companie))
#8 Print the first, middle and last company
print(it_companie[0])
print(it_companie[3])
print(it_companie[-1])
#9 Print the number of companies in the list
print(len(it_companie))

#10 Print the list after modifying one of the companies
print(it_companie)

#11Add an IT company to it_companies
it_companie.append('uber')

#12 Insert an IT company in the middle of the companies list
it_companie.insert(3,'Grub hub')

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companie[2] = it_companie

#14 Join the it_companies with a string '#;  '
resual = '#; '.join(it_companie)

#15 Check if a certain company exists in the it_companies list.
print('Apple' in it_companie)

#16 Sort the list using sort() method
it_companie.sort()

#17 Reverse the list in descending order using reverse() method
it_companie.reverse()

#18 Slice out the first 3 companies from the list
print(it_companie[:3])

#19 Slice out the last 3 companies from the list
print(it_companie[-3:])

#20 Slice out the middle IT company or companies from the list

#21 Remove the first IT company from the list
it_companie.remove('Amazon')
it_companie.pop()

#22 Remove the middle IT company or companies from the list
length = len(it_companie)

if length % 2 == 1:
    # odd number of companies → one middle
    middle = it_companie[length//2 : length//2 + 1]
else:
    # even number of companies → two middle
    middle = it_companie[length//2 - 1 : length//2 + 1]

print(middle)

#23 Remove the last IT company from the list
print(it_companie.pop(-1))

#24 Remove all IT companies from the list
print(it_companie.clear())

#25Destroy the IT companies list
del it_companie


# 26 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

"""
Exercises: Level 2
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]

ages.append(min_age)
ages.append(max_age)

n = len(ages)
if n % 2 == 1:
    # Odd length
    median = ages[n // 2]
else:
    # Even length
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2

print("Median age:", median)

sum_age = sum(ages)
average = sum_age // len(ages)
print(f'The average age is {average:.2f}')

#Exercise 6
#1 create an empty tuple
empty_tuple = ()

#2Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothes = ('Hani','John','Miki')
sisters = ('Dana','Saba','Merry')

#3Join brothers and sisters tuple and assign it to siblings
sibling = brothes + sisters

#4 How many sibling do you have
len(sibling)

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family = list(sibling)
family.insert(0,'Mymother')
family.insert(1,'myfather')

# 6 unpack siblings and parents from family_members
father, mother , *sibling = family
print(father, mother)
print(sibling)

#7 food_stuff_tp to food_stuff list
food_stuff_tp = ('pasta','pizza','hamberger', 'taco', 'barrito')
food_stuff = list(food_stuff_tp)

#8 slice out the middle item or items from the food_stuff_tp or food_stuff_it

num = len(food_stuff_tp)
if num % 2 == 1:
   middle = food_stuff_tp[num // 2]
else:
   middle = (food_stuff_tp[num // 2 + 1])

# 9 Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[:3])
print(food_stuff[-3:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# 10 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Denmark' in nordic_countries)

#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)


#///////////////////////////////////////////////

# Exercise 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Find the length of the set it_companies
len(it_companie)
# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Uber','Lyft','Grubhub'])

# 4 Remove one of the companies from the set it_companies
it_companies.remove('Uber')

# 5 What is the difference between remove and discard
#remove only remove item from the set if the item is in the set but return error if the item not in the set
#whie discard don't return error

#///////////////////////////////////////////////////
#///////////////////////////////////////////////////

#Exercise 8

# 1 Create an empty dictionary called dog
dog = {}
# 2 Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Flefly'
dog.update({
    'color': 'white & black',
    'breed': 'Germen sheber',
    'legs': 4,
    'age': 12
})
#  3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and 
# address as keys for the dictionary

student = {
   'first_name': 'Meda',
   'last_name': 'Mesh',
   'gender': 'Male',
   'age': 34,
   'is_maried': True,
   'skills' :['Python', 'C++','Java'],
   'country': 'USA',
   'city': 'Los Angeles',
   'address': {
      'street': '123 Main St',
      'Zipcode': '90098'
   }

}
# 4 Get the length of the student dictionary
print(len(student))
# 5 Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# 6 Modify the skills values by adding one or two skills
student['skills'].extend(['HTML','CSS'])
# 7 Get the dictionary keys as a list
keys_list = list(student.keys())

# 8 Get the dictionary values as a list
vales_list = list(student.values())

# 9 Change the dictionary to a list of tuples using items() method
list_items = list(student.items())

# 10 Delete one of the items in the dictionary
del student['country']

# 11 Delete one of the dictionaries
del student