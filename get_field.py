def get_field (field, text):
    if(field == "form"):

        type1 = "Form"
        type2 = "FORM"
        type3 = "form"

    if(field == "function"):

        type1 = "Function"
        type2 = "FUNCTION"
        type3 = "function"

    if(field == "content"):

        type1 = "Content"
        type2 = "CONTENT"
        type3 = "content"

    if(field == "context"):

        type1 = "Context"
        type2 = "CONTEXT"
        type3 = "context"

    #Get raw text
    try:
        raw = text.split(type1, 1)[1]
    except:
        try:
            raw = text.split(type2, 1)[1]
        except:
            raw = text.split(type3, 1)[1]
    #Parse 
    term_list = raw.split("|")
    field_output = []
    for s in term_list:
        if(len(field_output) == 3):
            break
        if(len(s) > 10):
            field_output.append(s)
    #Three terms for output
    return field_output