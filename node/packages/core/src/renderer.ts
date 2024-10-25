import { SeamlessOptions, Primitive, SeamlessElement } from "./types";
import { SEAMLESS_ELEMENT, SEAMLESS_INIT, SEAMLESS_EMPTY } from "./constants";

export class Renderer {
  private readonly eventObjectTransformer: (
    originalEvent: Event,
    outEvent: any
  ) => any;
  private readonly context: Record<any, any> = {};

  constructor(config?: SeamlessOptions) {
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
      value === null ||
      value === undefined
    );
  }
}
