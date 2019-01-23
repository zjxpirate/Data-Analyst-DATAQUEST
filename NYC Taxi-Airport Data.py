



import csv
import numpy as np


f = open("cars.csv", "r")

taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]


# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)
#print(converted_taxi_list)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

total_horsepower = taxi[:, 3]
total_weight = taxi[:, 4]

#weight_per_horsepower = np.divide(total_weight, total_horsepower)
#print(weight_per_horsepower)


bottom_sum = taxi.sum(axis=0)

#print(bottom_sum)


one_column = taxi[:, 0]

one_column = np.expand_dims(one_column, axis=1)


print(taxi.shape)
print(one_column.shape)

#print(one_column)

combined = np.concatenate([taxi, one_column], axis=1)

#print(combined)

fifth = taxi[:, 5]

sorted_order = np.argsort(fifth)

#print(sorted_order)


sorted_list = fifth[sorted_order]


print(sorted_list)
