import json
def find_by_key(dictionary,looking_for_kei):
    for dictionary_key, dictionary_value in dictionary.items():
        if dictionary_key == looking_for_kei:
            print("\nYour key has been found  \n {}:{}\n".format(looking_for_kei,dictionary_value))
            return 
        if type(dictionary_value) is dict:
            find_by_key(dictionary_value, looking_for_kei)


key_is_required = input("Enter the key by which you want to receive data: ")
dictionary_json={ "glossary":{
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }}

find_by_key(dictionary_json,key_is_required)
