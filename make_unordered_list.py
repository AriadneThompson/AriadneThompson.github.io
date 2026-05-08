# -*- coding: utf-8 -*-
"""
Makes "make_unordered_list.txt" into an HTML unordered list.
"""

file = open("make_unordered_list.txt", "r")

text = [line.strip() for line in file]

file.close()



file = open("make_unordered_list.txt", "w")

file.write("<ul>\n")

for line in text:
    file.write("\t<li>" + line + "</li>\n")
        
file.write("</ul>")
        
file.close()