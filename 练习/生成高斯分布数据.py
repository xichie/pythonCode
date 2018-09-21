import numpy as np
import matplotlib.pyplot as plt

def generate_data3():
    np.random.RandomState(1)

    #generate
    mean = [0.0, 0.0, 0.0]
    cov = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    x1 = np.random.multivariate_normal(mean, cov, size = [250000])
    x1 = np.c_[x1, np.ones([x1.shape[0], 1])]

    mean = [0.0, 1.0, 0.0]
    cov = [[1.0, 0.0, 1.0], [0.0, 2.0, 2.0], [1.0, 2.0, 5.0]]
    x2 = np.random.multivariate_normal(mean, cov, size = [250000])
    x2 = np.c_[x2, np.full([x2.shape[0], 1], 2)]

    mean = [-1.0, 0.0, 1.0]
    cov = [[2.0, 0.0, 0.0], [0.0, 6.0, 0.0], [0.0, 0.0, 1.0]]
    x3 = np.random.multivariate_normal(mean, cov, size = [250000])
    x3 = np.c_[x3, np.full([x2.shape[0], 1], 3)]

    mean = [0.0, 0.5, 1.0]
    cov = [[2.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 3.0]]
    x4 = np.random.multivariate_normal(mean, cov, size = [250000])
    x4 = np.c_[x4, np.full([x4.shape[0], 1], 4)]

    #merge
    result = np.r_[x1,x2]
    result = np.r_[result, x3]
    result = np.r_[result, x4]
    np.random.shuffle(result)
    print(result.shape)

    #save 
    np.savetxt("gauss3.txt", result, fmt = "%.5f")
    
    # plot 
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)
    x, y, z = x1[:10000, 0], x1[:10000, 1], x1[:10000, 2]
    ax.scatter3D(x, y ,z, c = 'b', marker = 'o')

    x, y, z = x2[:10000, 0], x2[:10000, 1], x2[:10000, 2]
    ax.scatter3D(x, y ,z, c = 'r', marker = 'o')

    x, y, z = x3[:10000, 0], x3[:10000, 1], x3[:10000, 2]
    ax.scatter3D(x, y ,z, c = 'k', marker = 'o')

    x, y, z = x4[:10000, 0], x4[:10000, 1], x4[:10000, 2]
    ax.scatter3D(x, y ,z, c = 'c', marker = 'o')

    plt.show()

def generate_data2():
    np.random.RandomState(1)
    #generate
    mean = [0.0, 0.0]
    cov = [[1.0, 0.0], [0.0, 1.0]]
    x1 = np.random.multivariate_normal(mean, cov, size = [400000])
    x1 = np.c_[x1, np.ones([x1.shape[0], 1])]

    mean = [1.0, 1.0]
    cov = [[1.0, 0.0], [0.0, 1.0]]
    x2 = np.random.multivariate_normal(mean, cov, size = [400000])
    x2 = np.c_[x2, np.full([x2.shape[0], 1], 2)]

    mean = 0.5 * np.array([0.5, 0.5]) + 0.5 * np.array([-0.5, 0.5])
    cov = [[1.0, 0.0], [0.0, 1.0]]
    x3 = np.random.multivariate_normal(mean, cov, size = [400000])
    x3 = np.c_[x3, np.full([x2.shape[0], 1], 3)]
    #merge
    result = np.r_[x1,x2]
    result = np.r_[result, x3]
    np.random.shuffle(result)
    print(result.shape)

    #save 
    np.savetxt("gauss2.txt", result, fmt = "%.5f")
    
    # plot 
    plt.figure()
    plt.scatter(x1[:,0], x1[:,1])
    plt.scatter(x2[:,0], x2[:,1])
    plt.scatter(x3[:,0], x3[:,1])
    plt.show()

def generate_data1():
    np.random.RandomState(1)

    #generate
    mean = [1.0, 1.0]
    cov = [[0.6, -0.2], [-0.2, 0.6]]
    x1 = np.random.multivariate_normal(mean, cov, size = [500000])
    x1 = np.c_[x1, np.ones([x1.shape[0], 1])]

    mean = [2.5, 2.5]
    cov = [[0.2, -0.1], [-0.1, 0.2]]
    x2 = np.random.multivariate_normal(mean, cov, size = [500000])
    x2 = np.c_[x2, np.full([x2.shape[0], 1], 2)]

    #plot 
    # plt.figure()
    # plt.scatter(x1[:,0], x1[:,1])
    # plt.scatter(x2[:,0], x2[:,1])
    # plt.show()

    #merge
    result = np.r_[x1,x2]
    np.random.shuffle(result)
    #save 
    # np.savetxt("gauss1.txt", result, fmt = "%.5f")

if __name__ == "__main__":
    generate_data3()