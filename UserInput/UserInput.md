## Taking user input

input() is used to take input.
 

like

```python
name = input()
print("Hello, " + name + "!")

age = input()
print("You are " + age + " years old.")
```

input() assumes that the input is a string.
You can convert it to an integer or numerical value using int()

```python
age = int(input())
print("You are", age, "years old.")
```

## Multiple string inputs

For multiple string inputs we use split().
For example, if the user inputs the following:

Good Great Awesome

You can read these inputs like this:

```python
a, b, c = input().split()
```
The split() function breaks this single line of input into multiple parts. By default, split() divides the input based on spaces, so each word separated by a space is treated as an independent input and stored in different variables.


## Multiple integer inputs

You cannot call the int function directly on the split input as int function can only be called on one value as a time and split input has multiple values.

To handle this, you can use the map function to convert the split inputs to integers in one step. Here's how you can do it:

```python
a, b, c = map(int, input().split())   # assigns integer input values to variables a, b and c
```

