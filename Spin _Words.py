def spinWords(string):
    input_str = string.split()
    print(input_str)
    
    result = ''
    for idx, word in enumerate(input_str):
        if len(word) > 4:
            word = word[::-1]

        if idx < len(input_str):
            result += word + ' '
        else:
            result += word
    print(result)
         
spinWords('Hey fellow warriors')
spinWords('This is a test')
spinWords('This is another test')