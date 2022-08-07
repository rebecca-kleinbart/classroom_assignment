#TODO: add comments
#TODO: Improve variable ordering heuristic

import time

from itertools import permutations
from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list
from mels_teachers_rooms_weights import G, teachers, rooms
from order_variables import order_variables

from draw_bipartite import draw_bipartite_solution
from subsection_of_matrix import subsection_matrix

def main():

    '''cost_whole = dict_to_list(G)'''
    m = 9
    print("m =", m)
    cost_unsorted = subsection_matrix(m)
    #print(cost_unsorted)
    cost = order_variables(cost_unsorted)
    #print(cost)


    m = len(cost)

    #create a list called score_sums to add sums and min_assignments_so_far to add orderings
    current_min = 100000000
    score_sums = []
    min_assignments_so_far = []
    value_of_assignment = 0
    mins = []
    mins_permutations = []

    list_of_solutions = []

    # enumerate all the permutations of the numbers 0 - (len(cost)-1)
    for assignment in permutations(range(m)):
        list_assignment = list(assignment)
        #Add to the list named "score_sums" the sum of the values for each possible permutation
        for i, j in enumerate(assignment):
            value_of_assignment += cost[i][j]
            if value_of_assignment > current_min:
                break
            min_assignments_so_far.append(list_assignment)
        if value_of_assignment <= current_min:
            current_min = value_of_assignment
            score_sums.append(value_of_assignment)
        value_of_assignment = 0
        #print("Here is score_sums: ", score_sums)
    #print("Here is the whole list, score_sums: ", score_sums)


    total_cost = min(score_sums)
    print("here is the minimum sum: ", total_cost)

    score_sums.count(total_cost)

    for i, num in enumerate(score_sums):
        if num == total_cost :
            #print("The minimum is the ", i, "th permutation", sep = '')
            #print("And its value is", num)
            #print(min_assignments_so_far[i])
            mins.append(i)
            mins_permutations.append(min_assignments_so_far[i])


    #printing out optimal solutions
    for assignment in mins_permutations:
        solution = []

        for i, j in enumerate(assignment):
            for x in range(len(assignment)):
                temp_teacher = teachers[x]
                temp_room = rooms[assignment[x]]
                #print(temp_teacher, ":", temp_room )
                temp_tuple = (temp_teacher, temp_room,G[temp_teacher][temp_room])
                solution.append(temp_tuple)
                #print(solution)
                draw_bipartite_solution(solution, "Bipartite Graph for Naive Approach")

        list_of_solutions.append(solution)
    #print("Here is a list of all the solutions: ", list_of_solutions)
    number_of_solutions = len(list_of_solutions)
    print("There are ", number_of_solutions, "optimal assignment solutions")
    return list_of_solutions,total_cost, number_of_solutions

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
