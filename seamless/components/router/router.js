const loadingComponentName = this.getAttribute("loading");
const parent = this.parentElement;
const PageStateChange = new Event("pageLocationChange");
let loadingComponent = null;

class IntConvertor {
  static regex = "\\d+";
  static convert(value) {
    return Number(value);
  }
}

class FloatConvertor {
  static regex = "\\d+(\\.\\d+)?";

  static convert(value) {
    return Number(value);
  }
}

const convertors = {
  int: IntConvertor,
  float: FloatConvertor,
};

routes = routes.map((route) => {
  regex = "";
  const regexConvertors = {};
  for (let i = 0; i < route.path.length; i++) {
    const key = route.path[i];
    if (key === "?") {
      break;
    }
    if (key === "{") {
      if (route.path[i + 1] === "{") {
        regex += "{";
        i++;
        continue;
      }
      let paramString = "";
      while (route.path[++i] !== "}") {
        paramString += route.path[i];
      }
      const [paramName, convertorType] = paramString.split(":");
      if (!convertorType) {
        regex += `(?<${paramName}>[^/]+)`;
      } else {
        const convertor = convertors[convertorType];
        if (convertor) {
          regex += `(?<${paramName}>${convertors[convertorType].regex})`;
          regexConvertors[paramName] = convertors[convertorType];
        } else {
          throw new Error(`Unknown convertor: ${convertorType}`);
        }
      }
    } else if (key === "*") {
      regex += "(.*)";
      break;
    } else {
      regex += key;
    }
  }
  return {
    regex: new RegExp(`^${regex}$`),
    regexConvertors,
    ...route,
  };
});

if (loadingComponentName) {
  seamless.instance.getComponent(loadingComponentName, {}).then((component) => {
    loadingComponent = seamless.instance.toDOMElement(component);
  });
}

const clearParent = () => {
  while (parent.firstChild) {
    parent.removeChild(parent.firstChild);
  }
};

const loadComponent = async (name, props = {}) => {
  return seamless.instance.toDOMElement(
    await seamless.instance.getComponent(name, props)
  );
};

window.addEventListener("pageLocationChange", () => {
  const path = window.location.pathname;
  let page;
  for (let i = 0; i < routes.length; i++) {
    const route = routes[i];
    const match = path.match(route.regex);
    if (match) {
      page = route;
      page.params = match.groups ? Object.fromEntries(
        Object.entries(match.groups).map(([key, value]) => [
          key,
          route.regexConvertors[key]
            ? route.regexConvertors[key].convert(value)
            : value,
        ])
      ) : {};
      break;
    }
  }

  if (!page) {
    return;
  }

  const props = Object.fromEntries(new URLSearchParams(window.location.search).entries());

  clearParent();
  if (loadingComponent) {
    parent.appendChild(loadingComponent);
  }

  loadComponent(page.name, { ...props, ...page.params }).then((component) => {
    clearParent();
    parent.appendChild(component);
  });
});

seamless.navigateTo = function (to) {
  window.history.pushState({}, "", to);
  window.dispatchEvent(PageStateChange);
  return false;
};

window.dispatchEvent(PageStateChange);
