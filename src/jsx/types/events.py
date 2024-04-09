from jsx import Element, Component

# region: Event Types

class Event:
    target: "Component | Element"


class MouseEvent(Event): ...


class KeyboardEvent(Event): ...


class FormDataEvent(Event): ...


class TouchEvent(Event): ...


class InputEvent(Event): ...


class DragEvent(Event): ...


# endregion
