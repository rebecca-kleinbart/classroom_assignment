from munkres import Munkres, print_matrix
from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list
from mels_teachers_rooms_weights import G, teachers, rooms
from draw_bipartite import draw_bipartite_solution


def main():

    cost = dict_to_list(G)
    m = Munkres()
    indexes = m.compute(cost)
    #print("these are the indexes: ", indexes)
    #print_matrix(cost, msg='Lowest cost through this matrix:')
    total_cost = 0
    solution = []
    for row, column in indexes:
        value = cost[row][column]
        total_cost += value
        #print(f'({row}, {column}) -> {value}')
        #print("running total: ", total_cost)
        temp_tuple = (teachers[row], rooms[column], G[teachers[row]][rooms[column]])
        solution.append(temp_tuple)

    print(f'total cost: {total_cost}')
    print(solution)

    draw_bipartite_solution(solution, "Bipartite Graph of Munkres Algorithm",total_cost)

    return solution, total_cost



if __name__ == '__main__':
    main()
