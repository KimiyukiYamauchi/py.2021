l = [0, 10, 20, 30, 40, 50, 60]

sl = slice(0, 5, 2)
print(sl)
# slice(2, 5, 2)

print(type(sl))
# <class 'slice'>

print(l[sl])
# [20, 40]