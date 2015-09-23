#!/usr/bin/python

import sys

def readfile(argument,filename):
	f = open(filename,'rU')
	text = f.readline()
	print text
	word = text.split()
	dict ={}
	for s in word:
		if s in dict:
			dict[s] +=  1
		else:
			dict[s] = 1
	#print dict
	counter = 0
	if argument == '--count':
		for w in dict:
			print w, dict[w]
	elif argument == '--topcount':
		for k in sorted(dict,key=dict.get,reverse=True):
			if counter < 3:
				print k, dict[k]
				counter = counter + 1
	f.close()
	
def main():
	readfile(sys.argv[1],sys.argv[2])	

if __name__ == '__main__':
  main() 