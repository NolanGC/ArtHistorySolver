import requests
import re
from bs4 import BeautifulSoup
from get_field import get_field as get

infile = open("links.text", "r")
links = infile.read().split("|")
infile.close()
f = open("out.txt", "w", encoding="utf-8")
for link in links:
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')
    print("Solving for " + link)
    #large string, raw text of page
    text = soup.get_text("|")
    
    #Write form to out
    form = get("form", text)
    for i in range(3):
        f.write(form[i] + "\n")
    f.write("\n\n")
    #Write function to out
    function = get("function", text)
    for i in range(3):
        f.write(function[i] + "\n")
    f.write("\n\n")
    #Write content to out
    content = get("content", text)
    for i in range(3):
        f.write(content[i] + "\n")
    f.write("\n\n")
    #Write context to out
    context = get("context", text)
    for i in range(3):
        f.write(context[i] + "\n")
    f.write("\n\n\n\n\n\n")

