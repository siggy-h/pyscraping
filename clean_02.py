#!/usr/bin/python
# Copyright (c) Siggy Hinds
# "clean_02.py"
# This program opens an external html file. Removes the specified attributes from css tags.
# Cleaned up html is then saved into a new file.
#
# I referenced this stackoverflow question for help eliminating the "class" attribute
# http://stackoverflow.com/questions/10037289/remove-class-attribute-from-html-using-python-and-lxml

# Some notes along the way
# All indentation must be 4 spaces.
# A 4 space indentation indicates a block level indent

import sys
import lxml.html
from lxml import etree
from lxml.html.clean import Cleaner

def main(): 

    # Lets grab this from the input
    # file_name = "test00.html"  # original html file
    input_file = sys.argv[1]
    cleaned_file = "foo.html"  # file for cleaned up html

    # The attributes I want to remove are specific to the file I am working on...

    # Notice my variable naming convention changes
    rm_tags = ['class', 'style', 'cellspacing', 'data-mc-pattern']

    tree = etree.parse(input_file)
    to_clean = etree.tostring(tree)

    # TODO: Use cleaner to clean extra stuff... 
    #clean = Cleaner(page_structure = False, links = False, style = True)

    # Call clean function and get the result. 
    # Takes etree, list [, True].  Use True as 3rd arg if you want to print a before and after
    result = clean_more_crud(to_clean, rm_tags, True) 

    # Save results to file
    #new_file = open(cleaned_file, 'w')
    #new_file.write(result)
    #new_file.close()

    # Cleaner way to write to files in python
    with open(cleaned_file, 'w') as f:
        f.write(result)


def clean_more_crud(to_clean, rm_tags, show_results = False):

    '''
    This function cleans up extra attributes in file
    if 3rd arg is true, it will print the input string 
    before and after cleaning
    '''

    html = lxml.html.fromstring(to_clean)	# Parse the html
	
    if show_results:
        result = lxml.html.tostring(html)
        print_result("BEFORE", result)

    # .xpath below gives us a list of all elements that have a class attribute
    # // = select all tags matching expression
    #  * = match any tag,  [@class] = match all class attributes

    for a in rm_tags: # Go through the list and remove 
        for tag in html.xpath('//*[@' + a + ']'):
            tag.attrib.pop(a)

    result = lxml.html.tostring(html) 

    if show_results:
        print_result("AFTER", result)
    
    return result

	
def print_result(label, toPrint):

    '''
    If 3rd arg is true, this will print 
    the input string before and after cleaning
    '''
    print("\n*****   " + label +"   *****\n")
    print(toPrint)



if __name__ == "__main__":
	main()

