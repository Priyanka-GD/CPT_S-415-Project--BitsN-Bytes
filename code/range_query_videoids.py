# importing module
from pandas import *
import collections
from operator import itemgetter
from itertools import chain
import operator

# reading CSV file
data = read_csv("/Users/priyanka/Desktop/Big_Data.nosync/Project/Code Files/csv_youtube.csv")
# converting column data to list
length = data['length'].tolist()
videos = []
print("Please enter the value of first range t1 :")
t1=float(input())
print("Please enter the value of first range t2 :")
t2=float(input())
print("Please enter the category :")
cat=input()
for index, row in data.iterrows():
    if t2>t1:
        if row['length']>=t1 and row['length']<=t2 and row['category']==cat:
            videos.append(row['video_ID'])
    else:
        print("Enter a valid range:")
print("Video ID's in given range:")
print(videos)
