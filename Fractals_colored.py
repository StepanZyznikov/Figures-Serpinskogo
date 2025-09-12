"""Fractal generator.
travel_distance
This script generates a bunch of fractals using random and partial distance travel.

Stepan Zyznikov, McMaster, 2025"""


## Libraries
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import copy

## Classes
class Coordinates:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

## Constants
CANVAS_SIZE = 1
CANVAS_SIZE_INCH = 7
DOT_NUMBER = 10**5

## Functions
def wrapped_input(data_type=str, input_message=''):
    return data_type(input(input_message))

def kissing_ratio(vertex_number): # https://www.sciencedirect.com/science/article/pii/S096007792100494X
    a = np.pi/vertex_number
    e = 2 * a * (np.ceil(vertex_number/4) - 1 / 2) - np.pi / 2
    return round(1 - np.sin(a) / (np.sin(a) + np.cos(e)), 3)

def travel_performer(dot1: Coordinates, dot2: Coordinates, travel_dist_coef):
    return Coordinates(dot1.x * (1-travel_dist_coef) + dot2.x * travel_dist_coef,
                       dot1.y * (1-travel_dist_coef) + dot2.y * travel_dist_coef)

def dot_generation(vertex_coords, mode):
    vertex_number = len(vertex_coords)

    if mode == 1 or mode == 2 and vertex_number == 4:
        travel_distance = 0.5
        jump_distance = 1
    elif mode == 3:
        jump_distance = vertex_number // 2 if vertex_number != 4 else 1
        travel_distance = 2
        mode = 0
    else:
        travel_distance = kissing_ratio(vertex_number)
        jump_distance = vertex_number // 2 if vertex_number != 4 else 1
        mode = 0
    
    prev_coords = Coordinates(0, 0)
    dot_coords = []

    rng = np.random.default_rng()
    curr_vertex_index = rng.integers(vertex_number)

    for i in range(vertex_number):
        dot_coords.append(copy.deepcopy([[]]))

    for i in range(DOT_NUMBER):
        if 2 * jump_distance + 1 > vertex_number:
            shift = rng.integers(vertex_number)
        else:
            shift = rng.integers(2*jump_distance+1)-jump_distance
        curr_vertex_index = (shift + curr_vertex_index + vertex_number + mode) % vertex_number
        dot_coords[curr_vertex_index][0].append(travel_performer(prev_coords, vertex_coords[curr_vertex_index], travel_distance))
        prev_coords = dot_coords[curr_vertex_index][0][-1]
        
    return dot_coords


## Inputs
vertex_number = wrapped_input(int, "Enter integer vertex number:")
mode = wrapped_input(int, "Do you want to generate a regular fractal? 0 for yes.")
if mode == 3: # Quazi-stable fractal generation
    CANVAS_SIZE = 1000


# plot
plt.style.use('_mpl-gallery')
fig = plt.figure(figsize=(CANVAS_SIZE_INCH, CANVAS_SIZE_INCH)) 
ax = plt.subplot()
ax.set(xlim=(-CANVAS_SIZE, CANVAS_SIZE), xticks=[], ylim=(-CANVAS_SIZE, CANVAS_SIZE), yticks=[])


# vertex initialization
cmap = mpl.colormaps["plasma"]
vertex_colors = [cmap(i/vertex_number) for i in range(vertex_number)]

if vertex_number == 4:
    vertex_coords= [Coordinates(1, 1), Coordinates(-1, 1), Coordinates(-1, -1), Coordinates(1, -1)]
else:
    vertex_coords = [Coordinates(np.cos(2*np.pi*i/vertex_number), np.sin(2*np.pi*i/vertex_number)) for i in range(1, vertex_number + 1)]


# starting position generation
dot_coords = dot_generation(vertex_coords, mode)


# plotting
for i in range(vertex_number):
    ax.scatter([j.x for j in dot_coords[i][0]], [j.y for j in dot_coords[i][0]], s=10**3/DOT_NUMBER, c=vertex_colors[i])

plt.show()
