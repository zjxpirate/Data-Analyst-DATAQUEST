



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


#print(taxi.shape)
#print(one_column.shape)

#print(one_column)

combined = np.concatenate([taxi, one_column], axis=1)

#print(combined)

fifth = taxi[:, 5]

sorted_order = np.argsort(fifth)

#print(sorted_order)


sorted_list = fifth[sorted_order]


#print(sorted_list)



#1
taxi = np.genfromtxt('cars.csv', delimiter=',', skip_header=1)

#print(taxi)


#2
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100

#print(a_bool)
#print(b_bool)
#print(c_bool)


#3
pickup_month = taxi[:,3]

january_bool = pickup_month == 100
january = pickup_month[january_bool]
january_rides = january.shape[0]

#print(january_rides)


#4
tip_amount = taxi[:,3]

tip_bool = tip_amount > 100

top_tips = taxi[tip_bool, 3]

#print(top_tips)


#5
taxi_modified = taxi.copy()

taxi_modified[0, 1] = 1

taxi_modified[:, 6] = 80

mean_value = taxi_modified[:, 5].mean()
taxi_modified[0:3, 5] = mean_value

#print(taxi_modified)


#6
taxi_modified = taxi.copy()

# create a new column filled with `0`.
zeros = np.zeros([taxi_modified.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)

taxi_modified[taxi_modified[:, 1] == 4, 7] = 1

taxi_modified[taxi_modified[:, 1] == 6, 7] = 1

taxi_modified[taxi_modified[:, 1] == 8, 7] = 1

#print(taxi_modified[:, 1])


#7
jfk = taxi[taxi[:, 6]==2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:, 6]==3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:, 6]==5]
newark_count = newark.shape[0]








