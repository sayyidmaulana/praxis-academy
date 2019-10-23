tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel

a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)
x = {x: x**2 for x in (2, 4, 6)}
print(x)
y = dict(sape=4139, guido=4127, jack=4098)
print(y)