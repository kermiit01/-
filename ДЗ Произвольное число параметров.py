def single_root_words(root_word,*other_words):
    same_words=[]
    for i in other_words:
        if root_word.upper() in i.upper(): # В задаче прописанно что нужно найти примерно похожие слова, для этого можно добавить срез root_word'a, найти его через len и прописать в этот if как  root_word[:len//2].upper()
            same_words.append(i)
        else:
            if i.upper() in root_word.upper():
                same_words.append(i)
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement','Able', 'Mable', 'Disable', 'Bagel')
