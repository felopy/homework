'''#31
n = int(input("Enter number: "))
m = int(input("Enter number: "))
k = 0

for i in range(2,(n+m)//2+1):

    if n%i==0 and m%i==0:
        k = i   
print(k)

#32
n = int(input("Enter number: "))
m = int(input("Enter number: "))
k = 0
while True:
    k += 1
    if k%n==0 and k%m==0:
        print(k)
        break

#33
n = int(input())
m = int(input())
z = int(input())
k = z+n+m
if z==n or z==m or m==n:
    k = 0
print(k)
#34
n = int(input())
m = int(input())
k = n + m
z = (15,16,17,18,19,20)
while True:
    if k in z:
        k = 20
        print(k)
        break
#35
n = float(input())
m = float(input())
if abs(n-m)==5 or n+m==5 or n ==m:
    print(True)

#List
#1
ls = [1,3,5,-8]
p = 0
for i in ls:
    p += i
print(p)

#2
ls = [1,3,5,-8]
p = 1
for i in ls:
    p *= i
print(p)

#3
ls = [1,3,4,5,-8]
k = 0
for i in ls:
    if i > k:
        k = i
print(k)
#4
ls = [1,3,4,5,1]
k = 0
for i in ls:
    k = i
    if i < k:
        k = i
print(k)

#5
k = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in k:
    if i[0] == i[-1]:
        count +=1
print(count)

#6
k = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
m = len(k)
for i in range(m):
    for j in range(0,m-i-1):
        if k[j] > k[j+1]:
            k[j],k[j+1] = k[j+1],k[j]
print(k)

#7
k = [1,2,1,3,1,4]
m = []
for i in k:
    if i not in m:
        m.append(i)
print(m)
#8
k = [1,2,3]
m = []
if k == m:
    print(True)
else:
    print(False)

#9
k = [1,2,3]
print(k.copy())

#10
k = ['ass','a','sdf']
m = []
for i in k:
    if len(i) > 1:
        m.append(i)
print(m)
#11
def _list(x,y):
    result = False
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            if x[i] == y[j]:
                result = True
                return result
print(_list([1,2,3],[2,4,5]))

#12
k = [1,2,3,4,5,6]
k.pop(5)
k.pop(4)
k.pop(0)
print(k)

# Create a list 'color' with several color strings
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Use a list comprehension to create a new list 'color' that includes elements from the original list
# but only if their index (i) is not in the specified indices (0, 4, 5)
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

# Print the modified 'color' list, which excludes elements at indices 0, 4, and 5
print(color)

#13
# Create a 3D array using list comprehensions, with 3 rows, 4 columns, and each element initialized as '*'
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]

# Print the resulting 3D array
print(array)

#14
k = [1,2,3,4,5,'w',]
m = []
for i in range(len(k)):
    if  i%2!=0:
        m.append(i)
print(m)

#15
from random import shuffle
k = [1,2,3,4,4,5,9]

shuffle(k)
print(k)

#16
# Define a function named printValues
def printValues():
    # Create an empty list 'l'
    l = list()
    # Loop from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Calculate the square of 'i' and append it to the list 'l'
        l.append(i**2)
    # Print the first 5 elements of the list 'l'
    print(l[:5])
    # Print the last 5 elements of the list 'l'
    print(l[-5:])

# Call the printValues function to execute it
printValues()

#17
k = [1,2,3,4,5,6]
for i in range(len(k)):
    if i!=2 and i!=3 and i!=5 and i%2!=0 and i%3!=0 and i%5!=0:
        print(True)
    else:
        print(False)
# Define a function named 'test' that takes a list 'nums' as a parameter
def test(nums):
    # Use a generator expression to check if each number in 'nums' is prime, and return True if all are prime
    return all(is_prime(i) for i in nums)

# Define a function named 'is_prime' that checks if a number 'n' is prime
def is_prime(n):
    # Check if 'n' is equal to 1; if so, it's not prime
    if (n == 1):
        return False
    # Check if 'n' is equal to 2; if so, it's prime
    elif (n == 2):
        return True
    else:
        # Iterate through numbers from 2 to 'n' - 1
        for x in range(2, n):
            # If 'n' is divisible by 'x', it's not prime; return False
            if (n % x == 0):
                return False
        # If no divisors were found, 'n' is prime; return True
        return True

# Define a list 'nums' containing a sequence of numbers
nums = [0, 3, 4, 7, 9]
# Print the original list of numbers
print("Original list of numbers:")
print(nums)
# Check if each number in 'nums' is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

# Reassign 'nums' with a different list of numbers
nums = [3, 5, 7, 13]
# Print the original list of numbers
print("\nOriginal list of numbers:")
print(nums)
# Check if each number in the new 'nums' list is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

# Reassign 'nums' with another list of numbers
nums = [1, 5, 3]
# Print the original list of numbers
print("\nOriginal list of numbers:")
print(nums)
# Check if each number in the new 'nums' list is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums)) 

#18
#poxarkwumner@ stugelu hamar
# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Use 'itertools.permutations' to generate all permutations of the list [1, 2, 3], and convert the result to a list
# This will produce all possible orderings of the elements in the list
print(list(itertools.permutations([1, 2, 3])))

#19
k = [1,2,3,4]
m = [2,6,7,8]
l = []
for i in k:
    if i not in m:
        l.append(i)
for j in m:
    if j not in k:
        l.append(j)
print(l)

# Define a list 'list1' containing numbers
list1 = [1, 3, 5, 7, 9]

# Define another list 'list2' containing different numbers
list2 = [1, 2, 4, 6, 7, 8]

# Calculate the difference between 'list1' and 'list2' by converting them to sets and subtracting the sets
diff_list1_list2 = list(set(list1) - set(list2))

# Calculate the difference between 'list2' and 'list1' by converting them to sets and subtracting the sets
diff_list2_list1 = list(set(list2) - set(list1))

# Concatenate the differences 'diff_list1_list2' and 'diff_list2_list1' to obtain a list of all unique differences
total_diff = diff_list1_list2 + diff_list2_list1

# Print the total difference, which represents elements that are unique to each list
print(total_diff)

#20
# Define a list 'nums' containing a sequence of numbers
nums = [5, 15, 35, 8, 98]
# Use a 'for' loop with 'enumerate' to iterate through 'nums' and obtain both the index and value of each element
for num_index, num_val in enumerate(nums):
    # Print the index and value of each element in 'nums'
    print(num_index, num_val)

#21
k = ['1','sdd','3eed']
m = ','.join(k)
print(m)

#22
k = [1,2,3,4,5]
print(k.index(1))

#23
# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Define a list 'original_list' containing nested sublists
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# Use 'itertools.chain' and the unpacking operator (*) to merge the sublists into a single flat list
new_merged_list = list(itertools.chain(*original_list))

# Print the newly merged list 'new_merged_list'
print(new_merged_list)

#24
p = [1,2,3,4]
k = [3,5,6,7]
p.extend(k)
print(p)

# Define a list 'list1' containing numeric elements
list1 = [1, 2, 3, 0]

# Define another list 'list2' containing string elements
list2 = ['Red', 'Green', 'Black']

# Concatenate 'list1' and 'list2' to create a single list 'final_list'
final_list = list1 + list2

# Print the 'final_list,' which contains elements from both 'list1' and 'list2'
print(final_list)

#25
import random
l = [1,2,3,4]
k = random.choice(l)
print(k)

# Import the 'random' module, which provides functions for generating random values
import random
# Define a list 'color_list' containing various colors
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']

# Use the 'random.choice' function to select and print a random color from the 'color_list'
print(random.choice(color_list))

#26
# Define three lists: list1, list2, and list3, each containing a sequence of numbers
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

# Compare list1 and list2
print('Compare list1 and list2')

# Check if the string representation of list2 is present in the string representation of list1 repeated twice
# The result will be True if list2 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))

# Compare list1 and list3
print('Compare list1 and list3')

# Check if the string representation of list3 is present in the string representation of list1 repeated twice
# The result will be True if list3 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

#27
k = [25,4,5,7,3]
k.sort()
print(k[1])

#28
k = [12,23,4,5,6]
k.sort()
print(k[-2])

#29
my_list = [10, 20, 30, 40, 20, 50, 60, 40]

# Print the original list 'my_list'
print("Original List : ", my_list)

# Convert the 'my_list' to a set 'my_set' to eliminate duplicates and keep unique elements
my_set = set(my_list)

# Convert the 'my_set' back to a list 'my_new_list' to obtain a list of unique numbers
my_new_list = list(my_set)

# Print the list of unique numbers stored in 'my_new_list'
print("List of unique numbers : ", my_new_list)
'''
#30
import collections
mur = [1,2,3,4,5,6,5]
ctr = collections.Counter(mur)
print(ctr)
# Import the 'collections' module, which provides specialized container data types
import collections

# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# Print the original list 'my_list'
print("Original List : ", my_list)

# Use the 'collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'ctr'
ctr = collections.Counter(my_list)

# Print the frequency of the elements in the list, as provided by the 'ctr' object
print("Frequency of the elements in the List : ", ctr) 


