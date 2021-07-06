import re
docs = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Mght Also Sign Peace Security Clause. Arthur King Can."
word_list = re.split('[^\w]+',docs)
pe_table = {}
one_cap = {0,4,5,6,7,8,14,15,18}
for i, v in enumerate(word_list):
    if i in one_cap:
        pe_table[i+1] = v[0]
    elif v !="":
        pe_table[i+1] = v[:2]
        
print(word_list)
print(pe_table)