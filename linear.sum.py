from scipy.optimize import linear_sum_assignment
import numpy as np
from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list
from mels_teachers_rooms_weights import G, teachers, rooms

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mcolors

import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout
from draw_bipartite import draw_bipartite_solution


def main():
    cost = np.array(dict_to_list(G))

    row_ind, col_ind = linear_sum_assignment(cost)

    #array representing the optimal assignment
    optimal_assignment = col_ind

    total_cost = cost[row_ind, col_ind].sum()

    print(optimal_assignment)
    print(total_cost)

    #printing out optimal solution
    solution = []
    for x in range(len(optimal_assignment)):
        temp_teacher = teachers[x]
        temp_room = rooms[optimal_assignment[x]]
        temp_tuple = (temp_teacher, temp_room,G[temp_teacher][temp_room])
        print(temp_tuple)
        solution.append(temp_tuple)

    print(solution)
    draw_bipartite_solution(solution)

    return solution

if __name__ == '__main__':
    main()




""" Solution is below:
Ali : Float4
Archaga : 2075
Baxter : 3073
Bright : 1103
Cas : Float1
Ellis : Float6
Farnham : 0089
Gary : 2073
Gostomski : 4068A
Hendrick : 2067
Hurth : 1101
King : 2071
Kleinbart : Float3
Lotti : 1007
Masco : Float2
Maxfield : 3071
Morales : 2101
Newberger : 0072
Priestley : GymA
Robins : 4077
Rosenberg : 3077
Satriano : GymB
Sewall : 4078
Stern : 2106
Wallace : 2077
Winter : 4068B
Wolff : Float5
Zaino : 4073

"""
