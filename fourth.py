#!/usr/bin/python2.7.5 -tt

import commands


print "My First Python Program : Dictionary"
print " "
print "--" * 50

def main():

#	fp=open("temp.txt","r")
#	for i in fp:
#		print i
#	fp.close

	str = raw_input("Enter your input : ")
	
        cmd = 'cat DictionaryE.txt | grep -w "' + str + '"' + " | wc -l"
#	print cmd	
	output = commands.getoutput(cmd)
#	print output	
	if ( output == "1"):
		print "Word is correct"
	else:
		print "Incorrect Word"

	print "--" * 50

if __name__ == '__main__':
	main()
