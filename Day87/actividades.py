"""
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""
lista = [12,24,35,70,88,120,155]
lista = [lista[i] for i in range(len(lista)) if i not in (0, 4, 5)]
print(lista)


"""
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
"""
lista = [12,24,35,24,88,120,155]
lista = [i for i in lista if i != 24]
print(lista)


"""
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
"""
lista1 = set([1,3,6,78,35,55])
lista2 = set([12,24,35,24,88,120,155])
intersection = set.intersection(lista1, lista2)
print(intersection)


"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
"""
lista = [12,24,35,24,88,120,155,88,120,155]
for i in lista:
    if lista.count(i) > 1:
        lista.remove(i)
print(lista)


"""
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""
class Person(object):
    def getGender(self):
        return 'Person'
    
class Male(Person):
    def getGender(self):
        return 'Male'
    
class Female(Person):
    def getGender(self):
        return 'Female'
    
cMale = Male()
cFemale = Female()
print(cMale.getGender(), cFemale.getGender())


"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5 2 3 6 6 5

Then, the output of the program should be:

5
"""
points = '5 2 3 6 6 5'
lista = list(map(int, points.split()))
lista = sorted(set(lista))
print(lista[-2])


"""
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ 4

Then, the output of the program should be:

ABCD EFGH IJKL IMNO QRST UVWX YZ
"""

S = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ 4'
W = 4
C = 0
text = []
string = ''
for i in S:
    if C == W:
        text.append(string)
        string = ''
        C = 0
    else:
        C += 1
        string += i
S = ' '.join(text)
print(S)


import string


"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
$size = 3$
----c----

--c-b-c--

c-b-a-b-c

--c-b-c--

----c----
"""

def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = "-".join(alph[n - i - 1 : n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, "-")
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2 :: -1]:
            ans.append(i)
    ans = "\n".join(ans)
    print(ans)


n = 3
print_rangoli(n)