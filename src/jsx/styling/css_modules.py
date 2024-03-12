from os import PathLike
from pathlib import Path
import cssutils
from jsx.internal import short_uuid


class CSSClass:
    def __init__(self, class_name: str, css_text: str):
        self.class_name = class_name
        self.css_text = css_text
        self.uuid = short_uuid()

    def as_css(self, minified=False):
        text_lines = self.css_text.split("\n")
        text = ""
        for line in text_lines:
            line = line.strip()
            if not line:
                continue

            attr, value = line.split(":")
            attr = attr.strip()
            value = value.strip()
            if not value.endswith(";"):
                value += ";"
            if minified:
                text += f"{attr}:{value}"
            else:
                text += f"  {attr}: {value}\n"

        if minified:
            return f".{self.uuid}{{{text}}}"
        else:
            return f".{self.uuid} {{\n{text}}}"

    def __str__(self):
        return self.uuid


class CSSModule:
    def __init__(self, module_name):
        css = cssutils.parseFile(module_name)
        self.module_name = module_name
        self.classes = dict[str, CSSClass]()
        for rule in css:
            if rule.type == rule.STYLE_RULE:
                for selector in rule.selectorList:
                    if selector.seq[0].type == "class":
                        class_name = selector.seq[0].value.removeprefix(".")
                        self.classes[class_name] = CSSClass(
                            class_name, rule.style.cssText
                        )

    def __getattr__(self, __name: str) -> str:
        return str(self.classes[__name])


class CSSModulesManager:
    def __init__(self):
        self.modules = dict[str, CSSModule]()
        self.folder = Path.cwd()

    def module(self, css_path: PathLike):
        """
        Get a CSS module by its path.
        This will return a CSSModule object.
        """
        css_path = self._full_path(css_path)
        if css_path not in self.modules:
            self.modules[css_path] = CSSModule(css_path)
        return self.modules[css_path]

    def output(self, minified=False):
        """
        Get the CSS output of all the CSS modules.
        """
        output = ""
        for module in self.modules.values():
            for css_class in module.classes.values():
                output += css_class.as_css(minified=minified)
        return output

    def set_root_folder(self, folder: PathLike):
        """
        Set the folder where the CSS files are located.
        """
        if isinstance(folder, str):
            folder = Path(folder)

        self.folder = folder.absolute()

    def _full_path(self, css_path: PathLike):
        if isinstance(css_path, str):
            css_path = Path(css_path)

        if not css_path.is_absolute():
            return self.folder / css_path
        return css_path


CSS = CSSModulesManager()
