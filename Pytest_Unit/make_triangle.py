# Entity Comparison

def make_triangle(n):
    for i in range(n):
        yield '@' * i
        
def make_triangle_1(n):
    for i in range(1, n + 1):
        yield '@' * i
