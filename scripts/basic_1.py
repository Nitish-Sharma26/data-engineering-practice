# It is Chapter-2 (After you understand basic introduction to python)
#Name of Chapter-2 Variables, Expressions and Statements

# These are basic lines of code, which I am practicing as a complete beginner.
# Also, I am learning from Chuck's course
 
x = 2 
x =float(x)
print(x)

# Assignment Statements

x = 0.6
x = 3.9 * x * (1-x)
print(x)

x = 1 + 2 ** 3 / 4 * 5
print(x)

# Type in Python

eee = "hello" + " " + "there"
print(eee)
print(type(eee))

#Converting integer to floating point

print(float(99)+100)

#Also line 33,34 and 35 is one way to convert int() to float(). 
# Other simple way is line 33 and 36. 

i = 42
f = float(i)
print(f)
print(float(i))

# Integer Division
# The result is more specific in python3 compared to python2

print(99/9)

print(1234/4321)

# String conversions
# It can only be converted if a string contains  only number in it
# The thing that I am doing is writing code in two different manners. 
# The first one is line 52, 54 and 54 which is one way to do it, but it is tough. 
# Second one:- line 52 and 56 . But it is easy and decreases the line of code. 
# Line 53 is not necessary. 

sval = '1234'
print(type(sval))
ival = int(sval)
print(ival)
print(int(sval) + 1) 

#User Input 

nam = input("Who are you?")
print("Welcome", nam)
#Imagine that it asked this question and you wrote "Chuck". 
#The moment you hit enter, it will show you "Welcome Chuck".

#Converting User Input

#So now, let's think that we made an app. A floor conversion app. 
# It converts Europe floor no. to US floor no. 
# Now Europe's floor 0 is 1 in US. 
#Let's start

inp = input('Europe floor?') 
# This line is asking the no. of europe floor from the user. 
#maybe you typed 3. 
# now, you have to remember that the result to input is always a string and not a integer. 
usf = int(inp) + 1 
# Converted the result of input into integer and added 1 to it. 
#Because US floor's are +1. 
print('US floor', usf) 
#The printed result will be "US floor 4" 
#It is 3 line of code which I explained in much more lines. sorry. 


#Comments in Python

#Everything that starts after the hash sign is a comment. 
# Pyhon won't process it as a code. 



#Chapter-3
#Conditional Execution

#The if statement
#Conditional Steps

x = 5
if x < 10:
    print("Smaller") 
if x > 20:
    print("Bigger") 

print("Finis")  
 
#Comparison Operaators

#According to me, it's easy to understand. So, I won't explain it.
x = 5 
if x == 5:
    print('Equals 5') 
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5') 
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5') 
if x != 6:
    print('Not equal 5')

#Indentation

 #These spaces matter a lot

x = 5 
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#Two-way Decisions (if else statement)

x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All Done')

#Multi-way (if elif else)

x = 4
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All Done')

#No else

x = 5
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
print('All Done') 

#The try/except structure

#Sometimes you blow up the code with an error. 
#It creates a problem that the code won't work further. 
#To solve this issue, we use this structure. 

astr = 'Hello Bob' 
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr) 

astr = '1234' 
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

# How not to do try/except

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There') 
except:
    istr = -1 
print('Done', istr)

#Real life sample try/except 

rawstr = input('Enter a number') 
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')


    # Chapter-4
    # Functions 

#There are two types of functions in Python
# 1. Built-in function
# 2. def (Functions we define ourselves)

# 1. Built-in functions 
         # float(), int(), type(), print().... are some of the built-in function

# Max function

big = max('Hello world')
print(big) 

# Min function

small = min('Hello world')
print(small) 

# Functions of our own

# We do it with the help of 'def' 
# It does not execute it. Just defines it for later use. 

# Defining
def print_lyrics():
    print('I am a lumberjack, and I am okay.')
    print('I sleep all night and I work all day')

# Invoking

print('Yo')
print_lyrics()
 

# Putting Parameters and Arguements in def 
# lang is a parameter
# 'es' and 'fr' are arguements

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('es')

greet('fr')

greet('em')

#return value 

def greet():
    return 'hello' 

