import io from "socket.io-client";

export type Primitive = string | number | boolean | null;

export interface PyJSXElement {
  type: string;
  props: Record<string, any>;
  children: Array<PyJSXElement | Primitive> | null;
}

class PyJSX {
  private readonly jsxSocket;

  constructor() {
    this.jsxSocket = io({
      reconnectionDelayMax: 10000,
    });
    const allJsxElements = document.querySelectorAll<HTMLElement>("[jsx\\:id]");
    allJsxElements.forEach(this.attachEventListeners.bind(this));
  }

  private attachEventListeners(element: HTMLElement) {
    const jsxId = element.getAttribute("jsx:id");
    const jsxEvents = element.getAttribute("jsx:events")?.split(",") || [];
    jsxEvents.forEach((event) => {
      element.addEventListener(event, (e) => {
        this.jsxSocket.emit("dom_event", `${jsxId}:${event}`, {
          jsxId,
          foo: "bar",
        });
      });
    });
  }

  protected isPrimitive(value: any): value is Primitive {
    return (
      ["string", "number", "boolean"].includes(typeof value) || value === null
    );
  }

  getComponent(name: string, props: Record<string, any>) {
    this.jsxSocket.emit("component", name, props);
    return new Promise<PyJSXElement | Primitive>((resolve) => {
      this.jsxSocket.once(
        `component`,
        (component: PyJSXElement | Primitive) => {
          resolve(component);
        }
      );
    });
  }

  registerJsxEventListener(
    jsxId: string,
    event: string,
    callback: (e: any) => any
  ) {
    this.jsxSocket.on(`${jsxId}:${event}`, callback);
  }

  emit(event: string, ...args: any[]) {
    this.jsxSocket.emit(event, ...args);
  }
}

export default PyJSX;