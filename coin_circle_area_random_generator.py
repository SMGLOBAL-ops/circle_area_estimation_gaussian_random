import numpy as np
from matplotlib import pyplot as plt

def generate_unit_circle(N=0):

    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sqrt(1.0)

    x = np.random.uniform(-1.00, 1.00, size=N)
    y = np.random.uniform(-1.00, 1.00, size=N)

    coordinates = np.stack((x,y), axis=-1)
    
    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)

    points_outside_circle_coordinates = []

    # equation of unit circle inequality to capture points outside of the bounds of the circle but within 1x1 square
    for coordinate in coordinates:
        if coordinate[0]**2 + coordinate[1]**2 > r:
            points_outside_circle_coordinates.append(coordinate)

    points_outside_circle = len(points_outside_circle_coordinates)
    points_inside_circle = N - points_outside_circle

    percentage_outside = (points_outside_circle / N) * 100

    print(f'Total number of points generated: {N}')
    print("Number of points inside circle: ", points_inside_circle)
    print(f'Number of points outside circle: {points_outside_circle} ==> {percentage_outside}%')

    C = points_inside_circle

    area_approximation = 4*C / N
    area_error = abs(100 - (area_approximation / np.pi * 100))
    print(f'Approximation of area of circle: {area_approximation}')
    print(f'inaccuracy of area of circle: {area_error}%')
            
    fig, ax = plt.subplots(1)

    ax.plot(x1, x2)
    ax.set_aspect(1) 

    plt.scatter(x, y, s = 4)
    plt.xlim(-1.25, 1.25) 
    plt.ylim(-1.25, 1.25)
    plt.grid(linestyle='--')
    plt.title("Coin generator within unit circle", fontsize=8) 
    plt.show()

    return

# Arbitrary choice of 50 random points
generate_unit_circle(50)