print(greet(),'Glenn')

print(greet(), 'Sully')

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        return 'Hello'

print(greet('en'), 'Glenn')   

#Multiple Parameters/ Arguements 
 
def addtwo(a, b):
    added = a + b
    return added 

x = addtwo(5, 10)
print(x) 


      # Chapter - 5 
      # Loops and Iteration

 
#Loop Program 
 
# n is the Iteration here. The value given to the variable which changes each time through a loop. 
 
n = 5 
while n > 0:
    print(n) 
    n = n - 1 
print('Blastoff')
print(n)

# An Infinite Loop 

#You can also say that this loop has nothing to do with the iteration variable. So, it will be repeated infinitely.
#Click on the terminal and press Ctrl + C to stop the loop. 

n = 5 
while n > 0:
    print('Lather') 
    print('Rinse') 
print('Dry off')

#Another loop, but not infinite. It won't even run.

n = 0
while n > 0:
    print('Lather') 
    print('Rinse') 
print('Dry off') 

# Breaking out of a Loop 

#It will work in real life code, where user will enter something and their input will define the future of this loop. 

while True:
    line = input('> ')
    if line == 'done':
        break 
    print(line)
print('Done!') 

#Finishing an Iteration with CONTINUE 

#It is simply saying, Don't print anything that starts with a '#' 

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break 
    print(line)
print('Done!') 

#Definite Loops (for loop)

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

#Definite Loop with Strings

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#Looping through a Set

print('Before') 
for thing in [9, 42, 12, 3, 74, 15]:
    print(thing)
print('After')

# Finding the largest number

largest_so_far = -1
print('Before', largest_so_far) 
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far) 

#Counting in a Loop 

zork = 0 
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork) 

#Summing in a Loop 

zork = 0 
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork) 

#Finding the Average in a loop 

count = 0 
sum = 0 
print('Before', count, sum) 
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value 
    print(count, sum, value) 
print('After', count, sum, sum/count)

#Filtering in a Loop 

print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
     print('Large number', value)
print('After') 

#Search Using a Boolean Variable

found = False 
print('Before', found) 
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True 
    print(found, value) 
print('After', found)

#Finding the Smallest value 

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None:
        smallest = value 
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


    # Chapter - 6 
    # Strings

#String Data Type 

str1 = "Hello" 
str2 = "There" 
bob = str1 + str2 
print(bob)

str3 = '123' 
# (str3 = str3 + 1) would be wrong because it is a string and not a integer. 
x = int(str3) + 1
print(x)

#Reading and converting 

#what you need to understand is that in this line of code, the second line is actually not a part of the code. But the input by user. 

name = input('Enter:')
Chuck
print(name)

apple = input('Enter') 
100
# x = apple - 10 is wrong 
x = int(apple) - 10
print(x)

#Looking inside Strings 
 # So basically, [] is the index operator. it only contains integers and can count the position of an expression 


fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3 
w = fruit[x - 1] 
print(w)
#You cannot put integer bigger than the value ( if banana then upto 5)

#Finding the length of a string 
 # Length and position are different
fruit = 'banana' 
print(len(fruit))

# Looping through Strings 
 
 #while loop 
fruit = 'banana' 
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1 

#for loop 
fruit = 'banana' 
for letter in fruit:
    print(letter)


#Looping and Counting 

word ='banana' 
count = 0 
for letter in word:
    if letter == 'a' :
        count = count + 1
print(count)

# Slicing Strings

s = 'Monty Python' 
print(s[0:4]) 
print(s[6:7])
print(s[6:20]) 

s = 'Monty Python' 
print(s[:4]) 
print(s[8:])
print(s[:]) 

# String Concatenation

a = 'Hello'
b = a + 'There' 
print(b)
 
c = a + ' ' + 'There'
print(c) 

# Using 'in' as a logical operator 

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it!')

# String Comparisons

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
if word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# String Library

greet = 'Hello Bob'
zap = greet.lower()
print(zap)

print(greet)

print('Hi There'.lower()) 

# String Functions

stuff = 'Hello world'
type(stuff)

dir(stuff)

# This dir function tells us what we can do with the stuff
# It is maybe called string methods


