def combine_lists(lstAll):
    combine_set = set()
    for index in lstAll:
        combine_set.update(index)
    return list(combine_set)
print(combine_lists([[2,4,5], [3,4,8], [2,9,10]]))

def remove_duplicate_words(string):
    sentences = string.split('.')
    new_string = ""
    for sentence in sentences:
        sentence_words = sentence.split(' ')
        sentence_words = list(sorted(set(sentence_words), key = sentence_words.index)) #see note below
        new_sentence = ""
        for word in sentence_words:
            new_sentence += word + " "
        new_sentence = new_sentence.rstrip()
        new_string += new_sentence + "."
    new_string = new_string.rstrip('.') + '.'
    return new_string

string = "My name name is John. I migrated migrated from " \
         "from Abuja to Lagos. My native native language is is Edo."
print(remove_duplicate_words(string))


a = [9,4,1,20,4]
print(sorted(set(a), key = a.index))
