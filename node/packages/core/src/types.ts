import type { SocketOptions, ManagerOptions } from "socket.io-client";

export interface SeamlessOptions {
  socketOptions?: Partial<ManagerOptions & SocketOptions>;
  /**
   * A function that serializes the event object before sending it to the server
   * The default behavior is to return the event object as is
   *
   * @param originalEvent The original event object
   * @param outEvent The event object that is constructed by `serializeEventObject`
   * @returns The object that will be sent to the server
   */
  eventObjectTransformer?: (originalEvent: Event, outEvent: any) => any;
}

export interface OutEvent<T = any> {
  type: string;
  data: T;
}

export const enum PropertyType {
  Raw = "raw",
  Function = "function",
}

export interface PropertyData {
  type: PropertyType;
  value: any;
}

export type AttributeHandler = (element: Element) => void;

export type AttributeHandlerMatcher = (element: Element) => boolean;
