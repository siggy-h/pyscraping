#!/usr/bin/python
# Copyright (c) Siggy Hinds
# This program will extract unneeded elements
# from html.
from lxml import html # AHHH
import requests
from datetime import datetime # We will use this later



def main():
    page = requests.get('http://www.darkhorse.com')
    #with open("darkhorse_com_html.html", 'w') as f:
    #     f.write(page.content)
    #print("Done extracting html")

    # Use <object>.__dict__ as a built in that turns
    # a object into a dict
    # I use this as a simple way to debug objects
    #print(page.__dict__)
    print(page.__dict__.keys())
    # now that we know what the keys of the dict
    # are, aka the object attributes
    # We can index into the dict to grab content
    print(page.__dict__['_content'])






# Python formalism
if __name__ == "__main__":
    main()
