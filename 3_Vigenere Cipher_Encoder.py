
from math import gamma


input_string = "ЗАМЕНА"
input_key    = "КЛЮЧ"

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

    out_array_message = [""]

    for element in text:
        #print(str(dict_letters[element]))
        out_array_message.append( int(dict_letters[element]) )

    out_array_message.remove('')

    print("Text: \"{}\" is : \"{}\"".format(text, out_array_message))

    return out_array_message


def decode_text(encoded_text):

    decoded_array = []

    for element in encoded_text:
        decoded_array.append( str(dict_numbers[element]))

    out_string = ""
    for element in decoded_array:
        out_string += element

    return out_string


def obfuscate_encoded_text(text_code, key_code, mod_number):

    obfs_array_code = []

    counter = 0
    for element in text_code:
        obfs_element_code = ( int( element + (key_code[counter] % mod_number)) )
        if obfs_element_code <= len(dict_letters):
            obfs_array_code.append(obfs_element_code)
        else:
            obfs_array_code.append(obfs_element_code - (len(dict_letters)+1))

        print("{} -> {} -> {}".format(text_code, element, obfs_array_code))
        
        if counter + 1 >= len(key_code):
            counter = 0
        else:
            counter += 1

    return obfs_array_code



encoded_string_message = code_text(input_string)
encoded_string_key     = code_text(input_key)

obfs_result = obfuscate_encoded_text(encoded_string_message, encoded_string_key, 33)

decoded_text = decode_text(obfs_result)

print("Text: [{}]\n Key: [{}]\n Result: [{}] -> [{}]".format(input_string, input_key, obfs_result, decoded_text))

#code_text(encoded_string)