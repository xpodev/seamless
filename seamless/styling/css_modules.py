import inspect
from os import PathLike
from pathlib import Path
import cssutils
from seamless.internal import short_uuid


class CSSClass:
    def __init__(self, class_name: str, css_text: str = None):
        self.class_name = class_name
        self.sub_rules: dict[str, dict[str, str]] = {}
        self.uuid = short_uuid()
        if css_text is not None:
            self.add_rule("", css_text)

    def add_rule(self, rule: str, properties: dict[str, str]):
        if rule not in self.sub_rules:
            self.sub_rules[rule] = {}

        self.sub_rules[rule].update(properties)

    def to_css_string(self, minified=False):
        rules = []
        rules_format_string = (
            ".{0}{1} {{\n{2}}}\n" if not minified else ".{0}{1}{{{2}}}"
        )
        single_rule_format_string = "\t{0}: {1}\n" if not minified else "{0}:{1}"
        for key, rule in self.sub_rules.items():
            rule_text = ""
            for attr, value in rule.items():
                value = value.strip()
                if not value.endswith(";"):
                    value += ";"
                rule_text += single_rule_format_string.format(attr, value)

            rules.append(rules_format_string.format(self.uuid, key, rule_text))

        join_string = "" if minified else "\n"
        return join_string.join(rules)

    def __str__(self):
        return self.uuid


class CSSModule:
    def __init__(self, module_name):
        css = cssutils.parseFile(module_name)
        self.module_name = module_name
        self.classes: dict[str, CSSClass] = {}
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
                css_class = (
                    self.classes[base_name]
                    if base_name in self.classes
                    else CSSClass(base_name)
                )
                for selector in selectors:
                    css_class.add_rule(
                        selector.selectorText.replace(f".{base_name}", ""), style_dict
                    )

                self.classes[base_name] = css_class

    def __getattr__(self, __name: str):
        if __name not in self.classes:
            raise AttributeError(f"CSS class {__name} not found in {self.module_name}")
        return self.classes[__name].uuid

    def to_css_string(self, minified=False):
        join_string = "" if minified else "\n\n"
        return join_string.join(
            css_class.to_css_string(minified) for css_class in self.classes.values()
        )


class CSSModulesManager:
    def __init__(self):
        self.modules: dict[str, CSSModule] = {}
        self.folder: Path = Path.cwd()

    def module(self, css_path: PathLike):
        """
        Get a CSS module by its path.
        This will return a CSSModule object.
        """
        css_path = self._full_path(css_path)
        if css_path not in self.modules:
            self.modules[css_path] = CSSModule(css_path)
        return self.modules[css_path]

    def to_css_string(self, minified=False):
        """
        Get the CSS output of all the CSS modules.
        """
        join_string = "" if minified else "\n\n"
        return join_string.join(
            css_module.to_css_string(minified) for css_module in self.modules.values()
        )

    def set_root_folder(self, folder: PathLike):
        """
        Set the folder where the CSS files are located.
        """
        if isinstance(folder, str):
            folder = Path(folder)

        self.folder = folder.absolute()

    def _full_path(self, css_path: PathLike):
        if isinstance(css_path, str):
            if css_path.startswith("./"):
                frame = inspect.stack()[2]
                module = inspect.getmodule(frame[0])
                css_path = Path(module.__file__).parent / css_path

            css_path = Path(css_path)

        if not css_path.is_absolute():
            return self.folder / css_path
        return css_path


CSS = CSSModulesManager()

__all__ = ["CSS"]
