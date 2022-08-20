import json
from nis import cat
from random import randrange
categories = "life, love, truth"
qcategories = categories.split(",")
count = 1
new_q_list = []
new_final_dict = {}

with open('q_new_v2.json') as f:
    d = json.load(f)
    cat_length = len(qcategories)
    rand_cat = randrange(cat_length)
    print("Rand_category is:", qcategories[rand_cat])

    no_of_quotes = len(d['quotes'][qcategories[rand_cat]])
    print("No.of quotes", no_of_quotes)

    rand_q_idx = randrange(no_of_quotes)
    print("Rand quote idx", rand_q_idx)

    print(d['quotes'][qcategories[rand_cat]][rand_q_idx]['Quote'])
    print(d['quotes'][qcategories[rand_cat]][rand_q_idx]['Author'])

    # for category in qcategories:
    #     print(len(d['quotes'][category]))

#     for item in d["new_quotes"]:
#         new_q_list = []
#         category = item["Category"]
#         # print(category)
#         item.pop("Category", None)
#         # print(item)
#         if category not in new_final_dict:
#             new_q_list.append(item)
#             new_final_dict[category] = new_q_list
#             # print(new_final_dict)
#         else:
#             new_q_list = new_final_dict[category]
#             new_q_list.append(item)
#             new_final_dict[category] = new_q_list

#         # count += 1
#         # if count > 5:
#         #     break
#     new_quotes = {}
#     new_quotes['quotes'] = new_final_dict

# with open('q_new_v2.json', 'w') as f:
#     f.write(json.dumps(new_quotes))
    # json.dump({"new_quotes": new_q_list}, f, ensure_ascii=False)
    # for key, value in d.items():
    #     value.pop('id', None)
