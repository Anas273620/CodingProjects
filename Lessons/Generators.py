# iterable
# iterate
# generators

# def generator_function(num):
#     for i in range(num):
#         yield i
        
# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))



# for item in generator_function(1000):
#     print(item)




# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(list(range(100000)))


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration:
#             break
        
# special_for([1,2,3])



class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current +=1
            return num
        raise StopIteration


gen = MyGen(0,100)
for i in gen:
    print(i)