import json


# Load Function Schema
with open('./schemas/function_schema.json', 'r') as schema_file:
    schema = json.load(schema_file)




# test_function = schema[5]
# print(test_function)

#     # Loop through actions
#     for action in test_function['actions']:
#         function_name = action + '_' + test_function['base_name']
#         path = test_function['path']
#         if 'params' in test_function.keys():
#             parameters = ', '.join(test_function['params'])
#         else:
#             parameters = ''
#         if action == 'put' or action == 'post':
#             function_text = "def {}(client, payload, {}):\n\tr = requests.{}(client.address:client.port{})\n".format(function_name, parameters, action, path)
#         elif action == 'get' or action == 'del':
#             function_text = "def {}(client, {}):\n\tr = requests.{}(client.address:client.port{})\n".format(function_name, parameters, action, path)
#         print(function_text)

functions = []
functions.append('import json\n\n\n')

# Loop through
for function in schema:

    # Loop through actions
    for action in function['actions']:
        function_name = action + '_' + function['base_name']
        path = function['path']
        if 'params' in function.keys():
            parameters = ', '.join(function['params'])
        else:
            parameters = ''
        if action == 'put' or action == 'post':
            function_text = "def {}(client, payload, {}):\n\tbase_url = ".format(function_name, parameters) + '"{}{}:{}".format(client.protocol, client.address, client.port)' + '\n\tr = client.session.{}(base_url + {}, json=payload)'.format(action, path) + '\n\treturn r\n\n'
        elif action == 'get' or action == 'delete':
            function_text = "def {}(client, {}):\n\tbase_url = ".format(function_name, parameters) + '"{}{}:{}".format(client.protocol, client.address, client.port)' + '\n\tr = client.session.{}(base_url + {})'.format(action, path) + '\n\treturn json.loads(r.text.replace(".","_"))\n\n'
        functions.append(function_text)

with open('./kepware/api_wrapper.py', 'w') as output_file:
    for function in functions:
        output_file.write(function)