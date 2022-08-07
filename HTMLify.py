# -*- coding: utf-8 -*-

"""
For every page in pages, writes an HTML file with the header at the top and 
footer at the bottom. 
"""



FILENAME = 0
TITLE = 1
RETURNTO = 2
RETURNTEXT = 3
MATHJAX = 4



pages = ({FILENAME: "index", TITLE: "Ariadne's Website", RETURNTO: None, RETURNTEXT: None, MATHJAX: False},
         {FILENAME: "Writing", TITLE: "Ariadne's Writing", RETURNTO: "index", RETURNTEXT: "Return to Main Page", MATHJAX: False},
         {FILENAME: "Contact_Me", TITLE: "Contact Me", RETURNTO: "index", RETURNTEXT: "Return to Main Page", MATHJAX: False},
         {FILENAME: "A_Mountain_Inverted", TITLE: "A Mountain, Inverted", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "Practical_Applications_of_Fluid_Dynamics", TITLE: "Practical Applications of Fluid Dynamics", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "Question_One", TITLE: "Question One", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: True},
         {FILENAME: "Question_One_Screen_Reader_Friendly", TITLE: "Question One", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "Wretched_Creatures", TITLE: "Wretched Creatures", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "The_Human_Nature", TITLE: "The Human Nature", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "Fifty_Princesses", TITLE: "Fifty Princesses", RETURNTO: "Writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         )
          
          
    
    



for page in pages:
    html = open(page[FILENAME] + ".html", "w")
    
    
    
    # Header
    html.write("<!DOCTYPE html>\n\n")
    html.write("<html lang=\"en-UK\">\n\n")
    html.write("<head>\n\n")
    
    html.write("\t<title>" + page[TITLE] + "</title>\n\n")
    html.write("\t<meta charset=\"UTF-8\">\n\n")
    html.write("\t<link rel=\"shortcut icon\" href=\"Favicon.svg\">\n")
    html.write("\t<link rel=\"stylesheet\" type=\"text/css\" href=\"Dark.css\" title=\"Dark\">\n")
    html.write("\t<link rel=\"alternate stylesheet\" type=\"text/css\" href=\"Light.css\" title=\"Light\">\n\n")
    
    if page[MATHJAX]:
        html.write("\t<script src=\"https://polyfill.io/v3/polyfill.min.js?features=es6\"></script>\n")
        html.write("\t<script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\"></script>\n\n")
    
    html.write("</head>\n\n\n\n")
    html.write("<body>\n\n")
    
    
    
    txt = open("_" + page[FILENAME] + ".txt", "r")
    
    
        
    for line in txt: 
        html.write("\t" + line)
            
    txt.close()
        
    
    
    # Footer
    if page[RETURNTO] is not None:
        html.write("\n\n\t<div>\n\n")
        html.write("\t<h3><a href=\"" + page[RETURNTO] + ".html\">" + page[RETURNTEXT] + "</a></h3>\n\n")
        html.write("\t</div>")
    
    
    
    html.write("\n\n</body>\n\n")
    html.write("</html>")
    
    html.close()





































