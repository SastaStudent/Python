## Creating Arrays

Arrays in Python are commonly referred to as lists.
Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value

In Python, list is denoted by square brackets []

It can hold elements of different data types, such as numbers, strings, or even other lists.
Lists are mutable, which means you can modify them by adding, removing, or changing elements.

```python
# Consider the list  'fruits'  and  'numbers'  below
fruits = ["apple", "banana", "orange", "grape"]

numbers = [20, 10, 0, -5]
```

## check indexing and reverse indexing

## slicing is same as string

## Operations on Lists

There are four major functions that you can use to update any given list and its items.

1. append()
This function helps you to add a new item at the end of the list.

2. insert()
This function helps you to add a new item at a specific position in the list. You can exactly specify which position you want to add the new item.

3. remove()
This is used to remove a specific item from a list. You can exactly specify which item you want to remove from the list.

4. pop()
It have two variant
(i) without argument
This is used to remove the last element from the list.

(ii)with argument
It remove given index value


## List concatenation

When you use the addition operator on two lists, it combines them into one longer list, placing all the items from both lists together.

```python
fruits1 = ["apple", "banana"]
fruits2 = ["cherry", "date"]
all_fruits = fruits1 + fruits2
print(all_fruits) # Output: ["apple", "banana", "cherry", "date"]
```

## List String User Input

Use the INPUT() function to read the user input items separated by spaces.
Use the SPLIT() function to break the input string into individual items and store them in a list.

```python
fruits = input().split()
print(fruits)
 #If the user enters:

#apple banana cherry date
# The SPLIT() function will break this input string into individual items based on the spaces and create a list like this:

print(fruits) # Output: ["apple", "banana", "cherry", "date"]
```

## Note

When using input().split(), the input is read as a string by default.
If you need to read integer inputs, you'll need to convert these string inputs into integers.


## List Integer User Input

Read User Input: When you need to input a series of numbers, each number is initially read as a string.
To use these numbers in numerical operations, you must convert them from strings to integers.
Convert to Integers: Use the MAP() function to apply the INT() function to each item, converting them from strings to integers.
Create a List: LIST() function collects these elements into a list.
This list of integer values is stored inside a variable

```python
numbers = list(map(int, input().split()))
# If the user enters:

# 1 2 3 4 5
# The MAP() function will convert each item from a string to an integer, and LIST() will create a list of these numbers:

print(numbers) # Output: [1, 2, 3, 4, 5]
```
