import io from "socket.io-client";
import { SlarfOptions } from "./types";

export type Primitive = string | number | boolean | null;

export interface SlarfElement {
  type: string;
  props: Record<string, any>;
  children: Array<SlarfElement | Primitive> | null;
}

class Slarf {
  private readonly socket;
  private readonly eventObjectTransformer: (
    originalEvent: Event,
    outEvent: any
  ) => any;

  constructor(config?: SlarfOptions) {
    this.socket = io({
      reconnectionDelayMax: 10000,
      ...config?.socketOptions,
    });
    this.eventObjectTransformer =
      config?.eventObjectTransformer || ((_, outEvent) => outEvent);
    const allSlarfElements = document.querySelectorAll<HTMLElement>("[slarf\\:id]");
    allSlarfElements.forEach(this.attachEventListeners.bind(this));
  }

  private attachEventListeners(element: HTMLElement) {
    const slarfId = element.getAttribute("slarf:id");
    const slarfEvents = element.getAttribute("slarf:events")?.split(",") || [];
    slarfEvents.forEach((event) => {
      element.addEventListener(event, (e: Event) => {
        const outEvent = this.eventObjectTransformer(
          e,
          this.serializeEventObject(e)
        );
        this.socket.emit("dom_event", `${slarfId}:${event}`, outEvent);
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
    return await this.sendWaitResponse<SlarfElement | Primitive>(
      "component",
      name,
      props
    );
  }

  registerEventListener(
    slarfId: string,
    event: string,
    callback: (e: any) => any
  ) {
    this.socket.on(`${slarfId}:${event}`, callback);
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

export default Slarf;
