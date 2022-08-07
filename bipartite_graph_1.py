import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout
from mels_teachers_rooms_weights import G, teachers, rooms


'''Running this program creates a bipartite graph with one set of nodes
being the teachers and the other set being the rooms. The edges connect
zero-weighted pairs '''


def get_teacher_room_weighted_zero_edges(dict_of_dicts):
    '''The function,  get_teacher_room_weighted_zero_edges, m takes as input the dictionary of dictionaries
    which has names of teachers as outer keys and a dictionary of rooms
    and their respective weights for that teacher as the outer value.

    The function outputs a list of tuples that contain the edges of the graph.
    Each edge connects a teacher and a room, if the respective weight of that room
    in the input equals zero. '''

    edges = []
    for teacher in dict_of_dicts.items():
        for key in teacher[1].items():
            if key[1] == 0:
                temp_tuple = (teacher[0], key[0])
                edges.append(temp_tuple)
    return edges



def main():
    #create the graph using the imported from mels_teachers_rooms_weights and edges from the function, get_teacher_room_weighted_zero_edges, above.
    H = nx.Graph()
    H.add_nodes_from(teachers, bipartite = 0)
    H.add_nodes_from(rooms, bipartite = 1)
    edge_list = get_teacher_room_weighted_zero_edges(G)
    H.add_edges_from(edge_list)

    if bipartite.is_bipartite:
        nx.draw_networkx(H, pos = nx.drawing.layout.bipartite_layout(H, teachers ), node_size = 100, node_color = 'gray', width = 2, edge_color = (0,1,0))
        print("Graph drawn")
        plt.title("Graph of All Zero-Weight Edges")
        plt.show()
        plt.figure(1)
        plt.close(1)

    else:
        print("Could not print bipartite graph")
if __name__ == '__main__':
    main()
