

#def single_root_words(root_word, *other_words):
#    same_words = []
#    for i in other_words:
#        if i in other_words:
#            re.search(root_word, i)
#            same_words.append(i)

#    return same_words
#result = single_root_words('rich', 'richies', 'cheers', 'olichalcum', 'richiest')
#print(result)
#result2 = single_root_words('Disablement', 'Mable', 'Able', 'Disable', 'Bagel')
#print(result2)


#def single_root_words(root_word,*other_words):
#    same_wosrds = []
#   upper_word = root_word.upper()
#    for words in other_words:
#            same_wosrds.append(words)
#           return same_wosrds

#result = single_root_words('rich','richiest','orichalcum','cheer','richies')
#print(result)
#result2 = single_root_words('Disablement','Able','Mable','Disable','Bagel')
#print(result2)

#def single_root_words(root_word,*other_words):
#    same_words = []
#    for word in other_words:
#        if root_word.startswith(word)or word.startswith(root_word):
#            same_words.append(word)
#    return same_words

#result = single_root_words('rich','richiest','orichalcum','cheer','richies')
#print(result)
#result2 = single_root_words('Disablement','Able','Mable','Disable','Bagel')
#print(result2)

def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)