import numpy as np, matplotlib.pyplot as plt

# find the appropriate line for given point using formula
# 
#  m = Summation((x-x_mean)*(y-y_mean))/Summation((x-x_mean)*(x-x_mean))
# 
#  c = y_mean - m*x_mean
def getline(c_x,c_y):
    # calculate mean for np array
    x_mean = np.mean(c_x)
    y_mean = np.mean(c_y)

    # find value of m
    m = np.sum((c_x - x_mean)*(c_y-y_mean))/np.sum((c_x - x_mean)*(c_x - x_mean))

    # find value of c
    c = y_mean - m*x_mean
    return m,c

# Anscombe's Quartet
x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
x2 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
x3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

# First subplot
plt.subplot(2,2,1)
plt.scatter(x1,y1)
m,c = getline(x1,y1)
tempx = np.arange(0,20)
tempy = m*tempx+c
plt.plot(tempx,tempy,color="red")
plt.title("1st Dataset")

# Second subplot
plt.subplot(2,2,2)
plt.scatter(x2,y2)
m,c = getline(x2,y2)
tempx = np.arange(0,20)
tempy = m*tempx+c
plt.plot(tempx,tempy,color="red")
plt.title("2nd Dataset")

# Third subplot
plt.subplot(2,2,3)
plt.scatter(x3,y3)
m,c = getline(x3,y3)
tempx = np.arange(0,20)
tempy = m*tempx+c
plt.plot(tempx,tempy,color="red")
plt.title("3rd Dataset")

# Fourth subplot
plt.subplot(2,2,4)
plt.scatter(x4,y4)
m,c = getline(x4,y4)
tempx = np.arange(0,20)
tempy = m*tempx+c
plt.plot(tempx,tempy,color="red")
plt.title("4th Dataset")

plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()