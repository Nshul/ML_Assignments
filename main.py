import numpy as np, matplotlib.pyplot as plt

coordx = []
coordy = []

# find the appropriate line for given point using formula
# 
#  m = Summation((x-x_mean)*(y-y_mean))/Summation((x-x_mean)*(x-x_mean))
# 
#  c = y_mean - m*x_mean
def getline():
    c_x = np.array(coordx)
    c_y = np.array(coordy)
    
    # calculate mean for np array
    x_mean = np.mean(c_x)
    y_mean = np.mean(c_y)

    # find value of m
    m = np.sum((c_x - x_mean)*(c_y-y_mean))/np.sum((c_x - x_mean)*(c_x - x_mean))

    # find value of c
    c = y_mean - m*x_mean
    return m,c

# function to draw residual plot
def plt_residual(m,c):

    # for all the points that have been clicked
    for i in range(0,len(coordx)):

        # y coord as predicted from the line
        new_y = m*coordx[i]+c

        # find the points that will lie b/w actual and predicted point
        tempy= np.arange(min(new_y,coordy[i]),max(new_y,coordy[i]))

        # fill in the x coordinate as the the coordinate for which it is
        # being plotted
        tempx = np.ones(len(tempy))*coordx[i]

        # plot this dashed line in red
        ax.plot(tempx,tempy,color='red',linestyle='dashed')

# this event is called when user clicks on the graph
def onclick(event):
    global clk_x,clk_y
    clk_x, clk_y = event.xdata, event.ydata
    coordx.append(clk_x)
    coordy.append(clk_y)
    
    # clear previous plot
    ax.cla()

    # Scatter plot the clicked points
    ax.scatter(coordx,coordy)

    # if more than two points are clicked then draw line
    if(len(coordx)>=2):
        # find the suitable line
        m,c = getline()

        # draw this line
        tempx = np.arange(0,100)
        tempy = m*tempx+c
        ax.plot(tempx,tempy)

        # draw residual plot
        plt_residual(m,c)
    plt.axis([0,100,0,100])
    plt.show()

fig, ax = plt.subplots()

# add a Left Click handler for matplotlib
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# set axis for plot
plt.axis([0,100,0,100])
plt.show()