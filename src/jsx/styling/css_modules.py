from os import PathLike
from pathlib import Path
import cssutils
from jsx.internal import short_uuid


class CSSClass:
    def __init__(self, class_name: str, css_text: str = None):
        self.class_name = class_name
        self.sub_rules = dict[str, dict[str, str]]()
        self.uuid = short_uuid()
        if css_text is not None:
            self.add_rule("", css_text)

    def add_rule(self, rule: str, properties: dict[str, str]):
        if rule not in self.sub_rules:
            self.sub_rules[rule] = {}

        self.sub_rules[rule].update(properties)

    def as_css(self, minified=False):
        text = ""
        for key, rule in self.sub_rules.items():
            rule_text = ""
            for attr, value in rule.items():
                value = value.strip()
                if not value.endswith(";"):
                    value += ";"
                if minified:
                    rule_text += f"{attr}:{value}"
                else:
                    rule_text += f"  {attr}: {value}\n"

            if minified:
                text += f".{self.uuid}{key}{{{rule_text}}}"
            else:
                text += f".{self.uuid}{key} {{\n{rule_text}}}\n"

        return text

    def __str__(self):
        return self.uuid


class CSSModule:
    def __init__(self, module_name):
        css = cssutils.parseFile(module_name)
        self.module_name = module_name
        self.classes = dict[str, CSSClass]()
        for rule in css:
            if rule.type == rule.STYLE_RULE:
                selectors = rule.selectorList
                first_selector = selectors[0]
                if first_selector.seq[0].type != "class":
                    continue

                style_dict = {
                    css_property.name: css_property.value for css_property in rule.style
                }

                base_name = first_selector.seq[0].value.removeprefix(".")
                css_class = self.classes[base_name] if base_name in self.classes else CSSClass(base_name)
                for selector in selectors:
                    css_class.add_rule(
                        selector.selectorText.replace(f".{base_name}", ""), style_dict
                    )

                self.classes[base_name] = css_class

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
