import pandas as pd
import statistics as stx
import csv

df=pd.read_csv('StudentsPerformance.csv')

data=df['reading score'].tolist()

#mean

mean=sum(data)/len(data)
median=stx.median(data)
mode=stx.mode(data)
stdev=stx.stdev(data)

print('mean = ',mean)
print('mode = ',mode)
print('median = ',median)
print('stdev = ',stdev)

#1,2,3 standard deviation for weight

first_stdev_start,first_stdev_end= mean-stdev,+stdev
second_stdev_start,second_stdev_end= mean-(2*stdev),mean+(2*stdev)
third_stdev_start,third_stdev_end= mean-(3*stdev),mean+(3*stdev)

# % of data within 1,2,3 standard deviation for height

list_of_data_within_1_stdev=[result for result in list if result>first_stdev_start and result <first_stdev_end]
list_of_data_within_2_stdev=[result for result in list if result>second_stdev_start and result <second_stdev_end]
list_of_data_within_3_stdev=[result for result in list if result>third_stdev_start and result <third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(list_of_data_within_1_stdev)*100.0/len(list)))
print("{}% of data for height lies within 2 standard deviations".format(len(list_of_data_within_2_stdev)*100.0/len(list)))
print("{}% of data for height lies within 3 standard deviations".format(len(list_of_data_within_3_stdev)*100.0/len(list)))
