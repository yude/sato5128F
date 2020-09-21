import MeCab
import re
# 元の文章
data = "お家に、着いた。今から、愛美ちゃんと、通話をしながら、ゲームキューブで、スターフォックス、アサルトを、プレイする。"


print("変換後の文章: \n" + re.sub('[,.。、 ]', '', data))
print("\n構文解析: \n")
mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd').parse(re.sub('[,.。、 ]', '', data))
lines = mecab.split('\n')
items = (re.split('[\t]',line) for line in lines)
for item in items:
    print(item)