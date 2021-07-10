import pickle

#別ファイルに保存した、解析済みのデータを読み込む
with open("parsed_neko.pkl","rb") as f:
    parsed_neko = pickle.load(f)
flag = False

sequence_noun = []

for index, n in enumerate(parsed_neko):
    for index2, i in enumerate(n):
        if n[index2]["pos"] == "名詞" and flag == False:
            flag = True
            num = index2
            length = len(n) - 1
            temp = ""
            while(num <= length and n[num]["pos"] =="名詞"):
               
                temp += n[num]["surface"]
                num +=1
            sequence_noun.append(temp)

        elif n[index2]["pos"] != "名詞" and flag == True:
            flag = False
        else: 
            continue
            
           
print(sequence_noun[0:100])



