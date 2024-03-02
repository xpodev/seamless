(async function () {
  var __spreadArray =
    (this && this.__spreadArray) ||
    function (to, from, pack) {
      if (pack || arguments.length === 2)
        for (var i = 0, l = from.length, ar; i < l; i++) {
          if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
          }
        }
      return to.concat(ar || Array.prototype.slice.call(from));
    };
  var Ez = /** @class */ (function () {
    function Ez() {
      var _this = this;
      this.pyxSocket = io({
        reconnectionDelayMax: 10000,
      });
      document.addEventListener("DOMContentLoaded", function () {
        this.ezReactRootNode = ReactDOM.createRoot(
          document.getElementById("root")
        );
        var allPyxElements = document.querySelectorAll("[pyx-id]");
        allPyxElements.forEach(_this.attachEventListeners.bind(_this));
      });
    }
    Ez.prototype.attachEventListeners = function (element) {
      var _this = this;
      var _a;
      var pyxId = element.getAttribute("pyx-id");
      var pyxEvents =
        ((_a = element.getAttribute("pyx-events")) === null || _a === void 0
          ? void 0
          : _a.split(",")) || [];
      pyxEvents.forEach(function (event) {
        element.addEventListener(event, function (e) {
          _this.pyxSocket.emit(
            "dom_event",
            "".concat(pyxId, ":").concat(event),
            {
              pyxId: pyxId,
              foo: "bar",
            }
          );
        });
      });
    };
    Ez.prototype.convertToReact = function (element) {
      var _this = this;
      var _a;
      if (this.isPrimitive(element)) {
        return element;
      }
      if ("pyx-id" in element.props) {
        var events =
          ((_a = element.props["pyx-events"]) === null || _a === void 0
            ? void 0
            : _a.split(",")) || [];
        events.forEach(function (event) {
          event = _this.capitalizeFirstLetter(event);
          element.props["on".concat(event)] = function (e) {
            _this.pyxSocket.emit(
              "dom_event",
              "".concat(element.props["pyx-id"], ":").concat(event),
              {
                pyxId: element.props["pyx-id"],
                foo: "bar",
              }
            );
          };
        });
      }
      var children = Array.isArray(element.children)
        ? element.children.map(function (v) {
            return _this.convertToReact(v);
          })
        : [element.children];
      return React.createElement.apply(
        React,
        __spreadArray([element.type, element.props], children, false)
      );
    };
    Ez.prototype.isPrimitive = function (value) {
      return (
        ["string", "number", "boolean"].includes(typeof value) || value === null
      );
    };
    Object.defineProperty(Ez.prototype, "reactRootNode", {
      get: function () {
        return this.ezReactRootNode;
      },
      enumerable: false,
      configurable: true,
    });
    Ez.prototype.render = function (element) {
      this.ezReactRootNode.render(this.convertToReact(element));
    };
    Ez.prototype.getComponent = function (name, props) {
      var _this = this;
      this.pyxSocket.emit("component", name, props);
      return new Promise(function (resolve) {
        _this.pyxSocket.once("component", function (component) {
          resolve(component);
        });
      });
    };
    Ez.prototype.registerPyxEventListener = function (pyxId, event, callback) {
      this.pyxSocket.on("".concat(pyxId, ":").concat(event), callback);
    };
    Ez.prototype.capitalizeFirstLetter = function (string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    };
    return Ez;
  })();

//   await import("https://unpkg.com/react@18/umd/react.production.min.js");
//   await import(
//     "https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"
//   );
//   await import("https://cdn.socket.io/4.7.4/socket.io.min.js");

  var ez = new Ez();
})();
