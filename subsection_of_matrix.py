from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list
from mels_teachers_rooms_weights import G, teachers, rooms

def subsection_matrix(n = 4):
    cost = dict_to_list(G)
    #print("here is the cost matrix:", cost)
    cost_copy = []
    for i in range(n):
            temp_list = cost[i][:n]
            #print(temp_list)
            cost_copy.append(temp_list)

    #print("Here is the cost_copy:", cost_copy)
    return cost_copy

def main():
    print(subsection_matrix(5))


if __name__ == '__main__':
    main()
