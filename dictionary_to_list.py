def dict_of_weights_to_list_of_lists_of_weights(cost_dict):
    costs = []
    for teacher, rooms in cost_dict.items():
        print("\nName:", teacher)
        values = []
        for weight in rooms:
            print(weight + ':', rooms[weight])
            values.append(rooms[weight])
        costs.append(values)
    print(costs)

    return(costs)

def main():
    return dict_of_weights_to_list_of_lists_of_weights(G)

if __name__ == '__main__':
    main()
