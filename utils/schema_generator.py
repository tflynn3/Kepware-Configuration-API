import requests
from bs4 import BeautifulSoup
import re
import json


html = requests.get('http://10.50.1.213:57412/config/v1/doc').text
soup = BeautifulSoup(html, 'html.parser')

api_paths = soup.findAll('td', {'class': 'epPath'})
api_actions = soup.findAll('td', {'class': 'epAction'})

schema = []
for path, action in zip(api_paths, api_actions):

    # Skip transaction log and event log time queries
    if '?' in path.text:
        continue
    
    # Initialize function dict
    function = {}

    # Set request methods
    action_list = action.text.replace('del', 'delete').split(', ')
    function['actions'] = action_list

    # Create a pythonic function name
    function_base_name = path.text.replace('/config/v1/project/', '').replace('_', '').replace(r'/{name}','_').replace('/','_').replace('__', '_')
    function_base_name = function_base_name[:-1] if function_base_name.endswith('_') is True else function_base_name
    function['base_name'] = function_base_name

    # Parse out required parameters
    function_params = set()
    pattern = r"\w+\/\{\w+\}"
    matches = re.findall(pattern, path.text)
    for match in matches:
        function_params.add(match.replace('/{','_').replace('}',''))
    
    function['params'] = list(function_params)

    # Set API Path with new parameter names
    new_path = '"' + path.text.replace(r'{name}', '{}') + '"' +  ".format({})".format(', '.join(function_params))
    function['path'] = new_path

    schema.append(function)
with open('./schemas/function_schema.json', 'w') as output_file:
    json.dump(schema, output_file, indent=4)
