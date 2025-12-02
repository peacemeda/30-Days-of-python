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

#Exercise 3
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