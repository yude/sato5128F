import MeCab
import re

# 変換する日本語の文章を指定する。
text = "昨日、愛美ちゃんと電話で、もう少しコロナウイルスが、落ち着いたら、伊豆に旅行に行こうと、いう話になった。サフィール踊り子号で、行く予定だ。"

# 句読点を削除する。
print("変換対象の文章 (整形済み): \n" + re.sub('[,.。、 ]', '', text) + "\n")
text = re.sub('[,.。、 ]', '', text)

# MeCab で文章をパースする。配列には 「品詞で区切った単語」 -> 「品詞を識別するための ID」で格納される。
tagger = MeCab.Tagger("-F%m,%h, -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd --eos-format=")
mecab_output = tagger.parse(text)
mecab_output = mecab_output[:-1] # 最後の _ を削除する。

# [Debug] str_output の内容を出力する
print("mecab_output: \n", mecab_output)

# str_output に格納されている単語と品詞 ID をそれぞれの配列に分割する。
## まず、str_output を , ごとに区切り、配列に変換する。
## ここで、偶数の要素は単語、奇数の要素は品詞 ID となる。
mecab_split = mecab_output.split(",")
# print(mecab_split)

## 単語 -> words
## 品詞 -> id
words = mecab_split[0::2]
id = mecab_split[1::2]

# [Debug] 配列 words, id の内容を出力する。
print("words: \n", words)
print("id: \n", id)

# 結果を出力する

i = 0

for item in words:
    print(item, end='')
    if (id[i - 1] == "25") and id[i] == "67":
            print("、", end='')
    if i > 0:
        if id[i - 1] == "38" and id[i - 1] == "41":
            print("、", end='')
        if id[i] == "31" and id[i - 1] == "41":
            print("。", end='')
        if id[i] == "13" and id[i - 1] == "38":
            print("、", end='')
        if id[i] == "13" and id[i - 1] == "67":
            print("、", end='')
        if id[i] == "13" and id[i - 1] == "41":
            print("、", end='')

    if i > 1:
        if id[i] == "13" and id[i - 2] == "44":
            if id[i + 1] != "36":
                print("、", end='')
        if id[i] == "13" and id[i - 1] == "36" and id[i - 2] == "13":
            print("、", end='')
        if id[i] == "18" and id[i - 1] == "31" and id[i - 2] == "13":
            print("、", end='')
        if id[i] == "31" and id[i - 1] == "36" and id[i - 2] == "25":
            print("。", end='')
        if id[i] == "25" and id[i - 1] == "31" and id[i + 1] != "15" and id[i + 2] != "13" and id[i + 1] != "41":
            print("、", end='')
        if id[i - 3] == "36" and id[i - 2] == "13" and id[i - 1] == "31" and id[i] == "25":
            print("。", end='')
        if id[i - 1] == "36" and id[i] == "25":
            print("。", end='')
    i+=1
print("\n")
