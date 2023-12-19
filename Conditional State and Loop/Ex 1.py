#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:41:29 2023

@author: Sherzod Sanatov
"""

#Conditional state and loop

#Python program to get the next day of a given date

year=int(input("Input a year: \n>>>"))


if (year%400==0):
    leap_year=True
elif (year%100==0):
    leap_year=False
elif (year%4==0):
    leap_year=True
    
month=int(input("Input a month \n>>>"))

if month in [1,3,5,7,8,10,12]:
    month_length=31
elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
else:
    month_length=30

day=int(input("Input a day \n>>>"))

if day<month_length:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1
        
print(f"Next date is {year}:{month}:{day}")


