li = [1,2,3,4,5,6,7]

# obj = li.__iter__()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

#Exception : StopIteration

# for val in li:
#     print(val)

# __iter__
# __next__

# for val in range(1, 10):
#     print(val)

class myrange:
    def __init__(self, start=0, end=None, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        # print('__iter__ Executed...')
        return self

    def __next__(self):
        val = self.start
        self.start += self.step
        if self.start > self.end+self.step:
            raise StopIteration
        # print('__next__ Executed...')
        return val
    
obj = myrange(1,10)

for val in myrange(1, 10, 0.5):
    print(val)



string = 'rahul, sakeeb, shree., 12344 "vaibhav",ramesh,shrikant, madhav'
#Read and print the capitalized version of each name.

class stringfilter:
    def __init__(self, string):
        self.string = string
        self.pos = 0

    def __iter__(self):

        return self
    
    def __next__(self):

        return name
    
for name in stringfilter(string):
    print(name)