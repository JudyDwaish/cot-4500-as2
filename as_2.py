# Goudi Dwaish
# COT4500-23Spring 0001
# Assignment 2
# Professor Juna Parra 

# Using Neville’s method to find the 2nd degree interpolating value for f(3.7):
def neville_method(x, y, xi):
    n = len(x)
    Q = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        Q[i][0] = y[i]
    for i in range(1, n):
        for j in range(1, i+1):
            Q[i][j] = ((xi-x[i-j])*Q[i][j-1]-(xi-x[i])*Q[i-1][j-1])/(x[i]-x[i-j])
    return Q[n-1][2] # 2nd degree interpolating value

x = [3.6, 3.8, 3.9]
y = [1.675, 1.436, 1.318]
xi = 3.7
interpolating_val = neville_method(x, y, xi)
print(f"The 2nd degree interpolating value for f({xi}) is {interpolating_val:.6f}")

# Using Newton’s forward method, print out the polynomial approximations for degrees 1, 2, and 3 using the following set of data:
def newton_forward(x, y, xi, degree):
    n = len(x)
    h = x[1] - x[0]
    u = (xi - x[0]) / h
    diff = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        diff[i][0] = y[i]
    for j in range(1, n):
        for i in range(n-j):
            diff[i][j] = diff[i+1][j-1] - diff[i][j-1]
    approx = diff[0][0]
    for j in range(1, degree+1):
        term = diff[0][j]
        for i in range(j):
            term *= (u - i)
            term /= (i+1)
        approx += term
    return approx

x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]
xi = 7.3
for degree in range(1, 4):
    approx = newton_forward(x, y, xi, degree)
    print(f"The {degree} degree polynomial approximation for f({xi}) is {approx:.6f}")

# Using the results from 2, approximate f(7.3)?
approx = newton_forward(x, y, xi, 2)
print(f"The 2 degree polynomial approximation for f({xi}) is {approx:.6f}, which is the most accurate.")

# Using the divided difference method, print out the Hermite polynomial approximation matrix:
def hermite_polynomial(x, f, fp):
    n = len(x)
    Q = [[0 for i in range(2*n)] for j in range(2*n)]
    for i in range(n):
        Q[2*i][0] = f[i]
        Q[2*i+1][0] = f[i]
        Q[2*i+1][1] = fp[i]
        if i != 0:
            Q[2*i][1] = (Q[2*i][0] - Q[2*i-1
