import pickle
import collections
import re
import matplotlib.pyplot as plt

#別ファイルに保存した、解析済みのデータを読み込む
with open("parsed_neko.pkl","rb") as f:
    parsed_neko = pickle.load(f)

# print(parsed_neko[:10])
judge = re.compile("[「」？、。！（）]+")
words = []
for n in parsed_neko:
    for i in n:
        if not judge.search(i["surface"]):
            words.append( i["surface"] )

word_count = collections.Counter(words)
word_count_sorted = word_count.most_common()

#下の処理は時間かかりすぎ
# word_count = {}
# for n in word_list:
#     word_count[n] = words.count(n)

# print(word_count_sorted[:100])
x = []
y = []

for n in word_count_sorted[:10]:
    x.append(n[0])
    y.append(n[1])

plt.plot(x,y)
plt.show()

    
