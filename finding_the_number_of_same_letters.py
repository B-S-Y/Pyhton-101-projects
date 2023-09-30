def same_letters_count():
    word_1 = input("Please write the first word: ").lower()
    word_2 = input("Please write the second word: ").lower()
    already_counted_letters = []
    for i in word_1:
        if i in word_2:
            if i in already_counted_letters:
                continue
            else:
                print(i,word_1.count(i),word_2.count(i))
                already_counted_letters.append(i)
        else:
            continue


same_letters_count()
