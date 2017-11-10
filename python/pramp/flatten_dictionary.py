dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }

def flatten_dictionary(dict):

    output = {}

    def flatten_dictionary_helper(inner_dict, key_name = None):

        for key in inner_dict:
            tmp_name = key_name + "." + key
            if type(inner_dict[key]) != type({}):
                output[tmp_name] = inner_dict[key]
            else:
                inner_dict = inner_dict[key]
                flatten_dictionary_helper(inner_dict, tmp_name)

    for key in dict:
        if type(dict[key]) != type({}):
            output[key] = dict[key]
        else:
            flatten_dictionary_helper(dict[key], key)

    print(output)




flatten_dictionary(dict)