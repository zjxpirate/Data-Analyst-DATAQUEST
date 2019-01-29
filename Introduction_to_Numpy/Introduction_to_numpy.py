


# 2 begins here:

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
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

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

#print(taxi)




# 3 begins here:

taxi_five = taxi[:5]

taxi_ten = taxi[:10]

#print(taxi_five)




# 4 begins here:

row_0 = taxi[0]

rows_391_to_500 = taxi[391:501]

row_21_column_5 = taxi[21, 5]

#print(row_21_column_5)




# 5 begins here:

columns_1_4_7 = taxi[:,[1,4,7]]
row_99_columns_5_to_8 = taxi[99,5:9]
rows_100_to_200_column_14 = taxi[100:201,14]

#print(rows_100_to_200_column_14)





# 6 begins here:

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

trip_mph = trip_distance_miles / trip_length_hours

#print(trip_mph)





# 7 begins here:

# using the `/` operator:
trip_mph_1 = trip_distance_miles / trip_length_hours

# using the `numpy.divide()` function:
trip_mph_2 = np.divide(trip_distance_miles,trip_length_hours)

#print(trip_mph_2)





# 8 begins here:

mph_min = trip_mph.min()
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

#print(mph_max)





# 9 begins here:

taxi_column_means = taxi.mean(axis=0)

#print(taxi_column_means)





# 10 begins here:

trip_mph_2d = np.expand_dims(trip_mph, axis=1)

taxi = np.concatenate([taxi, trip_mph_2d], axis=1)

#print(taxi)





# 11 begins here:

trip_mph = taxi[:, 15]

sorted_order = np.argsort(trip_mph)

taxi_sorted = taxi[sorted_order]

#print(taxi_sorted)





































