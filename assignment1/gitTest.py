import numpy as np

x = np.array([[1001, 1002], [3, 4]])
def exp_minmax(x):
    np.exp(x - np.max(x))
    print(x - np.max(x))
    print(np.exp(x - np.max(x)))
print(np.apply_along_axis(exp_minmax, 1, x))

def my_func(a):
    return (a[0] + a[-1]) * 0.5
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.apply_along_axis(my_func, 0, b))

print(np.apply_along_axis(my_func, 1, b))



