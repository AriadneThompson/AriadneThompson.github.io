# -*- coding: utf-8 -*-

text_in = open("densen.txt", "r")

text = [line for line in text_in]

text_in.close()

text_out = open("densen.txt", "w")

for line in text:
    text_out.write("<p class=\"dense\">" + line.strip() + "</p>\n")
    
text_out.close()