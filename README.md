## Max Stack Increase

Palworld mod that increases the maximum stack size of items, with separate versions for different stack-size configurations.

## Required Tools

- [UAssetGUI](https://github.com/atenfyr/UAssetGUI/releases/latest)
- [FModel](https://github.com/4sval/FModel/releases/latest)
- [UnrealPak](https://github.com/xamarth/unrealpak)

## Repository Structure

```text
.
├── dist/
│   ├── MaxStackIncrease_P.pak
│   └── MaxStackIncreaseExtended_P.pak
│
├── mappings/
│   ├── Palworld-v1.0.5.usmap
│   └── ...
│
└── source/
    ├── MaxStackIncrease_P/
    │   └── Pal/Content/...
    │
    ├── MaxStackIncreaseExtended_P/
    │   └── Pal/Content/...
    │
    ├── Pal/
    │   └── Content/
    │       └── Pal/
    │           └── DataAsset/
    │               └── Item/
    │                   ├── DA_StaticItemDataAsset.uasset
    │                   └── DA_StaticItemDataAsset.uexp
    │
    └── DA_StaticItemDataAsset.json

```

- `source/MaxStackIncrease_P/` contains the modified assets for `MaxStackIncrease`
- `source/MaxStackIncreaseExtended_P/` contains the modified assets for `MaxStackIncreaseExtended`
- `source/Pal/` contains the original, unmodified game assets