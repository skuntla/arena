import json
from nis import cat
from profanity_filter import ProfanityFilter
# Had to create venv, upgrade pip, install numpy, then profanity filer
# spacy and en language download is also required for which run below:
# pip3 install spacy && python3 -m spacy download en


# qcategories = ['life','love','truth']

total_count = 0
valid_count = 0
non_eng_count = 0
over_the_length_count = 0
special_chars_count = 0
bad_word_count = 0
bad_categ_count = 0
new_q_list = []
new_final_dict = {}
non_eng_list = []
auth_length = 40
quote_length = 150


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def unused(s):
    special_chars = ['\\', '/', '{', '}', '[', ']']
    for i in special_chars:
        if i in s:
            return True
    return False


pf = ProfanityFilter()

with open('q_new.json') as f:
    d = json.load(f)
    for item in d["new_quotes"]:
        total_count += 1
        if len(item['Quote']) < quote_length and len(item['Author']) < auth_length:
            if isEnglish(item['Quote']) and isEnglish(item['Author']):
                if not unused(item['Quote']) and not unused(item['Author']):
                    if item['Category'] != 'god' and item['Category'] != 'romance' and item['Category'] != 'death':
                        if not ('fuck' in item['Quote'].lower() or 'sex' in item['Quote'].lower() or 'cock' in item['Quote'].lower()):
                            if not pf.is_profane(item['Quote']):
                                # if not ('fuck' in item['Quote'].lower() or 'sex' in item['Quote'].lower() or 'cock' in item['Quote'].lower()):
                                new_q_list = []
                                category = item["Category"]
                                item['Quote'] = item['Quote'].replace(
                                    "\"", "'")
                                item['quoteText'] = item['Quote']
                                item['quoteAuthor'] = item['Author']
                                item.pop("Category", None)
                                item.pop("Quote", None)
                                item.pop("Author", None)
                                if category not in new_final_dict:
                                    new_q_list.append(item)
                                    new_final_dict[category] = new_q_list
                                else:
                                    new_q_list = new_final_dict[category]
                                    new_q_list.append(item)
                                    new_final_dict[category] = new_q_list
                                valid_count += 1
                            bad_word_count += 1
                        else:
                            bad_word_count += 1
                    else:
                        bad_categ_count += 1
                else:
                    special_chars_count += 1
            else:
                non_eng_count += 1
        else:
            over_the_length_count += 1
            pass

    eliminated_count = non_eng_count + over_the_length_count + \
        special_chars_count + bad_word_count
    print(f"Total count is: {total_count} \n Quote > {quote_length} plus Author > {auth_length} is: {over_the_length_count} \n Non english quote & author count is: {non_eng_count} \n special char in quote & Author count is: {special_chars_count}\n Bad word count is: {bad_word_count} \n Bad category : {bad_categ_count} \n total eliminated : {eliminated_count}  \n Net count is: {valid_count}")
    # count += 1
    # if count > 5:
    #     break
    new_quotes = {}
    new_quotes['quotes'] = new_final_dict
    print(
        f"List of Categories: {list(filter(None,list(new_final_dict.keys())))} \n No.of Categories is: {len(list(filter(None,list(new_final_dict.keys()))))}")

with open('q_new_v2.json', 'w') as f:
    # print(new_quotes, file=f)
    f.write(json.dumps(new_quotes))
    # json.dump({"new_quotes": new_q_list}, f, ensure_ascii=False)
    # for key, value in d.items():
    #     value.pop('id', None)


# Total count is: 48391
#  Quote > 150 plus Author > 40 is: 21441
#  Non english quote & author count is: 2721
#  special char in quote & Author count is: 1940
#  Bad word count is: 21126
#  Bad category : 1163
#  total eliminated : 47228
#  Net count is: 20632
# List of Categories: ['life', 'happiness', 'inspiration', 'humor', 'philosophy', 'science', 'love', 'soul', 'books', 'wisdom', 'truth', 'knowledge', 'education', 'hope', 'friendship', 'writing', 'religion', 'success', 'arts', 'relationship', 'motivation', 'poetry', 'faith', 'mind', 'funny', 'quotes', 'purpose', 'positive']
#  No.of Categories is: 28
