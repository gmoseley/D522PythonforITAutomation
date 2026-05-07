# ─── Challenge 1: Variables & Print ───────────────────────────────────────────
#nameFirst = input('First name: ')
#nameLast = input('Last name: ')
#age = input('Age: ')
#colorFavorite = input('Favorite color: ')
#print(f"Hello. My name is {nameFirst} {nameLast}. I am {age} and my favorite color is {colorFavorite}")

# ─── Challenge 2: User Input & Type Conversion ────────────────────────────────
#integerX = input('please input the first number: ')
#integerY = input('please input the second number: ')
#print(int(integerX) * int(integerY))

# ─── Challenge 3: If/Else Logic ───────────────────────────────────────────────
#age = input("How old are you? ")
#if int(age) < 18:
#    print('You are a minor')
#elif 18 <= int(age) <= 64:
#    print('You are an adult')
#elif int(age) >= 65:
#    print('You are a senior')

# ─── Challenge 4: Loops ───────────────────────────────────────────────────────
#userInput = input('Please enter a number: ')
#for i in range(1, int(userInput) + 1):
#    print(i)
#print(sum(range(1, int(userInput) + 1)))

# ─── Challenge 5: Functions ───────────────────────────────────────────────────
#def greet(name):
#    print(f'Hello {name}!')
#name = input('Please enter your name: ')
#greet(name)
#
#def add(x, y):
#    return int(x) + int(y)
#print(add(4, 5))

# ─── Challenge 6: Lists ───────────────────────────────────────────────────────
#fruits = ['apples', 'bananas', 'kiwi', 'mango', 'pineapple']
#print(fruits)
#print(fruits[0])
#print(fruits[-1])
#fruits.append('pears')
#print(fruits)
#fruits.remove('apples')
#print(fruits)

# ─── Challenge 7: Dictionaries ────────────────────────────────────────────────
#people = {"name":"Jordan", "age": 28, "city":"Portland"}
#print(people)
#print(people['name'],people['city'])
#people['job'] = "IT Tech"
#print(people['job'])
#people['city'] = 'Atlanta'
#print(people)

# ─── Challenge 8: Error Handling ──────────────────────────────────────────────
#userNumber = input('Please enter a number to divide by 100: ')
#try:
#    result = int(userNumber) / 100
#    print(result)
#except ZeroDivisionError:
#    print('You may not divide by zero')
#except ValueError:
#    print('You did not enter an integer')

# ─── Challenge 9: File I/O ────────────────────────────────────────────────────
#with open('log.txt', 'w') as f:
#    f.write("line1\n")
#    f.write('line2\n')
#    f.write('line3\n')
#with open('log.txt', 'r') as f:
#    print(f.read())

#nameFirst = 'Maya'
#nameLast = 'Rivera'
#age = 12
#city = 'Portland'
#print(f'Hello, my name is {nameFirst} {nameLast}. I am {age} years old and I am from {city}')

# ─── Challenge 10: Putting It All Together ────────────────────────────────────
user = {}

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

user['name'] = input('Please input your name: ')
try:
    user['number'] = int(input('Please input a number: '))
except ValueError:
    print('You did not enter an integer')

print(f'Hello {user["name"]}!')

fizzbuzz(user['number'])

with open('log.txt', 'w') as f:
        f.write(f'{user["name"]},{user["number"]}\n')