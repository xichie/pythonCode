'''
    使用梯度下降求函数的极值
'''


import numpy as np

def f(x):
    return x**2 + 1

def gradient(x):
    return 2*x

temp_x = []
temp_y = []
def gradientDescent(cost, gradient, init_x, alpha = 0.1, difference = 1e-10,max_iter = 3000):
    cur_x = init_x
    cur_y = cost(cur_x)
    temp_x.append(cur_x)
    temp_y.append(cur_y)
    for i in range(max_iter):
        new_x = cur_x - alpha * gradient(cur_x)
        new_y = cost(new_x)
        temp_x.append(new_x)
        temp_y.append(new_y)
        if abs(new_y - cur_y) < difference:
            print("收敛了,迭代了%d次"%i)
            return new_x, new_y
        cur_x = new_x
        cur_y = new_y

result = gradientDescent(f, gradient, 8.0) 
print(result)
import matplotlib.pyplot as plt

pt_x = np.arange(len(temp_x))
pt_y = temp_x
plt.figure()
plt.title('y=x*x')
plt.plot(pt_x, pt_y, 'o')
plt.show()