from ortools.sat.python import cp_model

from dictionary_to_list import dict_of_weights_to_list_of_lists_of_weights as dict_to_list
from mels_teachers_rooms_weights import G, teachers, rooms

from draw_bipartite import draw_bipartite_solution

def main():
    # Data
    cost = dict_to_list(G)
    solution = []

    num_workers = len(cost)
    num_tasks = len(cost[0])

    # Model
    model = cp_model.CpModel()

    # Variables
    x = []
    for i in range(num_workers):
        t = []
        for j in range(num_tasks):
            t.append(model.NewBoolVar(f'x[{i},{j}]'))
        x.append(t)

    # Constraints
    # Each worker is assigned to at most one task.
    for i in range(num_workers):
        model.AddAtMostOne(x[i][j] for j in range(num_tasks))

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        model.AddExactlyOne(x[i][j] for i in range(num_workers))

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(cost[i][j] * x[i][j])
    model.Minimize(sum(objective_terms))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Total cost = {solver.ObjectiveValue()}')
        print()
        for i in range(num_workers):
            for j in range(num_tasks):
                if solver.BooleanValue(x[i][j]):
                    print(f' {teachers[i]} assigned to task {rooms[j]}; Cost = {cost[i][j]}')
                    temp_tuple = (teachers[i], rooms[j],cost[i][j])
                    solution.append(temp_tuple)

        total_cost = solver.ObjectiveValue()
        print(solution)
        draw_bipartite_solution(solution, "Bipartite Graph of CSP5 Solution (Ortools)", total_cost)

        return solution, total_cost

    else:
        print('No solution found.')


if __name__ == '__main__':
    main()
