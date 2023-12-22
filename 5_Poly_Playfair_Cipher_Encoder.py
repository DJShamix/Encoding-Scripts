
from math import gamma
from turtle import position
import re


input_string = "ШИФР ПЛЭЙФЕРА"
replace_char = "-"


# Define for X & Y in arrays
X = 0
Y = 1

dict_letters_h = [
    
    ['А', 'Ж', 'Б', 'М', 'Ц', 'В'],
    ['Ч', 'Г', 'Н', 'Ш', 'Д', 'О'],
    ['Е', 'Щ', ',', 'Х', 'У', 'П'],
    ['.', 'З', 'ъ', 'Р', 'И', 'Й'],
    ['С', 'Ь', 'К', 'Э', 'Т', 'Л'],
    ['Ю', 'Я', ' ', 'Ы', 'Ф', '-'],

]

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


def string_to_array(text):

    text_array = [char for char in text]

    #print("Text: \"{}\" is : \"{}\"".format(text, text_array))

    return text_array


def replace_repeat_chars(input_text):

    text_buffer = input_text

    # Check string twice for eliminating possible repeat after 1st try
    for search_try in range(0, 2):

        # Go throgh char dictionary to check pairs
        for replace_comb in dict_letters.keys():

                # If repeatitive pattern matched => insert repl. char between
                if 2*replace_comb in text_buffer:

                    text_buffer = str(text_buffer).replace(str(2 * replace_comb), str(replace_comb + replace_char + replace_comb))
                    #print(text_buffer)

    return text_buffer


def find_symbol_in_array(dictionary_set, search_symbol):

    symbol_position = [-1, -1]

    # Check each line for required symbol
    char_line_index = 0
    for row in dictionary_set:
                
        # Convert char set to string
        string = ''
        for ch in row:
            string += ch
        #print(string)

        # Look for index of char
        char_column_index = -1
        if search_symbol in string:

            char_column_index = string.index(search_symbol)
            symbol_position[X] = char_column_index
            symbol_position[Y] = char_line_index

            #print("{} -> {} -> Pos X: {}, Y: {}".format(search_symbol, string, symbol_position[X], symbol_position[Y]))
            
        # Increase line index counter
        char_line_index += 1

    return symbol_position


def split_string_by_parts(input_string, split_factor):

    #[input_string[i:i+split_factor] for i in range(0, len(input_string), split_factor)]

    #substrings = [] 
    #for i in range(0, len(input_string), split_factor):     
    #    substring = input_string[i:i+split_factor]     
    #    substrings.append(substring)

    if len(input_string) % 2 != 0:
        input_string += " "

    start_index = 0
    output_string = []
    for char_index in input_string:
        output_string.append(input_string[start_index:start_index + split_factor])
        
        if start_index + 2 < len(input_string):
            start_index += 2
        else:
            break

    return output_string


def process_encoding(symbol_1_position, symbol_2_position, dictionary):

    # Horizontal encoding
    if symbol_1_position[Y] == symbol_2_position[Y]:
        #print("Horizontal encoding")

        # Set new position for symbol 1
        if symbol_1_position[X] + 1 < len(dictionary[X]):
            symbol_1_position[X] += 1
        else:
            symbol_1_position[X] = 0

        # Set new position for symbol 2
        if symbol_2_position[X] + 1 < len(dictionary[X]):
            symbol_2_position[X] += 1
        else:
            symbol_2_position[X] = 0


    # Vertical encoding
    elif symbol_1_position[X] == symbol_2_position[X]:
        #print("Vertical encoding")

        # Set new position for symbol 1
        if symbol_1_position[Y] + 1 < len(dictionary[Y]):
            symbol_1_position[Y] += 1
        else:
            symbol_1_position[Y] = 0

        # Set new position for symbol 2
        if symbol_2_position[Y] + 1 < len(dictionary[Y]):
            symbol_2_position[Y] += 1
        else:
            symbol_2_position[Y] = 0


    # Diagonal encoding
    else:
        #print("Diagonal encoding")

        # Set new position for symbols as rectangle
        prev_symbol_1_position = symbol_1_position[Y]
        symbol_1_position[Y] = symbol_2_position[Y]
        symbol_2_position[Y] = prev_symbol_1_position


    return symbol_1_position, symbol_2_position


def encode_message_part(input_message_parts):

    result_shuffled_array = []

    for message_part in input_message_parts:
            
        symbol_1_position = find_symbol_in_array(dict_letters_h, message_part[X])
        symbol_2_position = find_symbol_in_array(dict_letters_h, message_part[Y])

        new_positions = process_encoding(symbol_1_position, symbol_2_position, dict_letters_h)

        result_shuffled_array.append(new_positions)

        #print("New pos 1: X: {}, Y: {} - '{}'".format(new_positions[0][X], new_positions[0][Y], dict_letters_h[new_positions[0][Y]][new_positions[0][X]]))    
        #print("New pos 2: X: {}, Y: {} - '{}'\n".format(new_positions[1][X], new_positions[1][Y], dict_letters_h[new_positions[1][Y]][new_positions[1][X]]))  

    return result_shuffled_array


def encode_numbers_to_text(input_message_array):

    output_text = ""

    for pair_params in input_message_array:

        for element in pair_params:

           output_text = output_text + dict_letters_h[element[Y]][element[X]]


    return output_text


def obfuscate_encoded_text(text_code, replace_char):

    obfs_final_array_code = []
    text_buffer = text_code

    # Replace duplicates in string
    text_buffer = replace_repeat_chars(text_buffer)
    #print(text_buffer)

    # Split string into sets by 2 chars in each one
    split_text_result = split_string_by_parts(text_buffer, 2)
    #print(split_text_result)

    # Encode message
    result_shuffled_array = encode_message_part(split_text_result)

    # Convert number arrays to string text
    result_encoded_text = encode_numbers_to_text(result_shuffled_array)
    #print(result_encoded_text)   

    return result_encoded_text


def test_dict_reader(text):

    out_array_message = [""]

    for element in text:
        element_code = ( int(dict_letters[element]) )
        out_array_message.append(dict_letters_h[ element_code ])

        #print("{} -> {} -> {}".format(element, str(dict_letters[element]), str(dict_letters_h[ element_code ])))

    out_array_message.remove('')

    #print("\nText: \"{}\" is : \"{}\"".format(text, out_array_message))

    return out_array_message


encoded_string_message = string_to_array(input_string)

obfs_result = obfuscate_encoded_text(input_string, replace_char)

print("\nText: [{}]\nResult: [{}]".format(input_string, obfs_result))
