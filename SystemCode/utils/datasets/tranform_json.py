"""
此工具用于将官方爬取的json数据转换为更容易理解的数据
"""
import json

data_path = "../../statics/basic_info/trait.json"
save_path = "../../statics/basic_info/trait_convert.json"
data = json.load(open(data_path, 'r'))
data = data['data']

heroes = {}
for key in data.keys():
    heroes[data[key]['name']] = data[key]

# 解决保存中文乱码问题
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(heroes, f, ensure_ascii=False, indent=4)
