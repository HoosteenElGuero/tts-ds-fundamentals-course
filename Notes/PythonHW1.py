#1
fs = input("Enter your first name") #first name input
ls = input("Enter your last name") #last name input
print(ls,fs) #prints last name and first name in reverse with space

#2
n = input("Type in a number. I will calculate n + nn+ nnn") #n will be input as a string to so I will need to convert it to int
nn = int(n+n) #concatenates n to display "nn". starts as a string so I will convert it to an int
nnn = int(n+n+n)
n = int(n)
print(n+nn+nnn)

#3
bc = input("What country are you from?") #country input
print("I've heard that"+" "+bc+" "+"is a beautiful country!") #displays country with spaces as padding

#4
x = 10
y = 50
if (x ** 2 > 100 and y < 100): 
    print(x, y)
#There is no output because x^2 is equal to exactly 100, not more. Because both conditions are not met, the print command is not called.

#5
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
# the output is 
""
[10, 20, 30, 40]
[10, 20, 30, 40]
""
#the += operator takes the existing variable and adds the value after the operator to the variable. In this case, it extends the list to display all four numbers

#6
#What is the output of the following code and what arithmetic operators is being used here? 
print(2%6)
#Modulo: divides 2 by 6 and prints the remainder. This code prints "2"

#7
#What is the output of the following code and what arithmetic operators are used here? 
print(2 * 3 ** 3 * 4)
""
* = multiplication symbol
** = exponent symbol
The formula is 2 x 3^3 x 4
The result is 216
""

#8
“”
What is a text editor?
A text editor is a program for editing plain text, whether in a programming environment like Jupyter or Notepad++ or in a document-creating/typsetting enviroment like Microsoft Word or LaTeX
Programming text editors often provide tools to help read or debug code. They may highlight different bits of syntax (e.g. variables, commands) with different colors, and highlight snippets that may cause errors
“”


#9
“”
What is python?
Python is a general purpose programming language created in 1991. It was designed to emphasize code readability, and comes with many packages and libraries for common functions. It is currently the most popular programming language in the world.
“”


#10
“”
What is jupyter notebook, what type of python environment is it, and what alternatives are there to jupyter notebook?
Jupyter is an IDE environment. Other IDE environments include PyCharm, Atom and Spyder.
“”
