await import("https://cdn.socket.io/4.7.5/socket.io.js");
const socket = io(socketIOConfig);

seamless.emit = (event, ...data) => {
  socket.emit(event, ...data);
};

seamless.registerEventListener = (event, callback) => {
  socket.on(event, callback);
};

seamless.sendWaitResponse = (event, ...args) => {
  return new Promise((resolve) => {
    socket.emit(event, ...args, resolve);
  });
};

seamless.getComponent = async (name, props = {}) => {
  return await seamless.sendWaitResponse("component", name, props);
};

window.dispatchEvent(
  new CustomEvent("transportsAvailable", {
    detail: { clientId: socketIOConfig.query.client_id },
  })
);
