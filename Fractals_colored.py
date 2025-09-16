"""Fractal generator.
travel_distance
This script generates a bunch of fractals using random and partial distance travel.

Stepan Zyznikov, McMaster, 2025"""

# Libraries
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import copy

# Classes
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Constants
CANVAS_SIZE = 1
CANVAS_SIZE_INCH = 7
DOT_NUMBER = 10**5

# Functions
def wrapped_input(data_type=str, input_message=''):
    return data_type(input(input_message))


def kissing_ratio(vertex_number): # https://www.sciencedirect.com/science/article/pii/S096007792100494X
    a = np.pi/vertex_number
    e = 2 * a * (np.ceil(vertex_number/4) - 1 / 2) - np.pi / 2
    return round(1 - np.sin(a) / (np.sin(a) + np.cos(e)), 3)


def travel_performer(dot1: Coordinates, dot2: Coordinates, travel_dist_coef): # https://en.wikipedia.org/wiki/Section_formula
    return Coordinates(dot1.x * (1-travel_dist_coef) + dot2.x * travel_dist_coef,
                       dot1.y * (1-travel_dist_coef) + dot2.y * travel_dist_coef)


def default_dot_generation(vertex_coords): # https://en.wikipedia.org/wiki/Chaos_game
    vertex_number = len(vertex_coords)
    travel_distance = kissing_ratio(vertex_number)
    jump_distance = vertex_number // 2 if vertex_number != 4 else 1

    prev_coords = Coordinates(0, 0)
    dot_coords = []

    rng = np.random.default_rng()
    curr_vertex_index = rng.integers(vertex_number)

    for i in range(vertex_number):
        dot_coords.append(copy.deepcopy([]))

    for i in range(DOT_NUMBER):
        if 2 * jump_distance + 1 > vertex_number:
            shift = rng.integers(vertex_number)
        else:
            shift = rng.integers(2 * jump_distance + 1) - jump_distance

        curr_vertex_index = (shift + curr_vertex_index + vertex_number) % vertex_number

        dot_coords[curr_vertex_index].append(travel_performer(prev_coords, vertex_coords[curr_vertex_index], travel_distance))
        prev_coords = dot_coords[curr_vertex_index][-1]
    return dot_coords

def modded_dot_generation(vertex_coords, mode): # Restricted chaos game and quazi-stable chaos game
    vertex_number = len(vertex_coords)

    if mode == 1 or mode == 2 and vertex_number == 4:
        travel_distance = 0.5
        jump_distance = 1
    elif mode == 2 and (vertex_number == 5 or vertex_number == 6):
        vertex_coords.append(Coordinates(0, 0))
        travel_distance = kissing_ratio(vertex_number)
        jump_distance = vertex_number // 2 + 1
        vertex_number += 1
    elif mode == 3:
        jump_distance = vertex_number // 2 if vertex_number != 4 else 1
        travel_distance = 2
        mode = 0
    elif mode == 4 and vertex_number == 4:
        vertex_coords.extend([Coordinates(0, 1), Coordinates(
            1, 0), Coordinates(0, -1), Coordinates(-1, 0)])
        vertex_number = 8
        travel_distance = 2/3
        jump_distance = vertex_number // 2
    else:
        travel_distance = kissing_ratio(vertex_number)
        jump_distance = vertex_number // 2 if vertex_number != 4 else 1
        mode = 0

    prev_coords = Coordinates(0, 0)
    dot_coords = []

    rng = np.random.default_rng()
    curr_vertex_index = rng.integers(vertex_number)

    for i in range(vertex_number):
        dot_coords.append(copy.deepcopy([]))

    for i in range(DOT_NUMBER):
        if 2 * jump_distance + 1 > vertex_number:
            shift = rng.integers(vertex_number)
        else:
            shift = rng.integers(2 * jump_distance + 1) - jump_distance

        curr_vertex_index = (shift + curr_vertex_index + vertex_number + mode) % vertex_number

        dot_coords[curr_vertex_index].append(travel_performer(prev_coords, vertex_coords[curr_vertex_index], travel_distance))

        if curr_vertex_index == 5 and mode == 2 and vertex_number == 6:
            dot_coords[curr_vertex_index][-1].x *= -1

        prev_coords = dot_coords[curr_vertex_index][-1]

    return dot_coords


# Inputs
vertex_number = wrapped_input(int, "Enter integer vertex number:")
mode = wrapped_input(
    int, "Do you want to generate a regular fractal? 0 for yes.")
if mode == 3:  # Quazi-stable fractal generation
    CANVAS_SIZE = 1000


# plot
plt.style.use('_mpl-gallery')
fig = plt.figure(figsize=(CANVAS_SIZE_INCH, CANVAS_SIZE_INCH))
ax = plt.subplot()
ax.set(xlim=(-CANVAS_SIZE, CANVAS_SIZE), xticks=[],
       ylim=(-CANVAS_SIZE, CANVAS_SIZE), yticks=[])


# vertex initialization
cmap = mpl.colormaps["plasma"]
if vertex_number == 4 and mode == 4:
    vertex_colors = [cmap(i/8) for i in range(8)]
else:
    vertex_colors = [cmap(i/vertex_number) for i in range(vertex_number)]
vertex_colors.append("#000000")

if vertex_number == 4:
    vertex_coords = [Coordinates(
        1, 1), Coordinates(-1, 1), Coordinates(-1, -1), Coordinates(1, -1)]
else:
    vertex_coords = [Coordinates(np.cos(2*np.pi*i/vertex_number), np.sin(
        2*np.pi*i/vertex_number)) for i in range(1, vertex_number + 1)]


# starting position generation
if mode == 0:
    dot_coords = default_dot_generation(vertex_coords)
else:
    dot_coords = modded_dot_generation(vertex_coords, mode)


# plotting
for i in range(len(dot_coords)):
    ax.scatter([j.x for j in dot_coords[i]], [
               j.y for j in dot_coords[i]], s=10**3/DOT_NUMBER, c=vertex_colors[i])

plt.show()
