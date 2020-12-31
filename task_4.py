translation_dict = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
new_file = []
with open('eng.txt', 'r', encoding="UTF-8") as eng_text:

    for string in eng_text:
        string = string.split(" ")
        if string[2].endswith("\n"):
            string[2] = string[2][:-1]
        new_file.append(translation_dict[string[0]] + " " + string[1] + " " + string[2])
    print(new_file)

with open('rus.txt', 'w', encoding="UTF-8") as rus_text:
    text_str = []
    for word in new_file:
        word += "\n"
        text_str.append(word)
    rus_text.writelines(text_str)

