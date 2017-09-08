#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
																								
def rank_last(last):
	rank_dict = {}
	ranked_last = []
	for character in last:
		if rank_dict.get(character, 0) == 0:
			ranked_char = character+'0'
			ranked_last.append(ranked_char)
			rank_dict[character] = 1
		else:
			ranked_char = character+str(rank_dict[character])
			ranked_last.append(ranked_char)
			rank_dict[character] = rank_dict[character]+1
	return ranked_last
	
	
def lf_mapping(last):
	ranked_last = rank_last(last)
	ranked_first =[]
	for element in alpha:
		counter = 0
		for character in last:

			if element == character:
				ranked_char = character+str(counter)
				ranked_first.append(ranked_char)
				counter=counter+1
	pointer = 0
	decript = ''
	temporary = ranked_last[0]
	while len(decript) < len(ranked_first)-1:
		for element in ranked_first:
			if temporary != element: 
				pointer=pointer+1
			else: break
		temporary = ranked_last[pointer]
		decript = ranked_first[pointer][0]+decript
		pointer=0
	return decript
		
	

if __name__ == "__main__":
	alphafile=open('config.txt', 'r')
	alpha=alphafile.readline().rstrip().strip()
	if len(sys.argv)<3: 
		print 'Two arguments are required. Possible choices for argument 1: file, text. Argument 2: <filename> or <text_to_transform>'
	else:		
		input_type=sys.argv[1]
		l=[]
		if input_type == 'file':	
			filename= sys.argv[2]
			text= open(filename, 'r')
			newfile_name= 'LF_' + filename
			outfile= open(newfile_name, 'w')
			file=''	
			for riga in text:
				file=file+riga
			counter = 0
			for character in file:
				if character != '\n': counter = counter + 1
				else: file=file[0:counter]+'>'+file[counter+1:]
			decript = lf_mapping(file)
			counter = 0
			for character in decript:
				if character != '>': counter = counter + 1
				else: decript=decript[0:counter]+'\n'+decript[counter+1:]
			outfile.write(decript)
		elif input_type != 'file' and input_type != 'text': print 'Invalid argument. First argument must be: file or text.'
		elif len(sys.argv)>3: print 'Max number of argument is 2. Use _ instead of space for direct text insertion. Space, > and < are not allowed.'
		else:
			riga = sys.argv[2].strip().rstrip()
			print riga
			decript = lf_mapping(riga)
			print decript	
			
			
			
			
			