# Searching a String

fruit = 'banana'
pos = fruit.find('na')
print(pos)
 
aa = fruit.find('z')
print(aa) 

# Making everything UPPER CASE  and lower case 

greet = 'Hello Bob'
nnn = greet.lower()
print(nnn)

www = greet.upper()
print(www)

# Search and Replace 

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'John')
print(nstr)

nstr = greet.replace('o', 'x')
print(nstr)

# Stripping Whitespaces 

greet = '    Hello Bob    '
greet.lstrip()
greet.rstrip()
greet.strip()

# Prefixes

line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p') 

# Parsing and Extracting 

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)


   # Chapter - 7 
   # Reading Files

# importing mbox.txt

import os

# Example for Windows
file_path = r"C:\Users\HP\data-engineering\mbox.txt"

# Example for macOS/Linux
# file_path = "/Users/yourusername/Downloads/example.txt"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("File content:\n", content)
else:
    print("File not found:", file_path)


# importing mbox-short.txt


import os

# Example for Windows
file_path = r"C:\Users\HP\data-engineering\mbox-short.txt"

# Example for macOS/Linux
# file_path = "/Users/yourusername/Downloads/example.txt"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("File content:\n", content)
else:
    print("File not found:", file_path)


# Checking the directory

import os
print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())

#Using open()
#In python open() is used to open the file for us to read or write. Mostly read



fhand = open('mbox.txt', 'r')
print(fhand) 
 
 # Handle is something you need to get the data out of the file

 # The newline character ( \n ) 

stuff = 'Hello\nWorld'
stuff

print(stuff)

stuff = 'X\nY'
print(stuff)
len(stuff)

# File Handle as a Sequence

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)


# Counting lines in a File

fhand = open('mbox.txt')
count = 0 
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Reading the *Whole* File

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Searching through a file

fhand = open('mbox-short.txt')
for line in fhand: 
    if line.startswith('From:'):
        print(line)

#Python adds new lines in it, which works as spaces with new and old line.
# How to solve it?
 
#Searching through a File (fixed)

fhand = open('mbox-short.txt')
for line in fhand: 
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)     

# Skipping with Continue 


fhand = open('mbox-short.txt')
for line in fhand: 
    line = line.rstrip()
    if not line.startswith('From:'):
        continue 
    print(line) 

# Using 'in' to select lines 


fhand = open('mbox-short.txt')
for line in fhand: 
    line = line.rstrip()
    if not '@uct.ac.rn' in line:
        continue 
    print(line) 

# How prompt works on different files ( short or long)

fname = input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Code for bad file names 

fname = input('Enter the file name:')
try: 
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)


           # Chapter - 8 
           # Python Lists 

# We are now starting with Data Structures 

# Normal Algorithms 

x = 2
x = 4 
print(x)

# It cannot remember both values or data given to it. That's where Data Structure comes in. 

friends = ['Joseph', 'Glenn', 'Mike']
print(friends)

# These Data Structures are also called Lists

# Lists Constants 

print([1, 24, 43])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])
print([])


# Looking Inside Lists

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

# Lists are Mutable 
 
fruit = 'Banana'
#fruit[0] = 'b'      # - Traceback 
x = fruit.lower()
print(x) 

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28 
print(lotto) 

# How long is a List?

greet = 'Hello Bob'
print(len(greet))

x = [1, 2, 'joe', 9]
print(len(x))

# Using the Range Function 

print(list(range(4)))

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(list(range(len(friends)))) 

# A tale of two loops 

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

    # Loop Operations 

# Concatenating lists using + 

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b 
print(c)
print(a)

# Lists can be sliced using ':' 

t = [9, 41, 12, 3, 74, 15]
t[1:3]
t[:4]
t[3:]
t[:]

# Building a List fron Scratch 

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

# Is Something in a List?

some = [1, 9, 21, 10, 16]
9 in some
15 in some 
20 not in some

# Lists are in Order 

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])

# Built - in Functions and Lists 

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# So now, there are two ways of doing things.
# One is the old way and the other one is by making a list. 

total = 0 
count = 0 
while True: 
    inp = input('Enter a number')
    if inp == 'Done': break
    value = float(inp)
    total = total + value 
    count = count + 1
