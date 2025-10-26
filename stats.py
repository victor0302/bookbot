def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in count:
            count[lower_char] +=1
        else:
            count[lower_char] =1 
    return count

def sort_on(item):
    return item['num']

def make_sorted_list(count):
    pairs = []
    for ch,n in count.items():
        pairs.append({"char":ch, "num":n})
    pairs.sort(reverse=True, key= sort_on)
    return pairs