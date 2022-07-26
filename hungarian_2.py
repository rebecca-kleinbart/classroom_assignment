from hungarian_algorithm import algorithm

#import bipartite_graph_1
def main():

    G = {
        'Ali':      {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Archaga':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 1,  '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Baxter':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 1,  '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Bright':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        #'Cas':      {'0072': 1,  '0089':20, '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071':  1, '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1,  '2106': 1,  '3071': 1,  '3073': 1,  '3077': 1,  '4068A': 1,  '4068B': 1,  '4073': 1,  '4077': 1,  '4078': 1,  'GymA': 1,  'GymB': 1,  'Float1': 1,  'Float2': 1,  'Float3': 1,  'Float4': 1,  'Float5': 1,  'Float6': 1},
        'Ellis':    {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 1,  '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Farnham':  {'0072': 100,'0089':1,  '1007': 100, '1101': 100,'1103': 100,'2067': 100,'2071': 100,'2073': 100,'2075': 100,'2077': 100,'2101': 100,'2106': 100,'3071': 100,'3073': 100,'3077': 100,'4068A': 100,'4068B': 100,'4073': 100,'4077': 100,'4078': 100,'GymA': 120,'GymB': 120,'Float1': 140,'Float2': 140,'Float3': 140,'Float4': 140,'Float5': 140,'Float6': 140},
        'Gary':     {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 1,  '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Gostomski':{'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 1,  '4068B': 120,'4073': 20, '4077': 20, '4078': 120,'GymA': 140,'GymB': 140,'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Hendrick': {'0072': 1,  '0089':1,  '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071': 1,  '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1,  '2106': 1,  '3071': 1,  '3073': 1,  '3077': 1,  '4068A': 1,  '4068B': 1,  '4073': 1,  '4077': 1,  '4078': 1,  'GymA': 20, 'GymB': 20, 'Float1': 40, 'Float2': 40, 'Float3': 40, 'Float4': 40, 'Float5': 40, 'Float6': 40},
        'Hurth':    {'0072': 20, '0089':20, '1007': 20,  '1101': 1,  '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'King':     {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 1,  '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Kleinbart':{'0072': 20, '0089':20, '1007': 20,  '1101': 1,  '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Lotti':    {'0072': 20, '0089':20, '1007': 1,   '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Masco':    {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1,  '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Maxfield': {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 1,  '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Morales':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 1,  '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Newberger':{'0072': 1,  '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Priestley':{'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 120,'4068B': 120,'4073': 120,'4077': 120,'4078': 120,'GymA': 1,  'GymB': 20, 'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Robins':   {'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 20, '4068B': 120,'4073': 20, '4077': 1,  '4078': 120,'GymA': 140,'GymB': 140,'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Rosenberg':{'0072': 80, '0089':80, '1007': 80,  '1101': 80, '1103': 80, '2067': 80, '2071': 80, '2073': 80, '2075': 80, '2077': 80, '2101': 80, '2106': 80, '3071': 80, '3073': 80, '3077': 1,  '4068A': 60, '4068B': 60, '4073': 60, '4077': 60, '4078': 80, 'GymA': 100,'GymB': 100,'Float1': 120,'Float2': 120,'Float3': 120,'Float4': 120,'Float5': 120,'Float6': 120},
        'Satriano': {'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 120,'4068B': 120,'4073': 120,'4077': 120,'4078': 120,'GymA': 20, 'GymB': 1,  'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Sewall':   {'0072': 1,  '0089':1,  '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071': 1,  '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1,  '2106': 1,  '3071': 1,  '3073': 1,  '3077': 1,  '4068A': 1,  '4068B': 1,  '4073': 1,  '4077': 1,  '4078': 1,  'GymA': 20, 'GymB': 20, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Stern':    {'0072': 20, '0089':1,  '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 1,  '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Wallace':  {'0072': 20, '0089':1,  '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 1,  '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Winter':   {'0072': 80, '0089':80, '1007': 80,  '1101': 80, '1103': 80, '2067': 80, '2071': 80, '2073': 80, '2075': 80, '2077': 80, '2101': 80, '2106': 80, '3071': 80, '3073': 80, '3077': 20, '4068A': 60, '4068B': 1,  '4073': 60, '4077': 60, '4078': 80, 'GymA': 100,'GymB': 100,'Float1': 120,'Float2': 120,'Float3': 120,'Float4': 120,'Float5': 120,'Float6': 120},
        'Wolff':    {'0072': 20, '0089':1,  '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Zaino':    {'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 20, '4068B': 120,'4073': 1,  '4077': 20, '4078': 120,'GymA': 140,'GymB': 140,'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
    }

    H = {
    	'A': { '#191': 22,  '#122': 14,  '#173': 120, '#121': 21, '#128': 4,   '#104': 51 },
    	'B': { '#191': 19,  '#122': 12,  '#173': 172, '#121': 21, '#128': 28,  '#104': 43 },
    	'C': { '#191': 161, '#122': 122, '#173': 2,   '#121': 50, '#128': 128, '#104': 39 },
    	'D': { '#191': 19,  '#122': 22,  '#173': 90,  '#121': 11, '#128': 28,  '#104': 4 },
    	'E': { '#191': 1,   '#122': 30,  '#173': 113, '#121': 14, '#128': 28,  '#104': 86 },
    	'F': { '#191': 60,  '#122': 70,  '#173': 170, '#121': 28, '#128': 68,  '#104': 104 },
    }

    ex_H = {
    	'x1': {'y1': 1, 'y2': 6},
    	'x2': {'y2': 8, 'y3': 6},
    	'x3': {'y1': 4, 'y3': 1}
    }

    G_mod_A = {
        'Ali':      {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Archaga':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 1,  '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Baxter':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 1,  '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Bright':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
    }

    G_mod_B = {
        'Ali':      {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20},
        'Archaga':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 1,  '2077': 20, '2101': 20},
        'Baxter':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20},
        'Bright':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20},
        'Cas':      {'0072': 1,  '0089':20, '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071':  1, '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1},
        'Ellis':    {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20},

    }

    G_mod_C = {
        'Ali':      {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20},
        'Archaga':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20},
        'Baxter':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20},
        'Bright':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1},

    }

    G_mod_D = {
        'Ali':      {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20},
        'Archaga':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20},
        'Baxter':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20},
        'Bright':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1, '2067': 20, '2071': 20, '2073': 20},
        'Cas':      {'0072': 1,  '0089':20, '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071':  1, '2073': 1},
        'Ellis':    {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20},
        'Farnham':  {'0072': 100,'0089':1,  '1007': 100, '1101': 100,'1103': 100,'2067': 100,'2071': 100,'2073': 100},
        'Gary':     {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 1},
    }

    G_mod_E = {
        'Ali':      {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Archaga':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 1,  '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Baxter':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 1,  '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Bright':   {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Cas':      {'0072': 1,  '0089':20, '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071':  1, '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1,  '2106': 1,  '3071': 1,  '3073': 1,  '3077': 1,  '4068A': 1,  '4068B': 1,  '4073': 1,  '4077': 1,  '4078': 1,  'GymA': 1,  'GymB': 1,  'Float1': 1,  'Float2': 1,  'Float3': 1,  'Float4': 1,  'Float5': 1,  'Float6': 1},
        'Ellis':    {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 1,  '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Farnham':  {'0072': 100,'0089':1,  '1007': 100, '1101': 100,'1103': 100,'2067': 100,'2071': 100,'2073': 100,'2075': 100,'2077': 100,'2101': 100,'2106': 100,'3071': 100,'3073': 100,'3077': 100,'4068A': 100,'4068B': 100,'4073': 100,'4077': 100,'4078': 100,'GymA': 120,'GymB': 120,'Float1': 140,'Float2': 140,'Float3': 140,'Float4': 140,'Float5': 140,'Float6': 140},
        'Gary':     {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 1,  '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Gostomski':{'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 1,  '4068B': 120,'4073': 20, '4077': 20, '4078': 120,'GymA': 140,'GymB': 140,'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Hendrick': {'0072': 1,  '0089':1,  '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071': 1,  '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1,  '2106': 1,  '3071': 1,  '3073': 1,  '3077': 1,  '4068A': 1,  '4068B': 1,  '4073': 1,  '4077': 1,  '4078': 1,  'GymA': 20, 'GymB': 20, 'Float1': 40, 'Float2': 40, 'Float3': 40, 'Float4': 40, 'Float5': 40, 'Float6': 40},
        'Hurth':    {'0072': 20, '0089':20, '1007': 20,  '1101': 1,  '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'King':     {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 1,  '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Kleinbart':{'0072': 20, '0089':20, '1007': 20,  '1101': 1,  '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Lotti':    {'0072': 20, '0089':20, '1007': 1,   '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Masco':    {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 1,  '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Maxfield': {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 1,  '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Morales':  {'0072': 20, '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 1,  '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Newberger':{'0072': 1,  '0089':20, '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Priestley':{'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 120,'4068B': 120,'4073': 120,'4077': 120,'4078': 120,'GymA': 1,  'GymB': 20, 'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Robins':   {'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 20, '4068B': 120,'4073': 20, '4077': 1,  '4078': 120,'GymA': 140,'GymB': 140,'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Rosenberg':{'0072': 80, '0089':80, '1007': 80,  '1101': 80, '1103': 80, '2067': 80, '2071': 80, '2073': 80, '2075': 80, '2077': 80, '2101': 80, '2106': 80, '3071': 80, '3073': 80, '3077': 1,  '4068A': 60, '4068B': 60, '4073': 60, '4077': 60, '4078': 80, 'GymA': 100,'GymB': 100,'Float1': 120,'Float2': 120,'Float3': 120,'Float4': 120,'Float5': 120,'Float6': 120},
        'Satriano': {'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 120,'4068B': 120,'4073': 120,'4077': 120,'4078': 120,'GymA': 20, 'GymB': 1,  'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},
        'Sewall':   {'0072': 1,  '0089':1,  '1007': 1,   '1101': 1,  '1103': 1,  '2067': 1,  '2071': 1,  '2073': 1,  '2075': 1,  '2077': 1,  '2101': 1,  '2106': 1,  '3071': 1,  '3073': 1,  '3077': 1,  '4068A': 1,  '4068B': 1,  '4073': 1,  '4077': 1,  '4078': 1,  'GymA': 20, 'GymB': 20, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Stern':    {'0072': 20, '0089':1,  '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 1,  '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Wallace':  {'0072': 20, '0089':1,  '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 1,  '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Winter':   {'0072': 80, '0089':80, '1007': 80,  '1101': 80, '1103': 80, '2067': 80, '2071': 80, '2073': 80, '2075': 80, '2077': 80, '2101': 80, '2106': 80, '3071': 80, '3073': 80, '3077': 20, '4068A': 60, '4068B': 1,  '4073': 60, '4077': 60, '4078': 80, 'GymA': 100,'GymB': 100,'Float1': 120,'Float2': 120,'Float3': 120,'Float4': 120,'Float5': 120,'Float6': 120},
        'Wolff':    {'0072': 20, '0089':1,  '1007': 20,  '1101': 20, '1103': 20, '2067': 20, '2071': 20, '2073': 20, '2075': 20, '2077': 20, '2101': 20, '2106': 20, '3071': 20, '3073': 20, '3077': 20, '4068A': 20, '4068B': 20, '4073': 20, '4077': 20, '4078': 20, 'GymA': 40, 'GymB': 40, 'Float1': 60, 'Float2': 60, 'Float3': 60, 'Float4': 60, 'Float5': 60, 'Float6': 60},
        'Zaino':    {'0072': 120,'0089':120,'1007': 120, '1101': 120,'1103': 120,'2067': 120,'2071': 120,'2073': 120,'2075': 120,'2077': 120,'2101': 120,'2106': 120,'3071': 120,'3073': 120,'3077': 120,'4068A': 20, '4068B': 120,'4073': 1,  '4077': 20, '4078': 120,'GymA': 140,'GymB': 140,'Float1': 160,'Float2': 160,'Float3': 160,'Float4': 160,'Float5': 160,'Float6': 160},

    }

    list = algorithm.find_matching(G, matching_type = 'min', return_type = 'list')
    print(list)
    total = algorithm.find_matching(G, matching_type = 'min', return_type = 'total' )

    #print(list(G.algorithm.vertices.keys())[0])
    #generate = algorithm.generate_feasible_labeling(G, list(G.algorithm.vertices.keys())[0])

    bipartite = algorithm.Graph.is_bipartite(G,None)
    print(bipartite)
    print(list)
    print(total)

if __name__ == '__main__':
    main()
