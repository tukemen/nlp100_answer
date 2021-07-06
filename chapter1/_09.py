import random
def typoglycemia(words):
    words = words.split()
    #print(words)
    for i, word in enumerate(words):
        if len(word) > 4:
            temp1 = list(word)
            temp2 = list(word[1:-1])
            random.shuffle(temp2)
            
            temp1[1:-1] = temp2 
            temp1 = "".join(temp1)
            words[i] = temp1
    words = " ".join(words)
    return words
           

words = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(typoglycemia(words))