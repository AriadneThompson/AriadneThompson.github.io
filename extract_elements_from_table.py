# -*- coding: utf-8 -*-
"""
Takes the elements out of a numbered table by extracting every fourth line and 
removing the <td> tags, then puts them in a nice list for rolling on. 
"""

file = open("extract_elements_from_table.txt", "r")

elements = [line.strip()[4:-5].replace('"', '\\"') for line in file][3::4]

file.close()



print("[\"" + "\", \"".join(elements) + "\"]")