import io from "socket.io-client";
import { SeamlessOptions, OutEvent } from "./types";
export { SeamlessOptions };

export type Primitive = string | number | boolean | null;

export interface SeamlessElement {
  type: string;
  props: Record<string, any>;
  children: Array<SeamlessElement | Primitive> | null;
}

const SEAMLESS_ELEMENT = "seamless:element";
const SEAMLESS_INIT = "seamless:init";
const SEAMLESS_EMPTY = "seamless:empty";

class Seamless {
  protected readonly socket;
  private readonly eventObjectTransformer: (
    originalEvent: Event,
    outEvent: any
  ) => any;
  private readonly context: Record<any, any> = {};

  constructor(config?: SeamlessOptions) {
    this.socket = io({
      reconnectionDelayMax: 10000,
      ...config?.socketOptions,
    });
    this.eventObjectTransformer =
      config?.eventObjectTransformer || ((_, outEvent) => outEvent);

    this.context.instance = this;
    this.init();
  }

  init() {
    const allSeamlessElements = document.querySelectorAll<HTMLElement>(
      "[seamless\\:element]"
    );

    this.processElements(Array.from(allSeamlessElements));
  }

  processElements(elements: HTMLElement[]) {
    elements.forEach((element) => {
      if (element.hasAttribute(SEAMLESS_INIT)) {
        this.attachInit(element);
      }
    });
    elements.forEach((element) => {
      if (element.tagName.toLowerCase() === SEAMLESS_EMPTY) {
        this.initEmpty(element);
      }
    });
    elements.forEach((element) => {
      element.removeAttribute(SEAMLESS_ELEMENT);
    });
  }

  render(component: SeamlessElement, parentElement: any): void;
  render(component: SeamlessElement, parentElement: HTMLElement): void {
    this.toDOMElement(component, parentElement);
  }

  private toDOMElement(
    element: SeamlessElement | Primitive,
    parentElement?: HTMLElement
  ): HTMLElement | Text {
    if (this.isPrimitive(element)) {
      const primitiveNode = document.createTextNode(element?.toString() || "");
      if (parentElement) {
        parentElement.appendChild(primitiveNode);
      }
      return primitiveNode;
    }

    const domElement = document.createElement(element.type);
    Object.entries(element.props).forEach(([key, value]) => {
      domElement.setAttribute(key, value);
    });

    if (parentElement) {
      parentElement.appendChild(domElement);
    }

    if (Array.isArray(element.children)) {
      element.children.map((child) => this.toDOMElement(child, domElement));
    }

    if (domElement.hasAttribute(SEAMLESS_ELEMENT)) {
      this.processElements([domElement]);
    }

    return domElement;
  }

  protected attachInit(element: HTMLElement) {
    const initCode = element.getAttribute(SEAMLESS_INIT);
    if (initCode) {
      new Function("seamless", initCode).apply(element, [this.context]);
      element.removeAttribute(SEAMLESS_INIT);
    }
  }

  protected initEmpty(element: HTMLElement) {
    while (element.firstChild) {
      element.parentElement?.insertBefore(element.firstChild, element);
    }
    element.parentElement?.removeChild(element);
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
    const outEvent: OutEvent = {
      type: event.type,
      data: undefined,
    };

    switch (true) {
      case event instanceof CustomEvent:
        outEvent.data = (event as CustomEvent).detail;
        break;
      case event instanceof SubmitEvent:
        outEvent.data = this.serializeSubmitEvent(event);
        break;
      default:
        break;
    }

    return outEvent;
  }

  protected serializeSubmitEvent(event: SubmitEvent) {
    event.preventDefault();

    const form = event.target as HTMLFormElement;
    const formData = new FormData(form);
    const data: Record<string, any> = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    return data;
  }
}

export default Seamless;
