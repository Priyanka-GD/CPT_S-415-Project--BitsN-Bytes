# importing module
from pandas import *
import collections
from operator import itemgetter
from itertools import chain
import operator
import numpy
import math
# reading CSV file
data = read_csv("/Users/priyanka/Desktop/Big_Data.nosync/Project/csv_youtube.csv")
print("Please enter the value of k :")
k=input()
#To find top k rating videos
dict_rating = {}
for index, row in data.iterrows():
    if numpy.isnan(row['ratings']):
        val = 0
    else:
        val = int(row['ratings'])
        dict_rating[val]=row['video_ID']
sorted_ratings = dict( sorted(dict_rating.items(), key=operator.itemgetter(1),reverse=True))
print("Top K rating video Ids with respect to its ratings: ")
val = 1
for key,value in sorted_ratings.items():
    val = val+1
    if val<=int(k):
        print(value)
#To find top k popular videos
dict_views = {}
for index, row in data.iterrows():
    if numpy.isnan(row['views']):
        val = 0
    else:
        val = int(row['views'])
        dict_views[val]=row['video_ID']
sorted_views = dict( sorted(dict_views.items(), key=operator.itemgetter(1),reverse=True))
print("Top K popular video Ids with respect to views(Popular videos): ")
val = 1
for key,value in sorted_views.items():
    val = val+1
    if val<=int(k):
        print(value)
