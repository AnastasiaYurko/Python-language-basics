with open("test_text.txt", "r", encoding="UTF-8") as text:
    str_num = text.read().split("\n")
    print(f"В данном текстовом файле {len(str_num)} строки")
    
    i = 1
    for string in str_num:
        word_num = string.split( )
        print(f"В {i}-ой строке {len(word_num)} слов(а)")
        i += 1