import pickle
import collections
import re
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "MS Gothic"
#別ファイルに保存した、解析済みのデータを読み込む
with open("parsed_neko.pkl","rb") as f:
    parsed_neko = pickle.load(f)

judge = re.compile("[「」？、。！（）]+")
words = []
sentences_with_neko = []

#猫を含んだ分を洗い出す
for n in parsed_neko:
    for i in n:
        if i["surface"] == "猫":
            sentences_with_neko.append(n)
            break

for n in sentences_with_neko:
    for i in n:
        if not judge.search(i["surface"]) and i["surface"] != "猫":
            words.append( i["surface"] )

word_count  = collections.Counter(words)
word_count_sorted = word_count.most_common() 

x = []
y = []

for n in word_count_sorted[:10]:
    x.append(n[0])
    y.append(n[1])

plt.bar(x,y)
plt.show()
