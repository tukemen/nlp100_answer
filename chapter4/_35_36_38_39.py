import pickle
import collections
import re
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "MS Gothic"
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

#35
word_count = collections.Counter(words)
word_count_sorted = word_count.most_common()

#下の処理は時間かかりすぎ
# word_count = {}
# for n in word_list:
#     word_count[n] = words.count(n)

#36
# x = []
# y = []

# for n in word_count_sorted[:10]:
#     x.append(n[0])
#     y.append(n[1])

# plt.bar(x,y)
# plt.show()

#38
word_nums = list(word_count.values())
# print(max(word_nums))
# max_value = max(word_nums)
# plt.hist(word_nums,range = (0,max_value), bins = len(set(word_nums)))
# plt.show()

#39
word_nums_sorted = sorted(set(word_nums),reverse = True)
m = word_nums_sorted
n = list(range(1,len(m)+1))

ax = plt.gca()
ax.set_yscale("log")
ax.set_xscale("log")

plt.plot(m,n)
plt.show()
    
