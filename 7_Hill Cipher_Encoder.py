
from math import gamma
import numpy as np
import math 


input_string = "ШИФР  "
key_word     = "АЛЬПИНИЗМ"

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
    'Ь' : 29,
    'Э' : 30,
    'Ю' : 31,
    'Я' : 32,
    '.' : 33,
    ',' : 34,
    ' ' : 35,
    '?' : 36,
}

dict_numbers = {v : k for k, v in dict_letters.items() }


def code_text(text):

    out_array_code = [""]
    out_array_text = [""]

    for element in text:
        #print(str(dict_letters[element]))
        out_array_code.append( int(dict_letters[element]))


    out_array_code.remove('')

    print("Text: \"{}\" is : \"{}\"".format(text, out_array_code))

    return out_array_code


def convert_code_to_text(encoded_text):

    decoded_array = []

    for element in encoded_text:
        decoded_array.append( str(dict_numbers[element]))

    out_string = ""
    for element in decoded_array:
        out_string += element

    return out_string


def create_key_matrix(key_array):

    key_length = len(key_array)

    if key_length % 2 == 0:
        array_size = int(key_length / 2)
        #print("1Size: {}\n".format(array_size))
    else:
        array_size = int(math.sqrt(key_length))
        #print("2Size: {}\n".format(array_size))

    np_key_array = np.array(key_array)
    #print(np_key_array)


    if key_length % 2 == 0:
        np_reshaped_key_array = np_key_array.reshape(2, array_size)
    else:
        np_reshaped_key_array = np_key_array.reshape(array_size, array_size)
    #print(np_reshaped_key_array)

    return np_reshaped_key_array


def encode_message(message_array, key_array):

    # Multiply message and key matrices
    matrix_mult = np.matmul(message_array, key_array)

    # Detect dictionary size for future devision
    dictionary_size = len(dict_letters) + 1

    # Encode message by taking the rest of devision from matrix multiplication
    result_encoded_message = []
    for matrix_line in matrix_mult:
        for matrix_element in matrix_line:
            encoded_element = int( matrix_element % dictionary_size) 
            result_encoded_message.append(encoded_element)
            
    return result_encoded_message


encoded_string_code = code_text(input_string)
encoded_key_code = code_text(key_word)

payload_array = create_key_matrix(encoded_string_code)
key_array = create_key_matrix(encoded_key_code)

encoded_result = encode_message(payload_array, key_array)

encoded_text_result = convert_code_to_text(encoded_result)
print("Result: {}".format(encoded_text_result))

#decoded_text = decode_text(obfs_result)

#print("Text: [{}]\n Gamma: [{}]\n Result: [{}] -> [{}]".format(input_string, gamma_word, obfs_result, decoded_text))

#code_text(encoded_string)