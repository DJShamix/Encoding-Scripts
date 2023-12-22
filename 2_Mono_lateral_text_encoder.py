
input_string = "ШИФРОВАНИЕ ЗАМЕНОЙ"

dict_letters = {

    'А' : 1,
    'Б' : 2,
    'В' : 3,
    'Г' : 4,
    'Д' : 5,
    'Е' : 6,
    'Ж' : 7,
    'З' : 8,
    'И' : 9,
    'Й' : 10,
    'К' : 11,
    'Л' : 12,
    'М' : 13,
    'Н' : 14,
    'О' : 15,
    'П' : 16,
    'Р' : 17,
    'С' : 18,
    'Т' : 19,
    'У' : 20,
    'Ф' : 21,
    'Х' : 22,
    'Ц' : 23,
    'Ч' : 24,
    'Ш' : 25,
    'Щ' : 26,
    'Ь' : 27,
    'Ы' : 28,
    'Ь' : 29,
    'Э' : 30,
    'Ю' : 31,
    'Я' : 32,
    ' ' : 33,

}

dict_numbers = {v : k for k, v in dict_letters.items() }


def code_text(text):

    out_array_code = [""]
    out_array_text = [""]

    for element in text:
        #print(str(dict_letters[element]))
        out_array_code.append( 34 - int(dict_letters[element]) )


    out_array_code.remove('')
    for element in out_array_code:
        out_array_text.append( str(dict_numbers[element]))


    out_string = ""
    for element in out_array_text:
        out_string += element


    #print("Text: {} is : {}".format(text, out_array_code))
    print("Text: \"{}\" is : \"{}\"".format(text, out_string))

    return out_string




encoded_string = code_text(input_string)

code_text(encoded_string)