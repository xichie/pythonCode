'''
    问题描述：
        一栋楼共有N层，电梯从一层往上走，只允许停在其中某一层，所有乘客都从一楼上电梯，
        到达某层楼后，所有乘客从这一层爬楼梯道自己的目的层。在一楼时，每个乘客选择自己的目的层，
        电梯自动计算出应停的楼层。
    问：电梯停在哪一层楼，能够保证这次乘坐电梯的所有乘客爬楼梯的层数之和最少。
'''
# 解法1：暴力求解， 从第一层开始遍历，得到爬楼梯最少的楼层（时间复杂度O(N^2)）
nPerson = [-1, 1, 1, 1] # nPerson[i]表示到第i层的乘客数目
nFloor  = nMinFloor  = 0
nTargetFloor = -1
N = len(nPerson) - 1 # 楼层数

for n in range(1, N+1):
    nFloor = 0
    for j in range(1, n):
        nFloor += nPerson[j] * (n - j)
    for j in range(n+1, N+1):
        nFloor += nPerson[j] * (j - n)
    if nTargetFloor == -1 or nMinFloor > nFloor:
        nMinFloor = nFloor
        nTargetFloor = n
print(nTargetFloor, nMinFloor)

# 解法2 时间复杂度：O(N)
'''
    思路：
        假设电梯停在第i层楼， 计算出所有乘客总共要爬的层数Y, 如果有N1个乘客目的地在i层以下、
        有N2个乘客在i层， N3个乘客在i层以上。
        这时如果电梯改停在i-1层， 则N1个乘客少爬一层，N2个乘客多爬一层， N3个乘客多爬一层。
        则i-1层时乘客总共要爬的层数为：Y +(N2 + N3 - N1)
        如果电梯改停在i+1层，则N1个乘客多爬一层，N2个乘客多爬一层，N3个乘客少爬一层。则i+1层时
        乘客总共要爬的层数为：Y + (N1 + N2 - N3)
        综上分析：如果N1 > N2 + N3, 则电梯停在i-1层好，
                如果N3 > N1 + N2, 则电梯停在i+1层好。
'''
nPerson = [-1, 1, 1, 1] # nPerson[i]表示到第i层的乘客数目
nMinFloor = 0
N1 = N3 = 0
N2 = nPerson[1]
nTargetFloor = 1
N = len(nPerson) - 1 # 楼层数
# 电梯停在1楼，需要爬多少楼梯
for i in range(2, N + 1):
    N3 += nPerson[i]
    nMinFloor += nPerson[i] * (i - 1)
# 根据策略迭代
for i in range(2, N+1):
    if (N1 + N2) < N3:
        nTargetFloor = i
        nMinFloor += N1 + N2 - N3
        N1 += N2
        N2 = nPerson[i]
        N3 -= nPerson[i]
    else:
        break
print(nTargetFloor, nMinFloor)

