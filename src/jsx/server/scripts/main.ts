type Primitive = string | number | boolean | null;

interface PyJSXElement {
  type: string;
  props: Record<string, any>;
  children: Array<PyJSXElement | Primitive>;
}

class Ez {
  private pyxSocket = io({
    reconnectionDelayMax: 10000,
  });
  private ezReactRootNode = ReactDOM.createRoot(
    document.getElementById("root")
  );

  constructor() {
    document.addEventListener("DOMContentLoaded", () => {
      const allPyxElements = document.querySelectorAll("[pyx-id]");
      allPyxElements.forEach(this.attachEventListeners.bind(this));
    });
  }

  private attachEventListeners(element: HTMLElement) {
    const pyxId = element.getAttribute("pyx-id");
    const pyxEvents = element.getAttribute("pyx-events")?.split(",") || [];
    pyxEvents.forEach((event) => {
      element.addEventListener(event, (e) => {
        this.pyxSocket.emit("dom_event", `${pyxId}:${event}`, {
          pyxId,
          foo: "bar",
        });
      });
    });
  }

  private convertToReact(element: PyJSXElement | Primitive) {
    if (this.isPrimitive(element)) {
      return element;
    }

    if ("pyx-id" in element.props) {
      const events: string[] = element.props["pyx-events"]?.split(",") || [];
      events.forEach((event) => {
        event = this.capitalizeFirstLetter(event);
        element.props[`on${event}`] = (e: any) => {
          this.pyxSocket.emit(
            "dom_event",
            `${element.props["pyx-id"]}:${event}`,
            {
              pyxId: element.props["pyx-id"],
              foo: "bar",
            }
          );
        };
      });
    }
    
    const children = Array.isArray(element.children)
      ? element.children.map((v) => this.convertToReact(v))
      : [element.children];
    return React.createElement(element.type, element.props, ...children);
  }

  private isPrimitive(value: any): value is Primitive {
    return (
      ["string", "number", "boolean"].includes(typeof value) || value === null
    );
  }

  get reactRootNode() {
    return this.ezReactRootNode;
  }

  render(element: PyJSXElement | Primitive) {
    this.ezReactRootNode.render(this.convertToReact(element));
  }

  getComponent(name: string, props: Record<string, any>) {
    this.pyxSocket.emit("component", name, props);
    return new Promise((resolve) => {
      this.pyxSocket.once(
        `component`,
        (component: PyJSXElement | Primitive) => {
          resolve(component);
        }
      );
    });
  }

  registerPyxEventListener(
    pyxId: string,
    event: string,
    callback: (e: any) => any
  ) {
    this.pyxSocket.on(`${pyxId}:${event}`, callback);
  }

  capitalizeFirstLetter(string: string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
}
