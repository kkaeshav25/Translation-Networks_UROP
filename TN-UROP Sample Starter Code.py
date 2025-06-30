# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:58:56 2025

@author: kkaes
"""

import pandas as pd
words_per_line =[]
# replace the path with the file path on your end
file_path = r"C:\Users\kkaes\OneDrive\Desktop\UMich Stuff\Winter '25\UROP\Robinson Crusoe - Tamil Ch1.txt"
with open(file_path, "r", encoding = "utf-8") as file:
    for line in file:
        words = line.strip().split()
        words_per_line.append(words)
df_dynamic = pd.DataFrame(words_per_line)   
print(df_dynamic)
#Find a particular word
search_word = "1632-u"
positions = []
for row_idx, row in df_dynamic.iterrows():
    for col_idx, value in row.items():
        if value == search_word:
            index = 14*row_idx + col_idx;
            positions.append((row_idx, col_idx, index))
            

print("Word found at:", positions)

words_per_line =[]
#replace the path qith the file path on your end
file_path = r"C:\Users\kkaes\OneDrive\Desktop\UMich Stuff\Winter '25\UROP\Robinson Crusoe - English Full.txt"
with open(file_path, "r", encoding = "utf-8") as file:
    for line in file:
        words = line.strip().split()
        words_per_line.append(words)
df_dynamic = pd.DataFrame(words_per_line)   
print(df_dynamic)
search_word = "1632,"
positions = []
for row_idx, row in df_dynamic.iterrows():
    for col_idx, value in row.items():
        if value == search_word:
            positions.append((row_idx, col_idx))

print("Word found at:", positions)