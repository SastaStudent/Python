#manually
# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(arr)
# print(arr[0][1])
# print(end="")

#by user
print("Enter row ")
row=int(input())
print("Enter Col")
col=int(input())

# arr=[]
# #taking input by user
# for i in range(row):
#     rows=[]
#     for j in range(col):
#         rows.append(int(input()))
#     arr.append(rows)
        
# print("Print Element")

# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         # print("index",i,j)
#         print(arr[i][j],end=" ")
#     print()

#method 2................................

# arr = [[0] * col for _ in range(row)]
# for i in range(row):
#     rows=[]
#     for j in range(col):
#         rows.append(int(input()))
#     arr.append(rows)
# print(arr)

#method 3...............................

arr=[]
for i in range(row):
    rows= list(map(int,input().split()))
    arr.append(rows)
print(arr)