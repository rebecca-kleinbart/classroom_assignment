def order_variables(cost_matrix):
    """ Function orders cost matrix by greatet sum to least sum"""
    return sorted(cost_matrix,key=sum, reverse = True)
