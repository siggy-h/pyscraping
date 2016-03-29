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

import argparse
import sys
import lxml.html
from lxml import etree
from lxml.html.clean import Cleaner


def options_parser(argv):

    '''
    Function to gather and parse cli options.
    '''

    p = argparse.ArgumentParser(description='HTML Sanitizer.',
                                prog='pyclean')

    p.add_argument('inputfile', type=argparse.FileType('r'),
                   metavar='file', help='HTML input file to be cleansed.')

    p.add_argument('-o', '--output_file', type=str,
                   help='File to write output to.', required=False)

    p.add_argument('-t','--tags', nargs='+', dest='tags', 
                   help='Tags to clean', required=True)

    p.add_argument('-v', '--version', action='version',
                   version='%(prog)s 0.0.1')

    return p.parse_known_args()




def main(): 

    opts, leftovers = options_parser(sys.argv[1:])

    tree = etree.parse(opts.inputfile)
    file_to_clean = etree.tostring(tree)

    result = clean_more_crud(file_to_clean, opts.tags, True) 

    # Cleaner way to write to files in python
    if opts.output_file:
        with open(opts.output_file, 'w') as f:
            f.write(result)


def clean_more_crud(file_to_clean, rm_tags, show_results = False):

    '''returns result
 
    This function cleans up extra attributes in file
    if 3rd arg is true, it will print the input string 
    before and after cleaning

    
    :param file_to_clean: name of file to clean
    :param rm_tags: tags to be removed
    :param show_results: show the results
    :type to_clean: str
    :type rm_tags: list
    :type show_results: bool
    :returns: result
    :rtype: string
    '''

    html = lxml.html.fromstring(file_to_clean)
	
    if show_results:
        result = lxml.html.tostring(html)
        print_result("BEFORE", result)

    # .xpath below gives us a list of all elements that have a class attribute
    # // = select all tags matching expression
    #  * = match any tag,  [@class] = match all class attributes

    # Go through the list and remove 
    for a in rm_tags:      
        for tag in html.xpath('//*[@' + a + ']'):
            tag.attrib.pop(a)

    result = lxml.html.tostring(html) 

    if show_results:
        print_result("AFTER", result)

    return result

	
def print_result(label, to_print):

    '''
    If 3rd arg is true, this will print 
    the input string before and after cleaning
    '''
    print("\n*****   " + label +"   *****\n")
    print(to_print)



if __name__ == "__main__":
	main()

