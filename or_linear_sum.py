"""Solve assignment problem using linear assignment solver."""
from ortools.graph import pywrapgraph


def main():
    """Linear Sum Assignment example."""
    assignment = pywrapgraph.LinearSumAssignment()

    costs = [
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 0, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 0, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 0, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 0, 20, 0, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 0, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 0, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 0, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 0, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 0, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 0, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 0, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 0, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 0, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 0, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 0, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 0, 120, 0, 20, 20, 20, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 0, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 20, 60, 120, 0, 20, 20, 60, 20, 20],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 60, 120, 0, 20, 20, 0, 20, 120],
    [20, 20, 20, 20, 0, 20, 100, 20, 20, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 20, 60, 120, 0, 20, 20, 60, 20, 0],
    [20, 20, 20, 20, 0, 0, 100, 20, 20, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 0, 60, 120, 0, 20, 20, 60, 20, 20],
    [20, 20, 20, 20, 0, 20, 100, 20, 120, 0, 20, 20, 20, 20, 20, 20, 20, 20, 120, 120, 80, 120, 0, 20, 20, 80, 20, 120],
    [40, 40, 40, 40, 0, 40, 120, 40, 140, 20, 20, 20, 40, 40, 40, 40, 40, 40, 0, 140, 100, 20, 20, 40, 40, 100, 40, 140],
    [40, 40, 40, 40, 0, 40, 120, 40, 140, 20, 20, 20, 40, 40, 40, 40, 40, 40, 20, 140, 100, 0, 20, 40, 40, 100, 40, 140],
    [60, 60, 60, 60, 0, 60, 140, 60, 160, 40, 60, 60, 60, 60, 60, 60, 60, 60, 160, 160, 120, 160, 60, 60, 60, 120, 60, 160],
    [60, 60, 60, 60, 0, 60, 140, 60, 160, 40, 60, 60, 60, 60, 60, 60, 60, 60, 160, 160, 120, 160, 60, 60, 60, 120, 60, 160],
    [60, 60, 60, 60, 0, 60, 140, 60, 160, 40, 60, 60, 60, 60, 60, 60, 60, 60, 160, 160, 120, 160, 60, 60, 60, 120, 60, 160],
    [60, 60, 60, 60, 0, 60, 140, 60, 160, 40, 60, 60, 60, 60, 60, 60, 60, 60, 160, 160, 120, 160, 60, 60, 60, 120, 60, 160],
    [60, 60, 60, 60, 0, 60, 140, 60, 160, 40, 60, 60, 60, 60, 60, 60, 60, 60, 160, 160, 120, 160, 60, 60, 60, 120, 60, 160],
    [60, 60, 60, 60, 0, 60, 140, 60, 160, 40, 60, 60, 60, 60, 60, 60, 60, 60, 160, 160, 120, 160, 60, 60, 60, 120, 60, 160]]

    num_teachers = len(costs)
    num_rooms = len(costs[0])

    for teacher in range(num_teachers):
        for room in range(num_rooms):
            #if costs[worker][task]:
            assignment.AddArcWithCost(teacher, room, costs[teacher][room])

    status = assignment.Solve()

    if status == assignment.OPTIMAL:
        print(f'Total cost = {assignment.OptimalCost()}\n')
        for i in range(0, assignment.NumNodes()):
            print(f'Teacher {i} assigned to room {assignment.RightMate(i)}.' +
                  f'  Cost = {assignment.AssignmentCost(i)}')
    elif status == assignment.INFEASIBLE:
        print('No assignment is possible.')
    elif status == assignment.POSSIBLE_OVERFLOW:
        print(
            'Some input costs are too large and may cause an integer overflow.')


if __name__ == '__main__':
    main()