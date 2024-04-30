import io from "socket.io-client";
import { SeamlessOptions } from "./types";
export { SeamlessOptions };

export type Primitive = string | number | boolean | null;

export interface SeamlessElement {
  type: string;
  props: Record<string, any>;
  children: Array<SeamlessElement | Primitive> | null;
}

class Seamless {
  private readonly socket;
  private readonly eventObjectTransformer: (
    originalEvent: Event,
    outEvent: any
  ) => any;

  constructor(config?: SeamlessOptions) {
    this.socket = io({
      reconnectionDelayMax: 10000,
      ...config?.socketOptions,
    });
    this.eventObjectTransformer =
      config?.eventObjectTransformer || ((_, outEvent) => outEvent);
    const allSeamlessElements =
      document.querySelectorAll<HTMLElement>("[seamless\\:id]");
    allSeamlessElements.forEach(this.attachEventListeners.bind(this));
  }

  render(component: SeamlessElement, parentElement: any): void;
  render(component: SeamlessElement, parentElement: HTMLElement): void {
    const domElement = this.toDOMElement(component);
    parentElement.appendChild(domElement);
  }

  private toDOMElement(
    element: SeamlessElement | Primitive
  ): HTMLElement | Text {
    if (this.isPrimitive(element)) {
      return document.createTextNode(element?.toString() || "");
    }

    const domElement = document.createElement(element.type);
    Object.entries(element.props).forEach(([key, value]) => {
      domElement.setAttribute(key, value);
    });

    if (domElement.hasAttribute("seamless:id")) {
      this.attachEventListeners(domElement);
    }

    const children = Array.isArray(element.children)
      ? element.children.map(this.toDOMElement.bind(this))
      : [];
    children.forEach((child) => domElement.appendChild(child));
    return domElement;
  }

  private attachEventListeners(element: HTMLElement) {
    const seamlessId = element.getAttribute("seamless:id");
    const seamlessEvents =
      element.getAttribute("seamless:events")?.split(",") || [];
    seamlessEvents.forEach((event) => {
      element.addEventListener(event, (e: Event) => {
        const outEvent = this.eventObjectTransformer(
          e,
          this.serializeEventObject(e)
        );
        this.socket.emit("dom_event", `${seamlessId}:${event}`, outEvent);
      });
    });
  }

  protected isPrimitive(value: any): value is Primitive {
    return (
      typeof value === "string" ||
      typeof value === "number" ||
      typeof value === "boolean" ||
      value === null
    );
  }

  async getComponent(name: string, props: Record<string, any>) {
    return await this.sendWaitResponse<SeamlessElement | Primitive>(
      "component",
      name,
      props
    );
  }

  registerEventListener(
    seamlessId: string,
    event: string,
    callback: (e: any) => any
  ) {
    this.socket.on(`${seamlessId}:${event}`, callback);
  }

  emit(event: string, ...args: any[]) {
    this.socket.emit(event, ...args);
  }

  sendCustomEvent(event: string, data: any) {
    this.socket.emit("custom", event, data);
  }

  sendWaitResponse<T>(event: string, ...args: any[]) {
    return new Promise<T>((resolve) => {
      this.socket.emit(event, ...args, resolve);
    });
  }

  protected serializeEventObject(event: Event) {
    return {
      type: event.type,
      target: {
        id: (event.target as HTMLElement).id,
        tagName: (event.target as HTMLElement).tagName,
      },
    };
  }
}

export default Seamless;
