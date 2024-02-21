class Ez {
  #pyxSocket = io({
    reconnectionDelayMax: 10000,
  });
  #ezReactRootNode = ReactDOM.createRoot(document.getElementById("root"));

  constructor() {
    document.addEventListener("DOMContentLoaded", () => {
      const allPyxElements = document.querySelectorAll("[pyx-id]");
      allPyxElements.forEach((element) => {
        const pyxId = element.getAttribute("pyx-id");
        const pyxEvents = element.getAttribute("pyx-events").split(",");
        pyxEvents.forEach((event) => {
          element.addEventListener(event, (e) => {
            this.#pyxSocket.emit("dom_event", `${pyxId}:${event}`, {
              pyxId,
              foo: "bar",
            });
          });
        });
      });
    });
  }

  #convertToReact(element) {
    if (typeof element === "string") {
      return element;
    }
    const children = Array.isArray(element.children)
      ? element.children.map((v) => this.#convertToReact(v))
      : [element.children];
    return React.createElement(element.type, element.props, ...children);
  }

  get reactRootNode() {
    return this.#ezReactRootNode;
  }

  render(element) {
    this.#ezReactRootNode.render(this.#convertToReact(element));
  }

  async getComponent(componentName, props = {}) {
    const response = await fetch(`/c/${componentName}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(props),
    });
    return await response.json();
  }

  registerPyxEventListener(pyxId, event, callback) {
    this.#pyxSocket.on(`${pyxId}:${event}`, callback);
  }
}