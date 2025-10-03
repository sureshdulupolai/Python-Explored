"""
Iteration:
process of taking each item of something one after another
exp:- whenever you use a loop for visiting every item of sequence

Iterator:
an iterator is an object that allows programmers to travers throught a sequence of data without 
storign the data in the memory.

Iterable:
jiske upar iteration hota hai. this is continer of multiple items

"""

data = [10, 20, 30] # iterable => python create internally a iterator object to iterate inside list for a particular object

for ele in data:
    print(ele)

L = [10, 20, 30, 40]
iter_obj = iter(L) # return a iterate object
print(type(iter_obj))

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
# print(next(iter_obj)) => show error for non exist (StopIteration)


# iterator remember every last element that he have give to us
L = [10, 20, 30, 40]
iter_obj = iter(L)
print(next(iter_obj)) # 10
print(next(iter_obj)) # 20
for i in iter_obj:
    print(i)  # 30, 40 only


# How to check weather an object is iterable or not ?
# how to check an object is iterable or iterator ?

# __iter__ => iterable
# __iter__ , __next__ => iterator

L = [10, 20, 30, 40] # iterable but not iterator
iter_obj = iter(L) # iterator => because we can use in for loop or next() to iterate
# every iterator is iterable. You can run loop on every iterator.

print(dir(L))
print()
print(dir(iter_obj))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
"""




# same to create an iterator obj
L = [10, 20, 30, 40] 
iter_obj = L.__iter__() # same as iter() => when you write this then it call to __iter__ magic method in py
print(type(iter_obj))

# like next() => it call __next__() magic method
print(iter_obj.__next__())


# it doesnt create a new iter same iterator, reduce memeory storage
# when you create an iterator of iterator. it return itself
L = [10, 20, 30]
iter_obj = iter(L)
print(f"Id Of 1: {id(iter_obj)}")

iter_obj1 = iter(iter_obj)
print(f"Id Of 2: {id(iter_obj1)}")



# to check memory consume
import sys
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # => L ke liye memeory aloted hua hai uske baad uske andar jitna bhi element hai uske liye allot kiya gaya hai
for i in L:
    print(i**2)
print('L: ', sys.getsizeof(L)) # more memory consume

a = range(1, 11) # a ko allot karne ke liye memory use hua, aur iterator karne ke liye, value update hote jayega 1, 2,.. 10
for i in a:
    print(i**2)
print('A: ', sys.getsizeof(a)) # use less memory fix memory always it doent meter that is the range