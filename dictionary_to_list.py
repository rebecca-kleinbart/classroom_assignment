""" This function takes a cost dictionary as its input (A dictionary of dictionaries with the outer key being teachers and the outer values being a dictionary with the inner key being rooms and the inner values being weights/costs).
    It outputs a cost matrix, a list of lists. Each list represents the costs of one teacher, for each room. """

def dict_of_weights_to_list_of_lists_of_weights(cost_dict):
    #create a list called 'costs'
    costs = []
    #loop over inputted dictionary and create a list of costs for a particular teacher. Then add that entire list to costs.
    for teacher, rooms in cost_dict.items():
        values = []
        for weight in rooms:
            values.append(rooms[weight])
        costs.append(values)

    return(costs)

def main():
    return dict_of_weights_to_list_of_lists_of_weights(G)

if __name__ == '__main__':
    main()
