import type { SocketOptions, ManagerOptions } from 'socket.io-client';

export interface SlarfOptions {
    socketOptions?: Partial<ManagerOptions & SocketOptions>;
}