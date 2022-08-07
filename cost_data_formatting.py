import numpy as np
import pandas as pd
from mels_teachers_rooms_weights import G, teachers, rooms
from tabulate import tabulate
from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list

def list_to_numpy(listy):
    lst = listy
    a = np.array(lst)
    return a

def main():
    # display table
    cost = np.array(dict_to_list(G))
    print(tabulate(cost))
    print("\n" * 5)

    numpy_cost = list_to_numpy(cost)
    df_cost = pd.DataFrame(cost, teachers, columns = rooms)

    #print(numpy_cost)
    print(df_cost)

    df_cost.to_csv('cost_matrix.csv')

if __name__ == '__main__':
    main()
