import json
json.dumps([1, 'simple', 'list'])

f = 'hello'
x = json.load(f)
json.dump(x, f)

