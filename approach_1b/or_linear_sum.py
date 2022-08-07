"""Solve assignment problem using ortools linear assignment solver."""
from ortools.graph import pywrapgraph

from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list
from mels_teachers_rooms_weights import G, teachers, rooms

from draw_bipartite import draw_bipartite_solution

def main():
    """Linear Sum Assignment using  OR Tools"""
    assignment = pywrapgraph.LinearSumAssignment()

    cost = dict_to_list(G)
    solution = []

    num_teachers = len(cost)
    num_rooms = len(cost[0])

    for teacher in range(num_teachers):
        for room in range(num_rooms):
            #if cost[worker][task]:
            assignment.AddArcWithCost(teacher, room, cost[teacher][room])

    status = assignment.Solve()

    if status == assignment.OPTIMAL:
        print(f'Total cost = {assignment.OptimalCost()}\n')
        for i in range(0, assignment.NumNodes()):
            print(f'{teachers[i]} assigned to room {rooms[assignment.RightMate(i)]}.' +  f'  Cost = {assignment.AssignmentCost(i)}')
            temp_tuple = (teachers[i], rooms[assignment.RightMate(i)],assignment.AssignmentCost(i))
            solution.append(temp_tuple)

        total_cost = assignment.OptimalCost()
        print(solution)
        draw_bipartite_solution(solution, "Bipartite Graph of Linear Sum Assignment 3 (Ortools)", total_cost)

        return solution, total_cost

    elif status == assignment.INFEASIBLE:
        print('No assignment is possible.')

        return solution, -1


    elif status == assignment.POSSIBLE_OVERFLOW:
        print(
            'Some input costs are too large and may cause an integer overflow.')
        return solution, -1


if __name__ == '__main__':
    main()
