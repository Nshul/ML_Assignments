import numpy as np
import matplotlib.pyplot as plt
import sys

coordx = []
coordy = []
m_ans = 0
c_ans = 25

# this event is called when user clicks on the graph


def onclick(event):
    global clk_x, clk_y
    global m_ans, c_ans
    try:
        clk_x, clk_y = event.xdata, event.ydata
        coordx.append(clk_x)
        coordy.append(clk_y)
        y_calc = m_ans*clk_x+c_ans
        cum_m = cum_c = 4
        # for loop in range(100):
        while abs(cum_m) > 0.000002 or abs(cum_c) > 0.000002:
            # cum_error = 0
            cum_m = 0
            cum_c = 0
            for itr in range(len(coordx)):
                clk_x = coordx[itr]
                clk_y = coordy[itr]
                y_calc = m_ans*clk_x+c_ans
                error = clk_y - y_calc
                cum_m += 0.0001*error*clk_x
                cum_c += 0.0001*error
                print("**")
                print(m_ans)
                print(c_ans)
                print(error)
                print("**")
            m_ans += (cum_m/len(coordx))
            c_ans += (cum_c/len(coordx))

            # clear previous plot
            ax.cla()

            # Scatter plot the clicked points
            ax.scatter(coordx, coordy)

            # draw this line
            tempx = np.arange(0, 50)
            tempy = m_ans*tempx+c_ans
            ax.plot(tempx, tempy)

            plt.axis([0, 50, 0, 50])
            plt.draw()
            plt.pause(0.001)
    except KeyboardInterrupt:
        print("Interrupt")
        sys.exit()
    # plt.show()


fig, ax = plt.subplots()

# add a Left Click handler for matplotlib
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# set axis for plot
plt.axis([0, 50, 0, 50])
plt.ion()
plt.show(block=True)
