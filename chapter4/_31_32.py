import pickle

#別ファイルに保存した、解析済みのデータを読み込む
with open("parsed_neko.pkl","rb") as f:
    parsed_neko = pickle.load(f)

base_verbs = []
sarface_verbs = []
for index, n in enumerate(parsed_neko):
    for index2, i in enumerate(n):
        if i["pos"] == "名詞":
            sarface_verbs.append(parsed_neko[index][index2]["surface"])
            base_verbs.append(parsed_neko[index][index2]["base"])
    

print(base_verbs[100:200])
# print(parsed_neko[:10])
