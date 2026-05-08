# -*- coding: utf-8 -*-
"""
Adds <p> and </p> onto any non-empty line in "add_p_tags.txt".
"""

file = open("add_p_tags.txt", "r")

text = [line.strip() for line in file]

file.close()



file = open("add_p_tags.txt", "w")

for line in text:
    if line: 
        file.write("<p>" + line + "</p>\n")
    
    else:
        file.write("\n")
        
file.close()