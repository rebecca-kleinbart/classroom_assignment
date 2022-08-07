import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout

from mels_teachers_rooms_weights import G, teachers, rooms

def draw_bipartite_solution(S_Graph, title_of_graph = "Bipartite Graph", total_cost = ""):
    """Input: A list of tuples with teacher name, room, and weight (created as solution to  assignment) and string for a title
       Output: Draws and displays bipartite graph. """

    #Create graph and add one set of nodes from the imported list of teachers and other from the imported ist of rooms
    Solution_Graph = nx.Graph()
    Solution_Graph.add_nodes_from(teachers, bipartite = 0)
    Solution_Graph.add_nodes_from(rooms, bipartite = 1)

    #Create edges using
    e = S_Graph
    weights =[tup[2] for tup in e]

    if bipartite.is_bipartite(Solution_Graph):
        Solution_Graph.add_edges_from(((a,b) for a,b, *_ in e))
        colors = [(1 - (.006 * i)) for i in weights]

        rgb_colors = []
        for x in colors:
            rgb_colors.append((0,x,0))
        print(rgb_colors)
        plt.title(title_of_graph)
        plt.suptitle("Bright Green = 0 \n Black = 160",x = .9, y = .95 , fontsize=8)
        #cost_label = "total cost = " + total_cost
        plt.xlabel("total cost = " + str(total_cost))
        nx.draw_networkx(Solution_Graph, pos = nx.drawing.layout.bipartite_layout(Solution_Graph, teachers ), node_size = 100, node_color = 'gray', width = 2, edge_color = rgb_colors)
        plt.show()
        plt.figure(1)
        plt.close(1)
    else:
        print("A bipartite graph cannot be created from the data supplied.")
