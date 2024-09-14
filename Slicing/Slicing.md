## String Slicing

Slicing is a way to extract a part (substring) from a string.

Syntax:
Substring = string[start:end]

It is give a substring from index( start to end-1)

like:

```python
str = 'Interesting'
substring = str[0:4]
print(substring)

#output is Inte
```

Code Snippet

```python
s = "abcdefghij"
print(s[2:-2])

#output is cdefgh ..(because start =2 end= index(-2)-1 which is -3)
```

There's another syntax to slice a string:

substring = string[start:end:step]

Step is how many characters you move forward each time you read. If your step is 1, you read one character at a time. If your step is 2, you skip one character and then read the next one.

Let's say our string is 'abcde':

```python
s = 'abcde'
print(s[0:4:2]) # Output: ac

```

You can also use slicing to change the value of a character.
We can achieve this by slicing the string into parts before and after the character to be changed, then concatenate these parts with the new character in between.

```python
string = 'Chaf'
new_string = string[:2] + 'e' + string[3:]
print(new_string) # Output: Chef
# This code modifies the string 'Chaf' to 'Chef'
```

## Reverse slicing

You can use [start:end:step] format to print a string in reverse. Let's see how.

We know when slicing, the traversal (movement) always happens from left to right. But there is a way to traverse from right to left by mentioning a negative step.

```python
s='abcde'
print(s[4:0:-1]) # Output: edcb
```

When you mention a negative step the slicing starts from right to left.
So, your start index will be 4 and the slicing stops at 1 because the end index is 0

If you had to print the entire string in reverse then you write:

```python
print(s[::-1]) # Output: edcba
```

## Summary

Indexing: Allows access to individual characters in a string. Positive indexing starts from the beginning (0), while negative indexing starts from the end (-1).

Slicing: Extracts a substring from a string. The slice includes the start index but excludes the end index. You can use both positive and negative indexes for slicing.