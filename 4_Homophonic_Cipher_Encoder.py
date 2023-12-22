
from cmath import pi
from math import gamma


input_string = "ПРИВЕТИВВДДДДДЙ"
#input_string = "ТЕСТ"


dict_letters_h = [
    [],
    [21, 27, 31, 40],   # А
    [15],               # Б
    [1, 33],            # В
    [20, 34],           # Г
    [20, 28, 32, 36],   # Д
    [5],                # Е
    [17],               # Ж
    [14],               # З
    [2, 29, 41],        # И
    [19],               # Й
    [3],                # К
    [39, 42],       # Л
    [9, 43],        # М
    [12, 48],       # Н
    [60],           # О
    [26, 44],       # П
    [25],           # Р
    [24, 49],       # С
    [10, 99],       # Т
    [6, 55, 96],    # У
    [16, 94],       # Ф
    [23],           # Х
    [13],           # Ц
    [11],           # Ч
    [8],            # Ш
    [4],            # Щ
    [38],           # Ь
    [18],           # Ы
    [37],           # Ь
    [7],            # Э
    [85, 97],       # Ю
    [30, 45],       # Я

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


def obfuscate_encoded_text(text_code):

    obfs_final_array_code = []

    for element in text_code:

        obfs_element_variants_array = ( dict_letters_h[element] )

        if len(obfs_element_variants_array) > 1:

            if len(obfs_final_array_code) > 0:

                element_found_counter = 0
                variants_list = obfs_element_variants_array
                for obfs_elem_variant in obfs_element_variants_array:

                    #print("Checking {} Code {} List [{}]".format(element, obfs_elem_variant, variants_list))

                    # Check if element is in array?
                    check_index = 0
                    if obfs_elem_variant in obfs_final_array_code:
                        check_index = obfs_final_array_code[::].index(obfs_elem_variant)

                    # If we've found element, check for duplicates
                    if check_index != 0:
                        # check next element in dictionary
                        if (element_found_counter + 1) >= (len(obfs_element_variants_array)):
                            obfs_final_array_code.append(obfs_element_variants_array[0])
                            #print("Finished")
                        else:
                            element_found_counter = element_found_counter + 1
                            #print("Not Finished - C: {}".format(element_found_counter))

                        #print("Found - {} at {}".format(obfs_elem_variant, check_index))
                    else:
                        # set this element to final array
                        obfs_final_array_code.append(obfs_elem_variant)
                        #print("Not found")
                        break

            else:
                obfs_final_array_code.append(obfs_element_variants_array[0])

        else:
            obfs_final_array_code.append(obfs_element_variants_array[0])


        print("{} -> {} -> {}".format(text_code, element, obfs_final_array_code)) #26 - 25 - 2 - 1 - 5 - 10
        
    return obfs_final_array_code


def test_dict_reader(text):

    out_array_message = [""]

    for element in text:
        element_code = ( int(dict_letters[element]) )
        out_array_message.append(dict_letters_h[ element_code ])

        print("{} -> {} -> {}".format(element, str(dict_letters[element]), str(dict_letters_h[ element_code ])))

    out_array_message.remove('')

    print("\nText: \"{}\" is : \"{}\"".format(text, out_array_message))

    return out_array_message


encoded_string_message = code_text(input_string)
print(encoded_string_message)

#result = test_dict_reader(input_string)

obfs_result = obfuscate_encoded_text(encoded_string_message)

print("\nText: [{}]\nResult: [{}]".format(input_string, obfs_result))

#code_text(encoded_string)