import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout

teachers = ['Ali','Archaga','Baxter','Bright', 'Cas', 'Ellis', 'Farnham', 'Gary', 'Gostomski', 'Hendrick', 'Hurth', 'King', 'Kleinbart', 'Lotti', 'Masco', 'Maxfield', 'Morales', 'Newberger', 'Priestley', 'Robins', 'Rosenberg', 'Satriano', 'Sewall', 'Stern', 'Wallace', 'Winter', 'Wolff','Zaino']
rooms = ['0072','0089','1007', '1101','1103','2067','2071','2073','2075','2077','2101','2106','3071','3073','3077','4068A','4068B','4073','4077','4078','GymA','GymB','Float1','Float2','Float3','Float4','Float5','Float6']

G = nx.Graph()

#G.add_nodes_from(['Ali','Archaga','Baxter','Bright', 'Cas', 'Ellis', 'Farnham', 'Gary', 'Gostomski', 'Hendrick', 'Hurth', 'King', 'Kleibart', 'Lotti', 'Masco', 'Maxfield', 'Morales', 'Newberger', 'Priestley', 'Robins', 'Rosenberg', 'Satriano', 'Sewall', 'Stern', 'Wallace', 'Winter', 'Wolff','Zaino'], bipartite=0)
G.add_nodes_from(teachers, bipartite = 0)
#G.add_nodes_from(['0072','0089','1007', '1101','1103','2067','2071','2073','2075','2077','2101','2106','3071','3073','3077','4068A','4068B','4073','4077','4078','GymA','GymB','Float1','Float2','Float3','Float4','Float5','Float6'],bipartite=1)
G.add_nodes_from(rooms, bipartite = 1)
#bottom_nodes, top_nodes = bipartite.sets(G)

G.add_edges_from([('Archaga', "2075"),('Baxter', "3075"),('Bright', "1103"),('Cas', "0072"),('Cas', "0089"),('Cas', "1077"),('Cas', "1101"),('Cas', "1103"),('Cas', "2067"),('Cas', "2071"),('Cas', "2073"),('Cas', "2075"),('Cas', "2077"),('Cas', "2101"),('Cas', "2106"),('Cas', "3071"),('Cas', "3073"),('Cas', "3077"),('Cas', "4068A"),('Cas', "4068B"),('Cas', "4073"),('Cas', "4077"),('Cas', "4078"),('Cas', "GymA"),('Cas', "GymB"),('Cas', "Float1"),('Cas', "Float2"),('Cas', "Float3"),('Cas', "Float4"),('Cas', "Float5"),('Cas', "Float6"),('Ellis', "4077"),('Farnham', "0089"),('Gary', "2073"),('Gostomski', "4068"),('Hendrick', "0072"),('Hendrick', "0089"),('Hendrick', "1077"),('Hendrick', "1101"),('Hendrick', "1103"),('Hendrick', "2067"),('Hendrick', "2071"),('Hendrick', "2073"),('Hendrick', "2075"),('Hendrick', "2077"),('Hendrick', "2101"),('Hendrick', "2106"),('Hendrick', "3071"),('Hendrick', "3073"),('Hendrick', "3077"),('Hendrick', "4068A"),('Hendrick', "4068B"),('Hendrick', "4073"),('Hendrick', "4077"),('Hendrick', "4078"),('Hurth', "1101"),('King', "2071"),('Kleinbart', "1101"),('Lotti', "1077"),('Masco', "1103"),('Maxfield', "3071"),('Morales', "2101"),('Newberger', "0072"),('Priestley', "GymA"),('Rosenberg',"3077"),('Robins', "3077"),('Satriano', "GymB"),('Hurth', "1101"),('Sewall', "0072"),('Sewall', "0089"),('Sewall', "1077"),('Sewall', "1101"),('Sewall', "1103"),('Sewall', "2067"),('Sewall', "2071"),('Sewall', "2073"),('Sewall', "2075"),('Sewall', "2077"),('Sewall', "2101"),('Sewall', "2106"),('Sewall', "3071"),('Sewall', "3073"),('Sewall', "3077"),('Sewall', "4068A"),('Sewall', "4068B"),('Sewall', "4073"),('Sewall', "4077"),('Sewall', "4078"),('Stern', "2106"),('Wallace', "2077"),('Winter', "4068B"),('Wolff', "2067"),('Zaino', "4073")])
print(bipartite.is_bipartite(G))

#pos = bipartite_layout(G,teachers)
nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, teachers ), node_size = 100, node_color = 'gray', width = 2, edge_color = 'green')
print("Graph drawn")
plt.show()
plt.figure(1)
print("figure shown")
plt.close(1)
print("Graph shown")
print("Everything is done.")
