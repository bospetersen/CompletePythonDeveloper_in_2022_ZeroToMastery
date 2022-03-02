# square each element
my_list = [5, 4, 3]
print(list(map(lambda item: item**2, my_list)))

# List Sorting after second element
a = [(0,2),(9,9),(4,3),(10,-1)]
print(a) 

a.sort(key=lambda x: x[1])
print(a)