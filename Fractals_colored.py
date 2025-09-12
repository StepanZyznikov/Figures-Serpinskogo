"""Fractal generator.
travel_distance
This script generates a bunch of fractals using random and partial distance travel.

Stepan Zyznikov, McMaster, 2025"""


## Libraries
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import copy


## Constants
CANVAS_SIZE = 1
CANVAS_SIZE_INCH = 7
VERTEX_COLOR = '#FF0000'
START_COLOR = "#00FF00"
DOT_COLOR = '#000000'
DOT_NUMBER = 10**5


## Variable Names
vertex_number = 3 # Number of vertexies of the fractal
jump_distance = 1 # The jump distance
travel_distance = 2 # The travel distance


## Functions
def wrapped_input(data_type=str, input_message=''):
    return data_type(input(input_message))

def dot_generation(vertex_coords, jump_distance, vertex_number, travel_distance=0.5, start_coords=[0,0]):
    rng = np.random.default_rng()
    prev_coords = start_coords
    curr_vertex_index = rng.integers(vertex_number)
    dot_coords = []
    for i in range(vertex_number):
        dot_coords.append(copy.deepcopy([[], '#121212']))
    for i in range(DOT_NUMBER):
        shift = rng.integers(2*jump_distance+1)-jump_distance
        curr_vertex_index = (shift + curr_vertex_index + vertex_number) % vertex_number
        dot_coords[curr_vertex_index][0].append([(prev_coords[0] + vertex_coords[curr_vertex_index][0])*travel_distance, 
                                                    (prev_coords[1] + vertex_coords[curr_vertex_index][1])*travel_distance])
        prev_coords = dot_coords[curr_vertex_index][0][-1]
    return dot_coords



## Inputs
vertex_number = wrapped_input(int, "Enter integer vertex number:")
jump_distance = wrapped_input(int, "Enter integer jump distance:")
travel_distance = wrapped_input(float, "Enter divisor for travel distance:")
if travel_distance <= 0:
    travel_distance = 1/2


# plot
plt.style.use('_mpl-gallery')
fig = plt.figure(figsize=(CANVAS_SIZE_INCH, CANVAS_SIZE_INCH)) 
ax = plt.subplot()
ax.set(xlim=(-CANVAS_SIZE, CANVAS_SIZE), xticks=np.arange(-CANVAS_SIZE, CANVAS_SIZE), 
       ylim=(-CANVAS_SIZE, CANVAS_SIZE), yticks=np.arange(-CANVAS_SIZE, CANVAS_SIZE))

cmap = mpl.colormaps["plasma"]
VERTEX_COLORS = [cmap(i/vertex_number) for i in range(vertex_number)]


# vertex initialization
vertex_coords = [[np.cos(2*np.pi*i/vertex_number), np.sin(2*np.pi*i/vertex_number)] for i in range(1, vertex_number + 1)]


# starting position generation
start_coords = [0, 0]
dot_coords = dot_generation(vertex_coords, jump_distance, vertex_number, travel_distance, start_coords)


# plotting
ax.scatter(start_coords[0], start_coords[1], s=10, c=START_COLOR)
for i in range(vertex_number):
    ax.scatter([j[0] for j in dot_coords[i][0]], [j[1] for j in dot_coords[i][0]], s=0.002, c=VERTEX_COLORS[i])

for i in range(vertex_number):
    ax.scatter(vertex_coords[i][0], vertex_coords[i][1], s=50, c=VERTEX_COLORS[i])


plt.show()
