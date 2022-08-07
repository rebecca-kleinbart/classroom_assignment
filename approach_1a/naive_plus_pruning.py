from itertools import permutations

def main():

    score_matrix = [
    [100, 20, 120, 0],
    [0, 20, 120, 0],
    [100, 20, 120, 0],
    [100, 20, 120, 0],
    ]


    m = len(score_matrix)

    #create a list called score_sums to add sums and min_assignments_so_far to add orderings
    current_min = 100000000
    score_sums = []
    min_assignments_so_far = []
    value_of_assignment = 0
    mins = []
    mins_permutations = []
    # enumerate all the permutations of the numbers 0 - (len(score_matrix)-1)
    for assignment in permutations(range(m)):
        list_assignment = list(assignment)
        #Add to the list named "score_sums" the sum of the values for each possible permutation
        for i, j in enumerate(assignment):
            value_of_assignment += score_matrix[i][j]
            if value_of_assignment > current_min:
                break
            min_assignments_so_far.append(list_assignment)
        if value_of_assignment <= current_min:
            current_min = value_of_assignment
            score_sums.append(value_of_assignment)
        value_of_assignment = 0
        print("Here is score_sums: ", score_sums)
    print("Here is the whole list, score_sums: ", score_sums)


    minSum = min(score_sums)
    print("here is the minimum sum: ", minSum)

    score_sums.count(minSum)

    for i, num in enumerate(score_sums):
        if num == minSum :
            print("The minimum is the ", i, "th permutation", sep = '')
            print("And its value is", num)
            print(min_assignments_so_far[i])
            mins.append(i)
            mins_permutations.append(min_assignments_so_far[i])

    teachers = ['Ali','Archaga','Baxter','Bright', 'Cas', 'Ellis', 'Farnham', 'Gary', 'Gostomski', 'Hendrick', 'Hurth', 'King', 'Kleinbart', 'Lotti', 'Masco', 'Maxfield', 'Morales', 'Newberger', 'Priestley', 'Robins', 'Rosenberg', 'Satriano', 'Sewall', 'Stern', 'Wallace', 'Winter', 'Wolff','Zaino']
    rooms = ['0072','0089','1007', '1101','1103','2067','2071','2073','2075','2077','2101','2106','3071','3073','3077','4068A','4068B','4073','4077','4078','GymA','GymB','Float1','Float2','Float3','Float4','Float5','Float6']


    #printing out optimal solutions
    for assignment in mins_permutations:
        for i, j in enumerate(assignment):
            for x in range(len(assignment)):
                temp_teacher = teachers[x]
                temp_room = rooms[assignment[x]]
                print(temp_teacher, ":", temp_room )

if __name__ == '__main__':
    main()


#solution =  min(
    #sum(score_matrix[i][j] for i, j in enumerate(assignment))
    #for assignment in permutations(range(m))
#)

#print("Here is the/an optimal solution:", solution)
