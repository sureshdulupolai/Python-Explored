import numpy as np

s1 = 'Polai is my name'
s2 = 'I am an indian'

a = np.char.add(s1, s2)
b = np.char.upper(s1)
c = np.char.lower(s2)
d = np.char.split(s1)
print(d)

s3 = 'Suresh is my\nname'
e = np.char.splitlines(s3)
print(e)

f = np.char.replace(s1, 'name', 'sirname')

print('****************good bye****************')
g = np.char.center('good bye', 40, '*')
print(g)