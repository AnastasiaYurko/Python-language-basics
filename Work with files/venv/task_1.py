with open("user_text.txt", "w", encoding="UTF-8") as user_text:
    while True:
        text = input("Напишите что-нибудь: ").split( )
        if text:
            text[len(text)-1] += "\n"
            text_str = []
            for word in text:
                word += " "
                text_str.append(word)
            user_text.writelines(text_str)
        else:
            break
