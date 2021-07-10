import pickle

#別ファイルに保存した、解析済みのデータを読み込む
with open("parsed_neko.pkl","rb") as f:
    parsed_neko = pickle.load(f)

sequence_noun = []
for index, n in enumerate(parsed_neko):
    for index2, i in enumerate(n):
        if i["pos"] == "名詞" and n[index2-1]["surface"] == "の": #名詞の前に"の"がある場合は、"の"の前は必ず名詞
            #名詞と"の"とその前の要素(名詞であると仮定)を連結しリストに加える
            sequence_noun.append( n[index2-2]["surface"] + n[index2-1]["surface"] + i["surface"])


print(sequence_noun[:100])