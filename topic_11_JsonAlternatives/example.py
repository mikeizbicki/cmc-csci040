import json
import yaml
#import tomllib
import tomli_w

code = '''
print("hello world")
print("hola mundo")
print("salve munde")
'''.strip()
data = {'code': code}

print('============')
print('code')
print('============')
print(code)

print('============')
print('json')
print('============')
print(json.dumps(data, indent=2))

print('============')
print('yaml')
print('============')
print(yaml.dump(data, default_flow_style=False, default_style='|'))

print('============')
print('toml')
print('============')
print(tomli_w.dumps(data, multiline_strings=True))
