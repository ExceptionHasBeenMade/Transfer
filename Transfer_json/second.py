from json import load, dump
with open("./connect.json", encoding='utf-8', errors='ignore') as json_data:
    imported = load(json_data, strict=False)
print("Press \"w\" to send trigger")

while True:
    inp = input()
    if (inp == "w"):
        imported["action"] = True
        connector = open("./connect.json", "w", encoding="utf-8")
        dump(imported, connector)
        connector.close()
        imported["action"] = False
        connector = open("./connect.json", "w", encoding="utf-8")
        dump(imported, connector)
        connector.close()
