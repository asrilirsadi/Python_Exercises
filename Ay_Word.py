def ay_word(text):
    list_text = text.split()
    str_res = ''
    char_temp = ''
    # print(list_text)
    for item in list_text:
        try:
            char_temp = item[0] + 'ay'
            if not(char_temp.isalpha()):
                char_temp = item[1] + 'ay'
                item = item.replace(item[1],'')
                item += char_temp
            else:
                item = item.replace(item[0],'')
                item += char_temp
            str_res += item + ' '
        except:
            str_res += item + ' '
    print(str_res)

ay_word('Pig latin is cool')
ay_word('Hello world !')
ay_word('!Stop the war')
