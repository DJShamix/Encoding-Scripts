
from math import gamma


input_string = "ПРИКАЗ"
gamma_word   = "ГАММА"

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
        out_array_code.append( int(dict_letters[element]) )


    out_array_code.remove('')

    print("Text: \"{}\" is : \"{}\"".format(text, out_array_code))

    return out_array_code


def decode_text(encoded_text):

    decoded_array = []

    for element in encoded_text:
        decoded_array.append( str(dict_numbers[element]))

    out_string = ""
    for element in decoded_array:
        out_string += element

    return out_string


def obfuscate_encoded_text(text_code, gamma_code, mod_number):

    obfs_array_code = []

    counter = 0
    for element in text_code:
        obfs_array_code.append( int( element + (gamma_code[counter] % mod_number)) )
        print("{} -> {} -> {}".format(text_code, element, obfs_array_code))
        
        if counter + 1 >= len(gamma_code):
            counter = 0
        else:
            counter += 1

    return obfs_array_code



encoded_string_code = code_text(input_string)
encoded_gamma_code  = code_text(gamma_word)

obfs_result = obfuscate_encoded_text(encoded_string_code, encoded_gamma_code, 33)

decoded_text = decode_text(obfs_result)

print("Text: [{}]\n Gamma: [{}]\n Result: [{}] -> [{}]".format(input_string, gamma_word, obfs_result, decoded_text))

#code_text(encoded_string)