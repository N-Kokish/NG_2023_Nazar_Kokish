import json
def find_by_key(dictionary,looking_for_kei):
    for dictionary_key, dictionary_value in dictionary.items():
        if dictionary_key == looking_for_kei:
            print("\nYour key has been found  \n {}:{}\n".format(looking_for_kei,dictionary_value))
            return 
        if type(dictionary_value) is dict:
            find_by_key(dictionary_value, looking_for_kei)
file_name = input("Enter the name of the file in which there is json: ")
key_is_required = input("Enter the key by which you want to receive data: ")
with open(file_name, "r") as file:
    dictionary_json = json.loads(file.read())
find_by_key(dictionary_json,key_is_required)
