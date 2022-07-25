import json



a = [[1,2,3], [5,6,8]]


with open("teste.json", 'w') as teste_json:
    json.dump(a, teste_json)

teste_json.close()