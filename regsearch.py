#! python3
# regsearch.py - this script search for the search parameter or regular expression specified on the command line
#				in all the .txt file in the specified directory.
# Usage: py.exe regsearch.py  <directoty > <search parameter or a regular expression>
import re,os,sys

#using command line arguement  to perform the whole task
#checking if the command line argument are passed
if len(sys.argv) == 3:
	try:

		directory  = sys.argv[1]			# getting ther directory specified....
		search_parameter = sys.argv[2]		# geting thje search parameters......

		current_directory = os.chdir(directory)
		directory_list = os.listdir(current_directory)
		file_lists = []

		#check for the with .txt extension store in an array
		fileRegEx = re.compile(r'(\.txt)$')
		for file in directory_list:
			result = fileRegEx.search(file)
			if result != None:
				file_lists.append(file)
				
		if len(file_lists) !=  0:
			searchRegEx = re.compile(r''+search_parameter)
			for file in file_lists:
				file_record = open(file,"r")
				result = SearchRegEx.search(file_record.read())
				if result != None:
					print(result.group())
					print("found in %s" %file)
				else:
					print("not found in %s" %file)
		else:
			print("there is no .txt file in this Directory")
	#raise an exception if the directory is not found 
	except FileNotFoundError:
		print("The Directory specified does not Exist")



	#the for each file search for the specific regular expression