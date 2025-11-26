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