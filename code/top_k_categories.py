# importing module
from pandas import *
import collections
from operator import itemgetter
from itertools import chain
import operator
# reading CSV file
data = read_csv("/Users/priyanka/Desktop/Big_Data.nosync/Project/Code Files/csv_youtube.csv")
# converting column data to list
category = data['category'].tolist()
# printing list data
list_category = [ ]
for cat in category:
    val = str(cat)
    list_category.append(val.replace(u'\xa0', u' '))
#print('Category:', list_category)
print("Please enter the value of k :")
k=input()
temp = []
dict_cat = {}
# memoizing count
for sub in list_category:
        if sub != 'nan':
            if sub in dict_cat:
                val = dict_cat[sub]
                val = val+1
                dict_cat[sub]= val
            else:
                dict_cat[sub]= 1
sorted_d = dict( sorted(dict_cat.items(), key=operator.itemgetter(1),reverse=True))
print("Category with frequencies :")
print(sorted_d)
print("Top K frequent categories: ")
val = 1
for key in sorted_d.keys():
    val = val+1
    if val<=int(k):
        print(key)
