## If Statement
The else statement is optional.

Here is an example

```python
grade = 95
if grade >= 90:
    print("You got an A")

# Output:
# You got an A
```
## if else statement

```python
if condition:
    # code to run if the condition is true
else:
    # code to run if the above condition is false
```
Here's a table of common operators used in Python conditions:

Operator	Description	                Example
==	        Equal to	                a == b
!=	        Not equal to	            a != b
>	        Greater than	            a > b
<	        Less than	                a < b
>=	        Greater than or equal to	a >= b
<=	        Less than or equal to	    a <= b


## Indentation

Let us take a look at the code from last problem.

```python
age = int(input())

if age >= 18:
    print("Old enough to vote")
else:
    print("Not old enough to vote")

```
Two things to note here:

There is some space before the print statements.
There is a colon (:) after if and else statements.
The space before print is called indentation. Indentation is used to define scope in Python. Because of the space before print, Python knows that it has to execute the print statement if the condition becomes True.

The colon after IF and ELSE is also part of the syntax, you will get an error if you forget it.

## Elif Statement

The following example illustrates usage of elif.

```python
grade = 85

if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")

# Output:
# You got a B
```

