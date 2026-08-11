import json

INPUT = "/mnt/user-data/uploads/DA_StaticItemDataAsset.json"
OUTPUT = "/mnt/user-data/outputs/DA_StaticItemDataAsset_Mod.json"

OLD_VALUE = 9999
NEW_VALUE = 99999

with open(INPUT, encoding="utf-8") as f:
    data = json.load(f)

exports = data["Exports"]

changed = []
for export in exports:
    props = export.get("Data")
    if not isinstance(props, list):
        continue
    for prop in props:
        if isinstance(prop, dict) and prop.get("Name") == "MaxStackCount":
            if prop.get("Value") == OLD_VALUE:
                prop["Value"] = NEW_VALUE
                changed.append(export.get("ObjectName"))

print(f"Modified items: {len(changed)}")
for name in changed[:15]:
    print("  -", name)
if len(changed) > 15:
    print(f"  ... & {len(changed) - 15} more")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)