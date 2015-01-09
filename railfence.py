#!/bin/env python


def enc(seed, inputString):
	listoflines = list()
	outputList = list()
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
			outputList.append(c)

	print ''.join(outputList)


def dec(seed, inputString):
#================================
#		create main lists
	outputList = list()
	listoflines = list()
	listofindexes = list()
	for i in range(seed):
		listoflines.append(list())
		listofindexes.append(0)


#==================================
#		set up blank cypher
	index = 0
	direction = 0 #direction. 0= down 1= up
	
	for letter in inputString:

		(listoflines[index]).append(0)

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
	
#====================================
#		populate blank cypher
	index=0
	lineindex=0
	for line in listoflines:
		lineindex=0
		for c in line:
			line[lineindex]=inputString[index]
			lineindex+=1
			index+=1
			
	#DEBUG print listoflines

#=======================================================================
#		iterate trough populated cypher and output to outputList
	index = 0
	direction = 0 #direction. 0= down 1= up
	
	for letter in inputString:

		outputList.append((listoflines[index])[listofindexes[index]])
		
		listofindexes[index]+=1

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
	print ''.join(outputList)



