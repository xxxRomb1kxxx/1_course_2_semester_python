string = "money money money"
def acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym
print(string, acronym(string))