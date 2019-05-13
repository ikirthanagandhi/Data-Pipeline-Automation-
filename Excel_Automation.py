#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:49:48 2019

@author: kirth
"""

# Question 3

# Importing libraries
import os
import pandas as pd

#Set working directory
path = '/Users/kirth/Documents/KG/nested_bean'
os.chdir(path)

#Reading CSV file
format_df = pd.read_csv('AutomationTest3.csv')

#removing top row as we've irrelevant string 
format_df = format_df.drop(format_df.index[[0]])

#Converting data types to datetime format
format_df['Order Date'] = pd.to_datetime(format_df['Order Date'], format = '%m/%d/%y')
format_df['Ship Date'] = pd.to_datetime(format_df['Ship Date'], format = '%m/%d/%y')

#Formating Order Date and Ship Date to YYYY-MM-DD
format_df['Order Date'] = pd.to_datetime(format_df['Order Date'], format = '%Y-%m-%d')
format_df['Ship Date'] = pd.to_datetime(format_df['Ship Date'], format = '%Y-%m-%d')

#Saving file in the current working folder
format_df.to_excel("ABC orders Jan 2018.xlsx", sheet_name='Orders')







