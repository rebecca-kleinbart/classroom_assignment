import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout

from mels_teachers_rooms_weights import G, teachers, rooms

""""This program creates a complete bipartite graph using the teacher, 'Winter', as an arbitary example.
The teacher is one of the nodes and the the rooms are the other set.
The edges are the connections between each teacher and each room.
The colors of the edges represent the weights/costs of a teacher being assigned a particular room. (Bright green = zero and Black = 160, the highest weight)
Since using all teachers and all rooms would make the graph unreadable, we take this graph as one arbitrary illustation of the cost matrix model.
"""
def main():
    #create graph from dictionary of dictionaries fround in mels_teachers_rooms_weights.
    H = nx.Graph()
    H.add_nodes_from(teachers[25], bipartite = 0)
    H.add_nodes_from(rooms, bipartite = 1)

    #Set of tuples that connects the teacher name, the room, and the weight used in main for the edges
    e = [('Winter', "0072", 80),('Winter', "0089",80),('Winter', "1077",80),('Winter', "1101",80),('Winter', "1103", 80),('Winter', "2067", 80),('Winter', "2071", 80),('Winter', "2073", 80),('Winter', "2075", 80),('Winter', "2077", 80),('Winter', "2101", 80),('Winter', "2106", 80),('Winter', "3071", 80),('Winter', "3073", 80),('Winter', "3077", 20),('Winter', "4068A", 60),('Winter', "4068B", 0),('Winter', "4073", 60),('Winter', "4077", 60),('Winter', "4078", 80),('Winter', "GymA", 100),('Winter', "GymB",100),('Winter', "Float1", 120),('Winter', "Float2",120),('Winter', "Float3", 120),('Winter', "Float4", 120),('Winter', "Float5",120),('Winter', "Float6",120)]

    #Create a list of weights
    weights =[tup[2] for tup in e]

    #if graph is bipartite, draw it
    if bipartite.is_bipartite(H):
        H.add_edges_from(((a,b) for a,b, *_ in e))
        colors = [(1 - .006 * i) for i in weights]
        rgb_colors = []
        for x in colors:
            rgb_colors.append((0,x,0))
        nx.draw_networkx(H, pos = nx.drawing.layout.bipartite_layout(H, teachers), node_size = 100, node_color = 'gray', width = 2, edge_color = rgb_colors)
        plt.title("Complete Bipartite Graph: \n Cost of Assigning Winter To Each Room")
        plt.suptitle("Bright Green = 0 \n Black = 160",x = .9, y = .95 , fontsize=8)

        plt.show()
        plt.figure(1)
        plt.close(1)

if __name__ == '__main__':
    main()
