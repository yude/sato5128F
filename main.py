import MeCab
import re
i = 0
# 元の文章
data = "お家に、着いた。今から、愛美ちゃんと、通話をしながら、ゲームキューブで、スターフォックス、アサルトを、プレイする。"

# 元の文章を表示する
print("変換対象の文章 (整形前): \n" + data)
# 余分な記号などを文章から削除する
print("変換対象の文章 (整形済み): \n" + re.sub('[,.。、 ]', '', data) + "\n")
data = re.sub('[,.。、 ]', '', data)
# MeCab
tagger = MeCab.Tagger("-F '%m %h ' -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd --eos-format=''")
str_output = tagger.parse(data)

# MeCab の結果をプレビュー
print("素のデータ: ")
print(str_output + "\n")

print("配列化: ")
list_output = str_output.split(' ')
# MeCab の結果を配列に入れる (単語分)
print("単語: ")
list_output_words = list_output[::2]
print(list_output_words)
list_output_words.pop(-1)
# MeCab の結果を配列に入れる (品詞分)
print("品詞: ")
list_output_words_part = list_output[1::2]
print(list_output_words_part)
print("\n結果: ")

# 結果を出力する
for item in list_output_words:
    print(item, end='')
    if list_output_words_part[i] == "25":
            print("。", end='')
    if i != 0:
        if list_output_words_part[i - 1] == "38":
            print("、", end='')
    i+=1
print("\n")