import pathlib

HERE = pathlib.Path(__file__).parent

out_string = ""

with open(HERE / "__init__.py", "w") as f:
    for file in HERE.iterdir():
        if file.name.startswith("_"):
            continue

        print(f"from .{file.stem} import {file.stem.capitalize()}", file=f)
