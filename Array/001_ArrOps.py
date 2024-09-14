arr = [1,2,1,2,3,4,3,4]

#append()
print("append()")
arr.append(5)
print(arr)

#insert()
print("insert()")
arr.insert(0,6)
print(arr)

#remove()
print("remove()")
arr.remove(4)
print(arr)

#pop() with argument
print("pop()")
arr.pop(0)
print(arr) #it take index and remove that index value

#pop() without argument
print("Pop() w/o arg")
arr.pop()
print(arr) #it remove last element