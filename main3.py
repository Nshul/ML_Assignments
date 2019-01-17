import numpy as np
import matplotlib.pyplot as plt

coordx = []
coordy = []
m_ans = 0
c_ans = 0

# # draw this line
#         tempx = np.arange(0,100)
#         tempy = m*tempx+c
#         ax.plot(tempx,tempy)

# this event is called when user clicks on the graph


def onclick(event):
    global clk_x, clk_y
    global m_ans, c_ans
    clk_x, clk_y = event.xdata, event.ydata
    coordx.append(clk_x)
    coordy.append(clk_y)
    y_calc = m_ans*clk_x+c_ans
    error = clk_y - y_calc
    m_ans = m_ans + 0.0001*error*clk_x
    c_ans = c_ans + 0.0001*error
    # m_ans = m_ans + error*clk_x
    # c_ans = c_ans + error
    print(m_ans)
    print(c_ans)
    # clear previous plot
    ax.cla()

    # Scatter plot the clicked points
    ax.scatter(coordx, coordy)

    # draw this line
    tempx = np.arange(0, 100)
    tempy = m_ans*tempx+c_ans
    ax.plot(tempx, tempy)

    plt.axis([0, 100, 0, 100])
    plt.show()


fig, ax = plt.subplots()

# add a Left Click handler for matplotlib
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# set axis for plot
plt.axis([0,100,0,100])
plt.show()