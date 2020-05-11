import kepware as kep
import json
from pprint import pprint


client = kep.Client('dsf-piint1', 57412, use_ssl=False)

c = kep.get_channels(client, channels_name='OPCDA01', content=['property_definitions'])
print(c)
replace_dict = {
    'String': 'str',
    'Integer' : 'int',
    'SignedInteger' : 'int',
}

# define a functions that takes a string and a dict
def find_replace(string, dictionary):
    if string in dictionary.keys():
        # look up and replace
        string = dictionary[string]
    # return updated string
    return string

for prop in c:
    print("# {}\n{} : {} = {}\n".format(prop['display_description'], prop['symbolic_name'], find_replace(prop['type'], replace_dict), prop['default_value']))
