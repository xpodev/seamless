import pathlib

HERE = pathlib.Path(__file__).parent

with open(HERE / "__init__.py", "w") as f:
    items = []
    for file in HERE.iterdir():
        if file.name.startswith("_") or file.suffix != ".py":
            continue
        
        capitalized = file.stem.capitalize()
        items.append(capitalized)
        print(f"from .{file.stem} import {capitalized}", file=f)

    all = "\n".join(f"\t\"{item}\"," for item in items)
    print(f"\n__all__ = [\n{all}\n]", file=f)
