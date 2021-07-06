import re
def n_gram(sequence,n,gram_type):
    set_of_ngram = []
    if type(sequence)==str:
        sequence = re.split('[^\w]+',sequence)
        #print(sequence)
    if gram_type == "word" and n > len(sequence):
        print("nがシーケンスの要素数を超えています")
        return []
    elif gram_type == "char":
        sequence = ''.join(sequence)
        if n > len(sequence):
            print("nがシーケンスの要素数を超えています")
            return []    
    for i in range(len(sequence)):
                set_of_ngram.append(sequence[i:i+n])
                if i + (n-1)==len(sequence)-1:
                    break
    return set_of_ngram

# sequence = "I am an NLPer"
# list_ngram = n_gram(sequence,2,True)
# print(list_ngram)