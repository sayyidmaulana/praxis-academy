vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
bla = [x*2 for x in vec]
print(bla)
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
var = [abs(x) for x in vec]
print(var)
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
print(freshfruit)
# create a list of 2-tuples like (number, square)
tapel = [(x, x**2) for x in range(6)]
print(tapel)
# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]