average = total/count
print('Average:', average)

              #OR 

numlist = list()
while True:
    inp = input('Enter a number')
    if inp == 'Done': break 
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/ len(numlist)
print('Average:', average) 

# Strings vs Lists

# Best Friends : Strings and Lists 

abc = 'With three words'
stuff = abc.split()
print(stuff)

print(len(stuff))\

print(stuff[0])

print(stuff)
for w in stuff:
    print(w)

# Another example 

line = 'A lot        of  spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing)) 


# Think that the a file named 'mbox-short.txt' contains this info (From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008)
# Now finding the day 

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue 
    words = line.split()
    print(words[2]) 

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)

# The Double Split Pattern


line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


# Strings, Files, Lists & the Guardian Pattern

han = open('mbox-short.txt')        # We open the file

for line in han:                    # Loops through the file
    line =line.rstrip()             # Removes the whitespace
    print('Line:', line)            # Prints all the lines in which spaces are removed
    wds = line.split()              # Splits the data into words
    print('Words:', wds)            # It prints all the splitted lines
    # Guardian Pattern
    if len(wds) < 1 :               # It helps skipping the wds where a line does not have any word
        continue                    # The skipping helps in avoiding tracebacks where there in no data in line
    if wds[0] != 'From':            # Checks if the first word is not 'From'
        print('Ignore')             # Print Ignore, if it is not 'from' in that line
        continue                    # If yes, skips it
    print(wds[2])                   # If not, prints the 3rd word   


# Another way to do it is by skipping blanks

han = open('mbox-short.txt')       

for line in han:                   
    line =line.rstrip()            
    print('Line:', line) 
    if line == '' :                # It skips blank lines
        print('Skip Blanks')
        continue           
    wds = line.split()              
    print('Words:', wds)                                
    if wds[0] != 'From':            
        print('Ignore')             
        continue                    
    print(wds[2])                   

# At last we just got our result without blowing up the lne from both methods
# So let's get a proper result from our code by removing most of the print statements


han = open('mbox-short.txt')       

for line in han:                   
    line =line.rstrip()            
    wds = line.split()             
    # Guardian # Can also make our guardian a bit stronger by making it not less than 3 words
    # if len(wds) < 1:
    if len(wds) < 3:
        continue                                
    if wds[0] != 'From':                         
        continue                    
    print(wds[2])      # At last, it gives us the 3rd word properly. Done!


# |Another way 

han = open('mbox-short.txt')       

for line in han:                   
    line =line.rstrip()            
    wds = line.split()             
    # Guardian  in a compound statement   
    # Guardian always comes first                           
    if  len(wds) < 3 or wds[0] != 'From':                         
        continue                    
    print(wds[2])      


          # Chapter - 8 
          # Dictionaries

# Dictionaries  =  Collection 
# It is a bag of values with it's own label. 
# They can be messy. 
# Whereas lists stays in order
# We put label or keys on data or things we put into dictionary 
# Diff. names of dictionary -
          # associative arrays - Peri/PHP
          # Properties or Map or Hashmap - Java
          # Property Bag - c#/.Net 
        
# Database like collection 
# Powerful for data collection

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

# Comparing Lists and Dictionaries

# List

lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

# Dictionary 

ddd = dict()
ddd['age']  = 21
ddd['course'] = 183
print(ddd)
ddd['age'] = 23
print(ddd)

# Dictionary Literals (Constants)

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)

ooo = { }
print(ooo) 

        # COUNTING


# One common use of dictionary is counting how often we 'see' something 

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1 
print(ccc)

ccc = dict()
# print(ccc['csev'])    # You cannot do it to find csev in ccc dictionary
# Rather, Do this instead :-
'csev' in ccc

# Adding something to that key or label if we see it again 

# OR
# When we see a new name 

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
         counts[name] = counts[name] + 1
    else:
        counts[name] = 1 
print(counts)


# The get method 

# This method allows you to check if a key already exists or not. 

# Normal Method 

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts) 

# Counting words in text 

# Counting Pattern Eg. 

