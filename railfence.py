#!/bin/env python


def enc(seed, inputString):
	listoflines = list()
	for i in range(seed):
		listoflines.append(list())
		
	index = 0
	direction = 0 #direction. 0= down 1= up

	for letter in inputString:
		(listoflines[index]).append(letter)		

		if index==0:
			direction=0
			index=1
			continue
		elif index==(seed-1):
			direction=1
			index=seed-2
			continue
		elif direction==0:
			index=index+1
			continue
		elif direction==1:
			index=index-1
			continue
		else:
			print fail
			quit()
	
	#the printout
	for line in listoflines:
		for c in line:
			print c,
#def dec:
	
