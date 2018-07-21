'''
动态规划入门程序
'''
import numpy as np
import random

MAXSUM = -np.ones((100, 100))

def maxSum(arr, rowIndex, colIndex, n = 5):
    '''
    if rowIndex == n - 1:
        return arr[rowIndex][colIndex]
    else:
        # return arr[rowIndex][colIndex] + max(maxSum(arr, rowIndex + 1, colIndex), maxSum(arr, rowIndex + 1, colIndex + 1))
        return arr[rowIndex][colIndex] + max(maxSum(arr, rowIndex + 1, colIndex), maxSum(arr, rowIndex + 1, colIndex + 1))
    '''
    if MAXSUM[rowIndex, colIndex] != -1:
        return MAXSUM[rowIndex, colIndex]
    elif rowIndex == n - 1:
        MAXSUM[rowIndex, colIndex] = arr[rowIndex][colIndex]
    else:
        MAXSUM[rowIndex, colIndex] = arr[rowIndex][colIndex] + max(maxSum(arr, rowIndex + 1, colIndex), maxSum(arr, rowIndex + 1, colIndex + 1))

    return MAXSUM[rowIndex, colIndex]
if __name__ == '__main__':
    A = []
    n = int(input("请输入n："))
    for i in range(n):
        temp = []
        for j in range(i + 1):
            temp.append(int(input("请输入数据：")))
            # temp.append(random.randint(0, 99))
        A.append(temp)
    for arr in A:
        print(arr)
    result = maxSum(A, 0, 0)
    print(result)
                