# It will work when the user wil input a text
counts = dict()
print('Enter a line of text')
line = input('')

words = line.split()

print('Words:', words)

print('Counting....')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)


# Definite Loops and Dictionaries

counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key, value in counts.items():
    print(key, value)

# Retrieving lists of Keys and Values 

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))

print(jjj.keys())

print(jjj.values())

print(jjj.items())

#Bonus: Two Iteration Variables
# I did it before because my code wasn't working 

jj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aa, bb in jj.items():
    print(aa, bb)


# Finding the most appeared word and it's count

name = 'mbox-short.txt'
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 
#print(counts)
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount) 


# Counting Word Frequency using a Dictionary

import os 

fname = input('Enter files: ')

if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom : retrieve/create/update counter 
        di[w] = di.get(w,0) + 1
print(di)


# now we want to find the most common word 

largest = -1
theword = None
for k,v in di.items(): 
    if v > largest:
        largest = v
        theword = k # capture/remember the word that was largest

print('Done',theword, largest)


        # CHAPTER - 10 
        # TUPLES 


# Tuples are another kind of sequence that functions much like a list -
# they have elements which are indexed starting at 0 

x = ('Glenn', 'Sally', 'Joseph')  # Round Parenthesis and comma makes something a tuple
print(x[2])
y = ( 1, 9, 2 )   # Also a tuple
print(y)
print(max(y))

for iter in y :
    print(iter)


# TUPLES  ARE  IMMUTABLE (cannot be altered) 

x = [9, 8, 7]  # It is a  list and can be altered
x[2] = 5

y = 'Abc'    # String cannot be altered
y[2] = 'D'

x = (5, 4, 3)  # Tuple cannot be altered
x[2] = 10


# Things NOT to do with Tuples 

x = ( 3, 4, 5)
x.sort()
x.append()
x.reverse()

# A  tale of two sequences 

l = list()
dir(l)

t = (1, 2, 3, 4)
w = t.count(2)
x = len(t)
print(w, x)
dir(t)

t = tuple()
dir(t)

# Tuples are more efficient
# It is because they are better for "temporary variables" compared to lists


# Tuples and Assignment

# We can also put a tuple on the left- hand side of an assignment statement
# We can even omit the parentheses

(x, y) = ( 4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

# Tuple and Dictionaries

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

# Tuples are Comparable

(0, 1, 2) < (5, 4, 3)
(0, 1, 2000000) < (0, 3, 4)
('Jones', 'Sally') < ('Jones', 'Sam')
('Jones', 'Sally') > ('Adams', 'Sam')

# Sorting

# Sorting Lists of Tuples

# We are taking advantage of sorting a tuple to get a sorted dictionary

# First, we are sorting dictionary by key using items() and sorted() method

d = {'a':10, 'd':1, 'c':22}
d.items()
sorted(d.items())

# Using sorted()

d = {'a':10, 'd':1, 'c':22}
t = sorted(d.items())
t
for k,v in sorted(d.items()):
    print(k,v)

# Sort by values instead of key

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# The top 10 most common words 

fhand = open('clown.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(key,value)

# Even Shorter Version


c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v, k) for k,v in c.items() ], reverse=True) )


# Sorting a Dictionary with Tuples 

fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom : retrieve/create/update counter 
        di[w] = di.get(w,0) + 1

print(di)

#x = sorted(di.items())
#print(x[:5])

tmp = list()
for k,v in di.items():
    newt = (v, k)
    tmp.append(newt)

#print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])

for v,k in tmp[:5]:
    print(k,v)

        
        # CHAPTER - 11
        # REGULAR EXPRESSIONS

# Regualr Expression also known as 'regex' or 'regexp'. 
# Really clever 'wild card' expressions for matching and parsing strings

# UNDERSTANDING REGULAR EXPRESSIONS

# Powerful and cryptic
# Fun
# A language of 'marker characters' - programming with characters
# Old school language - compact
# Languauge unto themselves

# The Regualar Expression Module

# Before using R.E.  in program, import the library using 'import re' 
# re.search() in R.E. = find() method
# re.findall() = find() + var[5:10]


# Using re.search() like find() 

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

import re 

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


