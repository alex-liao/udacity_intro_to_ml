#!/usr/bin/python

import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    # calculate the number of data points that we are going to remove as outliers (10% of the total number of data points)
    n = int(math.ceil(len(ages) * 0.1))

    # shove the data points into the list 'cleaned_data' first
    for i in range(0, len(ages)):
        data_tuple = (ages[i][0], net_worths[i][0], abs(net_worths[i][0] - predictions[i][0]))
        cleaned_data.append(data_tuple)

    # sort the populated list 'cleaned_data' according to the 3rd value in each data tuple in the list in descending order
    cleaned_data.sort(key=lambda tup: tup[2], reverse=True)

    # drop the 0th ~ nth lowest data tuples, which represents tuples with the biggest residual errors
    cleaned_data = cleaned_data[n:]

    return cleaned_data

