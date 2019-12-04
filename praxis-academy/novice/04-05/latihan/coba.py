# n = 10
def kiri(i, n):
# for i in range (0, n):
    a = ""
    for j in range(i, n):
        if i == 0:
            a += "*"
        elif j > i:
            a += " "
        else:
            a += "*"
    return a

def kanan(i, n):
    a = ""
    for j in range(i, n-1):
        if i == 0:
            a += "*"
        elif j < n-2:
            a += " "
        else:
            a += "*"
    return a

    # for j in range(i, n-1):
    #     if i == 0:
    #         a += "*"
    #     elif j < n-2:
    #         a += " "
    #     else:
    #         a += "*"
    # return a

n = 10
for i in range(0, n):
    a = ""
    for j in range(0, i):
        a += " "

    a += kiri(i, n)
    a += kanan(i, n)

    print(a)
