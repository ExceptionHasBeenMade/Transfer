import json
import time
with open("./connect.json", encoding='utf-8', errors='ignore') as json_data:
    imported = json.load(json_data, strict=False)
print("Press \"p\" to send trigger")

while True:
    inp = input()
    if (inp == "p"):
        imported["action"] = True
        connector = open("./connect.json", "w", encoding="utf-8")
        json.dump(imported, connector)
        connector.close()
        time.sleep(0.01)
        imported["action"] = False
        connector = open("./connect.json", "w", encoding="utf-8")
        json.dump(imported, connector)
        connector.close()
