const loadingComponentName = this.getAttribute("loading");
const parent = this.parentElement;
const PageStateChange = new Event("pageLocationChange");
let loadingComponent = null;

if (loadingComponentName) {
  seamless.instance.getComponent(loadingComponentName, {}).then((component) => {
    loadingComponent = seamless.instance.toDOMElement(component);
  });
}

const clearParent = () => {
  while (parent.firstChild) {
    parent.removeChild(parent.firstChild);
  }
}

const loadComponent = async (name) => {
  return seamless.instance.toDOMElement(await seamless.instance.getComponent(name, {}));
}

window.addEventListener("pageLocationChange", () => {
  const path = window.location.pathname;
  const page = routes.find(
    (page) => page.path.replace(/^\//, "") === path.replace(/^\//, "")
  );

  if (!page) {
    return;
  }

  clearParent();
  if (loadingComponent) {
    parent.appendChild(loadingComponent);
  }

  loadComponent(page.name).then((component) => {
    clearParent();
    parent.appendChild(component);
  });
});

seamless.navigateTo = function (to) {
  window.history.pushState({}, "", to);
  window.dispatchEvent(PageStateChange);
  return false;
}

window.dispatchEvent(PageStateChange);
