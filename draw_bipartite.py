#TODO: Make this stop running after a certain amount of time

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mcolors

import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout

from mels_teachers_rooms_weights import G, teachers, rooms

def draw_bipartite_solution(S_Graph):
    Solution_Graph = nx.Graph()

    Solution_Graph.add_nodes_from(teachers, bipartite = 0)
    Solution_Graph.add_nodes_from(rooms, bipartite = 1)

    e = S_Graph
    weights =[tup[2] for tup in e]

    #print(bipartite.is_bipartite(Solution_Graph))

    Solution_Graph.add_edges_from(((a,b) for a,b, *_ in e))
    colors = [(1 - (.008 * i)) for i in weights]
    print("These are the color weights:")
    print(colors)

    rgb_colors = []
    for x in colors:
        rgb_colors.append((0,x,0))
    print(rgb_colors)
    plt.title("Solution from Linear Sum Algorithm")
    nx.draw_networkx(Solution_Graph, pos = nx.drawing.layout.bipartite_layout(Solution_Graph, teachers ), node_size = 100, node_color = 'gray', width = 2, edge_color = rgb_colors)
    plt.show()
    plt.figure(1)
    plt.close(1)