# Using re.search() like startswith()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)


# Wild-Card Characters

# The character 'dot' or '.' matches any characters
# 'Asterisk' or '*' means any number of times
# '^' means the start of line

# For eg:-    ^X.*:   they will match until column
           # "X-sievesldkfjf:" sfdslkfsdfk
           # "X-sdf:sdfd" 


# FINE TUNING YOUR MATCH

#EG:-   ^X-\S+:
# Here \S  means match S with any non-whitespace character. No space should be there until S arrives
# If it does not work use \\S

# MATCHING AND EXTRACTING DATA

# re.search() gives true/false
# re.findall gives matching strings if we want them to be extracted

import re

x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x)  # Here [0-9]+ does not literally mean these 9 numbers but anything matching either one or more digits
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

# Warning: Greedy Matching 

# the repeat characters(* and + ) push outward in both directions to match the largest poosible string

import re

x = 'From: Using the: characters'
y = re.findall('^F.+:', x)
print(y)

# Non - Greedy Matching

# adding a ? will stop them 

import re

x = 'From: Using the: characters'
y = re.findall('^F.+?:', x)
print(y)

# Fine-Tuning String Extraction

# refining re.findall() using parentheses to exactly determine what to be extracted 

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\\S+@\\S+', x)
print(y)

y = re.findall('^From (\\S+@\\S+)', x)
print(y)

# String Parsing
# The Regex Version 

import re 

lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print(y)

y = re.findall('From .*@([^ ]*)', lin)
print(y)

# CODE TIME 

# Finding line in file 'X-DSPAM-Confidence: 0.8475' like this
# And then getting this last 0.8475 type numbers. 
# Then finding the max. number out of all the extracted lines

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff= re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: 
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# Escape Character

# To make R.E. character to behave normally : prefix "\\"

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\\$[0-9.]+', x)
print(y)


          # CHAPTER - 12
          # NETWORKED PROGRAMS


# TCP CONNECTIONS/ SOCKETS  
# TCP PORTS

# Sockets in Python 

# Python has a built-in for TCP Sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80)) 

# Write a Web Browser

# An HTTP Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80)) 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# Representing Simple Strings 

# Each character is represented by a number between 0 and 256 stored in 8 bits of memory. 
# 8 bits = 1 byte 
# The ord() function tells the numeric value of simple ASCII  character


print(ord('\1'))
print(ord('\a'))
print(ord('A'))

x = b'abc'
type(x) 

# Making HTTP Easier With urllib

# Since HTTP is so common, we have a library that does all the socket work for us and make web pages look like a file 

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


# Like a file 

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

# Reading Web Pages 

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())


# Parsing HTML (a.k.a Web Scraping)

# When a program or script pretends to be a browser and retrieve web pages, look at them, extracts info, etc. It is web scraping 

#Checking Beautiful Soup
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.string)


# Getting Anchor tags out of beautiful soup 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags 
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))




# Getting Anchor tags out of beautiful soup 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags 
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) 


            # CHAPTER - 13
            # USING WEB SERVICES


# Data on Web

# There is a need to come up with an agreed way to represent data going between applications and across networks
# Two formats - XML and JSON 

# Sendig data across net through diff. applications and programming language makes a problem that data should be readable by others too. 
# So, there is a protocol called as 'wire protocol' to do that job and maintain uniformity. 

# Agreeing on a " Wire Format " 


     # XML 

# eXtensible Markup Language 
# Primary purpose is to help information systems share structured data
# It is a simplified subset of SGML 

   # XML Terminology 

# Tags - indicate the beginning and ending of elements 
# Attributes - keyword/value pairs on the opening tag of XML 
# Serialize/ De-Serialize - convert data in one program into a common format for storage and transmission in independent manner 

# XML Data 

import xml.etree.ElementTree as ET 

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Attr:', tree.find('phone').get('type'))

# NEXT 

import xml.etree.ElementTree as ET 

