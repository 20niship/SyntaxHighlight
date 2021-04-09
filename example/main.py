# coding: utf-8
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
 
from src import convert

print("################### example 1 ######################")

input_fname = "example.cpp"
output_fname = "output.html"
template_html_fname ="template.html"
inline_css = False

cc = convert.SyntaxHilighter(input_fname, output_fname, template_html_fname, inline_css_=inline_css)
cc.run()


print("\n\n################### example 1 ######################")
output_fname = "output_simple.html"
template_html_fname ="template_simple.html"
inline_css = True
cc = convert.SyntaxHilighter(input_fname, output_fname, template_html_fname, inline_css_=inline_css)
cc.run()
