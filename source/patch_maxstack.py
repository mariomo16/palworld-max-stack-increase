import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT = BASE_DIR / "./DA_StaticItemDataAsset.json"
OUTPUT = BASE_DIR / "./DA_StaticItemDataAsset_Mod.json"

OLD_VALUE = 9999
NEW_VALUE = 99999

with open(INPUT, encoding="utf-8") as f:
    data = json.load(f)

exports = data["Exports"]

changed = 0
for export in exports:
    props = export.get("Data")
    if not isinstance(props, list):
        continue
    for prop in props:
        if isinstance(prop, dict) and prop.get("Name") == "MaxStackCount":
            if prop.get("Value") == OLD_VALUE:
                prop["Value"] = NEW_VALUE
                changed += 1

print(f"Modified items: {changed}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
