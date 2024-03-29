import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Make a random walk, and plot the points.
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Set the size of the plotting window.
    fig, ax = plt.subplots(figsize=(16,10))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

    #Emphasize the first and last points
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove the axes
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    plt.show()
    
    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n': 
    #     break