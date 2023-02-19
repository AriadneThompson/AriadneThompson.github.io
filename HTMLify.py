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
         {FILENAME: "writing", TITLE: "Ariadne's Writing", RETURNTO: "index", RETURNTEXT: "Return to Main Page", MATHJAX: False},
         {FILENAME: "contact_me", TITLE: "Contact Me", RETURNTO: "index", RETURNTEXT: "Return to Main Page", MATHJAX: False},
         {FILENAME: "a_mountain_inverted", TITLE: "A Mountain, Inverted", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "practical_applications_of_fluid_dynamics", TITLE: "Practical Applications of Fluid Dynamics", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "question_one", TITLE: "Question One", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: True},
         {FILENAME: "question_one_screen_reader_friendly", TITLE: "Question One", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "wretched_creatures", TITLE: "Wretched Creatures", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "the_human_nature", TITLE: "The Human Nature", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         {FILENAME: "fifty_princesses", TITLE: "Fifty Princesses", RETURNTO: "writing", RETURNTEXT: "Return to Writing", MATHJAX: False},
         )
          
          
    
    



for page in pages:
    html = open(page[FILENAME] + ".html", "w")
    
    
    
    # Header
    html.write("<!DOCTYPE html>\n\n")
    html.write("<html lang=\"en-UK\">\n\n")
    html.write("<head>\n\n")
    
    html.write("\t<title>" + page[TITLE] + "</title>\n\n")
    html.write("\t<meta charset=\"UTF-8\">\n\n")
    html.write("\t<link rel=\"shortcut icon\" href=\"favicon.svg\">\n")
    html.write("\t<link rel=\"stylesheet\" type=\"text/css\" href=\"dark.css\" title=\"Dark\">\n")
    html.write("\t<link rel=\"alternate stylesheet\" type=\"text/css\" href=\"light.css\" title=\"Light\">\n\n")
    html.write("\t<script type=\"text/javascript\" src=\"switch_css.js\"></script>\n\n")
    
    if page[MATHJAX]:
        html.write("\t<script src=\"https://polyfill.io/v3/polyfill.min.js?features=es6\"></script>\n")
        html.write("\t<script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\"></script>\n\n")
    
    html.write("</head>\n\n\n\n")
    html.write("<body onload=\"set_style_from_cookie()\">\n\n")
    
    
    
    txt = open("_" + page[FILENAME] + ".txt", "r")
    
    
        
    for line in txt: 
        html.write("\t" + line)
            
    txt.close()
        
    
    
    # Footer
    html.write("\n\n\t<div>\n\n")
    
    if page[RETURNTO] is not None:
        html.write("\t<h3><a href=\"" + page[RETURNTO] + ".html\">" + page[RETURNTEXT] + "</a></h3>\n\n")
    
    html.write("\t<ul class=\"centred\">\n\n")
    html.write("\t\t<li class=\"horizontal\"><a href=\"javascript:switch_style('Dark')\">Dark theme</a></li>\n")
    html.write("\t\t<li class=\"horizontal\"><a href=\"javascript:switch_style('Light')\">Light theme</a></li>\n\n")
    html.write("\t</ul>\n\n")
    
    html.write("\t</div>\n\n")
    
    
    
    html.write("</body>\n\n")
    html.write("</html>")
    
    html.close()





































