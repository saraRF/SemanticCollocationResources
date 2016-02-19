#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open(input_path,'r')

total_cols = 0
filtered_by_pmi = 0
correct_cols = 0
correct_lfs = 0
correct_filtered_cols = 0
correct_filtered_lfs = 0

chunks = f.read().split('\n')

first_200 = chunks[:200]
next_200 = chunks[200:400]
final_200 = chunks[400:600]

for line in chunks[:600]:
	print line
	colFeatures = line.split(',')
	total_cols += 1
	if colFeatures[0][0] == '+':
		filtered_by_pmi += 1
		
	if colFeatures[1] == '+':
		correct_cols +=1
		
	if colFeatures[0][0] == '+' and colFeatures[1] == '+':
		correct_filtered_cols += 1
		
	if colFeatures[2].rstrip() == '+':
		correct_lfs += 1
		
	if colFeatures[0][0] == '+' and colFeatures[2].rstrip() == '+':
		correct_filtered_lfs += 1
		
print 'total number of collocations -> ' + str(total_cols)
print 'number of collocations after filtering by PMI -> ' + str(filtered_by_pmi)
print 'number of correct collocations -> ' + str(correct_cols) 
print 'number of correct filtered collocations -> ' + str(correct_filtered_cols)
print 'number of correct LFs -> ' + str(correct_lfs)
print 'number of correct filtered LFs -> ' + str(correct_filtered_lfs)

	
	

