import MeCab as mecab
import pickle as pk
#ファイル読み込み
temp = open("neko.txt")
neko_txt = temp.read()
temp.close()
sentences = neko_txt.split("\n")
# print(sentences[:10])

#形態素解析
#<出力フォーマット>
#表層形\t品詞,品詞細分類1,品詞細分類2,活用形,原形,読み,意味情報
#辞書: juman-utf8 mecab-ipadic-neologd ipadic ipadic-utf8 debian
tag = mecab.Tagger("-d /var/lib/mecab/dic/juman-utf8")
parsed_sentences = []

#EOS\n と　\t を取り除き、一文を一つの要素としたリストを生成
for n in sentences:
    temp = tag.parse(n).replace("EOS\n","")
    temp2 = temp.replace("\t",",")
    parsed_sentences.append( temp2.split("\n")[:-1] ) #[:-1]はsplitによって入ってしまう空文字を除去している


for index, n in enumerate(parsed_sentences):
    for index2, i in enumerate(n):
        temp = i.split(",")
        temp2 = {"surface": temp[0],"base": temp[5],"pos": temp[1],"pos1": temp[2]}
        parsed_sentences[index][index2] = temp2
    #[]を消したいときは以下の処理はしちゃだめ
    #例えば5番目の要素をpopで吹き飛ばしたときに,for は５回目だが 要素の処理が6番目に変わってしまう   
    # if n == []:
    #     parsed_sentences.pop(index)
    
parsed_sentences = [n for n in parsed_sentences if n != []] 

with open ("parsed_neko.pkl","wb") as f:
    pk.dump(parsed_sentences,f)

