# -*- coding: utf-8 -*-
def words(s):
	"""Returns the count of each word in a given sentence"""

	s2 = s.split() #split the sentence into individual words
	print s2 #print the individual words
	readw ={} #declare an enpty dictionary to store read words
	readw[s2[0]] = 1 #read the first word
	for j in range(1,len(s2)):
		if s2[j].isdigit(): #if word is a digit
			key = int(s2[j]) #convert it to int and assign it to variable key
		elif not s2[j].isdigit(): #
			key = s2[j] #else assign it to variable key
		if readw.has_key(key): #if the word has  been read previously
		    readw[key]+= 1 #increment it's count by one
		elif not readw.has_key(key): # else
			readw[key] = 1 #read it 


	return readw #return dictionary of read words and their counts

print words("testing 1 2 testin")
