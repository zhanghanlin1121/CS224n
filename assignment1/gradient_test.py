x_old = 0
x_new = 6
eps = 0.01
precision = 0.00001

def f_derivative(x):
    return 2 * x- 3
while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old -eps * f_derivative(x_old)
    print(x_new**2 + 3* x_new + 1)
print("min:" + str(x_new))
