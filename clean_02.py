# "clean_02.py"
# Copyright (c) Siggy Hinds
# This program opens an external html file. Removes the specified attributes from css tags.
# Cleaned up html is then saved into a new file.
#
# I referenced this stackoverflow question for help eliminating the "class" attribute
# http://stackoverflow.com/questions/10037289/remove-class-attribute-from-html-using-python-and-lxml

import lxml.html
from lxml import etree
from lxml.html.clean import Cleaner

def main(): 
	file_name 		= "test00.html"		# original html file
	cleaned_file 	= "foo.html"			# file for cleaned up html
	
	# The attributes I want to remove are specific to the file I am working on...
	rmFromTags = ['class', 'style', 'cellspacing', 'data-mc-pattern']

	tree = etree.parse(file_name)
	to_clean = etree.tostring(tree)

	# todo- Use cleaner to clean extra stuff... 
	#clean = Cleaner(page_structure = False, links = False, style = True)

	# Call clean function and get the result. 
	# Takes etree, list [, True].  Use True as 3rd arg if you want to print a before and after
	result = clean_more_crud(to_clean, rmFromTags, True) 
	
	# Save results to file
	new_file = open(cleaned_file, 'w')
	new_file.write(result)
	new_file.close()


# This function cleans up extra attributes in file 
# if 3rd arg is true, it will print the input string before and after cleaning
def clean_more_crud(to_clean, rmFromTags, show_results = False):  #takes

	html = lxml.html.fromstring(to_clean)	# Parse the html
	
	if show_results:
		result = lxml.html.tostring(html)
		print_result("BEFORE", result)

	# .xpath below gives us a list of all elements that have a class attribute
	# // = select all tags matching expression
	#  * = match any tag,  [@class] = match all class attributes
	for a in rmFromTags: # Go through the list and remove 
		for tag in html.xpath('//*[@' + a + ']'):
			tag.attrib.pop(a)

	result = lxml.html.tostring(html) 

	if show_results:
		print_result("AFTER", result)

	return result

	
# This prints a label and string
def print_result(label, toPrint):
	print("\n*****   " + label +"   *****\n")
	print(toPrint)



if __name__ == "__main__":
	main()

