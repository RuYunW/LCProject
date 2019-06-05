a = [[1,2,3],[1,4,[5,5,7]],5]
print(a)
a[1][2].append([666])
print(a)

b = a[0][0]
c = "777"
print(str(b)+c)

a = [1,2,3]
b = [2,3]
a = a+b
print(a)