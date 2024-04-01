import io from "socket.io-client";
import { SlarfOptions } from "./types";

export type Primitive = string | number | boolean | null;

export interface PyJSXElement {
    type: string;
    props: Record<string, any>;
    children: Array<PyJSXElement | Primitive> | null;
}

class PyJSX {
    private readonly jsxSocket;

    constructor(config?: SlarfOptions) {
        this.jsxSocket = io({
            reconnectionDelayMax: 10000,
            ...config?.socketOptions,
        });
        const allJsxElements = document.querySelectorAll<HTMLElement>("[jsx\\:id]");
        allJsxElements.forEach(this.attachEventListeners.bind(this));
    }

    private attachEventListeners(element: HTMLElement) {
        const jsxId = element.getAttribute("jsx:id");
        const jsxEvents = element.getAttribute("jsx:events")?.split(",") || [];
        jsxEvents.forEach((event) => {
            element.addEventListener(event, (e: Event) => {
                this.jsxSocket.emit("dom_event", `${jsxId}:${event}`, this.serializeEventObject(e));
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

export default PyJSX;