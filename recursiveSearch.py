#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:49:40 2021

@author: amane
"""

'''
Recursively loop through lists of lists to look for target
'''

target = 'a' #potential PII you are trying to identify

#define nested lists
#create 3 lists (n = 1)
base1 = ['a','b','c']
base2 = ['a','b','c']
base3 = ['a','b','c']

#create 3 lists of lists (n = 2)
l1 = [base1, base2, base3] 
l2 = [base1, base2, base3]
l3 = [base1, base2, base3, 'a']

#create a lists that containes 3 nested lists (n=3)
parent1 = [l1, l2, l3, 'a']

#for loop version searching n = 2
for i in range(0, len(parent1)):
    thing = parent1[i]
    for j in range(0, len(thing)):
        thing2 = thing[j]
        for k in range(0, len(thing2)):
            item = thing2[k]
            if item == target:
                print(item)
            else:
                pass
            
# Recursively search list of lists for target        
def inlist(element, target):
    for i in range(0, len(element)):
        if element[i] == target:
            print(target)

        else:
            if isinstance(element[i], list):
                for item in element[i]:
                    inlist(item , target)
    return True


inlist(parent1,target)


'''
Recursively loop through lists of lists to look for target
'''

##define nested dictionaries
#create 3 dictionaries with 3 key value paries (n = 1)
dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {1: 'a', 2: 'b', 3: 'c'}
dict3 = {1: 'a', 2: 'b', 3: 'c'}

#create 3 dictionaries with dictionaries as values (n = 2)
d1 = {4: dict1, 5: dict2, 6: dict3}
d2 = {4: dict1, 5: dict2, 6: dict3}
d3 = {4: dict1, 5: dict2, 6: dict3}

#create a dictionary that containes 3 nested dictionaries (n=3)
parent2 = {7: d1, 8: d2, 9: d3, 'a': 'a'}

#recursively search dictionary of dictionary for target
def indict(element, target):
    for k,v in element.items():        
        if v == target:
            print(target)
        else:
            if isinstance(v, dict):
                indict(v,target)
    return True


indict(parent2,target)

'''
Recursively loop through combination of lists of dictionaries 
and dictionary of lists to look for target
'''
target = 'a' #potential PII you are trying to identify

#create 3 lists (n = 1)
list1 = ['a','b','c']
list2 = ['a','b','c']
list3 = ['a','b','c']

#create 3 dictionaries with 3 key value paries (n = 1)
dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {1: 'a', 2: 'b', 3: 'c'}
dict3 = {1: 'a', 2: 'b', 3: 'c'}

## n = 2
d1 = {4: list1, 5: list1, 6: list3} #dictionary of lists
d2 = {4: dict1, 5: dict2, 6: dict3} #dictionary of dictionaries
d3 = {4: dict1, 5: list1, 6: dict2} #dictionary of lists and dictionaries

l1 = [list1, list2, list3] #list of lists
l2 = [dict1, dict2, dict3] #list of dictionaries
l3 = [list1, dict2, list2] #list of lists and dictionaries


## n = 3
parent_list = [l1, d1, l2, d2, l3, d3, 'a'] #list of nested lists and nested dictionaries
parent_dict = {1:l1, 'x':d1, 2:l2, 'y':d2, 3:l3, 'z':d3, 4:'a'} #dictionary of nested lists and nested dictionaries


count=0
#recursive Function to search for target variable
def inthere(structure):
    if structure == target: #if the input is the target variable of interest
         print(target)
         print(type(structure))
    elif isinstance(structure, list): #if the input is a list
        for i in range(0, len(structure)): #iterate over every item in a list
            if structure[i] == target: #if the item is the target variable
                print(target)
                print(type(structure))
            else:
                if isinstance(structure[i], list): #if item is a list then recurse back on list
                        inthere(structure[i])
                elif isinstance(structure[i], dict):  #if item is a dictionary then recurse back on each value in the dictionary
                    for k,v in structure[i].items():
                        inthere(v)        
    elif isinstance(structure, dict): #if the input is a dictionary
        for k,v in structure.items(): #iterate over every key:value pair
            if v == target: #if the value is the target variable
                print(target)
                print(type(structure))
            else:
                if isinstance(v, dict): #if value is a dictionary then recurse back on value
                    inthere(v)
                elif isinstance(v, list): #if value is a list then recurse back on each item in the list
                    for i in range(0, len(v)):
                        inthere(v[i])
    return True

inthere(parent_list)
#returns 19 targets

inthere(parent_dict)
#returns 19 targets