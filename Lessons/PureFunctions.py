#map, filter, zip and reduce
from functools import reduce
my_list = [1,2,3]

#lambda param: action(param)
   
print(reduce(lambda acc, item: acc+item, my_list))
print(my_list)


