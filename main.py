import MeCab
import re
# 元の文章
data = "お家に、着いた。今から、愛美ちゃんと、通話をしながら、ゲームキューブで、スターフォックス、アサルトを、プレイする。"


print("変換対象の文章: \n" + re.sub('[,.。、 ]', '', data))

str_output = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd').parse(re.sub('[,.。、 ]', '', data))
mecab_formatted = str_output.replace("\nEOS", "")
print("\n構文解析: ")
print(mecab_formatted)