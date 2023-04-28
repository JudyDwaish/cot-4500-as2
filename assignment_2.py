# Goudi Dwaish
# COT4500-23Spring 0001
# Assignment 2
# Professor Juna Parra

import numpy as np

def neville(x, f, xi):
    n = len(x)
    Q = np.zeros((n,n))
    Q[:,0] = f
    for i in range(1,n):
        for j in range(1,i+1):
            Q[i,j] = ((xi - x[i-j])*Q[i,j-1] - (xi - x[i])*Q[i-1,j-1])/(x[i]-x[i-j])
    return Q[n-1,n-1]

x = [3.6, 3.6, 3.9]
f = [1.675, 1.436, 1.318]
xi = 3.7

result = neville(x, f, xi)
print(result)

def divided_difference_table(x, f):
    n = len(x)
    table = np.zeros((n,n))
    table[:,0] = f
    for j in range(1,n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j]-x[i])
    return table

def newton_forward(x, f, xi, table):
    n = len(x)
    h = x[1]-x[0]
    p = (xi-x[0])/h
    res = f[0]
    for i in range(1,n):
        term = table[0][i]
        for j in range(i):
            term *= (p-j)
        res += term
    return res

x = [7.2, 7.4, 7.5, 7.6]
f = [23.5492, 25.3913, 26.8224, 27.4589]

table = divided_difference_table(x,f)

print("1st degree approximation:", newton_forward(x, f, 7.3, table[:,0:2]))
print("2nd degree approximation:", newton_forward(x, f, 7.3, table[:,0:3]))
print("3rd degree approximation:", newton_forward(x, f, 7.3, table))

