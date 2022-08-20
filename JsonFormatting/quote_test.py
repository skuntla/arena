import json
from nis import cat
count = 1
new_q_list = []
with open('quotes.json') as f:
    d = json.load(f)
    category_list = []
    for item in d["quotes_list"]:

        item.pop("Tags", None)
        if item["Category"] not in category_list:
            category_list.append(item["Category"])
        print(item)
        new_q_list.append(item)
    print(category_list)

with open('q_new.json', 'w') as f:
    json.dump({"new_quotes": new_q_list}, f, ensure_ascii=False)
    # for key, value in d.items():
    #     value.pop('id', None)
