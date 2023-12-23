
from cgitb import text
from math import gamma


input_string = "ШИФРОВАНИЕ*ЗАМЕНОЙ"
input_key    = "КЛЮЧ"
shift_key    = "К"


dict_letters = {

    'А' : 0,
    'Б' : 1,
    'В' : 2,
    'Г' : 3,
    'Д' : 4,
    'Е' : 5,
    'Ё' : 6,
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
    'Ъ' : 29,
    'Э' : 30,
    'Ю' : 31,
    'Я' : 32,
    ' ' : 33,
    '*' : 34
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


def code_key(key):

    out_key = key + input_string[:-(len(key))]
    encoded_key_message = code_text(out_key)

    return encoded_key_message


def decode_text(encoded_text):

    decoded_array = []

    for element in encoded_text:
        decoded_array.append( str(dict_numbers[element]))

    out_string = ""
    for element in decoded_array:
        out_string += element

    return out_string


def obfuscate_encoded_text(text_code, key_code, shift_key):

    # This is result array
    obfs_array_code = []

    # Combine key code and shift key
    key_code = shift_key + key_code

    key_element_index = 0
    for element in text_code:
        result_element = (element + key_code[key_element_index]) % (len(dict_letters) + 1)
        obfs_array_code.append(result_element)
        key_element_index += 1

        #print(obfs_array_code)

    return obfs_array_code



encoded_string_message = code_text(input_string)
encoded_string_key     = code_key(input_key)
encoded_shift_key      = code_text(shift_key) 

encodded_result = obfuscate_encoded_text(encoded_string_message, encoded_string_key, encoded_shift_key)

encodded_result_final = obfuscate_encoded_text(encoded_string_message, encodded_result, encoded_shift_key)

decoded_text = decode_text(encodded_result_final)

print("\n\nText: [{}]\n Key: [{}]\n Secured Text 1: [{}]\n Secured Text 2 : [{}]\n Result: -> [{}]".format(input_string, input_key, encodded_result, encodded_result_final, decoded_text))

#code_text(encoded_string)