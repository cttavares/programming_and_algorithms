import json

with open ("exemplo_palavras/exemplo_json.json","r") as file:
    content = json.load (file)

print (content)