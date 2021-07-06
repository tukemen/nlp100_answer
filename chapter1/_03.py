import re
docs = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
doc_list = re.split("[^\w]+",docs)
word_length = [len(n) for n in doc_list if n!=""]
print(word_length)
