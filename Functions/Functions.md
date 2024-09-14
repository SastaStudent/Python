## Functions

def keyword used to declared a function in python

```python
def function_name(parameters):
    # Function body (code block)
    # ...
    return result  # Optional return statement
```

Check this

```python
def compute_value(a, b):
    # Solution as follows
    c = a*a + 2*a*b + b*b
    d = a + b
    print(c)
    print(d)

t = 3
for _ in range(t):
    A, B = map(int, input().split())
    compute_value(A, B)
```

## Variable scope
Scope in Python can be broadly categorized into two types: global scope and local scope

## Accessing Variables from Different Scopes
A function can access variables in its local scope, as well as variables in the global scope.
However, a local variable will take precedence over a global variable if they have the same name.

## Nested Functions