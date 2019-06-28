# ArtHistorySolver

Program that quickly compiles research on an art piece in 4 categories (Form, Function, Content, Context). 

```python
 if(field == "form"):
     type1 = "Form"
     type2 = "FORM"
     type3 = "form"
```

Different forms of the four field names improves flexibility. 

```python
text = soup.get_text("|")
```
Entire raw text of the page is grabbed using the get_text() method of a BeautifulSoup object (soup). "|" is a delimiter placed after every 

```python
try:
    raw = text.split(type1, 1)[1]
except:
    try:
        raw = text.split(type2, 1)[1]
    except:
         raw = text.split(type3, 1)[1]
term_list = raw.split("|")
```
Split entire raw text by one of the three different forms. The variable raw is assigned to all of the text after the keyword. Term list splits raw by the delimiter, getting a list of lines following the keyword.

```python
for s in term_list:
    if(len(field_output) == 3):
        break
    if(len(s) > 10):
        field_output.append(s)
```
Loop that takes the first three lines of term_list that are over 10 characters. (Character minimum protects against grabbing an odd character like a single colon or a couple words)

field_output is what is printed to out.txt
