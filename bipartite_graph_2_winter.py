import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mcolors

import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout

def main():

    teachers = ['Winter']
    rooms = ['0072','0089','1007', '1101','1103','2067','2071','2073','2075','2077','2101','2106','3071','3073','3077','4068A','4068B','4073','4077','4078','GymA','GymB','Float1','Float2','Float3','Float4','Float5','Float6']

    G = nx.Graph()

    #G.add_nodes_from(['Ali','Archaga','Baxter','Bright', 'Cas', 'Ellis', 'Farnham', 'Gary', 'Gostomski', 'Hendrick', 'Hurth', 'King', 'Kleibart', 'Lotti', 'Masco', 'Maxfield', 'Morales', 'Newberger', 'Priestley', 'Robins', 'Rosenberg', 'Satriano', 'Sewall', 'Stern', 'Wallace', 'Winter', 'Wolff','Zaino'], bipartite=0)
    G.add_nodes_from(teachers, bipartite = 0)
    #G.add_nodes_from(['0072','0089','1007', '1101','1103','2067','2071','2073','2075','2077','2101','2106','3071','3073','3077','4068A','4068B','4073','4077','4078','GymA','GymB','Float1','Float2','Float3','Float4','Float5','Float6'],bipartite=1)
    G.add_nodes_from(rooms, bipartite = 1)
    #bottom_nodes, top_nodes = bipartite.sets(G)
    #G.add_edge('Winter', "0072", weight = 80)
    print("edge added")

    e = [('Winter', "0072", 80),('Winter', "0089",80),('Winter', "1077",80),('Winter', "1101",80),('Winter', "1103", 80),('Winter', "2067", 80),('Winter', "2071", 80),('Winter', "2073", 80),('Winter', "2075", 80),('Winter', "2077", 80),('Winter', "2101", 80),('Winter', "2106", 80),('Winter', "3071", 80),('Winter', "3073", 80),('Winter', "3077", 20),('Winter', "4068A", 60),('Winter', "4068B", 0),('Winter', "4073", 60),('Winter', "4077", 60),('Winter', "4078", 80),('Winter', "GymA", 100),('Winter', "GymB",100),('Winter', "Float1", 120),('Winter', "Float2",120),('Winter', "Float3", 120),('Winter', "Float4", 120),('Winter', "Float5",120),('Winter', "Float6",120)]

    print("list e is saved")

    weights =[tup[2] for tup in e]

    print(weights)
    print(type(weights[1]))
    print(type(i for i in weights))
    #G.add_edges_from([('Winter', "0072", weight = 80),('Winter', "0089",weight = 80),('Winter', "1077",weight = 80),('Winter', "1101",weight = 80),('Winter', "1103",weight = 80),('Winter', "2067",weight = 80),('Winter', "2071",weight = 80),('Winter', "2073",weight = 80),('Winter', "2075",weight = 80),('Winter', "2077",weight = 80),('Winter', "2101",weight = 80),('Winter', "2106",weight = 80),('Winter', "3071",weight = 80),('Winter', "3073",weight = 80),('Winter', "3077",weight = 20),('Winter', "4068A",weight = 60),('Winter', "4068B",weight = 0),('Winter', "4073",weight = 60),('Winter', "4077",weight = 60),('Winter', "4078",weight = 80),('Winter', "GymA",weight = 100),('Winter', "GymB",weight = 100),('Winter', "Float1",weight = 120),('Winter', "Float2",weight = 120),('Winter', "Float3",weight = 120),('Winter', "Float4",weight = 120),('Winter', "Float5",weight = 120),('Winter', "Float6",weight = 120)])
    print(bipartite.is_bipartite(G))

    G.add_edges_from(((a,b) for a,b, *_ in e))
    #pos = bipartite_layout(G,teachers)
    #color = (0,(1 - .8 * (i for i in weights ))),0)
    colors = [(1 - .008 * i) for i in weights]
    #print((1 - .8 * i)) for i in weights
    print("These are the color weights:")
    print(colors)

    rgb_colors = []
    for x in colors:
        rgb_colors.append((0,x,0))
    print(rgb_colors)
    nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, teachers ), node_size = 100, node_color = 'gray', width = 2, edge_color = rgb_colors)
    print("Graph drawn")
    plt.show()
    plt.figure(1)
    print("figure shown")
    plt.close(1)
    print("Graph shown")
    print("Everything is done.")

if __name__ == '__main__':
    main()
