#JSON processing

import json

def find_more_value(data, result):

    my_list = []

    for key,value in data.items():
        L1 = []
        if result == key:
            L1.append(key)
            L1.append(value)
            T1 = tuple(L1)
            my_list.append(T1)

                
        if type(value) is dict:
            d = find_more_value(value, result)
            for x in d:
                my_list.append(x)
                
        if type(value) is list:
            def iterate_list(value, result):
                for i in value:
                    if type(i) is dict:
                        d = find_more_value(i, result)
                        for x in d:
                            my_list.append(x)
            iterate_list(value, result)

    return my_list

def pp_json(json_thing, sort=True, indents=4):
    print(json.dumps(json_thing, sort_keys=sort, indent=indents))

open_file = True
while open_file:
    try:
        json_file_input = input("Enter the name of the json file: ")
        with open(json_file_input) as json_file: 
            data = json.load(json_file)
            pp_json(data)
            open_file = False
    except:
        print("Error in opening file")
        try_again = ''
        while try_again not in ['y', 'Y', 'n', 'N']:
            try_again = input("Try again?(y/n): ")
        if try_again == 'y' or try_again == 'Y':
            pass
        else:
            exit()


def find_type_of_data(data):
    if type(data) == dict:
        my_list = find_more_value(data, result)
        return my_list
    elif type(data) == list:
        final_list = []
        for item in data:
            my_list = find_more_value(item, result)
            if len(my_list) != 0:
                for x in my_list:
                    final_list.append(x)
        return final_list


while True:
    print("-----------------------------------------------------\n")
    result = input("Enter key to search(or 'q' to quit): ")
    if result=='q':
        break;
    else:
        my_list = find_type_of_data(data)

        if len(my_list) == 0:
            print('No key found')
        else:
            for x,y in my_list:
                print(x, end=': ')
                pp_json(y)
            print(f'\n{len(my_list)} key found')