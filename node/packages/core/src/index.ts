import io from "socket.io-client";
import {
  SeamlessOptions,
  OutEvent,
  PropertyData,
  PropertyType,
  AttributeHandlerMatcher,
  AttributeHandler,
} from "./types";
export { SeamlessOptions };

export type Primitive = string | number | boolean | null;

export interface SeamlessElement {
  type: string;
  props: Record<string, any>;
  children: Array<SeamlessElement | Primitive> | null;
}

const SEAMLESS_ELEMENT = "seamless:element";
const SEAMLESS_EVENT = "seamless:event:";
const SEAMLESS_INIT = "seamless:init";
const SEAMLESS_EMPTY = "seamless:empty";

class Seamless {
  protected readonly socket;
  private readonly eventObjectTransformer: (
    originalEvent: Event,
    outEvent: any
  ) => any;
  private readonly attributeHandlers = new Map<
    AttributeHandlerMatcher,
    AttributeHandler
  >();
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
    this.attributeHandlers.set(
      (element) => element.hasAttribute(SEAMLESS_ELEMENT),
      (element) => this.attachEventListeners(element as HTMLElement)
    );
    this.attributeHandlers.set(
      (element) => element.hasAttribute(SEAMLESS_INIT),
      (element) => this.attachInit(element as HTMLElement)
    );
    this.attributeHandlers.set(
      (element) => element.tagName.toLowerCase() === SEAMLESS_EMPTY,
      (element) => this.initEmpty(element as HTMLElement)
    );


    const allSeamlessElements = document.querySelectorAll<HTMLElement>(
      "[seamless\\:element]"
    );
    allSeamlessElements.forEach((element) =>
      this.attributeHandlers.forEach((handler, matcher) => {
        if (matcher(element)) {
          handler(element);
        }
      })
    );
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

    this.attributeHandlers.forEach((handler, matcher) => {
      if (matcher(domElement)) {
        handler(domElement);
      }
    });

    return domElement;
  }

  protected attachEventListeners(element: HTMLElement, removeAttribute = true) {
    const attributes = element.attributes;

    for (let i = 0; i < attributes.length; i++) {
      const attribute = attributes[i];
      if (attribute.name.startsWith(SEAMLESS_EVENT)) {
        const eventName = attribute.name.replace(SEAMLESS_EVENT, "");
        element.addEventListener(eventName, (event: Event) => {
          const outEvent = this.eventObjectTransformer(
            event,
            this.serializeEventObject(event)
          );
          this.socket.emit("event", attribute.value, outEvent);
        });

        element.removeAttribute(attribute.name);
      }
    }

    removeAttribute && element.removeAttribute(SEAMLESS_ELEMENT);
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
    const component = await this.sendWaitResponse<SeamlessElement | Primitive>(
      "component",
      name,
      props
    );

    const prepareComponent = (component: SeamlessElement | Primitive) => {
      if (this.isPrimitive(component)) {
        return component;
      }

      if (component.props) {
        // component.props = this.parseProps(component.props);
      }

      if (component.children) {
        component.children = component.children.map(prepareComponent);
      }

      return component;
    };

    return prepareComponent(component);
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

  private parseProps(props: Record<string, PropertyData>) {
    const parsedProps: Record<string, any> = {};
    Object.entries(props).forEach(([key, prop]) => {
      switch (prop.type) {
        case PropertyType.Function:
          parsedProps[key] = new Function(prop.value);
          break;
        default:
          parsedProps[key] = prop.value;
      }
    });

    return parsedProps;
  }
}

export default Seamless;
