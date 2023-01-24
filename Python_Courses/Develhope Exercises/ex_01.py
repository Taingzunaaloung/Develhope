print('Exercise 1')
firstname='Mario'
print(firstname)

print('Exercise 2')
Age=25
print(Age)

print ('Exercise 3')
sentence= 'Hello, I\'m Mario!'
print(sentence)

print ('Exercise 4')
amount_1=float(2022.22)
amount_2=2022.22
print(amount_1)
print(amount_2)

print ('Exercise 5')
var_1 = ('True')
var_2 = ('true')
var_3 = ('True')
print(var_1, var_2, var_3)

print('Exercise 6')
my_first_Name = 'Mario'
print(my_first_Name)
print('Although the \'2\' after first is not an illegal character, it has been removed to give better meaning to the variable')

print('Exercise 7')
string='single quote'
print (string)
print ("both single and double quotes can be used to define a string and if the string contains one, the other can be used to define the whole string")

print ('Exercise 8')
Name, Age, Colour = ('Francis', 20, 'Black')
print(Name, Age, Colour)
print('Exercise 5 was initially interpreted as exercise 8, although not inacurrate, i think that was not the thought behind the question and it has been rectified')

print ('Exercise 9')
a=10
b='twenty'
print('Swapping a and b')
c=a
a=b
b=c
print(a,b)
print('Alternatively, they can be swapped as follows')
a, b = b, a
print (a,b)

print ('Exercise 10')
print('just realized this question and 9 are subsequent questions of 8, but since i cannot change my repo link, i am creating a new variable to answer this')
Intro='My name is Francis and I am a Ghanaian'
len(Intro)

print ('Exercise 11')
a = 'hello' #capitalize
b = 'tom' #uppercase
c = 'LAURA' #lowercase
question = 'How are you' #change o in e
age_question = 'How old are you?' #use the correct method to create a string for each word
print(a.capitalize())
print(b.upper())
print(c.lower())
print(question.replace('o','e'))
print(age_question.split()) 

print('Exercise 12')
name = 'Francis'
age = 28
hello = (f"Hello, My name is {name}! I'm {age} years old.")
print(hello)

print('Exercise Operators - 1') #Amended
print(False and True) 

print('Exercise Operators - 2') #Amended
print(False and (0 != 0 or True)) # Should print True (original question)
print(False or (0 != 0 or True))  # I don't understand the comment "check the content of the question !!" if changing 'and' to 'or' is wrong

print('Exercise Operators - 3')
print(23 % 7)

print('Exercise Operators - 4') #Amended
print(not ("testing" == "testing" and "Mario" == "Cool Guy")) # Should print True

print('Exercise Operators - 5')
firstName = "Mario"
lastName = "Rossi"
sentence = f'"{firstName} {lastName}"'
print(sentence) # Should print "Mario Rossi"

print('Exercise Operators - 6')
brands = ['adidas', 'balenciaga', 'nike', 'gucci']
print('nike' in brands)

print('Exercise Operators - 7')
print('reebok' not in brands)

print('Exercise Methods - 1')
print('In jupyter notebook, there is no need to include the print command to know the data type, or for that matter run any code but i use it because i am coding in vs code')
print(type(1))

print('Exercise Methods - 2')
num1 = 12
num2 = 7.532
num3 = 6 + 9j
num4 = 3.234234
num5 = 8.0349
##
num1 = float(num1)
num2 = int(num2)
num3 = complex(num3)
num4 = round(num4)
num5 = round(num5)
##
print(num1, num2, num3, num4, num5)
print(type(num1), type(num2), type(num3), type(num4), type(num5))

print('Exercise Methods - 3')
num1_str = str(num1)   # question 1
print(num1_str)

print(len(num1_str))  # question 2. length of string
print(num1_str[2])  # question 3. third element of string
print(num1_str[2:6])  # question 4. 3-5 elements of string

if not isinstance(num2, str): # question 5
    num2 = str(num2)
print(num2)

if not isinstance(num3, str): # question 6
    num3 = str(num3)
print(num3)

string = 'Python is interesting'
string_with_0 = "0" + string # question 7
print(string_with_0)

print(string_with_0[:4]) # question 8. characters of string_with_0 from start to position 4
print(string_with_0[4:]) # question 9. characters of string_with_0 from position 5 until the end
print(string_with_0[5:8])
print(string_with_0[-17:-14]) # question 10. negative indexing to reach the "567"

print('Exercise Conditions - 1')
num1 = 335 
num2 = 66
if num1 > num2:
    print(True)
else:
    print(False)

print('Exercise Conditions - 2')
number1 = 66 
number2 = 66
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
   print(f"{number2} is greater than {number1}") 
else:
    print(f"{number1} equals to {number2}")

print('Exercise Conditions - 3')
import random
number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
if number1 > number2:
    print(f"{number1} greater than {number2}")
elif number1 < number2:
    print(f"{number1} is less than {number2}")
else:
    print(f"{number1} is equal to {number2}")  

print('Exercise Conditions - 4')
number1 = random.randint(-100,100)
number2 = random.randint(-100,100)
if abs(number1) > abs(number2):
     print(f"{number1}'s absolute value greater than {number2}'s absolute value")
elif abs(number1) < abs(number2):
    print(f"{number1}'s absolute value less than {number2}'s absolute value")
else:
    print(f"{number1}'s absolute is equal to {number2}'s absolute value")  

print ('PYTHON PART 2')

print ('Iterators - While Loop')
i = 1 
while i <6:
    print("*"*i)
    i = i + 1

print ('Iterators - For Loop')
for i in range(1,6):
    if i%2==0:
        continue
    else:
        print("*"*i)