input = '''
<stuff>
   <users>
       <user x="2">
           <id>001</id>
           <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))


# XML Schema

# Describing a "contract" as to what is acceptable XML. 

# Description of the legal format of an XML document
# Expressed in terms of constraints on the structure and the content of documents

# MANY XML SCHEMA LANGUAGES 

# 1. Document Type Definition - (DTD)
# 2. XML Schema fron W3C - (XSD)

# XSD XML Schema (W3C spec)

# We will focus on the World Wide Web Consortium (W3C) version 
# It is often "W3C Schema" because "Schema" is considered generic 
# More commonly it is called XSD because the file names end in .xsd 

# It's structure contains xs:element , xs:sequence , xs:complexType



# JavaScript Object Notation - JSON 
     # Douglas Crockford - "Discovered" JSON 
     # Object literal notation in JavaScript 

# More JSON is used than XML 
# XML is used for rich and hierarchical documents
# JSON is best for just pulling data out of system and moving in between two systems and minimum of fuss


import json
data = '''
{
   "name" : "Chuck",
   "phone" : 
   {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
      "email" : 
   {
         "hide" : "yes" 
    }
}'''
# It is a dictionary with this {}
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
# JSON represents data as nested "lists" and "dictionaties"

# Another one

import json
input = '''
[
  ( "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  ),
  ( "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  )
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
# At top [] means list



# Service Oriented Approach

# It is an approach in which we solve complex application problem where all the data really isn't present in one computer system
# And somehow spread over the internet connected via internet or connected network

# Most non-trivial web applications use services 
# They use services from other applications
      # Credit Card Charge 
      # Hotel Reservation systems
# Services publish the "rules" applications must follow to make use of the service (API)


# Multiple Systems 

# Initially two systems cooperate and split the problem  and later more join to use the application after it beacomes useful 


      # Web Services 

# APPLICATION PROGRAM INTERFACE (API)

# API specifes an interface and controls the behaviour of the objects specifed in that interface 
# The software that provides the functionality described by an API is said to be an "implementation" of the API

# Old code to get location from google. It does not work now. 
import urllib.request, urllib.parsee, urllib.error 
import json 

serviceurl ='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break 

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
            js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

print(json.dumps(js, indent=4))

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat',lat,'lng', lng)
location = js['results'][0]['formatted_address']
print(location)


# New code to get location for opengeo because google is paid and it is a lot different
import urllib.request, urllib.parse, urllib.error 
import json 

serviceurl ='http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break 

    url = serviceurl + urllib.parse.urlencode(
        {'q': address})

    print('Retrieving', url)

    try:
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        js = json.loads(data)
    except Exception as e:
        print('=== Failure to Retrieve ===')
        print(e)
        continue
    
    print(json.dumps(js, indent=4))

    try:
        plus_code = js['features'][0]['properties']['plus_code']
        print('Plus code:', plus_code)

        lat =  js['features'][0]['properties']['lat']
        lon = js['features'][0]['properties']['lon']
        print('Long', lon, 'lat', lat)
        location = js['features'][0]['properties']['formatted']
        print(location)
    except (IndexError, KeyError, TypeError):
            print('=== Cannot find plus_code ===')

# API Security and Rate Limiting 

# The resources to run these APIs are not 'free' 
# The data provided by these APIs is usually valuable 
# The data providers might limit the number of requests per day or even charge for usage 


import urllib.request, urllib.parse, urllib.error
import json

# Prompt for URL or use the course sample data by default
url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)

# Use standard urllib request handle
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Parse the JSON string
js = json.loads(data)

total_sum = 0
count = 0

# Loop through the comments list
for item in js['comments']:
    total_sum = total_sum + int(item['count'])
    count = count + 1

print('Count:', count)
print('Sum:', total_sum)


           # CHAPTER - 14 
           # PYTHON OBJECTS


# An Object is a bit of self-contained Code and Data
# A key aspect of the Object approach is to brake the problem into smaller understandable parts (divide and conquer)
# Objects have boundaries that allow us to ignore un-needed detail
# We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects


# SOME DEFINITIONS\\

# Class - a template - Dog 
# Method or Message - A defined capability of a class - bark()
# Filed or attribute - A bit of data in a class - length 
# Object or Instance - A particular instance of a class - Lasie

# A SAMPLE CODE\\

class PartyAnimal:
    x = 0 

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()



# PLAYING WITH dir() AND type()  \\\\\

print("Type", type(an))
print("Dir", dir(an))

# OBJECT LIFECYCLE 

# Objects are created, used and discarded 
# We have special blocks of code that get called
     # constructor   (used a lot)
     # destructor    (seldom used)


class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

# MANY INSTANCES\\\\

# A class can have multiple instances(objects) having their  own variable 

class PartyAnimal:
    x = 0 
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()


# INHERITANCE \\\\\
          # also known as subclasses 
# It is like making a new class but inheriting an existing class for it and then adding our own little bit for making the new class
# Store and reuse
# Write once - use many times 
# The new class (child) has all the capabilities of the old class (parent) and also some more 


class PartyAnimal:
    x = 0 
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()

          
          # CHAPTER - 15
          # DATABASES

# Maybe I'll do some of the things in SQL

# Getting the number of somethng appears in a file and then making a sql table out of table
 
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email text, count integer)''')

fname = input('Enter file name: ')
if(len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1) ', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()









import urllib.request, urllib.parse, urllib.error
import sqlite3
import json
import time
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Connect to our notebook database file
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (
    address TEXT UNIQUE, 
    retrieved INTEGER
)''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    user_input = input('Enter a location (or "quit"): ')
    if user_input == 'quit': 
        break
        
    if len(user_input) < 1:
        cur.execute('SELECT address FROM Locations WHERE retrieved = 0 LIMIT 1')
        row = cur.fetchone()
        if row is not None:
            # We take index 0 directly to get pure text format
            target_location = row[0]
            print('Spider automatically picked:', target_location)
        else:
            print('No unretrieved locations found in database.')
            continue
    else:
        target_location = user_input

    target_location = target_location.strip()
    
    url = serviceurl + urllib.parse.urlencode({'q': target_location})
    print('Retrieving', url)
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        uh = urllib.request.urlopen(req, context=ctx)
        data = uh.read().decode('utf-8', errors='ignore') # ✨ IGNORES CORRUPTED SYMBOLS
        print('Retrieved', len(data), 'characters')
        
        js = json.loads(data)
    except Exception as e:
        print('=== Broken data packet skipped! ===')
        # Prevent spinning in an infinite error loop:
        cur.execute('INSERT OR REPLACE INTO Locations (address, retrieved) VALUES (?, 1)', (target_location,))
        conn.commit()
        continue

    # Mark this location as officially finished (retrieved = 1)
    cur.execute('INSERT OR REPLACE INTO Locations (address, retrieved) VALUES (?, 1)', (target_location,))

    if 'features' not in js:
        print('=== Server returned empty details ===')
        continue

    for feature in js['features']:
        try:
            if 'properties' in feature and 'name' in feature['properties']:
                new_place = feature['properties']['name']
                if new_place is None or len(new_place) < 1:
                    continue
                
                cur.execute('SELECT retrieved FROM Locations WHERE address = ? LIMIT 1', (new_place,))
                row = cur.fetchone()
                if row is not None: 
                    continue 
                
                cur.execute('INSERT INTO Locations (address, retrieved) VALUES (?, 0)', (new_place,))
                print('   Found new sub-location:', new_place)
        except Exception:
            continue

    conn.commit()
    time.sleep(1)

cur.execute('SELECT address, retrieved FROM Locations LIMIT 10')
print('\n=== Top 10 Locations in Database ===')
for row in cur.fetchall():
    status = "Visited" if row[1] == 1 else "Waiting"
    print(f"[{status}] {row[0]}")
print('====================================\n')

cur.close()



#SQL

# Making a database out of xml file 

import xml.etree.ElementTree as ET 
import sqlite3

conn = sqlite.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title  TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name:')
if(len(fname) < 1): fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if (lookup(entry, 'Track ID') is None) :
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist,) )
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES (?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ))

    conn.commit()


# MANY-TO-MANY TABLE

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id    INTEGER,
    course_id  INTEGER,
    role       INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id) VALUES (?, ?)''',
        (user_id,course_id) )
    
    conn.commit()


        

        # CHAPTER - 16
        # DATA VISUALIZATION

# RETRIEVING AND VISUALIZING DATA 


