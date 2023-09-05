import json

x = '{"name": "Gab", "age": 30 }'

jsonobj = json.loads(x)

print(jsonobj["name"])


# python json object to string

pjson = {
     "name": "John"
    ,"age": 20
}

print(json.dumps(pjson))