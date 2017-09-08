#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
															
def bwt(l):
	matrix_list=[]
	bwt_text=''
	matrix_list.append(l)
	for index in range(1, len(l)):		
		matrix_list.append(l[index:] + l[:index])
	position=0
	print matrix_list
	sorted_matrix = matrix_sort(matrix_list, position)
	print sorted_matrix
	bwt=''
	for riga in sorted_matrix: bwt=bwt+riga[-1]
	matrix_list=[]
	bwt_text=bwt_text+bwt
	return bwt_text
	
def matrix_sort(matrix, posizione):							###ordina a seconda della chiave la matrice di stringhe in input, aumentando di 1 la posizione in caso di conflitti
	sorted_matrix = []
	for carattere in alpha:
		temporary_matrix = []
		for elemento in matrix:
			if elemento[posizione] == carattere: temporary_matrix.append(elemento) 
		if len(temporary_matrix)>1: 
			for sorted_element in matrix_sort(temporary_matrix, posizione+1):
				sorted_matrix.append(sorted_element)
		else: 
			for sorted_element in temporary_matrix:
				sorted_matrix.append(sorted_element)
		
	return sorted_matrix

#def randomize(text):
#	for character in text: 
		

def conversion(text):
	list=['0','1','2','3','4','5','6','7','8','9']
	dict={'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
	counter=0
	for character in text:
		if character in list: 
			text=text[0:counter]+dict[character]+text[counter+1:]
		counter=counter+1
	return text

if __name__ == "__main__":
	alphafile=open('alpha.txt', 'r')
	alpha=alphafile.readline().rstrip().strip()
	if len(sys.argv)<3: 
		print 'Two arguments are required. Possible choices for argument 1: file, text. Argument 2: <filename> or <text_to_transform>'
	else:		
		input_type=sys.argv[1]
		if input_type == 'file':	
			filename= sys.argv[2]
			text= open(filename, 'r')
			newfile_name= 'bwt_' + filename
			outfile= open(newfile_name, 'w')
			file=alpha[0]	
			for riga in text:
				file = file + riga
			counter = 0
			for character in file:
				if character != '\n': counter = counter + 1
				else: file=file[0:counter]+'>'+file[counter+1:] 
			transform = bwt(file)
			counter = 0
			for character in transform:
				if character != '>': counter = counter + 1
				else: transform = transform[0:counter]+'\n'+transform[counter+1:] 					
			outfile.write(transform)
			print transform
		elif input_type != 'file' and input_type != 'text': print 'Invalid argument. First argument must be: file or text.'
		elif len(sys.argv)>3: print 'Max number of argument is 2. Use _ instead of space for direct text insertion.'
		else:
			riga = alpha[0]+ sys.argv[2].strip().rstrip()
			transform = bwt(riga)
			print transform						
	
	