# Closures

def outer():
    x = 10
    def inner():
        print(x)   # outer ka variable access kar raha hai
    inner()

outer()


def outer():
    x = 10
    def inner():
        return x
    return inner   # function return kar diya, execute nahi kiya

closure_func = outer()
print(closure_func())   # 👉 10


# Closure with Different Variables
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times2 = make_multiplier(2)  
times3 = make_multiplier(3)

print(times2(5))  # 👉 10
print(times3(5))  # 👉 15


# Data hiding / encapsulation
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 👉 1
print(c())  # 👉 2
print(c())  # 👉 3


# Agar inner function ko outer function ka variable modify karna hai, to nonlocal keyword use karna padega.
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

f = outer()
print(f())  # 👉 6
print(f())  # 👉 7
