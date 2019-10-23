




# flatten a list using a listcomp with two 'for'
ved = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in ved for num in elem]


from math import pi
var = [str(round(pi, i)) for i in range(1, 6)]
print(var)