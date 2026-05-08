# -*- coding: utf-8 -*-
"""
Makes "make_numbered_table.txt" into an HTML table with the first column a set of increasing numbers.
"""

invisible = False
prepend_numbers = True # Non-invisible tables only
add_roll_button = True # Non-invisible tables only
label = "critic_appearance" # Label for <span> tag for roll button result



file = open("make_numbered_table.txt", "r")

text = [line.strip().replace('"', '\\\"').split(" /// ") for line in file]

columns = len(text[0])

file.close()



file = open("make_numbered_table.txt", "w")



if invisible: 
    file.write("<table class=\"invisible\">\n")
    
    for line in text:
        file.write("\t<tr>\n")
        
        for i in range(columns):
            file.write("\t\t<td class=\"invisible\">" + line[i] + "</td>\n")
        file.write("\t</tr>\n")
    
    
    
else:
    file.write("<table>\n")
    
    if add_roll_button:
        file.write("\t<tr>\n")
        
        # Add blank cells to the left, assumes only the rightmost cell has the roll button.
        if prepend_numbers:
            padding_columns = columns
        else:
            padding_columns = columns - 1
        
        for i in range(padding_columns):
            file.write("\t\t<td></td>\n")
            
        roll_table = ", ".join(['"' + line[-1] + '"' for line in text])
        
        file.write("\t\t<td><button type=\"button\" onclick='fill_from_table(\"" + label + "\", [" + roll_table + "])'>Roll</button> <span id=\"" + label + "\"></span></td>\n")
        
        
        
    n = 1

    for line in text:
        file.write("\t<tr>\n")
        
        if prepend_numbers:
            file.write("\t\t<td>" + str(n) + "</td>\n")
            
        for i in range(columns):
            file.write("\t\t<td>" + line[i] + "</td>\n")
        file.write("\t</tr>\n")
        
        n += 1
        


file.write("</table>")
        
file.close()