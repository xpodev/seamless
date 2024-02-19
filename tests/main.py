from pathlib import Path
from importlib import import_module

HERE = Path(__file__).parent

for file in HERE.iterdir():

    if file.name.startswith("_") or file.suffix != ".py" or file.stem == "main":
        continue

    module = import_module(f"tests.{file.stem}")
    main = getattr(module, "main", None)
    if main:
        main()
    else:
        print(f"No main function in {file.stem}")
