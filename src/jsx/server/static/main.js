//@ts-nocheck
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
var Ez = /** @class */ (function () {
    function Ez() {
        this.jsxSocket = io({
            reconnectionDelayMax: 10000,
        });
        this.ezReactRootNode = ReactDOM.createRoot(document.getElementById("root"));
        var allJsxElements = document.querySelectorAll("[jsx-id]");
        allJsxElements.forEach(this.attachEventListeners.bind(this));
    }
    Ez.prototype.attachEventListeners = function (element) {
        var _this = this;
        var _a;
        var jsxId = element.getAttribute("jsx-id");
        var jsxEvents = ((_a = element.getAttribute("jsx-events")) === null || _a === void 0 ? void 0 : _a.split(",")) || [];
        jsxEvents.forEach(function (event) {
            element.addEventListener(event, function (e) {
                _this.jsxSocket.emit("dom_event", "".concat(jsxId, ":").concat(event), {
                    jsxId: jsxId,
                    foo: "bar",
                });
            });
        });
    };
    Ez.prototype.convertToReact = function (element) {
        var _this = this;
        var _a;
        if (this.isPrimitive(element)) {
            return element;
        }
        if ("jsx-id" in element.props) {
            var events = ((_a = element.props["jsx-events"]) === null || _a === void 0 ? void 0 : _a.split(",")) || [];
            events.forEach(function (event) {
                event = _this.capitalizeFirstLetter(event);
                element.props["on".concat(event)] = function (e) {
                    _this.jsxSocket.emit("dom_event", "".concat(element.props["jsx-id"], ":").concat(event), {
                        jsxId: element.props["jsx-id"],
                        foo: "bar",
                    });
                };
            });
        }
        var children = Array.isArray(element.children)
            ? element.children.map(function (v) { return _this.convertToReact(v); })
            : [element.children];
        return React.createElement.apply(React, __spreadArray([element.type, element.props], children, false));
    };
    Ez.prototype.isPrimitive = function (value) {
        return (["string", "number", "boolean"].includes(typeof value) || value === null);
    };
    Object.defineProperty(Ez.prototype, "reactRootNode", {
        get: function () {
            return this.ezReactRootNode;
        },
        enumerable: false,
        configurable: true
    });
    Ez.prototype.render = function (element) {
        this.ezReactRootNode.render(this.convertToReact(element));
    };
    Ez.prototype.getComponent = function (name, props) {
        var _this = this;
        this.jsxSocket.emit("component", name, props);
        return new Promise(function (resolve) {
            _this.jsxSocket.once("component", function (component) {
                resolve(component);
            });
        });
    };
    Ez.prototype.registerJsxEventListener = function (jsxId, event, callback) {
        this.jsxSocket.on("".concat(jsxId, ":").concat(event), callback);
    };
    Ez.prototype.capitalizeFirstLetter = function (string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    };
    return Ez;
}());
document.addEventListener("DOMContentLoaded", function () {
    var ez = new Ez();
});
