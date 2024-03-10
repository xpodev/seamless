import React from "react";
import { createRoot } from "react-dom/client";
import io from "socket.io-client";

type Primitive = string | number | boolean | null;

interface PyJSXElement {
  type: string;
  props: Record<string, any>;
  children: Array<PyJSXElement | Primitive> | null;
}

type ReactElement = ReturnType<typeof React.createElement<Record<string, any>>>;

class Ez {
  private readonly jsxSocket;
  private readonly ezReactRootNode;

  constructor() {
    const rootElement = document.getElementById("root");
    if (!rootElement) {
      throw new Error("Root element not found (id=root)");
    }
    this.ezReactRootNode = createRoot(rootElement);
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

  private convertToReact(element: PyJSXElement | Primitive): ReactElement | Primitive {
    if (this.isPrimitive(element)) {
      return element;
    }

    if ("jsx:id" in element.props) {
      const events: string[] = element.props["jsx:events"]?.split(",") || [];
      events.forEach((event) => {
        event = this.capitalizeFirstLetter(event);
        element.props[`on${event}`] = (e: any) => {
          this.jsxSocket.emit(
            "dom_event",
            `${element.props["jsx:id"]}:${event}`,
            {
              jsxId: element.props["jsx:id"],
              foo: "bar",
            }
          );
        };
      });
    }

    const children = (
      Array.isArray(element.children) ? element.children : [element.children]
    ).map((v) => this.convertToReact(v));
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
    this.jsxSocket.emit("component", name, props);
    return new Promise((resolve) => {
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

  capitalizeFirstLetter(string: string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const ez = new Ez();
});
