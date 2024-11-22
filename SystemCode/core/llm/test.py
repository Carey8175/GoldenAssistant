"""
测试大模型恢复效果
测试结果：
大模型测试效果很不好基本可以抛弃
"""
from openai import OpenAI
import json


heroes_data = json.load(open('../../statics/basic_info/heroes_convert.json', 'r'))
heroes_data = json.dumps(heroes_data)
traits_data = json.load(open('../../statics/basic_info/trait_convert.json', 'r'))
traits_data = json.dumps(traits_data)


chat_client = OpenAI(
    api_key="sk-goX9KyBKx94WEu7XgsH4MFrAULepB5JQ236G6Cxj9n4ErFxK",
    base_url="https://api.chatanywhere.org"
)

state = {
    "level": 3,
    "gold": 5,
    "heroes": [
        {"name": "沃里克", "level": 1, "position": [1, 5]},
        {"name": "图奇", "level": 1, "position": [4, 2]},
        {"name": "莉莉娅", "level": 1, "position": ["备战席", 1]},
        {"name": "莉莉娅", "level": 1, "position": ["备战席", 2]},
        {"name": "图奇", "level": 1, "position": ["备战席", 3]},
    ],
    "life": 100,
    "stage": "2-1",
    "heroes_in_shop": ["莉莉娅", "沃里克", "图奇", "莉莉娅", "图奇"],
    "XP": 2
}

messages = [
    {"role": "system", "content": """你将用于给出《金铲铲之战》的操作策略，所有操作请严格按以下格式回复：不操作：["stay"];购买等级：["level": i] （i 为购买等级的次数）;购买商店中的一个或多个英雄：["buy": [x, y, z]] （x, y, z 为要购买的第 i 个英雄，如购买第1和第2个英雄则为 [1, 2]）;重新布阵：["change": [[old_position1, new_position1], [old_position2, new_position2]]] （备战席与棋盘可容纳英雄，格式为旧位置与新位置的配对）;出售英雄：["sell": [position1, position2]]"""},
    {"role": "user", "content": f"{json.dumps(state)}; 请根据上述信息，给出你的操作策略。"}
]

chat_resp = chat_client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",
    messages=messages
)

resp = chat_resp.choices[0].message.content
print(resp)
