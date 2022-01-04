#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:12:55 2021

@author: josephmontenegro
"""
import pandas as pd
import matplotlib.pyplot as plt

path_to_data = "//Users//josephmontenegro//Downloads//stockd//data.csv"
df = pd.read_csv(path_to_data)

val = input("Maximum or minimum")
val = val.lower()

stat = input("Price, Delta, Gamma")
stat = stat.lower()

if(val == "minumum"):
    if(stat == "gamma"):
        print(df)
        print("Date: ", end="")
        print(df[df.gex == df.gex.min()])
        print("Minimum: " + str(min(df['gex'])))
    
elif (val == "maximum"):
    if(stat == "gamma"):
        print(df)
        print("Date: ", end="")
        print(df[df.gex == df.gex.max()])
        print("Maximum: " + str(max(df['gex'])))    
    elif(stat == "price"):
        print("Date: ", end="")
        print(df[df.price == df.price.max()])
        print("Maximum: " + str(max(df['price'])))

else:
    print("Bad input. Need 'maximum' or 'minimum' ")
