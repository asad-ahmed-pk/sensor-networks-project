# plot.py
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import read_db

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    #time.sleep(1)
    # Add x and y to lists
    #xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))

    temp, time = read_db.get_last_temp_record()
    ys.append(temp)

    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    ys = ys[-20:]
    #print(xs)
    #print(ys)
    # Draw x and y lists
    ax.clear()
    ax.plot(ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature Reading')
    plt.ylabel('Temperature (C)')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
