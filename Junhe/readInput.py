import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
import math
import json
import seaborn as sns
import collections


# data=pd.read_csv('Brazilian Foreign-Born Estimates from ACS Data 2013-2015.csv')
# data=data.iloc[2:]
# new_header = data.iloc[0] #grab the first row for the header
# data = data[1:] #take the data less the header row
# data.columns = new_header #set the header row as the df header

inputList=[]
age_input = input("Please enter age : ")
input_age = age_input.split(' ')
if len(input_age)==1:
    inputList.append(int(input_age[0]))
else:
    print("Illegal age.")
    exit();

gender_input = input("Please enter gender,Female or Male : ")
input_gender = gender_input
if input_gender.strip()=='Female' or input_gender.strip()=='Male':
    inputList.append(input_gender)
else:
    print("Illegal gender.")
    exit();

marriage_input = input("Please enter marriage status,Married,Widowed,Divorced,Separated or 'Never married or < 15' : ")
input_marriage = marriage_input
if input_marriage.strip()=='Married' or input_marriage.strip()=='Widowed' or input_marriage.strip()=='Divorced' or input_marriage.strip()=='Separated' or input_marriage.strip()=='Never married or < 15':
    inputList.append(input_marriage)
else:
    print("Illegal marriage status.")
    exit();

citizen_input = input("Please enter marriage status,Naturalized Citizen or American citizen : ")
input_citizen = citizen_input
if input_citizen.strip()=='Naturalized Citizen' or input_citizen.strip()=='American citizen':
    inputList.append(input_citizen)
else:
    print("Illegal citizen.")
    exit();

edu_input = input("Please enter education status,'Bachelors Degree or Higher', HighSchool or 'Less than high school': ")
input_edu = edu_input
if input_edu.strip()=='Bachelors Degree or Higher' or input_edu.strip()=='HighSchool' or input_edu.strip()=='Less than high school':
    inputList.append(input_edu)
else:
    print("Illegal education status.")
    exit();

print(inputList)